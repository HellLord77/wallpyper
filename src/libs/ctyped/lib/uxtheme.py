from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# noinspection PyTypeChecker
OpenNcThemeData: _Callable[[_type.HWND,  # hWnd
                            _type.LPCWSTR],  # pszClassList
                           _type.HTHEME] = 49
# noinspection PyTypeChecker
RefreshImmersiveColorPolicyState: _Callable[[],
                                            _type.c_void] = 104
# noinspection PyTypeChecker
GetIsImmersiveColorUsingHighContrast: _Callable[[_enum.IMMERSIVE_HC_CACHE_MODE],  # mode
                                                _type.c_bool] = 106
# noinspection PyTypeChecker
ShouldAppsUseDarkMode: _Callable[[],
                                 _type.c_bool] = 132
# noinspection PyTypeChecker
AllowDarkModeForWindow: _Callable[[_type.HWND,  # hWnd
                                   _type.c_bool],  # allow
                                  _type.c_bool] = 133
# noinspection PyTypeChecker
SetPreferredAppMode: _Callable[[_enum.PreferredAppMode],  # appMode
                               _enum.PreferredAppMode] = 135
# noinspection PyTypeChecker
FlushMenuThemes: _Callable[[],
                           _type.c_void] = 136
# noinspection PyTypeChecker
IsDarkModeAllowedForWindow: _Callable[[],
                                      _type.c_bool] = 137
# noinspection PyTypeChecker
ShouldSystemUseDarkMode: _Callable[[],
                                   _type.c_bool] = 138
# noinspection PyTypeChecker
IsDarkModeAllowedForApp: _Callable[[],
                                   _type.c_bool] = 139
# Uxtheme
BeginPanningFeedback: _Callable[[_type.HWND],
                                _type.BOOL]
BufferedPaintInit: _Callable[[],
                             _type.HRESULT]
BufferedPaintUnInit: _Callable[[],
                               _type.HRESULT]
CloseThemeData: _Callable[[_type.HTHEME],
                          _type.HRESULT]
DrawThemeBackground: _Callable[[_type.HTHEME,
                                _type.HDC,
                                _type.c_int,
                                _type.c_int,
                                _Pointer[_struct.RECT],
                                _Optional[_Pointer[_struct.RECT]]],
                               _type.HRESULT]
DrawThemeBackgroundEx: _Callable[[_type.HTHEME,
                                  _type.HDC,
                                  _type.c_int,
                                  _type.c_int,
                                  _Pointer[_struct.RECT],
                                  _Optional[_Pointer[_struct.DTBGOPTS]]],
                                 _type.HRESULT]
DrawThemeEdge: _Callable[[_type.HTHEME,
                          _type.HDC,
                          _type.c_int,
                          _type.c_int,
                          _Pointer[_struct.RECT],
                          _type.UINT,
                          _type.UINT,
                          _Optional[_Pointer[_struct.RECT]]],
                         _type.HRESULT]
DrawThemeParentBackground: _Callable[[_type.HWND,
                                      _type.HDC,
                                      _Optional[_Pointer[_struct.RECT]]],
                                     _type.HRESULT]
DrawThemeParentBackgroundEx: _Callable[[_type.HWND,
                                        _type.HDC,
                                        _type.DWORD,
                                        _Optional[_Pointer[_struct.RECT]]],
                                       _type.HRESULT]
DrawThemeText: _Callable[[_type.HTHEME,
                          _type.HDC,
                          _type.c_int,
                          _type.c_int,
                          _type.LPCWSTR,
                          _type.c_int,
                          _type.DWORD,
                          _type.DWORD,
                          _Pointer[_struct.RECT]],
                         _type.HRESULT]
EnableTheming: _Callable[[_type.BOOL],
                         _type.HRESULT]
EnableThemeDialogTexture: _Callable[[_type.HWND,
                                     _type.DWORD],
                                    _type.HRESULT]
EndPanningFeedback: _Callable[[_type.HWND,
                               _type.BOOL],
                              _type.BOOL]
