from __future__ import annotations

import functools
import http.client
import queue
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Iterator, Mapping, Optional

from . import Header as _Header
from . import Session as _Session
from . import _TAuth
from . import _TCookies
from . import _THeaders
from . import _TParams
from . import _TProxies
from . import _TVerify
from . import contains_case_insensitive as _contains_case_insensitive
from . import eq_case_insensitive as _eq_case_insensitive
from . import get_header_list as _get_header_list


class _ConnectionPoolMeta(type):
    _scheme_: str

    _pools: dict[str, type[ConnectionPool]] = {}

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if cls._scheme_:
            # noinspection PyTypeChecker
            cls[cls._scheme_.lower()] = cls

    def __contains__(self, scheme: str) -> bool:
        return scheme.lower() in self._pools

    def __getitem__(self, scheme: str) -> type[ConnectionPool]:
        return self._pools[scheme.lower()]

    def __setitem__(self, scheme: str, pool: type[ConnectionPool]):
        self._pools[scheme.lower()] = pool

    def __delitem__(self, scheme: str):
        del self._pools[scheme.lower()]

    def __iter__(self) -> Iterator[str]:
        return iter(self._pools)

    @staticmethod
    def get_key(context: Mapping[str, Any]):
        return frozenset(context.items())


class ConnectionPool(metaclass=_ConnectionPoolMeta):
    _scheme_: str = ''
    _port_: int = 0
    _tconn_: type = type

    def __init__(self, host: str, port: Optional[int] = None,
                 timeout: Optional[float] = None, size: int = 1,
                 block: bool = False, **conn_kwargs):
        self._host = host
        self._port = self._port_ if port is None else port
        self.timeout = timeout
        self._pool = queue.LifoQueue(size)
        for _ in range(size):
            self._pool.put(None)
        self.block = block
        self.conn_kwargs = conn_kwargs

    def __getitem__(self, url: str, timeout: Optional[float] = None):
        assert self.is_same_host(url)

    def __setitem__(self, url: str, value):
        assert self.is_same_host(url)
        try:
            self._pool.put_nowait(value)
        except (AttributeError, queue.Full):
            return False
        else:
            return True

    def __enter__(self):
        return self

    def __exit__(self, *_, **__):
        self.close()

    def close(self):
        self._pool = None

    def is_same_host(self, url: str) -> bool:
        if url.startswith('/'):
            return True
        else:
            if '://' not in url:
                url = '//' + url
            components = urllib.parse.urlsplit(url)
            scheme = components.scheme
            port = components.port
            host = components.hostname
            return (scheme == '' or _eq_case_insensitive(scheme, self._scheme_) and
                    (port is None or port == self._port) and
                    (host is None or _eq_case_insensitive(host, self._host)))


class HTTPConnectionPool(ConnectionPool):
    _scheme_ = 'http'
    _port_ = http.client.HTTP_PORT
    _tconn_ = http.client.HTTPConnection

    def __getitem__(self, url: str, timeout: Optional[float] = None) -> http.client.HTTPConnection:
        ConnectionPool.__getitem__(self, url)
        try:
            conn = self._pool.get(self.block, timeout)
        except queue.Empty:
            if self.block:
                raise
            else:
                conn = None
        if conn is None:
            conn = self._tconn_(self._host, self._port,
                                self.timeout, **self.conn_kwargs)
        else:
            # noinspection PyProtectedMember
            response = conn._HTTPConnection__response
            if conn.sock is None or (response is not None and not response.isclosed()):
                conn.close()
        return conn

    def __setitem__(self, url: str, value: http.client.HTTPConnection):
        if not ConnectionPool.__setitem__(self, url, value):
            value.close()

    def close(self):
        if self._pool is not None:
            pool, self._pool = self._pool, None
            while True:
                try:
                    conn = pool.get_nowait()
                except queue.Empty:
                    break
                else:
                    if conn is not None:
                        conn.close()


class HTTPSConnectionPool(HTTPConnectionPool):
    _scheme_ = 'https'
    _port_ = http.client.HTTPS_PORT
    _tconn_ = http.client.HTTPSConnection


class ConnectionPoolManager:
    def __init__(self, count: int = 10, **pool_kwargs):
        self.count = count
        self.pool_kwargs = pool_kwargs

    def __enter__(self):
        return self

    def __exit__(self, *_, **__):
        self.close()

    def __call__(self, key) -> ConnectionPool:
        pool_kwargs = dict(key)
        return ConnectionPool[pool_kwargs.pop('scheme')](**pool_kwargs)

    @property
    def count(self) -> int:
        return self.pool_from_key.cache_info().maxsize

    @count.setter
    def count(self, value: int):
        self.pool_from_key = functools.lru_cache(value)(self)

    def close(self):
        self.pool_from_key = None  # TODO close all pools

    def pool_from_context(self, context) -> ConnectionPool:
        return self.pool_from_key(ConnectionPool[context['scheme']].get_key(context))

    def pool_from_host(self, scheme: str, host: str,
                       port: Optional[int] = None, **pool_kwargs) -> ConnectionPool:
        if port is None:
            # noinspection PyProtectedMember
            port = ConnectionPool[scheme]._port_
        context = self.pool_kwargs.copy()
        for key, value in pool_kwargs.items():
            if value is None:
                try:
                    del context[key]
                except KeyError:
                    pass
            else:
                context[key] = value
        context['scheme'] = scheme.lower()
        context['host'] = host
        context['port'] = port
        return self.pool_from_context(context)

    def pool_from_url(self, url: str, **pool_kwargs) -> ConnectionPool:
        components = urllib.parse.urlsplit(url)
        return self.pool_from_host(components.scheme, components.hostname,
                                   components.port, **pool_kwargs)


