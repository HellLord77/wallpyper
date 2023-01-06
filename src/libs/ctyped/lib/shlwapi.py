from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .. import union as _union
from .._utils import _Pointer
from ..interface.um import Unknwnbase as _Unknwnbase
from ..interface.um import objidlbase as _objidlbase

# noinspection PyTypeChecker
GUIDFromStringA: _Callable[[_type.LPCSTR,
                            _Pointer[_struct.GUID]],
                           _type.BOOL] = 269
# noinspection PyTypeChecker
GUIDFromStringW: _Callable[[_type.LPCWSTR,
                            _Pointer[_struct.GUID]],
                           _type.BOOL] = 270
DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                         _type.HRESULT]
# Shlwapi
PathMakePrettyA: _Callable[[_type.LPCSTR],  # pszPath
                           _type.BOOL]
PathMakePrettyW: _Callable[[_type.LPCWSTR],  # pszPath
                           _type.BOOL]
PathMatchSpecA: _Callable[[_type.LPCSTR,  # pszFile
                           _type.LPCSTR],  # pszSpec
                          _type.BOOL]
PathMatchSpecW: _Callable[[_type.LPCWSTR,  # pszFile
                           _type.LPCWSTR],  # pszSpec
                          _type.BOOL]
PathMatchSpecExA: _Callable[[_type.LPCSTR,  # pszFile
                             _type.LPCSTR,  # pszSpec
                             _type.DWORD],  # dwFlags
                            _type.BOOL]
PathMatchSpecExW: _Callable[[_type.LPCWSTR,  # pszFile
                             _type.LPCWSTR,  # pszSpec
                             _type.DWORD],  # dwFlags
                            _type.BOOL]
PathSkipRootA: _Callable[[_type.LPCSTR],  # pszPath
                         _type.LPSTR]
PathSkipRootA: _Callable[[_type.LPCWSTR],  # pszPath
                         _type.LPWSTR]
PathStripPathA: _Callable[[_type.LPSTR],  # pszPath
                          _type.c_void]
PathStripPathW: _Callable[[_type.LPWSTR],  # pszPath
                          _type.c_void]
PathStripToRootA: _Callable[[_type.LPSTR],  # pszPath
                            _type.BOOL]
PathStripToRootW: _Callable[[_type.LPWSTR],  # pszPath
                            _type.BOOL]
PathUnmakeSystemFolderA: _Callable[[_type.LPSTR],  # pszPath
                                   _type.BOOL]
PathUnmakeSystemFolderW: _Callable[[_type.LPWSTR],  # pszPath
                                   _type.BOOL]
PathUndecorateA: _Callable[[_type.LPSTR],  # pszPath
                           _type.c_void]
PathUndecorateW: _Callable[[_type.LPWSTR],  # pszPath
                           _type.c_void]
# TODO
IsInternetESCEnabled: _Callable[[],
                                _type.BOOL]
IStream_Copy: _Callable[[_objidlbase.IStream,
                         _objidlbase.IStream,
                         _type.DWORD],
                        _type.HRESULT]
IStream_Read: _Callable[[_objidlbase.IStream,
                         _type.c_void_p,
                         _type.ULONG],
                        _type.HRESULT]
IStream_ReadStr: _Callable[[_objidlbase.IStream,
                            _Pointer[_type.PCWSTR]],
                           _type.HRESULT]
IStream_Reset: _Callable[[_objidlbase.IStream],  # pstm
                         _type.HRESULT]
IStream_Size: _Callable[[_objidlbase.IStream,  # pstm
                         _Pointer[_union.ULARGE_INTEGER]],  # pui
                        _type.HRESULT]
IStream_Write: _Callable[[_objidlbase.IStream,
                          _type.c_void_p,
                          _type.ULONG],
                         _type.HRESULT]
IStream_WriteStr: _Callable[[_objidlbase.IStream,
                             _Pointer[_type.PCWSTR]],
                            _type.HRESULT]
IUnknown_AtomicRelease: _Callable[[_type.c_void_p],
                                  _type.HRESULT]
IUnknown_GetSite: _Callable[[_Unknwnbase.IUnknown,
                             _Pointer[_struct.IID],
                             _type.c_void_p],
                            _type.HRESULT]
