from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .. import union as _union
from .._utils import _Pointer
from ..interface.um import ShObjIdl_core as _ShObjIdl_core
from ..interface.um import objidl as _objidl
from ..interface.um import propsys as _propsys

# noinspection PyTypeChecker
GUIDFromStringA: _Callable[[_type.LPCSTR,
                            _Pointer[_struct.GUID]],
                           _type.BOOL] = 703
# noinspection PyTypeChecker
GUIDFromStringW: _Callable[[_type.LPCWSTR,
                            _Pointer[_struct.GUID]],
                           _type.BOOL] = 704
DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                         _type.HRESULT]
# shellapi
SHGetFileInfoA: _Callable[[_type.LPCSTR,  # pszPath
                           _type.DWORD,  # dwFileAttributes
                           _Pointer[_struct.SHFILEINFOA],  # psfi
                           _type.UINT,  # cbFileInfo
                           _type.UINT],  # uFlags
                          _type.DWORD_PTR]
SHGetFileInfoW: _Callable[[_type.LPCWSTR,  # pszPath
                           _type.DWORD,  # dwFileAttributes
                           _Pointer[_struct.SHFILEINFOW],  # psfi
                           _type.UINT,  # cbFileInfo
                           _type.UINT],  # uFlags
                          _type.DWORD_PTR]
# TODO
InitNetworkAddressControl: _Callable[[],
                                     _type.BOOL]
ShellExecuteA: _Callable[[_Optional[_type.HWND],
                          _Optional[_type.LPCSTR],
                          _type.LPCSTR,
                          _Optional[_type.LPCSTR],
                          _Optional[_type.LPCSTR],
                          _type.INT],
                         _type.HINSTANCE]
ShellExecuteW: _Callable[[_Optional[_type.HWND],
                          _Optional[_type.LPCWSTR],
                          _type.LPCWSTR,
                          _Optional[_type.LPCWSTR],
                          _Optional[_type.LPWSTR],
                          _type.INT],
                         _type.HINSTANCE]
ShellExecuteExA: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOA]],
                           _type.BOOL]
ShellExecuteExW: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOW]],
                           _type.BOOL]
Shell_NotifyIconA: _Callable[[_type.DWORD,
                              _Pointer[_struct.NOTIFYICONDATAA]],
                             _type.BOOL]
Shell_NotifyIconW: _Callable[[_type.DWORD,
                              _Pointer[_struct.NOTIFYICONDATAW]],
                             _type.BOOL]
Shell_NotifyIconGetRect: _Callable[[_Pointer[_struct.NOTIFYICONIDENTIFIER],
                                    _Pointer[_struct.RECT]],
                                   _type.BOOL]
SHEmptyRecycleBinA: _Callable[[_Optional[_type.HWND],
                               _Optional[_type.LPCSTR],
                               _type.DWORD],
                              _type.BOOL]
SHEmptyRecycleBinW: _Callable[[_Optional[_type.HWND],
                               _Optional[_type.LPCWSTR],
                               _type.DWORD],
                              _type.BOOL]
SHGetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                 _type.BOOL]
SHGetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                  _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                 _type.BOOL]
SHGetDriveMedia: _Callable[[_type.PCWSTR,
                            _Pointer[_type.DWORD]],
                           _type.UINT]
SHGetStockIconInfo: _Callable[[_enum.SHSTOCKICONID,
                               _type.UINT,
                               _Pointer[_struct.SHSTOCKICONINFO]],
                              _type.HRESULT]
SHQueryUserNotificationState: _Callable[[_Pointer[_enum.QUERY_USER_NOTIFICATION_STATE]],
                                        _type.HRESULT]
SHQueryRecycleBinA: _Callable[[_Optional[_type.LPCSTR],
                               _Pointer[_struct.SHQUERYRBINFO]],
                              _type.HRESULT]
SHQueryRecycleBinW: _Callable[[_Optional[_type.LPCWSTR],
                               _Pointer[_struct.SHQUERYRBINFO]],
                              _type.HRESULT]
# ShlObj_core
ILAppendID: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]],  # pidl
                       _Pointer[_struct.SHITEMID],  # pmkid
                       _type.BOOL],  # fAppend
                      _Pointer[_struct.ITEMIDLIST]]