_TPoolManager = int | ConnectionPoolManager


class _AbstractHTTPPoolHandler(urllib.request.AbstractHTTPHandler):
    def __init__(self, debuglevel: int = 0):
        super().__init__(debuglevel)
        self._man = ConnectionPoolManager()

    def __del__(self):
        self._man.close()

    def do_open(self, conn_pool: HTTPConnectionPool,
                request: urllib.request.Request, **_) -> http.client.HTTPResponse:
        conn = conn_pool[request.host]
        conn.timeout = request.timeout
        # noinspection PyUnresolvedReferences
        conn.set_debuglevel(self._debuglevel)

        headers = dict(request.unredirected_hdrs)
        headers.update({key: value for key, value in request.headers.items()
                        if key not in headers})
        headers = {key.title(): value for key, value in headers.items()}

        # noinspection PyUnresolvedReferences,PyProtectedMember
        if request._tunnel_host:
            tunnel_headers = {}
            proxy_auth_hdr = _Header.PROXY_AUTHORIZATION
            if proxy_auth_hdr in headers:
                tunnel_headers[proxy_auth_hdr] = headers[proxy_auth_hdr]
                del headers[proxy_auth_hdr]
            # noinspection PyUnresolvedReferences,PyProtectedMember
            conn.set_tunnel(request._tunnel_host, headers=tunnel_headers)

        try:
            try:
                conn.request(request.get_method(), request.selector,
                             request.data, headers, encode_chunked=request.has_header(
                        _Header.TRANSFER_ENCODING.capitalize()))
            except OSError as exc:
                raise urllib.error.URLError(exc)
            response = conn.getresponse()
        except:  # NOQA E722
            conn.close()
            raise
        if conn.sock and (request.has_proxy() or _contains_case_insensitive(
                dict(_get_header_list(response.getheader(_Header.CONNECTION, ''))), 'close')):
            conn.sock.close()
            conn.sock = None
        else:
            conn_pool[request.full_url] = conn

        response.url = request.get_full_url()
        response.msg = response.reason
        return response


class _HTTPPoolHandler(_AbstractHTTPPoolHandler):
    def http_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        # noinspection PyTypeChecker
        return self.do_open(self._man.pool_from_url(request.full_url), request)

    http_request = _AbstractHTTPPoolHandler.do_request_


class _HTTPSPoolHandler(_AbstractHTTPPoolHandler):
    def __init__(self, debuglevel=0, context=None, check_hostname=None):
        _AbstractHTTPPoolHandler.__init__(self, debuglevel)
        self._context = context
        self._check_hostname = check_hostname

    def https_open(self, request: urllib.request.Request) -> http.client.HTTPResponse:
        # noinspection PyTypeChecker
        return self.do_open(self._man.pool_from_url(
            request.full_url, context=getattr(request, '_verify', None)), request)

    https_request = _AbstractHTTPPoolHandler.do_request_


class Session(_Session):
    _thttp_ = _HTTPPoolHandler
    _thttps_ = _HTTPSPoolHandler

    def __init__(self, headers: Optional[_THeaders] = None, auth: Optional[_TAuth] = None,
                 proxies: Optional[_TProxies] = None, params: Optional[_TParams] = None, stream: Optional[bool] = None,
                 verify: Optional[_TVerify] = None, trust_env: bool = True, cookies: Optional[_TCookies] = None,
                 timeout: Optional[float] = None, allow_redirects: Optional[bool] = None, force_auth: Optional[bool] = None,
                 max_repeats: Optional[int] = None, max_redirections: Optional[int] = None,
                 http_debug_level: Optional[bool | int] = None, unredirected_hdrs: Optional[_THeaders] = None,
                 pool_manager: Optional[_TPoolManager] = None):
        super().__init__(headers, auth, proxies, params, stream, verify, trust_env, cookies, timeout, allow_redirects,
                         force_auth, max_repeats, max_redirections, http_debug_level, unredirected_hdrs)
        self.pool_manager = pool_manager

    @property
    def pool_manager(self) -> _TPoolManager:
        # noinspection PyProtectedMember
        return self._http_handler._man

    @pool_manager.setter
    def pool_manager(self, pool_manager: Optional[_TPoolManager]):
        if pool_manager is None:
            pool_manager = ConnectionPoolManager()
        elif isinstance(pool_manager, int):
            pool_manager = self.pool_manager.count = pool_manager
        self._http_handler._man = self._https_handler._man = pool_manager