IUnknown_GetWindow: _Callable[[_Unknwnbase.IUnknown,
                               _Pointer[_type.HWND]],
                              _type.HRESULT]
IUnknown_QueryService: _Callable[[_Unknwnbase.IUnknown,
                                  _Pointer[_struct.GUID],
                                  _Pointer[_struct.IID],
                                  _type.c_void_p],
                                 _type.HRESULT]
IUnknown_Set: _Callable[[_Pointer[_Unknwnbase.IUnknown],
                         _Optional[_Unknwnbase.IUnknown]],
                        _type.HRESULT]
IUnknown_SetSite: _Callable[[_Unknwnbase.IUnknown,
                             _Optional[_Unknwnbase.IUnknown]],
                            _type.HRESULT]
PathAddBackslashA: _Callable[[_type.LPSTR],
                             _type.LPSTR]
PathAddBackslashW: _Callable[[_type.LPWSTR],
                             _type.LPWSTR]
PathAddExtensionA: _Callable[[_type.LPSTR,
                              _Optional[_type.LPCSTR]],
                             _type.BOOL]
PathAddExtensionW: _Callable[[_type.LPWSTR,
                              _Optional[_type.LPCWSTR]],
                             _type.BOOL]
PathAppendA: _Callable[[_type.LPSTR,
                        _type.LPCSTR],
                       _type.BOOL]
PathAppendW: _Callable[[_type.LPWSTR,
                        _type.LPCWSTR],
                       _type.BOOL]
PathBuildRootA: _Callable[[_type.LPSTR,
                           _type.c_int],
                          _type.LPSTR]
PathBuildRootW: _Callable[[_type.LPWSTR,
                           _type.c_int],
                          _type.LPWSTR]
PathCanonicalizeA: _Callable[[_type.LPSTR,
                              _type.LPCSTR],
                             _type.BOOL]
PathCanonicalizeW: _Callable[[_type.LPWSTR,
                              _type.LPCWSTR],
                             _type.BOOL]
PathCombineA: _Callable[[_type.LPSTR,
                         _Optional[_type.LPCSTR],
                         _Optional[_type.LPCSTR]],
                        _type.BOOL]
PathCombineW: _Callable[[_type.LPWSTR,
                         _Optional[_type.LPCWSTR],
                         _Optional[_type.LPCWSTR]],
                        _type.BOOL]
PathCompactPathA: _Callable[[_Optional[_type.HDC],
                             _type.LPSTR,
                             _type.UINT],
                            _type.BOOL]
PathCompactPathW: _Callable[[_Optional[_type.HDC],
                             _type.LPWSTR,
                             _type.UINT],
                            _type.BOOL]
PathCompactPathExA: _Callable[[_type.LPSTR,
                               _type.LPCSTR,
                               _type.UINT,
                               _type.DWORD],
                              _type.BOOL]
PathCompactPathExW: _Callable[[_type.LPWSTR,
                               _type.LPCWSTR,
                               _type.UINT,
                               _type.DWORD],
                              _type.BOOL]
PathCommonPrefixA: _Callable[[_type.LPCSTR,
                              _type.LPCSTR,
                              _type.LPSTR],
                             _type.c_int]
PathCommonPrefixW: _Callable[[_type.LPCWSTR,
                              _type.LPCWSTR,
                              _type.LPWSTR],
                             _type.c_int]
PathFileExistsA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
PathFileExistsW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
PathFindExtensionA: _Callable[[_type.LPCSTR],
                              _type.LPSTR]
PathFindExtensionW: _Callable[[_type.LPCWSTR],
                              _type.LPWSTR]
PathFindFileNameA: _Callable[[_type.LPCSTR],
                             _type.LPSTR]
PathFindFileNameW: _Callable[[_type.LPCWSTR],
                             _type.LPWSTR]
PathFindNextComponentA: _Callable[[_type.LPCSTR],
                                  _type.LPSTR]
PathFindNextComponentW: _Callable[[_type.LPCWSTR],
                                  _type.LPWSTR]
PathFindOnPathA: _Callable[[_type.LPSTR,
                            _Optional[_Pointer[_type.PCSTR]]],
                           _type.BOOL]
PathFindOnPathW: _Callable[[_type.LPWSTR,
                            _Optional[_Pointer[_type.PCWSTR]]],
                           _type.BOOL]
PathGetArgsA: _Callable[[_type.LPCSTR],
                        _type.LPSTR]
