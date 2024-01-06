import sys

FLAG_PATCH = True

if sys.version_info < (3, 11):
    from . import enum
    from . import http
