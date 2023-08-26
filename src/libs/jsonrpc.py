__version__ = '0.0.2'

import json
import socketserver
import urllib.parse
import xmlrpc.client
import xmlrpc.server
from typing import Any, AnyStr
from xml.etree import ElementTree


def _xml_to_json_header(keyword: str, value: str) -> tuple[str, str]:
    if keyword == 'Content-Type' and value == 'text/xml':
        value = 'application/json'
    return keyword, value


def _marshal_struct(element: ElementTree.Element) -> tuple[str, Any]:
    return element[0].text, _marshal(element[1])


def _marshal(element: ElementTree.Element):
    if element.tag in ('methodCall', 'methodResponse'):
        method = {}
        for child in element:
            if child.tag == 'methodName':
                method[child.tag] = child.text
            elif child.tag == 'fault':
                method[child.tag] = _marshal(child[0])
            elif child.tag == 'params':
                method[child.tag] = list(map(_marshal, child))
        return {element.tag: method}
    elif element.tag in ('param', 'value'):
        return _marshal(element[0])
    elif element.tag == 'nil':
        return
    elif element.tag == 'boolean':
        return element.text == '1'
    elif element.tag in ('i1', 'i2', 'i4', 'i8', 'int', 'biginteger'):
        return int(element.text)
    elif element.tag in ('double', 'float'):
        return float(element.text)
    elif element.tag in 'string':
        return element.text
    elif element.tag == 'array':
        return list(map(_marshal, element[0]))
    elif element.tag == 'struct':
        return dict(map(_marshal_struct, element))
    elif element.tag in ('bigdecimal', 'base64', 'dateTime.iso8601'):
        return {f'${element.tag}': element.text}


def _xml_to_json(xml: AnyStr) -> AnyStr:
    json_ = json.dumps(_marshal(ElementTree.XML(xml)), separators=(',', ':'))
    if isinstance(xml, bytes):
        json_ = json_.encode()
    return json_


def dumps(params, methodname=None, methodresponse=None,
          encoding=None, allow_none=False):
    return _xml_to_json(xmlrpc.client.dumps(
        params, methodname, methodresponse, encoding, allow_none))


def _unmarshal(data, first: bool = False):
    element = ElementTree.Element('')
    if isinstance(data, dict):
        if len(data) == 1:
            key = next(iter(data))
            if first and key in ('methodCall', 'methodResponse'):
                element.tag = key
                for name, value in data[key].items():
                    if name == 'methodName':
                        method_name = ElementTree.Element(name)
                        method_name.text = value
                        element.append(method_name)
                    elif name == 'fault':
                        fault = ElementTree.Element(name)
                        fault.append(_unmarshal(value))
                        element.append(fault)
                    elif name == 'params':
                        params = ElementTree.Element(name)
                        for param in value:
                            param_ = ElementTree.Element('param')
                            value_ = ElementTree.Element('value')
                            value_.append(_unmarshal(param))
                            param_.append(value_)
                            params.append(param_)
                        element.append(params)
                return element
            elif key.startswith('$'):
                element.tag = key[1:]
                element.text = data[key]
                return element
        element = ElementTree.Element('struct')
        for name, value in data.items():
            member = ElementTree.Element('member')
            name_ = ElementTree.Element('name')
            name_.text = name
            member.append(name_)
            value_ = ElementTree.Element('value')
            value_.append(_unmarshal(value))
            member.append(value_)
            element.append(member)
    elif isinstance(data, list):
        element.tag = 'array'
        data_ = ElementTree.Element('data')
        for value in data:
            value_ = ElementTree.Element('value')
            value_.append(_unmarshal(value))
            data_.append(value_)
        element.append(data_)
    elif data is None:
        element.tag = 'nil'
    elif isinstance(data, bool):
        element.tag = 'boolean'
        element.text = '1' if data else '0'
    elif isinstance(data, int):
        element.tag = 'int'
        element.text = str(data)
    elif isinstance(data, float):
        element.tag = 'double'
        element.text = str(data)
    elif isinstance(data, str):
        element.tag = 'string'
        element.text = data
    return element


def _json_to_xml(json_: AnyStr) -> AnyStr:
    xml = ElementTree.tostring(_unmarshal(json.loads(
        json_), True), 'unicode', xml_declaration=True)
    if isinstance(json_, bytes):
        xml = xml.encode()
    return xml


def loads(data, use_datetime=False, use_builtin_types=False):
    return xmlrpc.client.loads(_json_to_xml(data), use_datetime, use_builtin_types)


class _Headers(list):
    def append(self, __object):
        super().append(_xml_to_json_header(*__object))


class Transport(xmlrpc.client.Transport):
    user_agent = f'Python-{__name__.rsplit(".", 1)[-1]}/{__version__}'

    def __init__(self, use_datetime=False,
                 use_builtin_types=False, *, headers=()):
        super().__init__(use_datetime, use_builtin_types, headers=headers)
        self._headers = _Headers(self._headers)

    def request(self, host, handler, request_body, verbose=False):
        return super().request(host, handler, _xml_to_json(request_body), verbose)


class SafeTransport(xmlrpc.client.SafeTransport, Transport):
    pass


class ServerProxy(xmlrpc.client.ServerProxy):
    def __init__(self, uri, transport=None, verbose=False,
                 allow_none=False, use_datetime=False,
                 use_builtin_types=False, *, headers=(), context=None):
        if transport is None:
            if urllib.parse.urlsplit(uri).scheme == 'https':
                handler = SafeTransport
                extra_kwargs = {'context': context}
            else:
                handler = Transport
                extra_kwargs = {}
            transport = handler(
                use_datetime=use_datetime, use_builtin_types=use_builtin_types,
                headers=headers, **extra_kwargs)
        super().__init__(uri, transport, None, verbose, allow_none)


class SimpleJSONRPCDispatcher(xmlrpc.server.SimpleXMLRPCDispatcher):
    def _marshaled_dispatch(self, data, dispatch_method=None, path=None):
        # noinspection PyProtectedMember
        return super()._marshaled_dispatch(
            _json_to_xml(data), dispatch_method, path)


class SimpleJSONRPCRequestHandler(xmlrpc.server.SimpleXMLRPCRequestHandler):
    def send_header(self, keyword: str, value: str):
        super().send_header(*_xml_to_json_header(keyword, value))


class SimpleJSONRPCServer(xmlrpc.server.SimpleXMLRPCServer, SimpleJSONRPCDispatcher):
    # noinspection PyPep8Naming
    def __init__(self, addr, requestHandler=SimpleJSONRPCRequestHandler,
                 logRequests=True, allow_none=False, encoding=None,
                 bind_and_activate=True, use_builtin_types=False):
        self.logRequests = logRequests
        SimpleJSONRPCDispatcher.__init__(self, allow_none, encoding, use_builtin_types)
        socketserver.TCPServer.__init__(self, addr, requestHandler, bind_and_activate)


class MultiPathJSONRPCServer(xmlrpc.server.MultiPathXMLRPCServer, SimpleJSONRPCServer):
    # noinspection PyPep8Naming
    def __init__(self, addr, requestHandler=SimpleJSONRPCRequestHandler,
                 logRequests=True, allow_none=False, encoding=None,
                 bind_and_activate=True, use_builtin_types=False):
        SimpleJSONRPCServer.__init__(self, addr, requestHandler, logRequests, allow_none,
                                     encoding, bind_and_activate, use_builtin_types)
        self.dispatchers = {}
        self.allow_none = allow_none
        self.encoding = encoding or 'utf-8'
