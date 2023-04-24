from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IAccessible(_oaidl.IDispatch):
    get_accParent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppdispParent
                             _type.HRESULT]
    get_accChildCount: _Callable[[_Pointer[_type.c_long]],  # pcountChildren
                                 _type.HRESULT]
    get_accChild: _Callable[[_struct.VARIANT,  # varChild
                             _Pointer[_oaidl.IDispatch]],  # ppdispChild
                            _type.HRESULT]
    get_accName: _Callable[[_struct.VARIANT,  # varChild
                            _Pointer[_type.BSTR]],  # pszName
                           _type.HRESULT]
    get_accValue: _Callable[[_struct.VARIANT,  # varChild
                             _Pointer[_type.BSTR]],  # pszValue
                            _type.HRESULT]
    get_accDescription: _Callable[[_struct.VARIANT,  # varChild
                                   _Pointer[_type.BSTR]],  # pszDescription
                                  _type.HRESULT]
    get_accRole: _Callable[[_struct.VARIANT,  # varChild
                            _Pointer[_struct.VARIANT]],  # pvarRole
                           _type.HRESULT]
    get_accState: _Callable[[_struct.VARIANT,  # varChild
                             _Pointer[_struct.VARIANT]],  # pvarState
                            _type.HRESULT]
    get_accHelp: _Callable[[_struct.VARIANT,  # varChild
                            _Pointer[_type.BSTR]],  # pszHelp
                           _type.HRESULT]
    get_accHelpTopic: _Callable[[_Pointer[_type.BSTR],  # pszHelpFile
                                 _struct.VARIANT,  # varChild
                                 _Pointer[_type.c_long]],  # pidTopic
                                _type.HRESULT]
    get_accKeyboardShortcut: _Callable[[_struct.VARIANT,  # varChild
                                        _Pointer[_type.BSTR]],  # pszKeyboardShortcut
                                       _type.HRESULT]
    get_accFocus: _Callable[[_Pointer[_struct.VARIANT]],  # pvarChild
                            _type.HRESULT]
    get_accSelection: _Callable[[_Pointer[_struct.VARIANT]],  # pvarChildren
                                _type.HRESULT]
    get_accDefaultAction: _Callable[[_struct.VARIANT,  # varChild
                                     _Pointer[_type.BSTR]],  # pszDefaultAction
                                    _type.HRESULT]
    accSelect: _Callable[[_type.c_long,  # flagsSelect
                          _struct.VARIANT],  # varChild
                         _type.HRESULT]
    accLocation: _Callable[[_Pointer[_type.c_long],  # pxLeft
                            _Pointer[_type.c_long],  # pyTop
                            _Pointer[_type.c_long],  # pcxWidth
                            _Pointer[_type.c_long],  # pcyHeight
                            _struct.VARIANT],  # varChild
                           _type.HRESULT]
    accNavigate: _Callable[[_type.c_long,  # navDir
                            _struct.VARIANT,  # varStart
                            _Pointer[_struct.VARIANT]],  # pvarEndUpAt
                           _type.HRESULT]
    accHitTest: _Callable[[_type.c_long,  # xLeft
                           _type.c_long,  # yTop
                           _Pointer[_struct.VARIANT]],  # pvarChild
                          _type.HRESULT]
    accDoDefaultAction: _Callable[[_struct.VARIANT],  # varChild
                                  _type.HRESULT]
    put_accName: _Callable[[_struct.VARIANT,  # varChild
                            _type.BSTR],  # szName
                           _type.HRESULT]
    put_accValue: _Callable[[_struct.VARIANT,  # varChild
                             _type.BSTR],  # szValue
                            _type.HRESULT]


class IAccessibleHandler(_Unknwnbase.IUnknown):
    AccessibleObjectFromID: _Callable[[_type.c_long,  # hwnd
                                       _type.c_long,  # lObjectID
                                       _Pointer[IAccessible]],  # pIAccessible
                                      _type.HRESULT]


class IAccessibleWindowlessSite(_Unknwnbase.IUnknown):
    AcquireObjectIdRange: _Callable[[_type.c_long,  # rangeSize
                                     IAccessibleHandler,  # pRangeOwner
                                     _Pointer[_type.c_long]],  # pRangeBase
                                    _type.HRESULT]
    ReleaseObjectIdRange: _Callable[[_type.c_long,  # rangeBase
                                     IAccessibleHandler],  # pRangeOwner
                                    _type.HRESULT]
    QueryObjectIdRanges: _Callable[[IAccessibleHandler,  # pRangesOwner
                                    _Pointer[_Pointer[_struct.SAFEARRAY]]],  # psaRanges
                                   _type.HRESULT]
    GetParentAccessible: _Callable[[_Pointer[IAccessible]],  # ppParent
                                   _type.HRESULT]


class IAccIdentity(_Unknwnbase.IUnknown):
    GetIdentityString: _Callable[[_type.DWORD,  # dwIDChild
                                  _Pointer[_Pointer[_type.BYTE]],  # ppIDString
                                  _Pointer[_type.DWORD]],  # pdwIDStringLen
                                 _type.HRESULT]