PathGetArgsW: _Callable[[_type.LPCWSTR],
                        _type.LPWSTR]
PathGetCharTypeA: _Callable[[_type.UCHAR],
                            _type.UINT]
PathGetCharTypeW: _Callable[[_type.WCHAR],
                            _type.UINT]
PathGetDriveNumberA: _Callable[[_type.LPCSTR],
                               _type.c_int]
PathGetDriveNumberW: _Callable[[_type.LPCWSTR],
                               _type.c_int]
PathIsContentTypeA: _Callable[[_type.LPCSTR,
                               _type.LPCSTR],
                              _type.BOOL]
PathIsContentTypeW: _Callable[[_type.LPCWSTR,
                               _type.LPCWSTR],
                              _type.BOOL]
PathIsDirectoryA: _Callable[[_type.LPCSTR],
                            _type.BOOL]
PathIsDirectoryW: _Callable[[_type.LPCWSTR],
                            _type.BOOL]
PathIsDirectoryEmptyA: _Callable[[_type.LPCSTR],
                                 _type.BOOL]
PathIsDirectoryEmptyW: _Callable[[_type.LPCWSTR],
                                 _type.BOOL]
PathIsFileSpecA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
PathIsFileSpecW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
PathIsLFNFileSpecA: _Callable[[_type.LPCSTR],
                              _type.BOOL]
PathIsLFNFileSpecW: _Callable[[_type.LPCWSTR],
                              _type.BOOL]
PathIsNetworkPathA: _Callable[[_type.LPCSTR],
                              _type.BOOL]
PathIsNetworkPathW: _Callable[[_type.LPCWSTR],
                              _type.BOOL]
PathIsPrefixA: _Callable[[_type.LPCSTR,
                          _type.LPCSTR],
                         _type.BOOL]
PathIsPrefixW: _Callable[[_type.LPCWSTR,
                          _type.LPCWSTR],
                         _type.BOOL]
PathIsRelativeA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
PathIsRelativeW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
PathIsRootA: _Callable[[_type.LPCSTR],
                       _type.BOOL]
PathIsRootW: _Callable[[_type.LPCWSTR],
                       _type.BOOL]
PathIsSameRootA: _Callable[[_type.LPCSTR,
                            _type.LPCSTR],
                           _type.BOOL]
PathIsSameRootW: _Callable[[_type.LPCWSTR,
                            _type.LPCWSTR],
                           _type.BOOL]
PathIsSystemFolderA: _Callable[[_type.LPCSTR,
                                _type.DWORD],
                               _type.BOOL]
PathIsSystemFolderW: _Callable[[_type.LPCWSTR,
                                _type.DWORD],
                               _type.BOOL]
PathIsUNCA: _Callable[[_type.LPCSTR],
                      _type.BOOL]
PathIsUNCW: _Callable[[_type.LPCWSTR],
                      _type.BOOL]
PathIsUNCServerA: _Callable[[_type.LPCSTR],
                            _type.BOOL]
PathIsUNCServerW: _Callable[[_type.LPCWSTR],
                            _type.BOOL]
PathIsUNCServerShareA: _Callable[[_type.LPCSTR],
                                 _type.BOOL]
PathIsUNCServerShareW: _Callable[[_type.LPCWSTR],
                                 _type.BOOL]
PathIsURLA: _Callable[[_type.LPCSTR],
                      _type.BOOL]
PathIsURLW: _Callable[[_type.LPCWSTR],
                      _type.BOOL]
PathMakeSystemFolderA: _Callable[[_type.LPCSTR],
                                 _type.BOOL]
PathMakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                 _type.BOOL]
PathRemoveFileSpecA: _Callable[[_type.LPSTR],
                               _type.BOOL]
PathRemoveFileSpecW: _Callable[[_type.LPWSTR],
                               _type.BOOL]
PathRenameExtensionA: _Callable[[_type.LPSTR,
                                 _type.LPCSTR],
                                _type.BOOL]
PathRenameExtensionW: _Callable[[_type.LPWSTR,
                                 _type.LPCWSTR],
                                _type.BOOL]
PathSearchAndQualifyA: _Callable[[_type.LPCSTR,
                                  _type.LPSTR,
                                  _type.UINT],
                                 _type.BOOL]
