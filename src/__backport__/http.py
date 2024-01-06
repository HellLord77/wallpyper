import http

from . import FLAG_PATCH
from . import enum


class HTTPMethod(enum.StrEnum):
    def __new__(cls, value, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.description = description
        return obj

    def __repr__(self):
        return "<%s.%s>" % (self.__class__.__name__, self._name_)

    CONNECT = 'CONNECT', 'Establish a connection to the server.'
    DELETE = 'DELETE', 'Remove the target.'
    GET = 'GET', 'Retrieve the target.'
    HEAD = 'HEAD', 'Same as GET, but only retrieve the status line and header section.'
    OPTIONS = 'OPTIONS', 'Describe the communication options for the target.'
    PATCH = 'PATCH', 'Apply partial modifications to a target.'
    POST = 'POST', 'Perform target-specific processing with the request payload.'
    PUT = 'PUT', 'Replace the target with the request payload.'
    TRACE = 'TRACE', 'Perform a message loop-back test along the path to the target.'


if FLAG_PATCH:
    http.HTTPMethod = HTTPMethod
