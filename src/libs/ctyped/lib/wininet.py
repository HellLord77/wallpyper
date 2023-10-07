from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer

# wininet
InternetCloseHandle: _Callable[[_type.HINTERNET],  # hInternet
                               _type.BOOLAPI]
InternetSetOptionA: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                               _type.DWORD,  # dwOption
                               _Optional[_type.LPVOID],  # lpBuffer
                               _type.DWORD],  # dwBufferLength
                              _type.BOOLAPI]
InternetSetOptionW: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                               _type.DWORD,  # dwOption
                               _Optional[_type.LPVOID],  # lpBuffer
                               _type.DWORD],  # dwBufferLength
                              _type.BOOLAPI]
InternetSetOptionExA: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                 _type.DWORD,  # dwOption
                                 _Optional[_type.LPVOID],  # lpBuffer
                                 _type.DWORD,  # dwBufferLength
                                 _type.DWORD],  # dwFlags
                                _type.BOOLAPI]
InternetSetOptionExW: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                 _type.DWORD,  # dwOption
                                 _Optional[_type.LPVOID],  # lpBuffer
                                 _type.DWORD,  # dwBufferLength
                                 _type.DWORD],  # dwFlags
                                _type.BOOLAPI]
InternetLockRequestFile: _Callable[[_type.HINTERNET,  # hInternet
                                    _Pointer[_type.HANDLE]],  # lphLockRequestInfo
                                   _type.BOOLAPI]
InternetUnlockRequestFile: _Callable[[_type.HANDLE],  # hLockRequestInfo
                                     _type.BOOLAPI]
InternetSetCookieA: _Callable[[_type.LPCSTR,  # lpszUrl
                               _Optional[_type.LPCSTR],  # lpszCookieName
                               _type.LPCSTR],  # lpszCookieData
                              _type.BOOLAPI]
InternetSetCookieW: _Callable[[_type.LPCWSTR,  # lpszUrl
                               _Optional[_type.LPCWSTR],  # lpszCookieName
                               _type.LPCWSTR],  # lpszCookieData
                              _type.BOOLAPI]
InternetGetCookieA: _Callable[[_type.LPCSTR,  # lpszUrl
                               _Optional[_type.LPCSTR],  # lpszCookieName
                               _type.LPSTR,  # lpszCookieData
                               _Pointer[_type.DWORD]],  # lpdwSize
                              _type.BOOLAPI]
InternetGetCookieW: _Callable[[_type.LPCWSTR,  # lpszUrl
                               _Optional[_type.LPCWSTR],  # lpszCookieName
                               _type.LPWSTR,  # lpszCookieData
                               _Pointer[_type.DWORD]],  # lpdwSize
                              _type.BOOLAPI]
InternetSetCookieExA: _Callable[[_type.LPCSTR,  # lpszUrl
                                 _Optional[_type.LPCSTR],  # lpszCookieName
                                 _type.LPCSTR,  # lpszCookieData
                                 _type.DWORD,  # dwFlags
                                 _Optional[_type.DWORD_PTR]],  # dwReserved
                                _type.DWORD]
InternetSetCookieExW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                 _Optional[_type.LPCWSTR],  # lpszCookieName
                                 _type.LPCWSTR,  # lpszCookieData
                                 _type.DWORD,  # dwFlags
                                 _Optional[_type.DWORD_PTR]],  # dwReserved
                                _type.DWORD]
InternetGetCookieExA: _Callable[[_type.LPCSTR,  # lpszUrl
                                 _Optional[_type.LPCSTR],  # lpszCookieName
                                 _type.LPSTR,  # lpszCookieData
                                 _Pointer[_type.DWORD],  # lpdwSize
                                 _type.DWORD,  # dwFlags
                                 _type.LPVOID],  # lpReserved
                                _type.BOOLAPI]
InternetGetCookieExW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                 _Optional[_type.LPCWSTR],  # lpszCookieName
                                 _type.LPWSTR,  # lpszCookieData
                                 _Pointer[_type.DWORD],  # lpdwSize
                                 _type.DWORD,  # dwFlags
                                 _type.LPVOID],  # lpReserved
                                _type.BOOLAPI]

_WinLib(__name__)