PathSearchAndQualifyW: _Callable[[_type.LPCWSTR,
                                  _type.LPWSTR,
                                  _type.UINT],
                                 _type.BOOL]
PathSkipRootA: _Callable[[_type.LPCSTR],
                         _type.LPSTR]
PathSkipRootW: _Callable[[_type.LPCWSTR],
                         _type.LPWSTR]
PathStripPathA: _Callable[[_type.LPSTR],
                          _type.c_void]
PathStripPathW: _Callable[[_type.LPWSTR],
                          _type.c_void]
PathStripToRootA: _Callable[[_type.LPCSTR],
                            _type.BOOL]
PathStripToRootW: _Callable[[_type.LPCWSTR],
                            _type.BOOL]
PathUndecorateA: _Callable[[_type.LPSTR],
                           _type.c_void]
PathUndecorateW: _Callable[[_type.LPWSTR],
                           _type.c_void]
PathUnExpandEnvStringsA: _Callable[[_type.LPCSTR,
                                    _type.LPSTR,
                                    _type.UINT],
                                   _type.BOOL]
PathUnExpandEnvStringsW: _Callable[[_type.LPCWSTR,
                                    _type.LPWSTR,
                                    _type.UINT],
                                   _type.BOOL]
PathUnmakeSystemFolderA: _Callable[[_type.LPCSTR],
                                   _type.BOOL]
PathUnmakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                   _type.BOOL]
PathUnquoteSpacesA: _Callable[[_type.LPCSTR],
                              _type.BOOL]
PathUnquoteSpacesW: _Callable[[_type.LPCWSTR],
                              _type.BOOL]
SHCreateMemStream: _Callable[[_Pointer[_type.BYTE],
                              _type.UINT],
                             _objidlbase.IStream]
SHCreateStreamOnFileA: _Callable[[_type.LPCSTR,  # pszFile
                                  _type.DWORD,  # grfMode
                                  _Pointer[_objidlbase.IStream]],  # ppstm
                                 _type.HRESULT]
SHCreateStreamOnFileW: _Callable[[_type.LPCWSTR,  # pszFile
                                  _type.DWORD,  # grfMode
                                  _Pointer[_objidlbase.IStream]],  # ppstm
                                 _type.HRESULT]
SHCreateStreamOnFileEx: _Callable[[_type.LPCWSTR,
                                   _type.DWORD,
                                   _type.DWORD,
                                   _type.BOOL,
                                   _Optional[_objidlbase.IStream],
                                   _Pointer[_objidlbase.IStream]],
                                  _type.HRESULT]
SHOpenRegStreamA: _Callable[[_type.HKEY,
                             _Optional[_type.LPCSTR],
                             _Optional[_type.LPCSTR],
                             _type.DWORD],
                            _objidlbase.IStream]
SHOpenRegStreamW: _Callable[[_type.HKEY,
                             _Optional[_type.LPCWSTR],
                             _Optional[_type.LPCWSTR],
                             _type.DWORD],
                            _objidlbase.IStream]
SHOpenRegStream2A: _Callable[[_type.HKEY,
                              _Optional[_type.LPCSTR],
                              _Optional[_type.LPCSTR],
                              _type.DWORD],
                             _objidlbase.IStream]
SHOpenRegStream2W: _Callable[[_type.HKEY,
                              _Optional[_type.LPCWSTR],
                              _Optional[_type.LPCWSTR],
                              _type.DWORD],
                             _objidlbase.IStream]
UrlGetLocationA: _Callable[[_type.PCSTR],
                           _type.LPCSTR]
UrlGetLocationW: _Callable[[_type.PCWSTR],
                           _type.LPCWSTR]
UrlIsA: _Callable[[_type.PCSTR,
                   _enum.URLIS],
                  _type.BOOL]
UrlIsW: _Callable[[_type.PCWSTR,
                   _enum.URLIS],
                  _type.BOOL]
UrlIsOpaqueA: _Callable[[_type.PCSTR],
                        _type.BOOL]
UrlIsOpaqueW: _Callable[[_type.PCWSTR],
                        _type.BOOL]
UrlIsNoHistoryA: _Callable[[_type.PCSTR],
                           _type.BOOL]
UrlIsNoHistoryW: _Callable[[_type.PCWSTR],
                           _type.BOOL]

_WinLib(__name__)