GetCurrentThemeName: _Callable[[_type.LPWSTR,
                                _type.c_int,
                                _Optional[_type.LPWSTR],
                                _type.c_int,
                                _Optional[_type.LPWSTR],
                                _type.c_int],
                               _type.HRESULT]
GetThemeBackgroundExtent: _Callable[[_type.HTHEME,
                                     _Optional[_type.HDC],
                                     _type.c_int,
                                     _type.c_int,
                                     _Pointer[_struct.RECT],
                                     _Pointer[_struct.RECT]],
                                    _type.HRESULT]
GetThemeBackgroundContentRect: _Callable[[_type.HTHEME,
                                          _Optional[_type.HDC],
                                          _type.c_int,
                                          _type.c_int,
                                          _Pointer[_struct.RECT],
                                          _Pointer[_struct.RECT]],
                                         _type.HRESULT]
GetThemeBackgroundRegion: _Callable[[_type.HTHEME,
                                     _Optional[_type.HDC],
                                     _type.c_int,
                                     _type.c_int,
                                     _Pointer[_struct.RECT],
                                     _Pointer[_type.HRGN]],
                                    _type.HRESULT]
GetThemeBool: _Callable[[_type.HTHEME,
                         _type.c_int,
                         _type.c_int,
                         _type.c_int,
                         _Pointer[_type.BOOL]],
                        _type.HRESULT]
GetThemeColor: _Callable[[_type.HTHEME,
                          _type.c_int,
                          _type.c_int,
                          _type.c_int,
                          _Pointer[_type.COLORREF]],
                         _type.HRESULT]
GetThemeEnumValue: _Callable[[_type.HTHEME,
                              _type.c_int,
                              _type.c_int,
                              _type.c_int,
                              _Pointer[_type.c_int]],
                             _type.HRESULT]
GetThemeDocumentationProperty: _Callable[[_type.LPCWSTR,
                                          _type.LPCWSTR,
                                          _type.LPWSTR,
                                          _type.c_int],
                                         _type.HRESULT]
GetThemeFilename: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _type.LPWSTR,
                             _type.c_int],
                            _type.HRESULT]
GetThemeFont: _Callable[[_type.HTHEME,
                         _Optional[_type.HDC],
                         _type.c_int,
                         _type.c_int,
                         _type.c_int,
                         _Pointer[_struct.LOGFONTW]],
                        _type.HRESULT]
GetThemeInt: _Callable[[_type.HTHEME,
                        _type.c_int,
                        _type.c_int,
                        _type.c_int,
                        _Pointer[_type.c_int]],
                       _type.HRESULT]
GetThemeIntList: _Callable[[_type.HTHEME,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Pointer[_struct.INTLIST]],
                           _type.HRESULT]
GetThemeMargins: _Callable[[_type.HTHEME,
                            _Optional[_type.HDC],
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Optional[_Pointer[_struct.RECT]],
                            _Pointer[_struct.MARGINS]],
                           _type.HRESULT]
GetThemeMetric: _Callable[[_type.HTHEME,
                           _Optional[_type.HDC],
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _Pointer[_type.c_int]],
                          _type.HRESULT]
GetThemePartSize: _Callable[[_type.HTHEME,
                             _Optional[_type.HDC],
                             _type.c_int,
                             _type.c_int,
                             _Optional[_Pointer[_struct.RECT]],
                             _enum.THEMESIZE,
                             _Pointer[_struct.SIZE]],
                            _type.HRESULT]
GetThemePosition: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_struct.POINT]],
                            _type.HRESULT]
GetThemeAppProperties: _Callable[[],
                                 _type.DWORD]
GetThemePropertyOrigin: _Callable[[_type.HTHEME,
                                   _type.c_int,
                                   _type.c_int,
                                   _type.c_int,
                                   _Pointer[_enum.PROPERTYORIGIN]],
                                  _type.HRESULT]
GetThemeRect: _Callable[[_type.HTHEME,
                         _type.c_int,
                         _type.c_int,
                         _type.c_int,
                         _Pointer[_struct.RECT]],
                        _type.HRESULT]