SHGetPathFromIDListEx: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                  _type.PWSTR,  # pszPath
                                  _type.DWORD,  # cchPath
                                  _type.GPFIDL_FLAGS],  # uOpts
                                 _type.BOOL]
SHGetPathFromIDListA: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                 _type.LPSTR],  # pszPath
                                _type.BOOL]
SHGetPathFromIDListW: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                 _type.LPWSTR],  # pszPath
                                _type.BOOL]
SHCreateDirectory: _Callable[[_Optional[_type.HWND],  # hwnd
                              _type.PCWSTR],  # pszPath
                             _type.c_int]
SHCreateDirectoryExA: _Callable[[_Optional[_type.HWND],  # hwnd
                                 _type.LPCSTR,  # pszPath
                                 _Pointer[_struct.SECURITY_ATTRIBUTES]],  # psa
                                _type.c_int]
SHCreateDirectoryExW: _Callable[[_Optional[_type.HWND],  # hwnd
                                 _type.LPCWSTR,  # pszPath
                                 _Pointer[_struct.SECURITY_ATTRIBUTES]],  # psa
                                _type.c_int]
SHGetSpecialFolderLocation: _Callable[[_type.HWND,  # hwnd
                                       _type.c_int,  # csidl
                                       _Pointer[_struct.ITEMIDLIST]],  # ppidl
                                      _type.HRESULT]
SHCloneSpecialIDList: _Callable[[_type.HWND,  # hwnd
                                 _type.c_int,  # csidl
                                 _type.BOOL],  # fCreate
                                _Pointer[_struct.ITEMIDLIST]]
SHGetSpecialFolderPathA: _Callable[[_type.HWND,  # hwnd
                                    _type.LPSTR,  # pszPath
                                    _type.c_int,  # csidl
                                    _type.BOOL],  # fCreate
                                   _type.BOOL]
SHGetSpecialFolderPathW: _Callable[[_type.HWND,  # hwnd
                                    _type.LPWSTR,  # pszPath
                                    _type.c_int,  # csidl
                                    _type.BOOL],  # fCreate
                                   _type.BOOL]
SHFlushSFCache: _Callable[[],
                          _type.c_void]
SHGetFolderPathA: _Callable[[_Optional[_type.HWND],  # hwnd
                             _type.c_int,  # csidl
                             _Optional[_type.HANDLE],  # hToken
                             _type.DWORD,  # dwFlags
                             _type.LPSTR],  # pszPath
                            _type.HRESULT]
SHGetFolderPathW: _Callable[[_Optional[_type.HWND],  # hwnd
                             _type.c_int,  # csidl
                             _Optional[_type.HANDLE],  # hToken
                             _type.DWORD,  # dwFlags
                             _type.LPWSTR],  # pszPath
                            _type.HRESULT]
SHGetFolderLocation: _Callable[[_type.HWND,  # hwnd
                                _type.c_int,  # csidl
                                _Optional[_type.HANDLE],  # hToken
                                _type.DWORD,  # dwFlags
                                _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                               _type.HRESULT]
SHSetFolderPathA: _Callable[[_type.c_int,  # csidl
                             _Optional[_type.HANDLE],  # hToken
                             _type.DWORD,  # dwFlags
                             _type.LPCSTR],  # pszPath
                            _type.HRESULT]
SHSetFolderPathW: _Callable[[_type.c_int,  # csidl
                             _Optional[_type.HANDLE],  # hToken
                             _type.DWORD,  # dwFlags
                             _type.LPCWSTR],  # pszPath
                            _type.HRESULT]
SHGetFolderPathAndSubDirA: _Callable[[_type.HWND,  # hwnd
                                      _type.c_int,  # csidl
                                      _Optional[_type.HANDLE],  # hToken
                                      _type.DWORD,  # dwFlags
                                      _Optional[_type.LPCSTR],  # pszSubDir
                                      _type.LPSTR],  # pszPath
                                     _type.HRESULT]
SHGetFolderPathAndSubDirW: _Callable[[_type.HWND,  # hwnd
                                      _type.c_int,  # csidl
                                      _Optional[_type.HANDLE],  # hToken
                                      _type.DWORD,  # dwFlags
                                      _Optional[_type.LPCWSTR],  # pszSubDir
                                      _type.LPWSTR],  # pszPath
                                     _type.HRESULT]
SHParseDisplayName: _Callable[[_type.PCWSTR,  # pszName
                               _Optional[_objidl.IBindCtx],  # pbc
                               _Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidl
                               _type.SFGAOF,  # sfgaoIn
                               _Optional[_Pointer[_type.SFGAOF]]],  # psfgaoOut
                              _type.HRESULT]
# TODO
GetCurrentProcessExplicitAppUserModelID: _Callable[[_Pointer[_type.PWSTR]],
                                                   _type.HRESULT]
ILClone: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                   _Pointer[_struct.ITEMIDLIST]]
ILCloneFirst: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                        _Pointer[_struct.ITEMIDLIST]]
ILCombine: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]],
                      _Optional[_Pointer[_struct.ITEMIDLIST]]],
                     _Pointer[_struct.ITEMIDLIST]]
