import functools
import importlib.resources
import json
import random
import urllib.request
from typing import Optional

from .. import Decoder as _Decoder
from .. import Header as _Header
from .. import Session as _Session
from .. import _TAuth
from .. import _TCookies
from .. import _THeaders
from .. import _TParams
from .. import _TProxies
from .. import _TVerify

_PATH = 'browsers.json'


class UserAgent:
    def __init__(self, desktop: bool = True, mobile: bool = True,
                 linux: bool = True, windows: bool = True, darwin: bool = True,
                 android: bool = True, ios: bool = True, chrome: bool = True,
                 firefox: bool = True, allow_brotli: Optional[bool] = None):
        devices = []
        if desktop:
            devices.append('desktop')
        if mobile:
            devices.append('mobile')
        self.device = random.choice(devices)
        platforms = []
        if self.device == 'desktop':
            if linux:
                platforms.append('linux')
            if windows:
                platforms.append('windows')
            if darwin:
                platforms.append('darwin')
        elif self.device == 'mobile':
            if android:
                platforms.append('android')
            if ios:
                platforms.append('ios')
        self.platform = random.choice(platforms)
        browsers = []
        if chrome:
            browsers.append('chrome')
        if firefox:
            browsers.append('firefox')
        self.browser = random.choice(browsers)
        if allow_brotli is None:
            allow_brotli = 'br' in _Decoder
        self.allow_brotli = allow_brotli

    def encode(self, request: Optional[urllib.request.Request] = None) -> tuple[dict[str, str], tuple[str, ...]]:
        browsers = load()
        headers = browsers['headers'][self.browser].copy()
        cipher_suite = tuple(browsers['cipherSuite'][self.browser])
        headers[_Header.USER_AGENT] = random.choice(
            browsers['user_agents'][self.device][self.platform][self.browser])
        if not self.allow_brotli:
            encodings = urllib.request.parse_http_list(headers[_Header.ACCEPT_ENCODING])
            try:
                encodings.remove('br')
            except ValueError:
                pass
            else:
                headers[_Header.ACCEPT_ENCODING] = ','.join(encodings)
        if request is not None:
            for header in headers:
                request.add_header(*header)
            if (verify := getattr(request, '_verify', None)) is not None:
                verify.set_ciphers(':'.join(cipher_suite))
        return headers, cipher_suite


_TUserAgent = tuple[dict[str, str], tuple[str, ...]] | UserAgent


class Session(_Session):
    def __init__(self, headers: Optional[_THeaders] = None, auth: Optional[_TAuth] = None,
                 proxies: Optional[_TProxies] = None, params: Optional[_TParams] = None, stream: Optional[bool] = None,
                 verify: Optional[_TVerify] = None, trust_env: bool = True, cookies: Optional[_TCookies] = None,
                 timeout: Optional[float] = None, allow_redirects: Optional[bool] = None, force_auth: Optional[bool] = None,
                 max_repeats: Optional[int] = None, max_redirections: Optional[int] = None,
                 http_debug_level: Optional[bool | int] = None, unredirected_hdrs: Optional[_THeaders] = None,
                 user_agent: Optional[_TUserAgent] = None):
        super().__init__(headers, auth, proxies, params, stream, verify, trust_env, cookies, timeout, allow_redirects,
                         force_auth, max_repeats, max_redirections, http_debug_level, unredirected_hdrs)
        self.user_agent = user_agent

    @property
    def user_agent(self) -> tuple[dict[str, str], list[dict[str, Optional[bool | int | str]]]]:
        return self.headers, self.verify.get_ciphers()

    @user_agent.setter
    def user_agent(self, user_agent: Optional[_TUserAgent]):
        if user_agent is None:
            user_agent = UserAgent(mobile=False)
        if isinstance(user_agent, UserAgent):
            user_agent = user_agent.encode()
        self.headers.update(user_agent[0])
        self.verify.post_handshake_auth = False
        self.verify.set_ciphers(':'.join(user_agent[1]))
        self.verify.set_ecdh_curve('prime256v1')


@functools.cache
def load() -> dict[str, dict]:
    return json.load((importlib.resources.files(__name__) / _PATH).open(encoding='utf-8'))


if __debug__:
    def download():
        import os
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/VeNoMouS/cloudscraper/master/cloudscraper/user_agent/',
            _PATH), os.path.join(os.path.dirname(__file__), _PATH))
        load.cache_clear()
        load()