GetThemeString: _Callable[[_type.HTHEME,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.LPWSTR,
                           _type.c_int],
                          _type.HRESULT]
GetThemeSysBool: _Callable[[_Optional[_type.HTHEME],
                            _type.c_int],
                           _type.BOOL]
GetThemeSysColor: _Callable[[_Optional[_type.HTHEME],
                             _type.c_int],
                            _type.COLORREF]
GetThemeSysColorBrush: _Callable[[_Optional[_type.HTHEME],
                                  _type.c_int],
                                 _type.HBRUSH]
GetThemeSysFont: _Callable[[_Optional[_type.HTHEME],
                            _type.c_int,
                            _Pointer[_struct.LOGFONTW]],
                           _type.HRESULT]
GetThemeSysInt: _Callable[[_type.HTHEME,
                           _type.c_int,
                           _Pointer[_type.c_int]],
                          _type.HRESULT]
GetThemeSysSize: _Callable[[_Optional[_type.HTHEME],
                            _type.c_int],
                           _type.c_int]
GetThemeSysString: _Callable[[_type.HTHEME,
                              _type.c_int,
                              _type.LPWSTR,
                              _type.c_int],
                             _type.HRESULT]
GetThemeTextExtent: _Callable[[_type.HTHEME,
                               _type.HDC,
                               _type.c_int,
                               _type.c_int,
                               _type.LPCWSTR,
                               _type.c_int,
                               _type.DWORD,
                               _Optional[_Pointer[_struct.RECT]],
                               _Pointer[_struct.RECT]],
                              _type.HRESULT]
GetThemeTextMetrics: _Callable[[_type.HTHEME,
                                _type.HDC,
                                _type.c_int,
                                _type.c_int,
                                _struct.TEXTMETRICW],
                               _type.HRESULT]
HitTestThemeBackground: _Callable[[_type.HTHEME,
                                   _Optional[_type.HDC],
                                   _type.c_int,
                                   _type.c_int,
                                   _type.DWORD,
                                   _Pointer[_struct.RECT],
                                   _Optional[_type.HRGN],
                                   _struct.POINT,
                                   _Pointer[_type.WORD]],
                                  _type.HRESULT]
IsAppThemed: _Callable[[],
                       _type.BOOL]
IsCompositionActive: _Callable[[],
                               _type.BOOL]
IsThemeActive: _Callable[[],
                         _type.BOOL]
IsThemeBackgroundPartiallyTransparent: _Callable[[_type.HTHEME,
                                                  _type.c_int,
                                                  _type.c_int],
                                                 _type.BOOL]
IsThemeDialogTextureEnabled: _Callable[[_type.HWND],
                                       _type.BOOL]
IsThemePartDefined: _Callable[[_type.HTHEME,
                               _type.c_int,
                               _type.c_int],
                              _type.BOOL]
OpenThemeData: _Callable[[_Optional[_type.HWND],
                          _type.LPCWSTR],
                         _type.HTHEME]
OpenThemeDataEx: _Callable[[_Optional[_type.HWND],
                            _type.LPCWSTR,
                            _type.DWORD],
                           _type.HTHEME]
OpenThemeDataForDpi: _Callable[[_Optional[_type.HWND],
                                _type.LPCWSTR,
                                _type.UINT],
                               _type.HTHEME]
GetWindowTheme: _Callable[[_type.HWND],
                          _type.HTHEME]
SetWindowThemeAttribute: _Callable[[_type.HWND,
                                    _enum.WINDOWTHEMEATTRIBUTETYPE,
                                    _type.PVOID,
                                    _type.DWORD],
                                   _type.HRESULT]
SetThemeAppProperties: _Callable[[_type.DWORD],
                                 _type.c_void]
SetWindowTheme: _Callable[[_type.HWND,
                           _Optional[_type.LPCWSTR],
                           _Optional[_type.LPCWSTR]],
                          _type.HRESULT]
UpdatePanningFeedback: _Callable[[_type.HWND,
                                  _type.LONG,
                                  _type.LONG,
                                  _type.BOOL],
                                 _type.BOOL]

_WinLib(__name__)