ILCreateFromPath: _Callable[[_type.PCWSTR],
                            _Pointer[_struct.ITEMIDLIST]]
ILCreateFromPathA: _Callable[[_type.PCSTR],
                             _Pointer[_struct.ITEMIDLIST]]
ILCreateFromPathW: _Callable[[_type.PCWSTR],
                             _Pointer[_struct.ITEMIDLIST]]
ILFindChild: _Callable[[_Pointer[_struct.ITEMIDLIST],
                        _Pointer[_struct.ITEMIDLIST]],
                       _Pointer[_struct.ITEMIDLIST]]
ILFindLastID: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                        _Pointer[_struct.ITEMIDLIST]]
ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                  _type.c_void]
ILGetNext: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                     _Pointer[_struct.ITEMIDLIST]]
ILGetSize: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                     _type.UINT]
ILIsEqual: _Callable[[_Pointer[_struct.ITEMIDLIST],
                      _Pointer[_struct.ITEMIDLIST]],
                     _type.BOOL]
ILIsParent: _Callable[[_Pointer[_struct.ITEMIDLIST],
                       _Pointer[_struct.ITEMIDLIST],
                       _type.BOOL],
                      _type.BOOL]
ILRemoveLastID: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                          _type.BOOL]
PathCleanupSpec: _Callable[[_Optional[_type.PCWSTR],
                            _type.PWSTR],
                           _type.c_int]
SetCurrentProcessExplicitAppUserModelID: _Callable[[_type.PCWSTR],
                                                   _type.HRESULT]
SHBrowseForFolderA: _Callable[[_Pointer[_struct.BROWSEINFOA]],
                              _Pointer[_Pointer[_struct.ITEMIDLIST]]]
SHBrowseForFolderW: _Callable[[_Pointer[_struct.BROWSEINFOW]],
                              _Pointer[_Pointer[_struct.ITEMIDLIST]]]
SHChangeNotify: _Callable[[_type.LONG,
                           _type.UINT,
                           _Optional[_type.LPCVOID],
                           _Optional[_type.LPCVOID]],
                          _type.c_void]
SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST],
                                       _type.UINT,
                                       _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                                       _type.DWORD],
                                      _type.SHSTDAPI]
SHOpenWithDialog: _Callable[[_Optional[_type.HWND],
                             _Pointer[_struct.OPENASINFO]],
                            _type.SHSTDAPI]
# ShObjIdl_core
SHCreateItemFromParsingName: _Callable[[_type.PCWSTR,
                                        _Optional[_Pointer[_objidl.IBindCtx]],
                                        _Pointer[_struct.IID],
                                        _Pointer[_ShObjIdl_core.IShellItem]],
                                       _type.SHSTDAPI]
SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                              _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                              _Pointer[_ShObjIdl_core.IShellItemArray]],
                                             _type.SHSTDAPI]
SHGetKnownFolderPath: _Callable[[_Pointer[_struct.KNOWNFOLDERID],
                                 _type.DWORD,
                                 _Optional[_type.HANDLE],
                                 _Pointer[_type.PWSTR]],
                                _type.HRESULT]
SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                              _Optional[_Pointer[_objidl.IBindCtx]],
                                              _enum.GETPROPERTYSTOREFLAGS,
                                              _Pointer[_struct.IID],
                                              _Pointer[_propsys.IPropertyStore]],
                                             _type.SHSTDAPI]

_WinLib(__name__)