class IAccPropServer(_Unknwnbase.IUnknown):
    GetPropValue: _Callable[[_Pointer[_type.BYTE],  # pIDString
                             _type.DWORD,  # dwIDStringLen
                             _struct.MSAAPROPID,  # idProp
                             _Pointer[_struct.VARIANT],  # pvarValue
                             _Pointer[_type.BOOL]],  # pfHasProp
                            _type.HRESULT]


class IAccPropServices(_Unknwnbase.IUnknown):
    SetPropValue: _Callable[[_Pointer[_type.BYTE],  # pIDString
                             _type.DWORD,  # dwIDStringLen
                             _struct.MSAAPROPID,  # idProp
                             _struct.VARIANT],  # var
                            _type.HRESULT]
    SetPropServer: _Callable[[_Pointer[_type.BYTE],  # pIDString
                              _type.DWORD,  # dwIDStringLen
                              _Pointer[_struct.MSAAPROPID],  # paProps
                              _type.c_int,  # cProps
                              IAccPropServer,  # pServer
                              _enum.AnnoScope],  # annoScope
                             _type.HRESULT]
    ClearProps: _Callable[[_Pointer[_type.BYTE],  # pIDString
                           _type.DWORD,  # dwIDStringLen
                           _Pointer[_struct.MSAAPROPID],  # paProps
                           _type.c_int],  # cProps
                          _type.HRESULT]
    SetHwndProp: _Callable[[_type.HWND,  # hwnd
                            _type.DWORD,  # idObject
                            _type.DWORD,  # idChild
                            _struct.MSAAPROPID,  # idProp
                            _struct.VARIANT],  # var
                           _type.HRESULT]
    SetHwndPropStr: _Callable[[_type.HWND,  # hwnd
                               _type.DWORD,  # idObject
                               _type.DWORD,  # idChild
                               _struct.MSAAPROPID,  # idProp
                               _type.LPCWSTR],  # str
                              _type.HRESULT]
    SetHwndPropServer: _Callable[[_type.HWND,  # hwnd
                                  _type.DWORD,  # idObject
                                  _type.DWORD,  # idChild
                                  _Pointer[_struct.MSAAPROPID],  # paProps
                                  _type.c_int,  # cProps
                                  IAccPropServer,  # pServer
                                  _enum.AnnoScope],  # annoScope
                                 _type.HRESULT]
    ClearHwndProps: _Callable[[_type.HWND,  # hwnd
                               _type.DWORD,  # idObject
                               _type.DWORD,  # idChild
                               _Pointer[_struct.MSAAPROPID],  # paProps
                               _type.c_int],  # cProps
                              _type.HRESULT]
    ComposeHwndIdentityString: _Callable[[_type.HWND,  # hwnd
                                          _type.DWORD,  # idObject
                                          _type.DWORD,  # idChild
                                          _Pointer[_Pointer[_type.BYTE]],  # ppIDString
                                          _Pointer[_type.DWORD]],  # pdwIDStringLen
                                         _type.HRESULT]
    DecomposeHwndIdentityString: _Callable[[_Pointer[_type.BYTE],  # pIDString
                                            _type.DWORD,  # dwIDStringLen
                                            _Pointer[_type.HWND],  # phwnd
                                            _Pointer[_type.DWORD],  # pidObject
                                            _Pointer[_type.DWORD]],  # pidChild
                                           _type.HRESULT]
    SetHmenuProp: _Callable[[_type.HMENU,  # hmenu
                             _type.DWORD,  # idChild
                             _struct.MSAAPROPID,  # idProp
                             _struct.VARIANT],  # var
                            _type.HRESULT]
    SetHmenuPropStr: _Callable[[_type.HMENU,  # hmenu
                                _type.DWORD,  # idChild
                                _struct.MSAAPROPID,  # idProp
                                _type.LPCWSTR],  # str
                               _type.HRESULT]
    SetHmenuPropServer: _Callable[[_type.HMENU,  # hmenu
                                   _type.DWORD,  # idChild
                                   _Pointer[_struct.MSAAPROPID],  # paProps
                                   _type.c_int,  # cProps
                                   IAccPropServer,  # pServer
                                   _enum.AnnoScope],  # annoScope
                                  _type.HRESULT]
    ClearHmenuProps: _Callable[[_type.HMENU,  # hmenu
                                _type.DWORD,  # idChild
                                _Pointer[_struct.MSAAPROPID],  # paProps
                                _type.c_int],  # cProps
                               _type.HRESULT]
    ComposeHmenuIdentityString: _Callable[[_type.HMENU,  # hmenu
                                           _type.DWORD,  # idChild
                                           _Pointer[_Pointer[_type.BYTE]],  # ppIDString
                                           _Pointer[_type.DWORD]],  # pdwIDStringLen
                                          _type.HRESULT]
    DecomposeHmenuIdentityString: _Callable[[_Pointer[_type.BYTE],  # pIDString
                                             _type.DWORD,  # dwIDStringLen
                                             _Pointer[_type.HMENU],  # phmenu
                                             _Pointer[_type.DWORD]],  # pidChild
                                            _type.HRESULT]
