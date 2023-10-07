from __future__ import annotations as _

from typing import Callable as _Callable

from . import Dimm as _Dimm
from . import DispEx as _DispEx
from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IHTMLFiltersCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]


class IIE70DispatchEx(_DispEx.IDispatchEx):
    pass


class IIE80DispatchEx(_DispEx.IDispatchEx):
    pass


class IHTMLEventObj(_oaidl.IDispatch):
    get_srcElement: _Callable[[_Pointer[IHTMLElement]],  # p
                              _type.HRESULT]
    get_altKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_ctrlKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_shiftKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_returnValue: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_returnValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_cancelBubble: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_cancelBubble: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    get_fromElement: _Callable[[_Pointer[IHTMLElement]],  # p
                               _type.HRESULT]
    get_toElement: _Callable[[_Pointer[IHTMLElement]],  # p
                             _type.HRESULT]
    put_keyCode: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_keyCode: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_button: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_qualifier: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_reason: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    get_clientX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_clientY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_offsetX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_offsetY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_screenX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_screenY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_srcFilter: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]


class IElementBehaviorSite(_Unknwnbase.IUnknown):
    GetElement: _Callable[[_Pointer[IHTMLElement]],  # ppElement
                          _type.HRESULT]
    RegisterNotification: _Callable[[_type.LONG],  # lEvent
                                    _type.HRESULT]


class IElementBehavior(_Unknwnbase.IUnknown):
    Init: _Callable[[IElementBehaviorSite],  # pBehaviorSite
                    _type.HRESULT]
    Notify: _Callable[[_type.LONG,  # lEvent
                       _Pointer[_struct.VARIANT]],  # pVar
                      _type.HRESULT]
    Detach: _Callable[[],
                      _type.HRESULT]


class IElementBehaviorFactory(_Unknwnbase.IUnknown):
    FindBehavior: _Callable[[_type.BSTR,  # bstrBehavior
                             _type.BSTR,  # bstrBehaviorUrl
                             IElementBehaviorSite,  # pSite
                             _Pointer[IElementBehavior]],  # ppBehavior
                            _type.HRESULT]


class IElementBehaviorSiteOM(_Unknwnbase.IUnknown):
    RegisterEvent: _Callable[[_type.LPOLESTR,  # pchEvent
                              _type.LONG,  # lFlags
                              _Pointer[_type.LONG]],  # plCookie
                             _type.HRESULT]
    GetEventCookie: _Callable[[_type.LPOLESTR,  # pchEvent
                               _Pointer[_type.LONG]],  # plCookie
                              _type.HRESULT]
    FireEvent: _Callable[[_type.LONG,  # lCookie
                          IHTMLEventObj],  # pEventObject
                         _type.HRESULT]
    CreateEventObject: _Callable[[_Pointer[IHTMLEventObj]],  # ppEventObject
                                 _type.HRESULT]
    RegisterName: _Callable[[_type.LPOLESTR],  # pchName
                            _type.HRESULT]
    RegisterUrn: _Callable[[_type.LPOLESTR],  # pchUrn
                           _type.HRESULT]


class IElementBehaviorRender(_Unknwnbase.IUnknown):
    Draw: _Callable[[_type.HDC,  # hdc
                     _type.LONG,  # lLayer
                     _Pointer[_struct.RECT],  # pRect
                     _Unknwnbase.IUnknown],  # pReserved
                    _type.HRESULT]
    GetRenderInfo: _Callable[[_Pointer[_type.LONG]],  # plRenderInfo
                             _type.HRESULT]
    HitTestPoint: _Callable[[_Pointer[_struct.POINT],  # pPoint
                             _Unknwnbase.IUnknown,  # pReserved
                             _Pointer[_type.BOOL]],  # pbHit
                            _type.HRESULT]


class IElementBehaviorSiteRender(_Unknwnbase.IUnknown):
    Invalidate: _Callable[[_Pointer[_struct.RECT]],  # pRect
                          _type.HRESULT]
    InvalidateRenderInfo: _Callable[[],
                                    _type.HRESULT]
    InvalidateStyle: _Callable[[],
                               _type.HRESULT]


class IDOMEvent(_oaidl.IDispatch):
    get_bubbles: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_cancelable: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    get_currentTarget: _Callable[[_Pointer[IEventTarget]],  # p
                                 _type.HRESULT]
    get_defaultPrevented: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    get_eventPhase: _Callable[[_Pointer[_type.USHORT]],  # p
                              _type.HRESULT]
    get_target: _Callable[[_Pointer[IEventTarget]],  # p
                          _type.HRESULT]
    get_timeStamp: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                             _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    initEvent: _Callable[[_type.BSTR,  # eventType
                          _type.VARIANT_BOOL,  # canBubble
                          _type.VARIANT_BOOL],  # cancelable
                         _type.HRESULT]
    preventDefault: _Callable[[],
                              _type.HRESULT]
    stopPropagation: _Callable[[],
                               _type.HRESULT]
    stopImmediatePropagation: _Callable[[],
                                        _type.HRESULT]
    get_isTrusted: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    put_cancelBubble: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_cancelBubble: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    get_srcElement: _Callable[[_Pointer[IHTMLElement]],  # p
                              _type.HRESULT]


class IHTMLDOMConstructor(_oaidl.IDispatch):
    get_constructor: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                               _type.HRESULT]
    LookupGetter: _Callable[[_type.BSTR,  # propname
                             _Pointer[_struct.VARIANT]],  # ppDispHandler
                            _type.HRESULT]
    LookupSetter: _Callable[[_type.BSTR,  # propname
                             _Pointer[_struct.VARIANT]],  # ppDispHandler
                            _type.HRESULT]
    DefineGetter: _Callable[[_type.BSTR,  # propname
                             _Pointer[_struct.VARIANT]],  # pdispHandler
                            _type.HRESULT]
    DefineSetter: _Callable[[_type.BSTR,  # propname
                             _Pointer[_struct.VARIANT]],  # pdispHandler
                            _type.HRESULT]


class IHTMLStyleSheetRule(_oaidl.IDispatch):
    put_selectorText: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_selectorText: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_style: _Callable[[_Pointer[IHTMLRuleStyle]],  # p
                         _type.HRESULT]
    get_readOnly: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]


class IHTMLCSSStyleDeclaration(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_parentRule: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    getPropertyValue: _Callable[[_type.BSTR,  # bstrPropertyName
                                 _Pointer[_type.BSTR]],  # pbstrPropertyValue
                                _type.HRESULT]
    getPropertyPriority: _Callable[[_type.BSTR,  # bstrPropertyName
                                    _Pointer[_type.BSTR]],  # pbstrPropertyPriority
                                   _type.HRESULT]
    removeProperty: _Callable[[_type.BSTR,  # bstrPropertyName
                               _Pointer[_type.BSTR]],  # pbstrPropertyValue
                              _type.HRESULT]
    setProperty: _Callable[[_type.BSTR,  # bstrPropertyName
                            _Pointer[_struct.VARIANT],  # pvarPropertyValue
                            _Pointer[_struct.VARIANT]],  # pvarPropertyPriority
                           _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_type.BSTR]],  # pbstrPropertyName
                    _type.HRESULT]
    put_fontFamily: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontFamily: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_fontStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_fontVariant: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_fontVariant: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_fontWeight: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontWeight: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontSize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_fontSize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_font: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_font: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_backgroundColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_backgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_backgroundImage: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_backgroundImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_backgroundRepeat: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_backgroundRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_backgroundAttachment: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_backgroundAttachment: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_backgroundPosition: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_backgroundPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_backgroundPositionX: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionX: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_backgroundPositionY: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionY: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_wordSpacing: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_wordSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_letterSpacing: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_letterSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textDecoration: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_textDecoration: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_verticalAlign: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_verticalAlign: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textTransform: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_textAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textIndent: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_textIndent: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_lineHeight: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_lineHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_marginTop: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_marginTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_marginRight: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_marginRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_marginBottom: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_marginBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_marginLeft: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_marginLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_margin: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_margin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_paddingTop: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_paddingTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_paddingRight: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_paddingRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_paddingBottom: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_paddingBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_paddingLeft: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_paddingLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_padding: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_padding: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_border: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_borderTop: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_borderTop: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderRight: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderRight: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderBottom: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_borderBottom: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_borderLeft: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_borderLeft: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_borderColor: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopColor: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightColor: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomColor: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderWidth: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopWidth: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightWidth: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomWidth: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftWidth: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderStyle: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopStyle: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderTopStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_borderRightStyle: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_borderRightStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_borderBottomStyle: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderBottomStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_borderLeftStyle: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_borderLeftStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_styleFloat: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_styleFloat: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_clear: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_display: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_display: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_visibility: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_visibility: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_listStyleType: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_listStyleType: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_listStylePosition: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_listStylePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_listStyleImage: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_listStyleImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_listStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_listStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_whiteSpace: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_whiteSpace: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_top: _Callable[[_struct.VARIANT],  # v
                       _type.HRESULT]
    get_top: _Callable[[_Pointer[_struct.VARIANT]],  # p
                       _type.HRESULT]
    put_left: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_left: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_zIndex: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_zIndex: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_overflow: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_overflow: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_pageBreakBefore: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakBefore: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_pageBreakAfter: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_pageBreakAfter: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_cssText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_cssText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_cursor: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_cursor: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_clip: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_clip: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_filter: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_filter: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_tableLayout: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_tableLayout: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderCollapse: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderCollapse: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_direction: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_behavior: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_behavior: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_position: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_unicodeBidi: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_unicodeBidi: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_bottom: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_bottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_right: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_right: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_imeMode: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_imeMode: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_rubyAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_rubyAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_rubyPosition: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_rubyOverhang: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyOverhang: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_layoutGridChar: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridChar: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridLine: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridLine: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridMode: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGridType: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridType: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGrid: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutGrid: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_textAutospace: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAutospace: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_wordBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_wordBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_lineBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_lineBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textJustify: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_textJustify: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textJustifyTrim: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_textJustifyTrim: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_textKashida: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_textKashida: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_overflowX: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowX: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_overflowY: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowY: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_accelerator: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_accelerator: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_layoutFlow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_zoom: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_zoom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_wordWrap: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_wordWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_textUnderlinePosition: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_textUnderlinePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_scrollbarBaseColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarBaseColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbarFaceColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarFaceColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbar3dLightColor: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_scrollbar3dLightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_scrollbarShadowColor: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_scrollbarShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_scrollbarHighlightColor: _Callable[[_struct.VARIANT],  # v
                                           _type.HRESULT]
    get_scrollbarHighlightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                           _type.HRESULT]
    put_scrollbarDarkShadowColor: _Callable[[_struct.VARIANT],  # v
                                            _type.HRESULT]
    get_scrollbarDarkShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                            _type.HRESULT]
    put_scrollbarArrowColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarArrowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_scrollbarTrackColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarTrackColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_writingMode: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_writingMode: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textAlignLast: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAlignLast: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textKashidaSpace: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_textKashidaSpace: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_textOverflow: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_textOverflow: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_minHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_minHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_msInterpolationMode: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msInterpolationMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_maxHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_maxHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_minWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_minWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_maxWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_maxWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_content: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_content: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_captionSide: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_captionSide: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_counterIncrement: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_counterIncrement: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_counterReset: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_counterReset: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outline: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_outline: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_outlineWidth: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_outlineStyle: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_outlineStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outlineColor: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_boxSizing: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_boxSizing: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderSpacing: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_borderSpacing: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_orphans: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_orphans: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_widows: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_widows: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_pageBreakInside: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakInside: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_emptyCells: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_emptyCells: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msBlockProgression: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_msBlockProgression: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_quotes: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_quotes: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_alignmentBaseline: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_alignmentBaseline: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_baselineShift: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_baselineShift: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_dominantBaseline: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_dominantBaseline: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_fontSizeAdjust: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_fontSizeAdjust: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_fontStretch: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_fontStretch: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_opacity: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_opacity: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_clipPath: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_clipPath: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_clipRule: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_clipRule: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_fill: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_fill: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_fillOpacity: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_fillOpacity: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_fillRule: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_fillRule: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_kerning: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_kerning: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_marker: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_marker: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_markerEnd: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_markerEnd: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_markerMid: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_markerMid: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_markerStart: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_markerStart: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_mask: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_mask: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_pointerEvents: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_pointerEvents: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_stopColor: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_stopColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_stopOpacity: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_stopOpacity: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_stroke: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_stroke: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_strokeDasharray: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_strokeDasharray: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_strokeDashoffset: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_strokeDashoffset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_strokeLinecap: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_strokeLinecap: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_strokeLinejoin: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_strokeLinejoin: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_strokeMiterlimit: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_strokeMiterlimit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_strokeOpacity: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_strokeOpacity: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_strokeWidth: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_strokeWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_textAnchor: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_textAnchor: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_glyphOrientationHorizontal: _Callable[[_struct.VARIANT],  # v
                                              _type.HRESULT]
    get_glyphOrientationHorizontal: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                              _type.HRESULT]
    put_glyphOrientationVertical: _Callable[[_struct.VARIANT],  # v
                                            _type.HRESULT]
    get_glyphOrientationVertical: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                            _type.HRESULT]
    put_borderRadius: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_borderRadius: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_borderTopLeftRadius: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_borderTopLeftRadius: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_borderTopRightRadius: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_borderTopRightRadius: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_borderBottomRightRadius: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_borderBottomRightRadius: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_borderBottomLeftRadius: _Callable[[_type.BSTR],  # v
                                          _type.HRESULT]
    get_borderBottomLeftRadius: _Callable[[_Pointer[_type.BSTR]],  # p
                                          _type.HRESULT]
    put_clipTop: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_clipTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_clipRight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_clipRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_clipBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_clipLeft: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_clipLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_cssFloat: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_cssFloat: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_backgroundClip: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_backgroundClip: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_backgroundOrigin: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_backgroundOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_backgroundSize: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_backgroundSize: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_boxShadow: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_boxShadow: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_msTransform: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_msTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_msTransformOrigin: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_msTransformOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]


class IHTMLCSSStyleDeclaration2(_oaidl.IDispatch):
    put_msScrollChaining: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_msScrollChaining: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msContentZooming: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_msContentZooming: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msContentZoomSnapType: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_msContentZoomSnapType: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_msScrollRails: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msScrollRails: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msContentZoomChaining: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_msContentZoomChaining: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_msScrollSnapType: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_msScrollSnapType: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msContentZoomLimit: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_msContentZoomLimit: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_msContentZoomSnap: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_msContentZoomSnap: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_msContentZoomSnapPoints: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_msContentZoomSnapPoints: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_msContentZoomLimitMin: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_msContentZoomLimitMin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_msContentZoomLimitMax: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_msContentZoomLimitMax: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_msScrollSnapX: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msScrollSnapX: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msScrollSnapY: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msScrollSnapY: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msScrollSnapPointsX: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msScrollSnapPointsX: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_msScrollSnapPointsY: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msScrollSnapPointsY: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_msGridColumn: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_msGridColumn: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_msGridColumnAlign: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_msGridColumnAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_msGridColumns: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msGridColumns: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msGridColumnSpan: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_msGridColumnSpan: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_msGridRow: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_msGridRow: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_msGridRowAlign: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_msGridRowAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_msGridRows: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msGridRows: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msGridRowSpan: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_msGridRowSpan: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_msWrapThrough: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msWrapThrough: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msWrapMargin: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_msWrapMargin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_msWrapFlow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msWrapFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msAnimationName: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_msAnimationName: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_msAnimationDuration: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msAnimationDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_msAnimationTimingFunction: _Callable[[_type.BSTR],  # v
                                             _type.HRESULT]
    get_msAnimationTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                             _type.HRESULT]
    put_msAnimationDelay: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_msAnimationDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msAnimationDirection: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msAnimationDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_msAnimationPlayState: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msAnimationPlayState: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_msAnimationIterationCount: _Callable[[_type.BSTR],  # v
                                             _type.HRESULT]
    get_msAnimationIterationCount: _Callable[[_Pointer[_type.BSTR]],  # p
                                             _type.HRESULT]
    put_msAnimation: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_msAnimation: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_msAnimationFillMode: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msAnimationFillMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_colorInterpolationFilters: _Callable[[_type.BSTR],  # v
                                             _type.HRESULT]
    get_colorInterpolationFilters: _Callable[[_Pointer[_type.BSTR]],  # p
                                             _type.HRESULT]
    put_columnCount: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_columnCount: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_columnWidth: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_columnWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_columnGap: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_columnGap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_columnFill: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_columnFill: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_columnSpan: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_columnSpan: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_columns: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_columns: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_columnRule: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_columnRule: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_columnRuleColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_columnRuleColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_columnRuleStyle: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_columnRuleStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_columnRuleWidth: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_columnRuleWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_breakBefore: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_breakBefore: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_breakAfter: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_breakAfter: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_breakInside: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_breakInside: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_floodColor: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_floodColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_floodOpacity: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_floodOpacity: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_lightingColor: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_lightingColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_msScrollLimitXMin: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_msScrollLimitXMin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_msScrollLimitYMin: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_msScrollLimitYMin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_msScrollLimitXMax: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_msScrollLimitXMax: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_msScrollLimitYMax: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_msScrollLimitYMax: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_msScrollLimit: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msScrollLimit: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textShadow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_textShadow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msFlowFrom: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msFlowFrom: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msFlowInto: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msFlowInto: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msHyphens: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_msHyphens: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_msHyphenateLimitZone: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_msHyphenateLimitZone: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_msHyphenateLimitChars: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_msHyphenateLimitChars: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_msHyphenateLimitLines: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_msHyphenateLimitLines: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_msHighContrastAdjust: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msHighContrastAdjust: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_enableBackground: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_enableBackground: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msFontFeatureSettings: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_msFontFeatureSettings: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_msUserSelect: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_msUserSelect: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_msOverflowStyle: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_msOverflowStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_msTransformStyle: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_msTransformStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_msBackfaceVisibility: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msBackfaceVisibility: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_msPerspective: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_msPerspective: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_msPerspectiveOrigin: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msPerspectiveOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_msTransitionProperty: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msTransitionProperty: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_msTransitionDuration: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_msTransitionDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_msTransitionTimingFunction: _Callable[[_type.BSTR],  # v
                                              _type.HRESULT]
    get_msTransitionTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                              _type.HRESULT]
    put_msTransitionDelay: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_msTransitionDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_msTransition: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_msTransition: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_msTouchAction: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msTouchAction: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_msScrollTranslation: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msScrollTranslation: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_msFlex: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_msFlex: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_msFlexPositive: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_msFlexPositive: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_msFlexNegative: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_msFlexNegative: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_msFlexPreferredSize: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_msFlexPreferredSize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_msFlexFlow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msFlexFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msFlexDirection: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_msFlexDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_msFlexWrap: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msFlexWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msFlexAlign: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_msFlexAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_msFlexItemAlign: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_msFlexItemAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_msFlexPack: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msFlexPack: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msFlexLinePack: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_msFlexLinePack: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_msFlexOrder: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_msFlexOrder: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_msTouchSelect: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_msTouchSelect: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_transform: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_transform: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_transformOrigin: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_transformOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_transformStyle: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_transformStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_backfaceVisibility: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_backfaceVisibility: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_perspective: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_perspective: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_perspectiveOrigin: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_perspectiveOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_transitionProperty: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_transitionProperty: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_transitionDuration: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_transitionDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_transitionTimingFunction: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_transitionTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_transitionDelay: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_transitionDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_transition: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_transition: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontFeatureSettings: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_fontFeatureSettings: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_animationName: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_animationName: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_animationDuration: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_animationDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_animationTimingFunction: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_animationTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_animationDelay: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_animationDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_animationDirection: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_animationDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_animationPlayState: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_animationPlayState: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_animationIterationCount: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_animationIterationCount: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_animation: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_animation: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_animationFillMode: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_animationFillMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]


class IHTMLCSSStyleDeclaration3(_oaidl.IDispatch):
    put_flex: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_flex: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_flexDirection: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_flexDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_flexWrap: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_flexWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_flexFlow: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_flexFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_flexGrow: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_flexGrow: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_flexShrink: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_flexShrink: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_flexBasis: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_flexBasis: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_justifyContent: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_justifyContent: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_alignItems: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_alignItems: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_alignSelf: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_alignSelf: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_alignContent: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_alignContent: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_borderImage: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderImage: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderImageSource: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderImageSource: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_borderImageSlice: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_borderImageSlice: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_borderImageWidth: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_borderImageWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_borderImageOutset: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderImageOutset: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_borderImageRepeat: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderImageRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_msImeAlign: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_msImeAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msTextCombineHorizontal: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_msTextCombineHorizontal: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_touchAction: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_touchAction: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class IHTMLCSSStyleDeclaration4(_oaidl.IDispatch):
    put_webkitAppearance: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_webkitAppearance: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_webkitUserSelect: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_webkitUserSelect: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_webkitBoxAlign: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_webkitBoxAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_webkitBoxOrdinalGroup: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_webkitBoxOrdinalGroup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_webkitBoxPack: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_webkitBoxPack: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_webkitBoxFlex: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_webkitBoxFlex: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_webkitBoxOrient: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_webkitBoxOrient: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_webkitBoxDirection: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_webkitBoxDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_webkitTransform: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_webkitTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_webkitBackgroundSize: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_webkitBackgroundSize: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_webkitBackfaceVisibility: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitBackfaceVisibility: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitAnimation: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_webkitAnimation: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_webkitTransition: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_webkitTransition: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_webkitAnimationName: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_webkitAnimationName: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_webkitAnimationDuration: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_webkitAnimationDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_webkitAnimationTimingFunction: _Callable[[_type.BSTR],  # v
                                                 _type.HRESULT]
    get_webkitAnimationTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                                 _type.HRESULT]
    put_webkitAnimationDelay: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_webkitAnimationDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_webkitAnimationIterationCount: _Callable[[_type.BSTR],  # v
                                                 _type.HRESULT]
    get_webkitAnimationIterationCount: _Callable[[_Pointer[_type.BSTR]],  # p
                                                 _type.HRESULT]
    put_webkitAnimationDirection: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitAnimationDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitAnimationPlayState: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitAnimationPlayState: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitTransitionProperty: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitTransitionProperty: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitTransitionDuration: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitTransitionDuration: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitTransitionTimingFunction: _Callable[[_type.BSTR],  # v
                                                  _type.HRESULT]
    get_webkitTransitionTimingFunction: _Callable[[_Pointer[_type.BSTR]],  # p
                                                  _type.HRESULT]
    put_webkitTransitionDelay: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_webkitTransitionDelay: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_webkitBackgroundAttachment: _Callable[[_type.BSTR],  # v
                                              _type.HRESULT]
    get_webkitBackgroundAttachment: _Callable[[_Pointer[_type.BSTR]],  # p
                                              _type.HRESULT]
    put_webkitBackgroundColor: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_webkitBackgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_webkitBackgroundClip: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_webkitBackgroundClip: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_webkitBackgroundImage: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_webkitBackgroundImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_webkitBackgroundRepeat: _Callable[[_type.BSTR],  # v
                                          _type.HRESULT]
    get_webkitBackgroundRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                          _type.HRESULT]
    put_webkitBackgroundOrigin: _Callable[[_type.BSTR],  # v
                                          _type.HRESULT]
    get_webkitBackgroundOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                          _type.HRESULT]
    put_webkitBackgroundPosition: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_webkitBackgroundPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_webkitBackgroundPositionX: _Callable[[_struct.VARIANT],  # v
                                             _type.HRESULT]
    get_webkitBackgroundPositionX: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                             _type.HRESULT]
    put_webkitBackgroundPositionY: _Callable[[_struct.VARIANT],  # v
                                             _type.HRESULT]
    get_webkitBackgroundPositionY: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                             _type.HRESULT]
    put_webkitBackground: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_webkitBackground: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_webkitTransformOrigin: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_webkitTransformOrigin: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_msTextSizeAdjust: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_msTextSizeAdjust: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_webkitTextSizeAdjust: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_webkitTextSizeAdjust: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_webkitBorderImage: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_webkitBorderImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_webkitBorderImageSource: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_webkitBorderImageSource: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_webkitBorderImageSlice: _Callable[[_type.BSTR],  # v
                                          _type.HRESULT]
    get_webkitBorderImageSlice: _Callable[[_Pointer[_type.BSTR]],  # p
                                          _type.HRESULT]
    put_webkitBorderImageWidth: _Callable[[_type.BSTR],  # v
                                          _type.HRESULT]
    get_webkitBorderImageWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                                          _type.HRESULT]
    put_webkitBorderImageOutset: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_webkitBorderImageOutset: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_webkitBorderImageRepeat: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_webkitBorderImageRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]
    put_webkitBoxSizing: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_webkitBoxSizing: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_webkitAnimationFillMode: _Callable[[_type.BSTR],  # v
                                           _type.HRESULT]
    get_webkitAnimationFillMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                           _type.HRESULT]


class IHTMLStyleEnabled(_oaidl.IDispatch):
    msGetPropertyEnabled: _Callable[[_type.BSTR,  # name
                                     _Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    msPutPropertyEnabled: _Callable[[_type.BSTR,  # name
                                     _type.VARIANT_BOOL],  # b
                                    _type.HRESULT]


class DispHTMLCSSStyleDeclaration(_oaidl.IDispatch):
    pass


class IHTMLStyle(_oaidl.IDispatch):
    put_fontFamily: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontFamily: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_fontStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_fontVariant: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_fontVariant: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_fontWeight: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontWeight: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontSize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_fontSize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_font: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_font: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_backgroundColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_backgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_backgroundImage: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_backgroundImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_backgroundRepeat: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_backgroundRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_backgroundAttachment: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_backgroundAttachment: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_backgroundPosition: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_backgroundPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_backgroundPositionX: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionX: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_backgroundPositionY: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionY: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_wordSpacing: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_wordSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_letterSpacing: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_letterSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textDecoration: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_textDecoration: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_textDecorationNone: _Callable[[_type.VARIANT_BOOL],  # v
                                      _type.HRESULT]
    get_textDecorationNone: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]
    put_textDecorationUnderline: _Callable[[_type.VARIANT_BOOL],  # v
                                           _type.HRESULT]
    get_textDecorationUnderline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                           _type.HRESULT]
    put_textDecorationOverline: _Callable[[_type.VARIANT_BOOL],  # v
                                          _type.HRESULT]
    get_textDecorationOverline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                          _type.HRESULT]
    put_textDecorationLineThrough: _Callable[[_type.VARIANT_BOOL],  # v
                                             _type.HRESULT]
    get_textDecorationLineThrough: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                             _type.HRESULT]
    put_textDecorationBlink: _Callable[[_type.VARIANT_BOOL],  # v
                                       _type.HRESULT]
    get_textDecorationBlink: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                       _type.HRESULT]
    put_verticalAlign: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_verticalAlign: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textTransform: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_textAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textIndent: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_textIndent: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_lineHeight: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_lineHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_marginTop: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_marginTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_marginRight: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_marginRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_marginBottom: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_marginBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_marginLeft: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_marginLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_margin: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_margin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_paddingTop: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_paddingTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_paddingRight: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_paddingRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_paddingBottom: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_paddingBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_paddingLeft: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_paddingLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_padding: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_padding: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_border: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_borderTop: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_borderTop: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderRight: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderRight: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderBottom: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_borderBottom: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_borderLeft: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_borderLeft: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_borderColor: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopColor: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightColor: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomColor: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderWidth: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopWidth: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightWidth: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomWidth: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftWidth: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderStyle: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopStyle: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderTopStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_borderRightStyle: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_borderRightStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_borderBottomStyle: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderBottomStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_borderLeftStyle: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_borderLeftStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_styleFloat: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_styleFloat: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_clear: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_display: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_display: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_visibility: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_visibility: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_listStyleType: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_listStyleType: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_listStylePosition: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_listStylePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_listStyleImage: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_listStyleImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_listStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_listStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_whiteSpace: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_whiteSpace: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_top: _Callable[[_struct.VARIANT],  # v
                       _type.HRESULT]
    get_top: _Callable[[_Pointer[_struct.VARIANT]],  # p
                       _type.HRESULT]
    put_left: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_left: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_zIndex: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_zIndex: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_overflow: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_overflow: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_pageBreakBefore: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakBefore: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_pageBreakAfter: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_pageBreakAfter: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_cssText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_cssText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_pixelTop: _Callable[[_type.c_long],  # v
                            _type.HRESULT]
    get_pixelTop: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    put_pixelLeft: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_pixelLeft: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_pixelWidth: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_pixelWidth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_pixelHeight: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_pixelHeight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_posTop: _Callable[[_type.c_float],  # v
                          _type.HRESULT]
    get_posTop: _Callable[[_Pointer[_type.c_float]],  # p
                          _type.HRESULT]
    put_posLeft: _Callable[[_type.c_float],  # v
                           _type.HRESULT]
    get_posLeft: _Callable[[_Pointer[_type.c_float]],  # p
                           _type.HRESULT]
    put_posWidth: _Callable[[_type.c_float],  # v
                            _type.HRESULT]
    get_posWidth: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    put_posHeight: _Callable[[_type.c_float],  # v
                             _type.HRESULT]
    get_posHeight: _Callable[[_Pointer[_type.c_float]],  # p
                             _type.HRESULT]
    put_cursor: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_cursor: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_clip: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_clip: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_filter: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_filter: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _struct.VARIANT,  # AttributeValue
                             _type.LONG],  # lFlags
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR,  # strAttributeName
                                _type.LONG,  # lFlags
                                _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                               _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]


class IHTMLStyle2(_oaidl.IDispatch):
    put_tableLayout: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_tableLayout: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderCollapse: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderCollapse: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_direction: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_behavior: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_behavior: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    setExpression: _Callable[[_type.BSTR,  # propname
                              _type.BSTR,  # expression
                              _type.BSTR],  # language
                             _type.HRESULT]
    getExpression: _Callable[[_type.BSTR,  # propname
                              _Pointer[_struct.VARIANT]],  # expression
                             _type.HRESULT]
    removeExpression: _Callable[[_type.BSTR,  # propname
                                 _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                                _type.HRESULT]
    put_position: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_unicodeBidi: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_unicodeBidi: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_bottom: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_bottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_right: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_right: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_pixelBottom: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_pixelBottom: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_pixelRight: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_pixelRight: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_posBottom: _Callable[[_type.c_float],  # v
                             _type.HRESULT]
    get_posBottom: _Callable[[_Pointer[_type.c_float]],  # p
                             _type.HRESULT]
    put_posRight: _Callable[[_type.c_float],  # v
                            _type.HRESULT]
    get_posRight: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    put_imeMode: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_imeMode: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_rubyAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_rubyAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_rubyPosition: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_rubyOverhang: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyOverhang: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_layoutGridChar: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridChar: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridLine: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridLine: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridMode: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGridType: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridType: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGrid: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutGrid: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_wordBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_wordBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_lineBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_lineBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textJustify: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_textJustify: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textJustifyTrim: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_textJustifyTrim: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_textKashida: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_textKashida: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_textAutospace: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAutospace: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_overflowX: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowX: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_overflowY: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowY: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_accelerator: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_accelerator: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class IHTMLStyle3(_oaidl.IDispatch):
    put_layoutFlow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_zoom: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_zoom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_wordWrap: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_wordWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_textUnderlinePosition: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_textUnderlinePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_scrollbarBaseColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarBaseColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbarFaceColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarFaceColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbar3dLightColor: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_scrollbar3dLightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_scrollbarShadowColor: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_scrollbarShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_scrollbarHighlightColor: _Callable[[_struct.VARIANT],  # v
                                           _type.HRESULT]
    get_scrollbarHighlightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                           _type.HRESULT]
    put_scrollbarDarkShadowColor: _Callable[[_struct.VARIANT],  # v
                                            _type.HRESULT]
    get_scrollbarDarkShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                            _type.HRESULT]
    put_scrollbarArrowColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarArrowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_scrollbarTrackColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarTrackColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_writingMode: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_writingMode: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textAlignLast: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAlignLast: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textKashidaSpace: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_textKashidaSpace: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]


class IHTMLStyle4(_oaidl.IDispatch):
    put_textOverflow: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_textOverflow: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_minHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_minHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class IHTMLStyle5(_oaidl.IDispatch):
    put_msInterpolationMode: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msInterpolationMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_maxHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_maxHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_minWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_minWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_maxWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_maxWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]


class IHTMLStyle6(_oaidl.IDispatch):
    put_content: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_content: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_captionSide: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_captionSide: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_counterIncrement: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_counterIncrement: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_counterReset: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_counterReset: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outline: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_outline: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_outlineWidth: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_outlineStyle: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_outlineStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outlineColor: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_boxSizing: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_boxSizing: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderSpacing: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_borderSpacing: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_orphans: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_orphans: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_widows: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_widows: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_pageBreakInside: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakInside: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_emptyCells: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_emptyCells: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msBlockProgression: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_msBlockProgression: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_quotes: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_quotes: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLRuleStyle(_oaidl.IDispatch):
    put_fontFamily: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontFamily: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_fontStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_fontVariant: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_fontVariant: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_fontWeight: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_fontWeight: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_fontSize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_fontSize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_font: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_font: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_backgroundColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_backgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_backgroundImage: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_backgroundImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_backgroundRepeat: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_backgroundRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_backgroundAttachment: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_backgroundAttachment: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_backgroundPosition: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_backgroundPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_backgroundPositionX: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionX: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_backgroundPositionY: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_backgroundPositionY: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_wordSpacing: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_wordSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_letterSpacing: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_letterSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textDecoration: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_textDecoration: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_textDecorationNone: _Callable[[_type.VARIANT_BOOL],  # v
                                      _type.HRESULT]
    get_textDecorationNone: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]
    put_textDecorationUnderline: _Callable[[_type.VARIANT_BOOL],  # v
                                           _type.HRESULT]
    get_textDecorationUnderline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                           _type.HRESULT]
    put_textDecorationOverline: _Callable[[_type.VARIANT_BOOL],  # v
                                          _type.HRESULT]
    get_textDecorationOverline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                          _type.HRESULT]
    put_textDecorationLineThrough: _Callable[[_type.VARIANT_BOOL],  # v
                                             _type.HRESULT]
    get_textDecorationLineThrough: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                             _type.HRESULT]
    put_textDecorationBlink: _Callable[[_type.VARIANT_BOOL],  # v
                                       _type.HRESULT]
    get_textDecorationBlink: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                       _type.HRESULT]
    put_verticalAlign: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_verticalAlign: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_textTransform: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_textAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textIndent: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_textIndent: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_lineHeight: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_lineHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_marginTop: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_marginTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_marginRight: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_marginRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_marginBottom: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_marginBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_marginLeft: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_marginLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_margin: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_margin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_paddingTop: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_paddingTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_paddingRight: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_paddingRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_paddingBottom: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_paddingBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_paddingLeft: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_paddingLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_padding: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_padding: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_border: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_borderTop: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_borderTop: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderRight: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderRight: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderBottom: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_borderBottom: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_borderLeft: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_borderLeft: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_borderColor: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopColor: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightColor: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomColor: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftColor: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderWidth: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopWidth: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_borderTopWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_borderRightWidth: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderRightWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderBottomWidth: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_borderBottomWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_borderLeftWidth: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderLeftWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_borderStyle: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderTopStyle: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderTopStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_borderRightStyle: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_borderRightStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_borderBottomStyle: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_borderBottomStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_borderLeftStyle: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_borderLeftStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_styleFloat: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_styleFloat: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_clear: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_display: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_display: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_visibility: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_visibility: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_listStyleType: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_listStyleType: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_listStylePosition: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_listStylePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_listStyleImage: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_listStyleImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_listStyle: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_listStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_whiteSpace: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_whiteSpace: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_top: _Callable[[_struct.VARIANT],  # v
                       _type.HRESULT]
    get_top: _Callable[[_Pointer[_struct.VARIANT]],  # p
                       _type.HRESULT]
    put_left: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_left: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_zIndex: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_zIndex: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_overflow: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_overflow: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_pageBreakBefore: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakBefore: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_pageBreakAfter: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_pageBreakAfter: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_cssText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_cssText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_cursor: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_cursor: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_clip: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_clip: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_filter: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_filter: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _struct.VARIANT,  # AttributeValue
                             _type.LONG],  # lFlags
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR,  # strAttributeName
                                _type.LONG,  # lFlags
                                _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                               _type.HRESULT]


class IHTMLRuleStyle2(_oaidl.IDispatch):
    put_tableLayout: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_tableLayout: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_borderCollapse: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_borderCollapse: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_direction: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_behavior: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_behavior: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_position: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_unicodeBidi: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_unicodeBidi: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_bottom: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_bottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_right: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_right: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_pixelBottom: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_pixelBottom: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_pixelRight: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_pixelRight: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_posBottom: _Callable[[_type.c_float],  # v
                             _type.HRESULT]
    get_posBottom: _Callable[[_Pointer[_type.c_float]],  # p
                             _type.HRESULT]
    put_posRight: _Callable[[_type.c_float],  # v
                            _type.HRESULT]
    get_posRight: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    put_imeMode: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_imeMode: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_rubyAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_rubyAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_rubyPosition: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_rubyOverhang: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_rubyOverhang: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_layoutGridChar: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridChar: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridLine: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_layoutGridLine: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_layoutGridMode: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGridType: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_layoutGridType: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_layoutGrid: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutGrid: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_textAutospace: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAutospace: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_wordBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_wordBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_lineBreak: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_lineBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textJustify: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_textJustify: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textJustifyTrim: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_textJustifyTrim: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_textKashida: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_textKashida: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_overflowX: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowX: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_overflowY: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_overflowY: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_accelerator: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_accelerator: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class IHTMLRuleStyle3(_oaidl.IDispatch):
    put_layoutFlow: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_layoutFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_zoom: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_zoom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_wordWrap: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_wordWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_textUnderlinePosition: _Callable[[_type.BSTR],  # v
                                         _type.HRESULT]
    get_textUnderlinePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    put_scrollbarBaseColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarBaseColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbarFaceColor: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_scrollbarFaceColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_scrollbar3dLightColor: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_scrollbar3dLightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_scrollbarShadowColor: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_scrollbarShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_scrollbarHighlightColor: _Callable[[_struct.VARIANT],  # v
                                           _type.HRESULT]
    get_scrollbarHighlightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                           _type.HRESULT]
    put_scrollbarDarkShadowColor: _Callable[[_struct.VARIANT],  # v
                                            _type.HRESULT]
    get_scrollbarDarkShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                            _type.HRESULT]
    put_scrollbarArrowColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarArrowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_scrollbarTrackColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_scrollbarTrackColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_writingMode: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_writingMode: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_textAlignLast: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_textAlignLast: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_textKashidaSpace: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_textKashidaSpace: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]


class IHTMLRuleStyle4(_oaidl.IDispatch):
    put_textOverflow: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_textOverflow: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_minHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_minHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class IHTMLRuleStyle5(_oaidl.IDispatch):
    put_msInterpolationMode: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_msInterpolationMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_maxHeight: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_maxHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_minWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_minWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_maxWidth: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_maxWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]


class IHTMLRuleStyle6(_oaidl.IDispatch):
    put_content: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_content: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_captionSide: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_captionSide: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_counterIncrement: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_counterIncrement: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    put_counterReset: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_counterReset: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outline: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_outline: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_outlineWidth: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_outlineStyle: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_outlineStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_outlineColor: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_outlineColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_boxSizing: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_boxSizing: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_borderSpacing: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_borderSpacing: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_orphans: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_orphans: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_widows: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_widows: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_pageBreakInside: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_pageBreakInside: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_emptyCells: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_emptyCells: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_msBlockProgression: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_msBlockProgression: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_quotes: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_quotes: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispHTMLStyle(_oaidl.IDispatch):
    pass


class DispHTMLRuleStyle(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetRulesCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLStyleSheetRule]],  # ppHTMLStyleSheetRule
                    _type.HRESULT]


class IHTMLStyleSheet(_oaidl.IDispatch):
    put_title: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_title: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_parentStyleSheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                                    _type.HRESULT]
    get_owningElement: _Callable[[_Pointer[IHTMLElement]],  # p
                                 _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_readOnly: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_imports: _Callable[[_Pointer[IHTMLStyleSheetsCollection]],  # p
                           _type.HRESULT]
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_id: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    addImport: _Callable[[_type.BSTR,  # bstrURL
                          _type.c_long,  # lIndex
                          _Pointer[_type.c_long]],  # plIndex
                         _type.HRESULT]
    addRule: _Callable[[_type.BSTR,  # bstrSelector
                        _type.BSTR,  # bstrStyle
                        _type.c_long,  # lIndex
                        _Pointer[_type.c_long]],  # plNewIndex
                       _type.HRESULT]
    removeImport: _Callable[[_type.c_long],  # lIndex
                            _type.HRESULT]
    removeRule: _Callable[[_type.c_long],  # lIndex
                          _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_cssText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_cssText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_rules: _Callable[[_Pointer[IHTMLStyleSheetRulesCollection]],  # p
                         _type.HRESULT]


class IHTMLCSSRule(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.USHORT]],  # p
                        _type.HRESULT]
    put_cssText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_cssText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_parentRule: _Callable[[_Pointer[IHTMLCSSRule]],  # p
                              _type.HRESULT]
    get_parentStyleSheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                                    _type.HRESULT]


class IHTMLCSSImportRule(_oaidl.IDispatch):
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_media: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    get_styleSheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                              _type.HRESULT]


class IHTMLCSSMediaRule(_oaidl.IDispatch):
    put_media: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    get_cssRules: _Callable[[_Pointer[IHTMLStyleSheetRulesCollection]],  # p
                            _type.HRESULT]
    insertRule: _Callable[[_type.BSTR,  # bstrRule
                           _type.c_long,  # lIndex
                           _Pointer[_type.c_long]],  # plNewIndex
                          _type.HRESULT]
    deleteRule: _Callable[[_type.c_long],  # lIndex
                          _type.HRESULT]


class IHTMLCSSMediaList(_oaidl.IDispatch):
    put_mediaText: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_mediaText: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_type.BSTR]],  # pbstrMedium
                    _type.HRESULT]
    appendMedium: _Callable[[_type.BSTR],  # bstrMedium
                            _type.HRESULT]
    deleteMedium: _Callable[[_type.BSTR],  # bstrMedium
                            _type.HRESULT]


class IHTMLCSSNamespaceRule(_oaidl.IDispatch):
    get_namespaceURI: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_prefix: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLMSCSSKeyframeRule(_oaidl.IDispatch):
    put_keyText: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_keyText: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_style: _Callable[[_Pointer[IHTMLRuleStyle]],  # p
                         _type.HRESULT]


class IHTMLMSCSSKeyframesRule(_oaidl.IDispatch):
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_cssRules: _Callable[[_Pointer[IHTMLStyleSheetRulesCollection]],  # p
                            _type.HRESULT]
    appendRule: _Callable[[_type.BSTR],  # bstrRule
                          _type.HRESULT]
    deleteRule: _Callable[[_type.BSTR],  # bstrKey
                          _type.HRESULT]
    findRule: _Callable[[_type.BSTR,  # bstrKey
                         _Pointer[IHTMLMSCSSKeyframeRule]],  # ppMSKeyframeRule
                        _type.HRESULT]


class DispHTMLCSSRule(_oaidl.IDispatch):
    pass


class DispHTMLCSSImportRule(_oaidl.IDispatch):
    pass


class DispHTMLCSSMediaRule(_oaidl.IDispatch):
    pass


class DispHTMLCSSMediaList(_oaidl.IDispatch):
    pass


class DispHTMLCSSNamespaceRule(_oaidl.IDispatch):
    pass


class DispHTMLMSCSSKeyframeRule(_oaidl.IDispatch):
    pass


class DispHTMLMSCSSKeyframesRule(_oaidl.IDispatch):
    pass


class IHTMLRenderStyle(_oaidl.IDispatch):
    put_textLineThroughStyle: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_textLineThroughStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_textUnderlineStyle: _Callable[[_type.BSTR],  # v
                                      _type.HRESULT]
    get_textUnderlineStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    put_textEffect: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_textEffect: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_textColor: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_textColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_textBackgroundColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_textBackgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_textDecorationColor: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_textDecorationColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_renderingPriority: _Callable[[_type.c_long],  # v
                                     _type.HRESULT]
    get_renderingPriority: _Callable[[_Pointer[_type.c_long]],  # p
                                     _type.HRESULT]
    put_defaultTextSelection: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_defaultTextSelection: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_textDecoration: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_textDecoration: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]


class DispHTMLRenderStyle(_oaidl.IDispatch):
    pass


class IHTMLCurrentStyle(_oaidl.IDispatch):
    get_position: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_styleFloat: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    get_backgroundColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_fontFamily: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_fontStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_fontVariant: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_fontWeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_fontSize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_backgroundImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_backgroundPositionX: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    get_backgroundPositionY: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    get_backgroundRepeat: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_borderLeftColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_borderTopColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_borderRightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    get_borderBottomColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    get_borderTopStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_borderRightStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_borderBottomStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    get_borderLeftStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_borderTopWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_borderRightWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    get_borderBottomWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    get_borderLeftWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_left: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    get_top: _Callable[[_Pointer[_struct.VARIANT]],  # p
                       _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_paddingLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    get_paddingTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_paddingRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_paddingBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    get_textAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_textDecoration: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_display: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_visibility: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_zIndex: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_letterSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    get_lineHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_textIndent: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_verticalAlign: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    get_backgroundAttachment: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    get_marginTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_marginRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    get_marginBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_marginLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_listStyleType: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_listStylePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    get_listStyleImage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_clipTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_clipRight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_clipBottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_clipLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_overflow: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_pageBreakBefore: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_pageBreakAfter: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_cursor: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_tableLayout: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_borderCollapse: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_behavior: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    get_unicodeBidi: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_right: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    get_bottom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_imeMode: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_rubyAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_rubyPosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_rubyOverhang: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_textAutospace: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_lineBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_wordBreak: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_textJustify: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_textJustifyTrim: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_textKashida: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    get_blockDirection: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_layoutGridChar: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_layoutGridLine: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_layoutGridMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_layoutGridType: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_borderStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_borderWidth: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_padding: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_margin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_accelerator: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_overflowX: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_overflowY: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_textTransform: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]


class IHTMLCurrentStyle2(_oaidl.IDispatch):
    get_layoutFlow: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_wordWrap: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_textUnderlinePosition: _Callable[[_Pointer[_type.BSTR]],  # p
                                         _type.HRESULT]
    get_hasLayout: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_scrollbarBaseColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    get_scrollbarFaceColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    get_scrollbar3dLightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    get_scrollbarShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    get_scrollbarHighlightColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                           _type.HRESULT]
    get_scrollbarDarkShadowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                            _type.HRESULT]
    get_scrollbarArrowColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    get_scrollbarTrackColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    get_writingMode: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_zoom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    get_filter: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_textAlignLast: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_textKashidaSpace: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    get_isBlock: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]


class IHTMLCurrentStyle3(_oaidl.IDispatch):
    get_textOverflow: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_minHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_wordSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    get_whiteSpace: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]


class IHTMLCurrentStyle4(_oaidl.IDispatch):
    get_msInterpolationMode: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    get_maxHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_minWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_maxWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]


class IHTMLCurrentStyle5(_oaidl.IDispatch):
    get_captionSide: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_outline: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_outlineWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_outlineStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_outlineColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_boxSizing: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_borderSpacing: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_orphans: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_widows: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_pageBreakInside: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_emptyCells: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_msBlockProgression: _Callable[[_Pointer[_type.BSTR]],  # p
                                      _type.HRESULT]
    get_quotes: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispHTMLCurrentStyle(_oaidl.IDispatch):
    pass


class IHTMLElement(_oaidl.IDispatch):
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _struct.VARIANT,  # AttributeValue
                             _type.LONG],  # lFlags
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR,  # strAttributeName
                                _type.LONG,  # lFlags
                                _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                               _type.HRESULT]
    put_className: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_className: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_id: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_id: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    get_tagName: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_parentElement: _Callable[[_Pointer[IHTMLElement]],  # p
                                 _type.HRESULT]
    get_style: _Callable[[_Pointer[IHTMLStyle]],  # p
                         _type.HRESULT]
    put_onhelp: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onhelp: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onclick: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_ondblclick: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondblclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onkeydown: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onkeydown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onkeyup: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onkeyup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onkeypress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onkeypress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmouseout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onmouseout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmouseover: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmouseover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmousemove: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousemove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmousedown: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousedown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmouseup: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmouseup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_document: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    put_title: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_title: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_language: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_language: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_onselectstart: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onselectstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    scrollIntoView: _Callable[[_struct.VARIANT],  # varargStart
                              _type.HRESULT]
    contains: _Callable[[IHTMLElement,  # pChild
                         _Pointer[_type.VARIANT_BOOL]],  # pfResult
                        _type.HRESULT]
    get_sourceIndex: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_recordNumber: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_lang: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_lang: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_offsetLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_offsetTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_offsetWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_offsetHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_offsetParent: _Callable[[_Pointer[IHTMLElement]],  # p
                                _type.HRESULT]
    put_innerHTML: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_innerHTML: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_innerText: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_innerText: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_outerHTML: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_outerHTML: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_outerText: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_outerText: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    insertAdjacentHTML: _Callable[[_type.BSTR,  # where
                                   _type.BSTR],  # html
                                  _type.HRESULT]
    insertAdjacentText: _Callable[[_type.BSTR,  # where
                                   _type.BSTR],  # text
                                  _type.HRESULT]
    get_parentTextEdit: _Callable[[_Pointer[IHTMLElement]],  # p
                                  _type.HRESULT]
    get_isTextEdit: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    click: _Callable[[],
                     _type.HRESULT]
    get_filters: _Callable[[_Pointer[IHTMLFiltersCollection]],  # p
                           _type.HRESULT]
    put_ondragstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]
    put_onbeforeupdate: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onbeforeupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onafterupdate: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onafterupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onerrorupdate: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onerrorupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onrowexit: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onrowexit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onrowenter: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onrowenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondatasetchanged: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_ondatasetchanged: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_ondataavailable: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_ondataavailable: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_ondatasetcomplete: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_ondatasetcomplete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onfilterchange: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onfilterchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_children: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_all: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                       _type.HRESULT]


class IHTMLRect(_oaidl.IDispatch):
    put_left: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_left: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_top: _Callable[[_type.c_long],  # v
                       _type.HRESULT]
    get_top: _Callable[[_Pointer[_type.c_long]],  # p
                       _type.HRESULT]
    put_right: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_right: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_bottom: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_bottom: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLRect2(_oaidl.IDispatch):
    get_width: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_float]],  # p
                          _type.HRESULT]


class IHTMLRectCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]


class IHTMLElementCollection(_oaidl.IDispatch):
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]
    put_length: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # name
                     _struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]
    tags: _Callable[[_struct.VARIANT,  # tagName
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLElement2(_oaidl.IDispatch):
    get_scopeName: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    setCapture: _Callable[[_type.VARIANT_BOOL],  # containerCapture
                          _type.HRESULT]
    releaseCapture: _Callable[[],
                              _type.HRESULT]
    put_onlosecapture: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onlosecapture: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    componentFromPoint: _Callable[[_type.c_long,  # x
                                   _type.c_long,  # y
                                   _Pointer[_type.BSTR]],  # component
                                  _type.HRESULT]
    doScroll: _Callable[[_struct.VARIANT],  # component
                        _type.HRESULT]
    put_onscroll: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onscroll: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_ondrag: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrag: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_ondragend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_ondragend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ondragenter: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondragover: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondragover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondragleave: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragleave: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondrop: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onbeforecut: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onbeforecut: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_oncut: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_oncut: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_onbeforecopy: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onbeforecopy: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_oncopy: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_oncopy: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onbeforepaste: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onbeforepaste: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onpaste: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onpaste: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_currentStyle: _Callable[[_Pointer[IHTMLCurrentStyle]],  # p
                                _type.HRESULT]
    put_onpropertychange: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onpropertychange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    getClientRects: _Callable[[_Pointer[IHTMLRectCollection]],  # pRectCol
                              _type.HRESULT]
    getBoundingClientRect: _Callable[[_Pointer[IHTMLRect]],  # pRect
                                     _type.HRESULT]
    setExpression: _Callable[[_type.BSTR,  # propname
                              _type.BSTR,  # expression
                              _type.BSTR],  # language
                             _type.HRESULT]
    getExpression: _Callable[[_type.BSTR,  # propname
                              _Pointer[_struct.VARIANT]],  # expression
                             _type.HRESULT]
    removeExpression: _Callable[[_type.BSTR,  # propname
                                 _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                                _type.HRESULT]
    put_tabIndex: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_tabIndex: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    focus: _Callable[[],
                     _type.HRESULT]
    put_accessKey: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_accessKey: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onresize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onresize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    blur: _Callable[[],
                    _type.HRESULT]
    addFilter: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                         _type.HRESULT]
    removeFilter: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                            _type.HRESULT]
    get_clientHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_clientWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_clientTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_clientLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    attachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch,  # pDisp
                            _Pointer[_type.VARIANT_BOOL]],  # pfResult
                           _type.HRESULT]
    detachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch],  # pDisp
                           _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onrowsdelete: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onrowsdelete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onrowsinserted: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onrowsinserted: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_oncellchange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_oncellchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_dir: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_dir: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    createControlRange: _Callable[[_Pointer[_oaidl.IDispatch]],  # range
                                  _type.HRESULT]
    get_scrollHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_scrollWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_scrollTop: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_scrollTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_scrollLeft: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_scrollLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    clearAttributes: _Callable[[],
                               _type.HRESULT]
    mergeAttributes: _Callable[[IHTMLElement],  # mergeThis
                               _type.HRESULT]
    put_oncontextmenu: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_oncontextmenu: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    insertAdjacentElement: _Callable[[_type.BSTR,  # where
                                      IHTMLElement,  # insertedElement
                                      _Pointer[IHTMLElement]],  # inserted
                                     _type.HRESULT]
    applyElement: _Callable[[IHTMLElement,  # apply
                             _type.BSTR,  # where
                             _Pointer[IHTMLElement]],  # applied
                            _type.HRESULT]
    getAdjacentText: _Callable[[_type.BSTR,  # where
                                _Pointer[_type.BSTR]],  # text
                               _type.HRESULT]
    replaceAdjacentText: _Callable[[_type.BSTR,  # where
                                    _type.BSTR,  # newText
                                    _Pointer[_type.BSTR]],  # oldText
                                   _type.HRESULT]
    get_canHaveChildren: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]
    addBehavior: _Callable[[_type.BSTR,  # bstrUrl
                            _Pointer[_struct.VARIANT],  # pvarFactory
                            _Pointer[_type.c_long]],  # pCookie
                           _type.HRESULT]
    removeBehavior: _Callable[[_type.c_long,  # cookie
                               _Pointer[_type.VARIANT_BOOL]],  # pfResult
                              _type.HRESULT]
    get_runtimeStyle: _Callable[[_Pointer[IHTMLStyle]],  # p
                                _type.HRESULT]
    get_behaviorUrns: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]
    put_tagUrn: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_tagUrn: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_onbeforeeditfocus: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onbeforeeditfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    get_readyStateValue: _Callable[[_Pointer[_type.c_long]],  # p
                                   _type.HRESULT]
    getElementsByTagName: _Callable[[_type.BSTR,  # v
                                     _Pointer[IHTMLElementCollection]],  # pelColl
                                    _type.HRESULT]


class IHTMLAttributeCollection3(_oaidl.IDispatch):
    getNamedItem: _Callable[[_type.BSTR,  # bstrName
                             _Pointer[IHTMLDOMAttribute]],  # ppNodeOut
                            _type.HRESULT]
    setNamedItem: _Callable[[IHTMLDOMAttribute,  # pNodeIn
                             _Pointer[IHTMLDOMAttribute]],  # ppNodeOut
                            _type.HRESULT]
    removeNamedItem: _Callable[[_type.BSTR,  # bstrName
                                _Pointer[IHTMLDOMAttribute]],  # ppNodeOut
                               _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLDOMAttribute]],  # ppNodeOut
                    _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IDOMDocumentType(_oaidl.IDispatch):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_entities: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_notations: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_publicId: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_systemId: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_internalSubset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]


class IHTMLDocument7(_oaidl.IDispatch):
    get_defaultView: _Callable[[_Pointer[IHTMLWindow2]],  # p
                               _type.HRESULT]
    createCDATASection: _Callable[[_type.BSTR,  # text
                                   _Pointer[IHTMLDOMNode]],  # newCDATASectionNode
                                  _type.HRESULT]
    getSelection: _Callable[[_Pointer[IHTMLSelection]],  # ppIHTMLSelection
                            _type.HRESULT]
    getElementsByTagNameNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                       _type.BSTR,  # bstrLocalName
                                       _Pointer[IHTMLElementCollection]],  # pelColl
                                      _type.HRESULT]
    createElementNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                _type.BSTR,  # bstrTag
                                _Pointer[IHTMLElement]],  # newElem
                               _type.HRESULT]
    createAttributeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                  _type.BSTR,  # bstrAttrName
                                  _Pointer[IHTMLDOMAttribute]],  # ppAttribute
                                 _type.HRESULT]
    put_onmsthumbnailclick: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onmsthumbnailclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    get_characterSet: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    createElement: _Callable[[_type.BSTR,  # bstrTag
                              _Pointer[IHTMLElement]],  # newElem
                             _type.HRESULT]
    createAttribute: _Callable[[_type.BSTR,  # bstrAttrName
                                _Pointer[IHTMLDOMAttribute]],  # ppAttribute
                               _type.HRESULT]
    getElementsByClassName: _Callable[[_type.BSTR,  # v
                                       _Pointer[IHTMLElementCollection]],  # pel
                                      _type.HRESULT]
    createProcessingInstruction: _Callable[[_type.BSTR,  # bstrTarget
                                            _type.BSTR,  # bstrData
                                            _Pointer[IDOMProcessingInstruction]],  # newProcessingInstruction
                                           _type.HRESULT]
    adoptNode: _Callable[[IHTMLDOMNode,  # pNodeSource
                          _Pointer[IHTMLDOMNode3]],  # ppNodeDest
                         _type.HRESULT]
    put_onmssitemodejumplistitemremoved: _Callable[[_struct.VARIANT],  # v
                                                   _type.HRESULT]
    get_onmssitemodejumplistitemremoved: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                                   _type.HRESULT]
    get_all: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                       _type.HRESULT]
    get_inputEncoding: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_xmlEncoding: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_xmlStandalone: _Callable[[_type.VARIANT_BOOL],  # v
                                 _type.HRESULT]
    get_xmlStandalone: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    put_xmlVersion: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_xmlVersion: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    hasAttributes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasAttributes
                             _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_oncanplay: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_oncanplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_oncanplaythrough: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_oncanplaythrough: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_ondrag: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrag: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_ondragend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_ondragend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ondragenter: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondragleave: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragleave: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondragover: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondragover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondrop: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_ondurationchange: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_ondurationchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onemptied: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onemptied: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onended: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onended: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_oninput: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_oninput: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onloadeddata: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onloadeddata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onloadedmetadata: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onloadedmetadata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onloadstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onloadstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onpause: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onpause: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onplay: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onplaying: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onplaying: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onprogress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onprogress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onratechange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onratechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onreset: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onreset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onscroll: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onscroll: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onseeked: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onseeked: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onseeking: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onseeking: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onstalled: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstalled: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onsubmit: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onsubmit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onsuspend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onsuspend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ontimeupdate: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_ontimeupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onvolumechange: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onvolumechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onwaiting: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onwaiting: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    normalize: _Callable[[],
                         _type.HRESULT]
    importNode: _Callable[[IHTMLDOMNode,  # pNodeSource
                           _type.VARIANT_BOOL,  # fDeep
                           _Pointer[IHTMLDOMNode3]],  # ppNodeDest
                          _type.HRESULT]
    get_parentWindow: _Callable[[_Pointer[IHTMLWindow2]],  # p
                                _type.HRESULT]
    putref_body: _Callable[[IHTMLElement],  # v
                           _type.HRESULT]
    get_body: _Callable[[_Pointer[IHTMLElement]],  # p
                        _type.HRESULT]
    get_head: _Callable[[_Pointer[IHTMLElement]],  # p
                        _type.HRESULT]


class IHTMLDOMNode(_oaidl.IDispatch):
    get_nodeType: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_parentNode: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    hasChildNodes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # fChildren
                             _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    get_attributes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    insertBefore: _Callable[[IHTMLDOMNode,  # newChild
                             _struct.VARIANT,  # refChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    removeChild: _Callable[[IHTMLDOMNode,  # oldChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    replaceChild: _Callable[[IHTMLDOMNode,  # newChild
                             IHTMLDOMNode,  # oldChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    cloneNode: _Callable[[_type.VARIANT_BOOL,  # fDeep
                          _Pointer[IHTMLDOMNode]],  # clonedNode
                         _type.HRESULT]
    removeNode: _Callable[[_type.VARIANT_BOOL,  # fDeep
                           _Pointer[IHTMLDOMNode]],  # removed
                          _type.HRESULT]
    swapNode: _Callable[[IHTMLDOMNode,  # otherNode
                         _Pointer[IHTMLDOMNode]],  # swappedNode
                        _type.HRESULT]
    replaceNode: _Callable[[IHTMLDOMNode,  # replacement
                            _Pointer[IHTMLDOMNode]],  # replaced
                           _type.HRESULT]
    appendChild: _Callable[[IHTMLDOMNode,  # newChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    get_nodeName: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_nodeValue: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_nodeValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_firstChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    get_lastChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                             _type.HRESULT]
    get_previousSibling: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                                   _type.HRESULT]
    get_nextSibling: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                               _type.HRESULT]


class IHTMLDOMNode2(_oaidl.IDispatch):
    get_ownerDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]


class IHTMLDOMNode3(_oaidl.IDispatch):
    put_prefix: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_prefix: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_localName: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_namespaceURI: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_textContent: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_textContent: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    isEqualNode: _Callable[[IHTMLDOMNode3,  # otherNode
                            _Pointer[_type.VARIANT_BOOL]],  # isEqual
                           _type.HRESULT]
    lookupNamespaceURI: _Callable[[_Pointer[_struct.VARIANT],  # pvarPrefix
                                   _Pointer[_struct.VARIANT]],  # pvarNamespaceURI
                                  _type.HRESULT]
    lookupPrefix: _Callable[[_Pointer[_struct.VARIANT],  # pvarNamespaceURI
                             _Pointer[_struct.VARIANT]],  # pvarPrefix
                            _type.HRESULT]
    isDefaultNamespace: _Callable[[_Pointer[_struct.VARIANT],  # pvarNamespace
                                   _Pointer[_type.VARIANT_BOOL]],  # pfDefaultNamespace
                                  _type.HRESULT]
    appendChild: _Callable[[IHTMLDOMNode,  # newChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    insertBefore: _Callable[[IHTMLDOMNode,  # newChild
                             _struct.VARIANT,  # refChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    removeChild: _Callable[[IHTMLDOMNode,  # oldChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    replaceChild: _Callable[[IHTMLDOMNode,  # newChild
                             IHTMLDOMNode,  # oldChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    isSameNode: _Callable[[IHTMLDOMNode3,  # otherNode
                           _Pointer[_type.VARIANT_BOOL]],  # isSame
                          _type.HRESULT]
    compareDocumentPosition: _Callable[[IHTMLDOMNode,  # otherNode
                                        _Pointer[_type.USHORT]],  # flags
                                       _type.HRESULT]
    isSupported: _Callable[[_type.BSTR,  # feature
                            _struct.VARIANT,  # version
                            _Pointer[_type.VARIANT_BOOL]],  # pfisSupported
                           _type.HRESULT]


class IHTMLDOMAttribute(_oaidl.IDispatch):
    get_nodeName: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_nodeValue: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_nodeValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_specified: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]


class IHTMLDOMAttribute2(_oaidl.IDispatch):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_expando: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_nodeType: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_parentNode: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    get_firstChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    get_lastChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                             _type.HRESULT]
    get_previousSibling: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                                   _type.HRESULT]
    get_nextSibling: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                               _type.HRESULT]
    get_attributes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    get_ownerDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    insertBefore: _Callable[[IHTMLDOMNode,  # newChild
                             _struct.VARIANT,  # refChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    replaceChild: _Callable[[IHTMLDOMNode,  # newChild
                             IHTMLDOMNode,  # oldChild
                             _Pointer[IHTMLDOMNode]],  # node
                            _type.HRESULT]
    removeChild: _Callable[[IHTMLDOMNode,  # oldChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    appendChild: _Callable[[IHTMLDOMNode,  # newChild
                            _Pointer[IHTMLDOMNode]],  # node
                           _type.HRESULT]
    hasChildNodes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # fChildren
                             _type.HRESULT]
    cloneNode: _Callable[[_type.VARIANT_BOOL,  # fDeep
                          _Pointer[IHTMLDOMAttribute]],  # clonedNode
                         _type.HRESULT]


class IHTMLDOMAttribute3(_oaidl.IDispatch):
    put_nodeValue: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_nodeValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_specified: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_ownerElement: _Callable[[_Pointer[IHTMLElement2]],  # p
                                _type.HRESULT]


class IHTMLDOMAttribute4(_oaidl.IDispatch):
    put_nodeValue: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_nodeValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    get_nodeName: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_firstChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    get_lastChild: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                             _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    hasAttributes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasAttributes
                             _type.HRESULT]
    hasChildNodes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # fChildren
                             _type.HRESULT]
    normalize: _Callable[[],
                         _type.HRESULT]
    get_specified: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]


class IHTMLDOMTextNode(_oaidl.IDispatch):
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    splitText: _Callable[[_type.c_long,  # offset
                          _Pointer[IHTMLDOMNode]],  # pRetNode
                         _type.HRESULT]


class IHTMLDOMTextNode2(_oaidl.IDispatch):
    substringData: _Callable[[_type.c_long,  # offset
                              _type.c_long,  # Count
                              _Pointer[_type.BSTR]],  # pbstrsubString
                             _type.HRESULT]
    appendData: _Callable[[_type.BSTR],  # bstrstring
                          _type.HRESULT]
    insertData: _Callable[[_type.c_long,  # offset
                           _type.BSTR],  # bstrstring
                          _type.HRESULT]
    deleteData: _Callable[[_type.c_long,  # offset
                           _type.c_long],  # Count
                          _type.HRESULT]
    replaceData: _Callable[[_type.c_long,  # offset
                            _type.c_long,  # Count
                            _type.BSTR],  # bstrstring
                           _type.HRESULT]


class IHTMLDOMTextNode3(_oaidl.IDispatch):
    substringData: _Callable[[_type.c_long,  # offset
                              _type.c_long,  # Count
                              _Pointer[_type.BSTR]],  # pbstrsubString
                             _type.HRESULT]
    insertData: _Callable[[_type.c_long,  # offset
                           _type.BSTR],  # bstrstring
                          _type.HRESULT]
    deleteData: _Callable[[_type.c_long,  # offset
                           _type.c_long],  # Count
                          _type.HRESULT]
    replaceData: _Callable[[_type.c_long,  # offset
                            _type.c_long,  # Count
                            _type.BSTR],  # bstrstring
                           _type.HRESULT]
    splitText: _Callable[[_type.c_long,  # offset
                          _Pointer[IHTMLDOMNode]],  # pRetNode
                         _type.HRESULT]
    get_wholeText: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    replaceWholeText: _Callable[[_type.BSTR,  # bstrText
                                 _Pointer[IHTMLDOMNode]],  # ppRetNode
                                _type.HRESULT]
    hasAttributes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasAttributes
                             _type.HRESULT]
    normalize: _Callable[[],
                         _type.HRESULT]


class IHTMLDOMImplementation(_oaidl.IDispatch):
    hasFeature: _Callable[[_type.BSTR,  # bstrfeature
                           _struct.VARIANT,  # version
                           _Pointer[_type.VARIANT_BOOL]],  # pfHasFeature
                          _type.HRESULT]


class IHTMLDOMImplementation2(_oaidl.IDispatch):
    createDocumentType: _Callable[[_type.BSTR,  # bstrQualifiedName
                                   _Pointer[_struct.VARIANT],  # pvarPublicId
                                   _Pointer[_struct.VARIANT],  # pvarSystemId
                                   _Pointer[IDOMDocumentType]],  # newDocumentType
                                  _type.HRESULT]
    createDocument: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                               _Pointer[_struct.VARIANT],  # pvarTagName
                               IDOMDocumentType,  # pDocumentType
                               _Pointer[IHTMLDocument7]],  # ppnewDocument
                              _type.HRESULT]
    createHTMLDocument: _Callable[[_type.BSTR,  # bstrTitle
                                   _Pointer[IHTMLDocument7]],  # ppnewDocument
                                  _type.HRESULT]
    hasFeature: _Callable[[_type.BSTR,  # bstrfeature
                           _struct.VARIANT,  # version
                           _Pointer[_type.VARIANT_BOOL]],  # pfHasFeature
                          _type.HRESULT]


class DispHTMLDOMAttribute(_oaidl.IDispatch):
    pass


class DispHTMLDOMTextNode(_oaidl.IDispatch):
    pass


class DispHTMLDOMImplementation(_oaidl.IDispatch):
    pass


class IHTMLAttributeCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_Pointer[_struct.VARIANT],  # name
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLAttributeCollection2(_oaidl.IDispatch):
    getNamedItem: _Callable[[_type.BSTR,  # bstrName
                             _Pointer[IHTMLDOMAttribute]],  # newretNode
                            _type.HRESULT]
    setNamedItem: _Callable[[IHTMLDOMAttribute,  # ppNode
                             _Pointer[IHTMLDOMAttribute]],  # newretNode
                            _type.HRESULT]
    removeNamedItem: _Callable[[_type.BSTR,  # bstrName
                                _Pointer[IHTMLDOMAttribute]],  # newretNode
                               _type.HRESULT]


class IHTMLAttributeCollection4(_oaidl.IDispatch):
    getNamedItemNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                               _type.BSTR,  # bstrName
                               _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                              _type.HRESULT]
    setNamedItemNS: _Callable[[IHTMLDOMAttribute2,  # pNodeIn
                               _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                              _type.HRESULT]
    removeNamedItemNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                  _type.BSTR,  # bstrName
                                  _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                                 _type.HRESULT]
    getNamedItem: _Callable[[_type.BSTR,  # bstrName
                             _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                            _type.HRESULT]
    setNamedItem: _Callable[[IHTMLDOMAttribute2,  # pNodeIn
                             _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                            _type.HRESULT]
    removeNamedItem: _Callable[[_type.BSTR,  # bstrName
                                _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                               _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLDOMAttribute2]],  # ppNodeOut
                    _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLDOMChildrenCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_oaidl.IDispatch]],  # ppItem
                    _type.HRESULT]


class IHTMLDOMChildrenCollection2(_oaidl.IDispatch):
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_oaidl.IDispatch]],  # ppItem
                    _type.HRESULT]


class DispHTMLAttributeCollection(_oaidl.IDispatch):
    pass


class DispStaticNodeList(_oaidl.IDispatch):
    pass


class DispDOMChildrenCollection(_oaidl.IDispatch):
    pass


class HTMLElementEvents4(_oaidl.IDispatch):
    pass


class HTMLElementEvents3(_oaidl.IDispatch):
    pass


class HTMLElementEvents2(_oaidl.IDispatch):
    pass


class HTMLElementEvents(_oaidl.IDispatch):
    pass


class IRulesAppliedCollection(_oaidl.IDispatch):
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IRulesApplied]],  # ppRulesApplied
                    _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_element: _Callable[[_Pointer[IHTMLElement]],  # p
                           _type.HRESULT]
    propertyInheritedFrom: _Callable[[_type.BSTR,  # name
                                      _Pointer[IRulesApplied]],  # ppRulesApplied
                                     _type.HRESULT]
    get_propertyCount: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    property: _Callable[[_type.c_long,  # index
                         _Pointer[_type.BSTR]],  # pbstrProperty
                        _type.HRESULT]
    propertyInheritedTrace: _Callable[[_type.BSTR,  # name
                                       _type.c_long,  # index
                                       _Pointer[IRulesApplied]],  # ppRulesApplied
                                      _type.HRESULT]
    propertyInheritedTraceLength: _Callable[[_type.BSTR,  # name
                                             _Pointer[_type.c_long]],  # pLength
                                            _type.HRESULT]


class IHTMLElement3(_oaidl.IDispatch):
    mergeAttributes: _Callable[[IHTMLElement,  # mergeThis
                                _Pointer[_struct.VARIANT]],  # pvarFlags
                               _type.HRESULT]
    get_isMultiLine: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    get_canHaveHTML: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    put_onlayoutcomplete: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onlayoutcomplete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onpage: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onpage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_inflateBlock: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_inflateBlock: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    put_onbeforedeactivate: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onbeforedeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    setActive: _Callable[[],
                         _type.HRESULT]
    put_contentEditable: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_contentEditable: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_isContentEditable: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                     _type.HRESULT]
    put_hideFocus: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_hideFocus: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_isDisabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    put_onmove: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onmove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_oncontrolselect: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_oncontrolselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    fireEvent: _Callable[[_type.BSTR,  # bstrEventName
                          _Pointer[_struct.VARIANT],  # pvarEventObject
                          _Pointer[_type.VARIANT_BOOL]],  # pfCancelled
                         _type.HRESULT]
    put_onresizestart: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onresizestart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onresizeend: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onresizeend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmovestart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmovestart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmoveend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmoveend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onmouseenter: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmouseenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onmouseleave: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmouseleave: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onactivate: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondeactivate: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_ondeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    dragDrop: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfRet
                        _type.HRESULT]
    get_glyphMode: _Callable[[_Pointer[_type.LONG]],  # p
                             _type.HRESULT]


class IHTMLElement4(_oaidl.IDispatch):
    put_onmousewheel: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmousewheel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    normalize: _Callable[[],
                         _type.HRESULT]
    getAttributeNode: _Callable[[_type.BSTR,  # bstrname
                                 _Pointer[IHTMLDOMAttribute]],  # ppAttribute
                                _type.HRESULT]
    setAttributeNode: _Callable[[IHTMLDOMAttribute,  # pattr
                                 _Pointer[IHTMLDOMAttribute]],  # ppretAttribute
                                _type.HRESULT]
    removeAttributeNode: _Callable[[IHTMLDOMAttribute,  # pattr
                                    _Pointer[IHTMLDOMAttribute]],  # ppretAttribute
                                   _type.HRESULT]
    put_onbeforeactivate: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onbeforeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onfocusin: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onfocusin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onfocusout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onfocusout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]


class IElementSelector(_oaidl.IDispatch):
    querySelector: _Callable[[_type.BSTR,  # v
                              _Pointer[IHTMLElement]],  # pel
                             _type.HRESULT]
    querySelectorAll: _Callable[[_type.BSTR,  # v
                                 _Pointer[IHTMLDOMChildrenCollection]],  # pel
                                _type.HRESULT]


class IHTMLElementRender(_Unknwnbase.IUnknown):
    DrawToDC: _Callable[[_type.HDC],  # hDC
                        _type.HRESULT]
    SetDocumentPrinter: _Callable[[_type.BSTR,  # bstrPrinterName
                                   _type.HDC],  # hDC
                                  _type.HRESULT]


class IHTMLUniqueName(_oaidl.IDispatch):
    get_uniqueNumber: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_uniqueID: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class IHTMLElement5(_oaidl.IDispatch):
    getAttributeNode: _Callable[[_type.BSTR,  # bstrname
                                 _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                _type.HRESULT]
    setAttributeNode: _Callable[[IHTMLDOMAttribute2,  # pattr
                                 _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                _type.HRESULT]
    removeAttributeNode: _Callable[[IHTMLDOMAttribute2,  # pattr
                                    _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                   _type.HRESULT]
    hasAttribute: _Callable[[_type.BSTR,  # name
                             _Pointer[_type.VARIANT_BOOL]],  # pfHasAttribute
                            _type.HRESULT]
    put_role: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_role: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_ariaBusy: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_ariaBusy: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_ariaChecked: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_ariaChecked: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_ariaDisabled: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaDisabled: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaExpanded: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaExpanded: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaHaspopup: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaHaspopup: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaHidden: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_ariaHidden: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_ariaInvalid: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_ariaInvalid: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_ariaMultiselectable: _Callable[[_type.BSTR],  # v
                                       _type.HRESULT]
    get_ariaMultiselectable: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]
    put_ariaPressed: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_ariaPressed: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_ariaReadonly: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaReadonly: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaRequired: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaRequired: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaSecret: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_ariaSecret: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_ariaSelected: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaSelected: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _struct.VARIANT],  # AttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR,  # strAttributeName
                                _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                               _type.HRESULT]
    get_attributes: _Callable[[_Pointer[IHTMLAttributeCollection3]],  # p
                              _type.HRESULT]
    put_ariaValuenow: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaValuenow: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaPosinset: _Callable[[_type.c_short],  # v
                                _type.HRESULT]
    get_ariaPosinset: _Callable[[_Pointer[_type.c_short]],  # p
                                _type.HRESULT]
    put_ariaSetsize: _Callable[[_type.c_short],  # v
                               _type.HRESULT]
    get_ariaSetsize: _Callable[[_Pointer[_type.c_short]],  # p
                               _type.HRESULT]
    put_ariaLevel: _Callable[[_type.c_short],  # v
                             _type.HRESULT]
    get_ariaLevel: _Callable[[_Pointer[_type.c_short]],  # p
                             _type.HRESULT]
    put_ariaValuemin: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaValuemin: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaValuemax: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaValuemax: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaControls: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaControls: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_ariaDescribedby: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_ariaDescribedby: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_ariaFlowto: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_ariaFlowto: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_ariaLabelledby: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_ariaLabelledby: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_ariaActivedescendant: _Callable[[_type.BSTR],  # v
                                        _type.HRESULT]
    get_ariaActivedescendant: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]
    put_ariaOwns: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_ariaOwns: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    hasAttributes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasAttributes
                             _type.HRESULT]
    put_ariaLive: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_ariaLive: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_ariaRelevant: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_ariaRelevant: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]


class IHTMLElement6(_oaidl.IDispatch):
    getAttributeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                               _type.BSTR,  # strAttributeName
                               _Pointer[_struct.VARIANT]],  # AttributeValue
                              _type.HRESULT]
    setAttributeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                               _type.BSTR,  # strAttributeName
                               _Pointer[_struct.VARIANT]],  # pvarAttributeValue
                              _type.HRESULT]
    removeAttributeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                  _type.BSTR],  # strAttributeName
                                 _type.HRESULT]
    getAttributeNodeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                                   _type.BSTR,  # bstrname
                                   _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                  _type.HRESULT]
    setAttributeNodeNS: _Callable[[IHTMLDOMAttribute2,  # pattr
                                   _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                  _type.HRESULT]
    hasAttributeNS: _Callable[[_Pointer[_struct.VARIANT],  # pvarNS
                               _type.BSTR,  # name
                               _Pointer[_type.VARIANT_BOOL]],  # pfHasAttribute
                              _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _Pointer[_struct.VARIANT]],  # pvarAttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR],  # strAttributeName
                               _type.HRESULT]
    getAttributeNode: _Callable[[_type.BSTR,  # strAttributeName
                                 _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                _type.HRESULT]
    setAttributeNode: _Callable[[IHTMLDOMAttribute2,  # pattr
                                 _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                _type.HRESULT]
    removeAttributeNode: _Callable[[IHTMLDOMAttribute2,  # pattr
                                    _Pointer[IHTMLDOMAttribute2]],  # ppretAttribute
                                   _type.HRESULT]
    hasAttribute: _Callable[[_type.BSTR,  # name
                             _Pointer[_type.VARIANT_BOOL]],  # pfHasAttribute
                            _type.HRESULT]
    getElementsByTagNameNS: _Callable[[_Pointer[_struct.VARIANT],  # varNS
                                       _type.BSTR,  # bstrLocalName
                                       _Pointer[IHTMLElementCollection]],  # pelColl
                                      _type.HRESULT]
    get_tagName: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_nodeName: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    getElementsByClassName: _Callable[[_type.BSTR,  # v
                                       _Pointer[IHTMLElementCollection]],  # pel
                                      _type.HRESULT]
    msMatchesSelector: _Callable[[_type.BSTR,  # v
                                  _Pointer[_type.VARIANT_BOOL]],  # pfMatches
                                 _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_oncanplay: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_oncanplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_oncanplaythrough: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_oncanplaythrough: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_ondurationchange: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_ondurationchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onemptied: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onemptied: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onended: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onended: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_oninput: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_oninput: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onloadeddata: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onloadeddata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onloadedmetadata: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onloadedmetadata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onloadstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onloadstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onpause: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onpause: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onplay: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onplaying: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onplaying: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onprogress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onprogress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onratechange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onratechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onreset: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onreset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onseeked: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onseeked: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onseeking: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onseeking: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onstalled: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstalled: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onsubmit: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onsubmit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onsuspend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onsuspend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ontimeupdate: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_ontimeupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onvolumechange: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onvolumechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onwaiting: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onwaiting: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    hasAttributes: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfHasAttributes
                             _type.HRESULT]


class IHTMLElement7(_oaidl.IDispatch):
    put_onmspointerdown: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerdown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointermove: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointermove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerup: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onmspointerup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onmspointerover: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerout: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmspointerout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmspointercancel: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmspointercancel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmspointerhover: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmspointerhover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmslostpointercapture: _Callable[[_struct.VARIANT],  # v
                                          _type.HRESULT]
    get_onmslostpointercapture: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                          _type.HRESULT]
    put_onmsgotpointercapture: _Callable[[_struct.VARIANT],  # v
                                         _type.HRESULT]
    get_onmsgotpointercapture: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                         _type.HRESULT]
    put_onmsgesturestart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsgesturestart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsgesturechange: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmsgesturechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmsgestureend: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgestureend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturehold: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmsgesturehold: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmsgesturetap: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgesturetap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturedoubletap: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_onmsgesturedoubletap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_onmsinertiastart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsinertiastart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    msSetPointerCapture: _Callable[[_type.c_long],  # pointerId
                                   _type.HRESULT]
    msReleasePointerCapture: _Callable[[_type.c_long],  # pointerId
                                       _type.HRESULT]
    put_onmstransitionstart: _Callable[[_struct.VARIANT],  # v
                                       _type.HRESULT]
    get_onmstransitionstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                       _type.HRESULT]
    put_onmstransitionend: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmstransitionend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmsanimationstart: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onmsanimationstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onmsanimationend: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsanimationend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsanimationiteration: _Callable[[_struct.VARIANT],  # v
                                          _type.HRESULT]
    get_onmsanimationiteration: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                          _type.HRESULT]
    put_oninvalid: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_oninvalid: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_xmsAcceleratorKey: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_xmsAcceleratorKey: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_spellcheck: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_spellcheck: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmsmanipulationstatechanged: _Callable[[_struct.VARIANT],  # v
                                                _type.HRESULT]
    get_onmsmanipulationstatechanged: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                                _type.HRESULT]
    put_oncuechange: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_oncuechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]


class IHTMLElementAppliedStyles(_oaidl.IDispatch):
    msGetRulesApplied: _Callable[[_Pointer[IRulesAppliedCollection]],  # ppRulesAppliedCollection
                                 _type.HRESULT]
    msGetRulesAppliedWithAncestor: _Callable[[_struct.VARIANT,  # varContext
                                              _Pointer[IRulesAppliedCollection]],  # ppRulesAppliedCollection
                                             _type.HRESULT]


class IElementTraversal(_oaidl.IDispatch):
    get_firstElementChild: _Callable[[_Pointer[IHTMLElement]],  # p
                                     _type.HRESULT]
    get_lastElementChild: _Callable[[_Pointer[IHTMLElement]],  # p
                                    _type.HRESULT]
    get_previousElementSibling: _Callable[[_Pointer[IHTMLElement]],  # p
                                          _type.HRESULT]
    get_nextElementSibling: _Callable[[_Pointer[IHTMLElement]],  # p
                                      _type.HRESULT]
    get_childElementCount: _Callable[[_Pointer[_type.c_long]],  # p
                                     _type.HRESULT]


class IHTMLDatabinding(_oaidl.IDispatch):
    put_dataFld: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_dataFld: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_dataSrc: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_dataSrc: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_dataFormatAs: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_dataFormatAs: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]


class IHTMLDocument(_oaidl.IDispatch):
    get_Script: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]


class IHTMLElementDefaults(_oaidl.IDispatch):
    get_style: _Callable[[_Pointer[IHTMLStyle]],  # p
                         _type.HRESULT]
    put_tabStop: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_tabStop: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_viewInheritStyle: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_viewInheritStyle: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_viewMasterTab: _Callable[[_type.VARIANT_BOOL],  # v
                                 _type.HRESULT]
    get_viewMasterTab: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    put_scrollSegmentX: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_scrollSegmentX: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    put_scrollSegmentY: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_scrollSegmentY: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    put_isMultiLine: _Callable[[_type.VARIANT_BOOL],  # v
                               _type.HRESULT]
    get_isMultiLine: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    put_contentEditable: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_contentEditable: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_canHaveHTML: _Callable[[_type.VARIANT_BOOL],  # v
                               _type.HRESULT]
    get_canHaveHTML: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    putref_viewLink: _Callable[[IHTMLDocument],  # v
                               _type.HRESULT]
    get_viewLink: _Callable[[_Pointer[IHTMLDocument]],  # p
                            _type.HRESULT]
    put_frozen: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_frozen: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]


class DispHTMLDefaults(_oaidl.IDispatch):
    pass


class IHTCDefaultDispatch(_oaidl.IDispatch):
    get_element: _Callable[[_Pointer[IHTMLElement]],  # p
                           _type.HRESULT]
    createEventObject: _Callable[[_Pointer[IHTMLEventObj]],  # eventObj
                                 _type.HRESULT]
    get_defaults: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_document: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]


class IHTCPropertyBehavior(_oaidl.IDispatch):
    fireChange: _Callable[[],
                          _type.HRESULT]
    put_value: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]


class IHTCMethodBehavior(_oaidl.IDispatch):
    pass


class IHTCEventBehavior(_oaidl.IDispatch):
    fire: _Callable[[IHTMLEventObj],  # pvar
                    _type.HRESULT]


class IHTCAttachBehavior(_oaidl.IDispatch):
    fireEvent: _Callable[[_oaidl.IDispatch],  # evt
                         _type.HRESULT]
    detachEvent: _Callable[[],
                           _type.HRESULT]


class IHTCAttachBehavior2(_oaidl.IDispatch):
    fireEvent: _Callable[[_struct.VARIANT],  # evt
                         _type.HRESULT]


class IHTCDescBehavior(_oaidl.IDispatch):
    get_urn: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTCDefaultDispatch(_oaidl.IDispatch):
    pass


class DispHTCPropertyBehavior(_oaidl.IDispatch):
    pass


class DispHTCMethodBehavior(_oaidl.IDispatch):
    pass


class DispHTCEventBehavior(_oaidl.IDispatch):
    pass


class DispHTCAttachBehavior(_oaidl.IDispatch):
    pass


class DispHTCDescBehavior(_oaidl.IDispatch):
    pass


class IHTMLUrnCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_type.BSTR]],  # ppUrn
                    _type.HRESULT]


class DispHTMLUrnCollection(_oaidl.IDispatch):
    pass


class IHTMLGenericElement(_oaidl.IDispatch):
    get_recordset: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    namedRecordset: _Callable[[_type.BSTR,  # dataMember
                               _Pointer[_struct.VARIANT],  # hierarchy
                               _Pointer[_oaidl.IDispatch]],  # ppRecordset
                              _type.HRESULT]


class DispHTMLGenericElement(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetRuleApplied(_oaidl.IDispatch):
    get_msSpecificity: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    msGetSpecificity: _Callable[[_type.c_long,  # index
                                 _Pointer[_type.c_long]],  # p
                                _type.HRESULT]


class IHTMLStyleSheetRule2(_oaidl.IDispatch):
    put_selectorText: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_selectorText: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]


class IHTMLStyleSheetRulesCollection2(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLCSSRule]],  # ppHTMLCSSRule
                    _type.HRESULT]


class DispHTMLStyleSheetRule(_oaidl.IDispatch):
    pass


class DispHTMLStyleSheetRulesCollection(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetPage(_oaidl.IDispatch):
    get_selector: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_pseudoClass: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class IHTMLStyleSheetPage2(_oaidl.IDispatch):
    put_selectorText: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_selectorText: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_style: _Callable[[_Pointer[IHTMLRuleStyle]],  # p
                         _type.HRESULT]


class IHTMLStyleSheetPagesCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLStyleSheetPage]],  # ppHTMLStyleSheetPage
                    _type.HRESULT]


class DispHTMLStyleSheetPage(_oaidl.IDispatch):
    pass


class DispHTMLStyleSheetPagesCollection(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetsCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]


class IHTMLStyleSheet2(_oaidl.IDispatch):
    get_pages: _Callable[[_Pointer[IHTMLStyleSheetPagesCollection]],  # p
                         _type.HRESULT]
    addPageRule: _Callable[[_type.BSTR,  # bstrSelector
                            _type.BSTR,  # bstrStyle
                            _type.c_long,  # lIndex
                            _Pointer[_type.c_long]],  # plNewIndex
                           _type.HRESULT]


class IHTMLStyleSheet3(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_isAlternate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    get_isPrefAlternate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]


class IHTMLStyleSheet4(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    get_title: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_ownerNode: _Callable[[_Pointer[IHTMLElement]],  # p
                             _type.HRESULT]
    get_ownerRule: _Callable[[_Pointer[IHTMLCSSRule]],  # p
                             _type.HRESULT]
    get_cssRules: _Callable[[_Pointer[IHTMLStyleSheetRulesCollection]],  # p
                            _type.HRESULT]
    get_media: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    insertRule: _Callable[[_type.BSTR,  # bstrRule
                           _type.c_long,  # lIndex
                           _Pointer[_type.c_long]],  # plNewIndex
                          _type.HRESULT]
    deleteRule: _Callable[[_type.c_long],  # lIndex
                          _type.HRESULT]


class DispHTMLStyleSheet(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetsCollection2(_oaidl.IDispatch):
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]


class DispHTMLStyleSheetsCollection(_oaidl.IDispatch):
    pass


class HTMLLinkElementEvents2(_oaidl.IDispatch):
    pass


class HTMLLinkElementEvents(_oaidl.IDispatch):
    pass


class IHTMLLinkElement(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_rel: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_rel: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_rev: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_rev: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_styleSheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                              _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLLinkElement2(_oaidl.IDispatch):
    put_target: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLLinkElement3(_oaidl.IDispatch):
    put_charset: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_hreflang: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_hreflang: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class IHTMLLinkElement4(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLLinkElement5(_oaidl.IDispatch):
    get_sheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                         _type.HRESULT]


class DispHTMLLinkElement(_oaidl.IDispatch):
    pass


class IHTMLTxtRange(_oaidl.IDispatch):
    get_htmlText: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    parentElement: _Callable[[_Pointer[IHTMLElement]],  # parent
                             _type.HRESULT]
    duplicate: _Callable[[_Pointer[IHTMLTxtRange]],  # Duplicate
                         _type.HRESULT]
    inRange: _Callable[[IHTMLTxtRange,  # Range
                        _Pointer[_type.VARIANT_BOOL]],  # InRange
                       _type.HRESULT]
    isEqual: _Callable[[IHTMLTxtRange,  # Range
                        _Pointer[_type.VARIANT_BOOL]],  # IsEqual
                       _type.HRESULT]
    scrollIntoView: _Callable[[_type.VARIANT_BOOL],  # fStart
                              _type.HRESULT]
    collapse: _Callable[[_type.VARIANT_BOOL],  # Start
                        _type.HRESULT]
    expand: _Callable[[_type.BSTR,  # Unit
                       _Pointer[_type.VARIANT_BOOL]],  # Success
                      _type.HRESULT]
    move: _Callable[[_type.BSTR,  # Unit
                     _type.c_long,  # Count
                     _Pointer[_type.c_long]],  # ActualCount
                    _type.HRESULT]
    moveStart: _Callable[[_type.BSTR,  # Unit
                          _type.c_long,  # Count
                          _Pointer[_type.c_long]],  # ActualCount
                         _type.HRESULT]
    moveEnd: _Callable[[_type.BSTR,  # Unit
                        _type.c_long,  # Count
                        _Pointer[_type.c_long]],  # ActualCount
                       _type.HRESULT]
    select: _Callable[[],
                      _type.HRESULT]
    pasteHTML: _Callable[[_type.BSTR],  # html
                         _type.HRESULT]
    moveToElementText: _Callable[[IHTMLElement],  # element
                                 _type.HRESULT]
    setEndPoint: _Callable[[_type.BSTR,  # how
                            IHTMLTxtRange],  # SourceRange
                           _type.HRESULT]
    compareEndPoints: _Callable[[_type.BSTR,  # how
                                 IHTMLTxtRange,  # SourceRange
                                 _Pointer[_type.c_long]],  # ret
                                _type.HRESULT]
    findText: _Callable[[_type.BSTR,  # String
                         _type.c_long,  # count
                         _type.c_long,  # Flags
                         _Pointer[_type.VARIANT_BOOL]],  # Success
                        _type.HRESULT]
    moveToPoint: _Callable[[_type.c_long,  # x
                            _type.c_long],  # y
                           _type.HRESULT]
    getBookmark: _Callable[[_Pointer[_type.BSTR]],  # Boolmark
                           _type.HRESULT]
    moveToBookmark: _Callable[[_type.BSTR,  # Bookmark
                               _Pointer[_type.VARIANT_BOOL]],  # Success
                              _type.HRESULT]
    queryCommandSupported: _Callable[[_type.BSTR,  # cmdID
                                      _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                     _type.HRESULT]
    queryCommandEnabled: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]
    queryCommandState: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                 _type.HRESULT]
    queryCommandIndeterm: _Callable[[_type.BSTR,  # cmdID
                                     _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                    _type.HRESULT]
    queryCommandText: _Callable[[_type.BSTR,  # cmdID
                                 _Pointer[_type.BSTR]],  # pcmdText
                                _type.HRESULT]
    queryCommandValue: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_struct.VARIANT]],  # pcmdValue
                                 _type.HRESULT]
    execCommand: _Callable[[_type.BSTR,  # cmdID
                            _type.VARIANT_BOOL,  # showUI
                            _struct.VARIANT,  # value
                            _Pointer[_type.VARIANT_BOOL]],  # pfRet
                           _type.HRESULT]
    execCommandShowHelp: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]


class IHTMLTextRangeMetrics(_oaidl.IDispatch):
    get_offsetTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_offsetLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_boundingTop: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_boundingLeft: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_boundingWidth: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    get_boundingHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]


class IHTMLTextRangeMetrics2(_oaidl.IDispatch):
    getClientRects: _Callable[[_Pointer[IHTMLRectCollection]],  # pRectCol
                              _type.HRESULT]
    getBoundingClientRect: _Callable[[_Pointer[IHTMLRect]],  # pRect
                                     _type.HRESULT]


class IHTMLTxtRangeCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]


class IHTMLDOMRange(_oaidl.IDispatch):
    get_startContainer: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                                  _type.HRESULT]
    get_startOffset: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_endContainer: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                                _type.HRESULT]
    get_endOffset: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_collapsed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_commonAncestorContainer: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                                           _type.HRESULT]
    setStart: _Callable[[_oaidl.IDispatch,  # refNode
                         _type.c_long],  # offset
                        _type.HRESULT]
    setEnd: _Callable[[_oaidl.IDispatch,  # refNode
                       _type.c_long],  # offset
                      _type.HRESULT]
    setStartBefore: _Callable[[_oaidl.IDispatch],  # refNode
                              _type.HRESULT]
    setStartAfter: _Callable[[_oaidl.IDispatch],  # refNode
                             _type.HRESULT]
    setEndBefore: _Callable[[_oaidl.IDispatch],  # refNode
                            _type.HRESULT]
    setEndAfter: _Callable[[_oaidl.IDispatch],  # refNode
                           _type.HRESULT]
    collapse: _Callable[[_type.VARIANT_BOOL],  # toStart
                        _type.HRESULT]
    selectNode: _Callable[[_oaidl.IDispatch],  # refNode
                          _type.HRESULT]
    selectNodeContents: _Callable[[_oaidl.IDispatch],  # refNode
                                  _type.HRESULT]
    compareBoundaryPoints: _Callable[[_type.c_short,  # how
                                      _oaidl.IDispatch,  # sourceRange
                                      _Pointer[_type.c_long]],  # compareResult
                                     _type.HRESULT]
    deleteContents: _Callable[[],
                              _type.HRESULT]
    extractContents: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDocumentFragment
                               _type.HRESULT]
    cloneContents: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDocumentFragment
                             _type.HRESULT]
    insertNode: _Callable[[_oaidl.IDispatch],  # newNode
                          _type.HRESULT]
    surroundContents: _Callable[[_oaidl.IDispatch],  # newParent
                                _type.HRESULT]
    cloneRange: _Callable[[_Pointer[IHTMLDOMRange]],  # ppClonedRange
                          _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # pRangeString
                        _type.HRESULT]
    detach: _Callable[[],
                      _type.HRESULT]
    getClientRects: _Callable[[_Pointer[IHTMLRectCollection]],  # ppRectCol
                              _type.HRESULT]
    getBoundingClientRect: _Callable[[_Pointer[IHTMLRect]],  # ppRect
                                     _type.HRESULT]


class DispHTMLDOMRange(_oaidl.IDispatch):
    pass


class HTMLFormElementEvents2(_oaidl.IDispatch):
    pass


class HTMLFormElementEvents(_oaidl.IDispatch):
    pass


class IHTMLFormElement(_oaidl.IDispatch):
    put_action: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_action: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_dir: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_dir: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_encoding: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_encoding: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_method: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_method: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_elements: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    put_target: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_onsubmit: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onsubmit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onreset: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onreset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    submit: _Callable[[],
                      _type.HRESULT]
    reset: _Callable[[],
                     _type.HRESULT]
    put_length: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # name
                     _struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]
    tags: _Callable[[_struct.VARIANT,  # tagName
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLFormElement2(_oaidl.IDispatch):
    put_acceptCharset: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_acceptCharset: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    urns: _Callable[[_struct.VARIANT,  # urn
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLFormElement3(_oaidl.IDispatch):
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[_oaidl.IDispatch]],  # pdisp
                         _type.HRESULT]


class IHTMLSubmitData(_oaidl.IDispatch):
    appendNameValuePair: _Callable[[_type.BSTR,  # name
                                    _type.BSTR],  # value
                                   _type.HRESULT]
    appendNameFilePair: _Callable[[_type.BSTR,  # name
                                   _type.BSTR],  # filename
                                  _type.HRESULT]
    appendItemSeparator: _Callable[[],
                                   _type.HRESULT]


class IHTMLFormElement4(_oaidl.IDispatch):
    put_action: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_action: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispHTMLFormElement(_oaidl.IDispatch):
    pass


class HTMLControlElementEvents2(_oaidl.IDispatch):
    pass


class HTMLControlElementEvents(_oaidl.IDispatch):
    pass


class IHTMLControlElement(_oaidl.IDispatch):
    put_tabIndex: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_tabIndex: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    focus: _Callable[[],
                     _type.HRESULT]
    put_accessKey: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_accessKey: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onresize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onresize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    blur: _Callable[[],
                    _type.HRESULT]
    addFilter: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                         _type.HRESULT]
    removeFilter: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                            _type.HRESULT]
    get_clientHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_clientWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_clientTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_clientLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLTextElement(_oaidl.IDispatch):
    pass


class DispHTMLTextElement(_oaidl.IDispatch):
    pass


class HTMLTextContainerEvents2(_oaidl.IDispatch):
    pass


class HTMLTextContainerEvents(_oaidl.IDispatch):
    pass


class IHTMLTextContainer(_oaidl.IDispatch):
    createControlRange: _Callable[[_Pointer[_oaidl.IDispatch]],  # range
                                  _type.HRESULT]
    get_scrollHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_scrollWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_scrollTop: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_scrollTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_scrollLeft: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_scrollLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_onscroll: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onscroll: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]


class IHTMLControlRange(_oaidl.IDispatch):
    select: _Callable[[],
                      _type.HRESULT]
    add: _Callable[[IHTMLControlElement],  # item
                   _type.HRESULT]
    remove: _Callable[[_type.c_long],  # index
                      _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLElement]],  # pdisp
                    _type.HRESULT]
    scrollIntoView: _Callable[[_struct.VARIANT],  # varargStart
                              _type.HRESULT]
    queryCommandSupported: _Callable[[_type.BSTR,  # cmdID
                                      _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                     _type.HRESULT]
    queryCommandEnabled: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]
    queryCommandState: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                 _type.HRESULT]
    queryCommandIndeterm: _Callable[[_type.BSTR,  # cmdID
                                     _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                    _type.HRESULT]
    queryCommandText: _Callable[[_type.BSTR,  # cmdID
                                 _Pointer[_type.BSTR]],  # pcmdText
                                _type.HRESULT]
    queryCommandValue: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_struct.VARIANT]],  # pcmdValue
                                 _type.HRESULT]
    execCommand: _Callable[[_type.BSTR,  # cmdID
                            _type.VARIANT_BOOL,  # showUI
                            _struct.VARIANT,  # value
                            _Pointer[_type.VARIANT_BOOL]],  # pfRet
                           _type.HRESULT]
    execCommandShowHelp: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]
    commonParentElement: _Callable[[_Pointer[IHTMLElement]],  # parent
                                   _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLControlRange2(_oaidl.IDispatch):
    addElement: _Callable[[IHTMLElement],  # item
                          _type.HRESULT]


class HTMLImgEvents2(_oaidl.IDispatch):
    pass


class HTMLImgEvents(_oaidl.IDispatch):
    pass


class IHTMLImgElement(_oaidl.IDispatch):
    put_isMap: _Callable[[_type.VARIANT_BOOL],  # v
                         _type.HRESULT]
    get_isMap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                         _type.HRESULT]
    put_useMap: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_useMap: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_mimeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileSize: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileCreatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_fileModifiedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_fileUpdatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_protocol: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_nameProp: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_lowsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_lowsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_vrml: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_vrml: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_dynsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_dynsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_complete: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_loop: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_start: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_start: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLImgElement2(_oaidl.IDispatch):
    put_longDesc: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_longDesc: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class IHTMLImgElement3(_oaidl.IDispatch):
    put_longDesc: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_longDesc: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_vrml: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_vrml: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_lowsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_lowsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_dynsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_dynsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLImgElement4(_oaidl.IDispatch):
    get_naturalWidth: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_naturalHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]


class IHTMLMSImgElement(_oaidl.IDispatch):
    put_msPlayToDisabled: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_msPlayToDisabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_msPlayToPrimary: _Callable[[_type.VARIANT_BOOL],  # v
                                   _type.HRESULT]
    get_msPlayToPrimary: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]


class IHTMLImageElementFactory(_oaidl.IDispatch):
    create: _Callable[[_struct.VARIANT,  # width
                       _struct.VARIANT,  # height
                       _Pointer[IHTMLImgElement]],  # __MIDL__IHTMLImageElementFactory0000
                      _type.HRESULT]


class DispHTMLImg(_oaidl.IDispatch):
    pass


class IHTMLBodyElement(_oaidl.IDispatch):
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_bgProperties: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_bgProperties: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_leftMargin: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_leftMargin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_topMargin: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_topMargin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_rightMargin: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_rightMargin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_bottomMargin: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_bottomMargin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_noWrap: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noWrap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_text: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_link: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_link: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_vLink: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_vLink: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_aLink: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_aLink: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onunload: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_scroll: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_scroll: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onbeforeunload: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onbeforeunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLBodyElement2(_oaidl.IDispatch):
    put_onbeforeprint: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onbeforeprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onafterprint: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onafterprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]


class IHTMLBodyElement3(_oaidl.IDispatch):
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_ononline: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_ononline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onoffline: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onoffline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onhashchange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onhashchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]


class IHTMLBodyElement4(_oaidl.IDispatch):
    put_onmessage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmessage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onstorage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstorage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class IHTMLBodyElement5(_oaidl.IDispatch):
    put_onpopstate: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onpopstate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]


class DispHTMLBody(_oaidl.IDispatch):
    pass


class IHTMLFontElement(_oaidl.IDispatch):
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_face: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_face: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_size: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]


class DispHTMLFontElement(_oaidl.IDispatch):
    pass


class HTMLAnchorEvents2(_oaidl.IDispatch):
    pass


class HTMLAnchorEvents(_oaidl.IDispatch):
    pass


class IHTMLAnchorElement(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_target: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_rel: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_rel: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_rev: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_rev: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_urn: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_urn: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_Methods: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_Methods: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_host: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_host: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_hostname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_hostname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_pathname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_pathname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_port: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_port: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_protocol: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_protocol: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_search: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_search: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_hash: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_hash: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_accessKey: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_accessKey: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_protocolLong: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_mimeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_nameProp: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_tabIndex: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_tabIndex: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    focus: _Callable[[],
                     _type.HRESULT]
    blur: _Callable[[],
                    _type.HRESULT]


class IHTMLAnchorElement2(_oaidl.IDispatch):
    put_charset: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_coords: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_coords: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_hreflang: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_hreflang: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_shape: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_shape: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLAnchorElement3(_oaidl.IDispatch):
    put_shape: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_shape: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_coords: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_coords: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLAnchorElement(_oaidl.IDispatch):
    pass


class HTMLLabelEvents2(_oaidl.IDispatch):
    pass


class HTMLLabelEvents(_oaidl.IDispatch):
    pass


class IHTMLLabelElement(_oaidl.IDispatch):
    put_htmlFor: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_htmlFor: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_accessKey: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_accessKey: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class IHTMLLabelElement2(_oaidl.IDispatch):
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class DispHTMLLabelElement(_oaidl.IDispatch):
    pass


class IHTMLListElement(_oaidl.IDispatch):
    pass


class IHTMLListElement2(_oaidl.IDispatch):
    put_compact: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_compact: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]


class DispHTMLListElement(_oaidl.IDispatch):
    pass


class IHTMLUListElement(_oaidl.IDispatch):
    put_compact: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_compact: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLUListElement(_oaidl.IDispatch):
    pass


class IHTMLOListElement(_oaidl.IDispatch):
    put_compact: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_compact: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_start: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_start: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLOListElement(_oaidl.IDispatch):
    pass


class IHTMLLIElement(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]


class DispHTMLLIElement(_oaidl.IDispatch):
    pass


class IHTMLBlockElement(_oaidl.IDispatch):
    put_clear: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLBlockElement2(_oaidl.IDispatch):
    put_cite: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_cite: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLBlockElement3(_oaidl.IDispatch):
    put_cite: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_cite: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLBlockElement(_oaidl.IDispatch):
    pass


class IHTMLDivElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_noWrap: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noWrap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]


class DispHTMLDivElement(_oaidl.IDispatch):
    pass


class IHTMLDDElement(_oaidl.IDispatch):
    put_noWrap: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noWrap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]


class DispHTMLDDElement(_oaidl.IDispatch):
    pass


class IHTMLDTElement(_oaidl.IDispatch):
    put_noWrap: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noWrap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]


class DispHTMLDTElement(_oaidl.IDispatch):
    pass


class IHTMLBRElement(_oaidl.IDispatch):
    put_clear: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_clear: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLBRElement(_oaidl.IDispatch):
    pass


class IHTMLDListElement(_oaidl.IDispatch):
    put_compact: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_compact: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]


class DispHTMLDListElement(_oaidl.IDispatch):
    pass


class IHTMLHRElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_noShade: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_noShade: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_size: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]


class DispHTMLHRElement(_oaidl.IDispatch):
    pass


class IHTMLParaElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLParaElement(_oaidl.IDispatch):
    pass


class IHTMLElementCollection2(_oaidl.IDispatch):
    urns: _Callable[[_struct.VARIANT,  # urn
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLElementCollection3(_oaidl.IDispatch):
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[_oaidl.IDispatch]],  # pdisp
                         _type.HRESULT]


class IHTMLElementCollection4(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLElement2]],  # pNode
                    _type.HRESULT]
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[IHTMLElement2]],  # pNode
                         _type.HRESULT]


class DispHTMLElementCollection(_oaidl.IDispatch):
    pass


class IHTMLHeaderElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLHeaderElement(_oaidl.IDispatch):
    pass


class HTMLSelectElementEvents2(_oaidl.IDispatch):
    pass


class HTMLSelectElementEvents(_oaidl.IDispatch):
    pass


class IHTMLOptionElement(_oaidl.IDispatch):
    put_selected: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_selected: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_defaultSelected: _Callable[[_type.VARIANT_BOOL],  # v
                                   _type.HRESULT]
    get_defaultSelected: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]
    put_index: _Callable[[_type.LONG],  # v
                         _type.HRESULT]
    get_index: _Callable[[_Pointer[_type.LONG]],  # p
                         _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class IHTMLSelectElementEx(_Unknwnbase.IUnknown):
    ShowDropdown: _Callable[[_type.BOOL],  # fShow
                            _type.HRESULT]
    SetSelectExFlags: _Callable[[_type.DWORD],  # lFlags
                                _type.HRESULT]
    GetSelectExFlags: _Callable[[_Pointer[_type.DWORD]],  # pFlags
                                _type.HRESULT]
    GetDropdownOpen: _Callable[[_Pointer[_type.BOOL]],  # pfOpen
                               _type.HRESULT]


class IHTMLSelectElement(_oaidl.IDispatch):
    put_size: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_multiple: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_multiple: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_options: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                           _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_selectedIndex: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_selectedIndex: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    add: _Callable[[IHTMLElement,  # element
                    _struct.VARIANT],  # before
                   _type.HRESULT]
    remove: _Callable[[_type.c_long],  # index
                      _type.HRESULT]
    put_length: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # name
                     _struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]
    tags: _Callable[[_struct.VARIANT,  # tagName
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLSelectElement2(_oaidl.IDispatch):
    urns: _Callable[[_struct.VARIANT,  # urn
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLSelectElement4(_oaidl.IDispatch):
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[_oaidl.IDispatch]],  # pdisp
                         _type.HRESULT]


class IHTMLSelectElement5(_oaidl.IDispatch):
    add: _Callable[[IHTMLOptionElement,  # pElem
                    _Pointer[_struct.VARIANT]],  # pvarBefore
                   _type.HRESULT]


class IHTMLSelectElement6(_oaidl.IDispatch):
    add: _Callable[[IHTMLOptionElement,  # pElem
                    _Pointer[_struct.VARIANT]],  # pvarBefore
                   _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLSelectElement(_oaidl.IDispatch):
    pass


class DispHTMLWndSelectElement(_oaidl.IDispatch):
    pass


class IHTMLSelectionObject(_oaidl.IDispatch):
    createRange: _Callable[[_Pointer[_oaidl.IDispatch]],  # range
                           _type.HRESULT]
    empty: _Callable[[],
                     _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLSelectionObject2(_oaidl.IDispatch):
    createRangeCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # rangeCollection
                                     _type.HRESULT]
    get_typeDetail: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]


class IHTMLSelection(_oaidl.IDispatch):
    get_anchorNode: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                              _type.HRESULT]
    get_anchorOffset: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_focusNode: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                             _type.HRESULT]
    get_focusOffset: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_isCollapsed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    collapse: _Callable[[_oaidl.IDispatch,  # parentNode
                         _type.c_long],  # offfset
                        _type.HRESULT]
    collapseToStart: _Callable[[],
                               _type.HRESULT]
    collapseToEnd: _Callable[[],
                             _type.HRESULT]
    selectAllChildren: _Callable[[_oaidl.IDispatch],  # parentNode
                                 _type.HRESULT]
    deleteFromDocument: _Callable[[],
                                  _type.HRESULT]
    get_rangeCount: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    getRangeAt: _Callable[[_type.c_long,  # index
                           _Pointer[IHTMLDOMRange]],  # ppRange
                          _type.HRESULT]
    addRange: _Callable[[_oaidl.IDispatch],  # range
                        _type.HRESULT]
    removeRange: _Callable[[_oaidl.IDispatch],  # range
                           _type.HRESULT]
    removeAllRanges: _Callable[[],
                               _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # pSelectionString
                        _type.HRESULT]


class IHTMLOptionElement3(_oaidl.IDispatch):
    put_label: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_label: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLOptionElement4(_oaidl.IDispatch):
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLOptionElementFactory(_oaidl.IDispatch):
    create: _Callable[[_struct.VARIANT,  # text
                       _struct.VARIANT,  # value
                       _struct.VARIANT,  # defaultselected
                       _struct.VARIANT,  # selected
                       _Pointer[IHTMLOptionElement]],  # __MIDL__IHTMLOptionElementFactory0000
                      _type.HRESULT]


class DispHTMLOptionElement(_oaidl.IDispatch):
    pass


class DispHTMLWndOptionElement(_oaidl.IDispatch):
    pass


class HTMLButtonElementEvents2(_oaidl.IDispatch):
    pass


class HTMLButtonElementEvents(_oaidl.IDispatch):
    pass


class HTMLInputTextElementEvents2(_oaidl.IDispatch):
    pass


class HTMLOptionButtonElementEvents2(_oaidl.IDispatch):
    pass


class HTMLInputFileElementEvents2(_oaidl.IDispatch):
    pass


class HTMLInputImageEvents2(_oaidl.IDispatch):
    pass


class HTMLInputTextElementEvents(_oaidl.IDispatch):
    pass


class HTMLOptionButtonElementEvents(_oaidl.IDispatch):
    pass


class HTMLInputFileElementEvents(_oaidl.IDispatch):
    pass


class HTMLInputImageEvents(_oaidl.IDispatch):
    pass


class IHTMLInputElement(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    put_size: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_maxLength: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_maxLength: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    select: _Callable[[],
                      _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_defaultValue: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_defaultValue: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_readOnly: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_readOnly: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]
    put_indeterminate: _Callable[[_type.VARIANT_BOOL],  # v
                                 _type.HRESULT]
    get_indeterminate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    put_defaultChecked: _Callable[[_type.VARIANT_BOOL],  # v
                                  _type.HRESULT]
    get_defaultChecked: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    put_checked: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_checked: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_lowsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_lowsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_vrml: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_vrml: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_dynsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_dynsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_complete: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_loop: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_width: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_start: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_start: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLInputElement2(_oaidl.IDispatch):
    put_accept: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_accept: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_useMap: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_useMap: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLInputElement3(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_lowsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_lowsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_vrml: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_vrml: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_dynsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_dynsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLInputButtonElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLInputHiddenElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLInputTextElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    put_defaultValue: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_defaultValue: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_size: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_maxLength: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_maxLength: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    select: _Callable[[],
                      _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_readOnly: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_readOnly: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLInputTextElement2(_oaidl.IDispatch):
    put_selectionStart: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_selectionStart: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    put_selectionEnd: _Callable[[_type.c_long],  # v
                                _type.HRESULT]
    get_selectionEnd: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    setSelectionRange: _Callable[[_type.c_long,  # start
                                  _type.c_long],  # end
                                 _type.HRESULT]


class IHTMLInputFileElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    put_size: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_maxLength: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_maxLength: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    select: _Callable[[],
                      _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLOptionButtonElement(_oaidl.IDispatch):
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_checked: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_checked: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_defaultChecked: _Callable[[_type.VARIANT_BOOL],  # v
                                  _type.HRESULT]
    get_defaultChecked: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_status: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_indeterminate: _Callable[[_type.VARIANT_BOOL],  # v
                                 _type.HRESULT]
    get_indeterminate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class IHTMLInputImage(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_lowsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_lowsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_vrml: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_vrml: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_dynsrc: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_dynsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_complete: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_loop: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_start: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_start: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLInputRangeElement(_oaidl.IDispatch):
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_min: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_min: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_max: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_max: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_step: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_step: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_valueAsNumber: _Callable[[_type.c_double],  # v
                                 _type.HRESULT]
    get_valueAsNumber: _Callable[[_Pointer[_type.c_double]],  # p
                                 _type.HRESULT]
    stepUp: _Callable[[_type.c_long],  # n
                      _type.HRESULT]
    stepDown: _Callable[[_type.c_long],  # n
                        _type.HRESULT]


class DispHTMLInputElement(_oaidl.IDispatch):
    pass


class IHTMLTextAreaElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    put_defaultValue: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_defaultValue: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    select: _Callable[[],
                      _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_readOnly: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_readOnly: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_rows: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_rows: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_cols: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_cols: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_wrap: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_wrap: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLTextAreaElement2(_oaidl.IDispatch):
    put_selectionStart: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_selectionStart: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    put_selectionEnd: _Callable[[_type.c_long],  # v
                                _type.HRESULT]
    get_selectionEnd: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    setSelectionRange: _Callable[[_type.c_long,  # start
                                  _type.c_long],  # end
                                 _type.HRESULT]


class DispHTMLTextAreaElement(_oaidl.IDispatch):
    pass


class DispHTMLRichtextElement(_oaidl.IDispatch):
    pass


class IHTMLButtonElement(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_status: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    createTextRange: _Callable[[_Pointer[IHTMLTxtRange]],  # range
                               _type.HRESULT]


class IHTMLButtonElement2(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLButtonElement(_oaidl.IDispatch):
    pass


class HTMLMarqueeElementEvents2(_oaidl.IDispatch):
    pass


class HTMLMarqueeElementEvents(_oaidl.IDispatch):
    pass


class IHTMLMarqueeElement(_oaidl.IDispatch):
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_scrollDelay: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_scrollDelay: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_direction: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_behavior: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_behavior: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_scrollAmount: _Callable[[_type.c_long],  # v
                                _type.HRESULT]
    get_scrollAmount: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    put_loop: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_onfinish: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onfinish: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onstart: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onbounce: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onbounce: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_trueSpeed: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_trueSpeed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    start: _Callable[[],
                     _type.HRESULT]
    stop: _Callable[[],
                    _type.HRESULT]


class DispHTMLMarqueeElement(_oaidl.IDispatch):
    pass


class IHTMLHtmlElement(_oaidl.IDispatch):
    put_version: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLHeadElement(_oaidl.IDispatch):
    put_profile: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_profile: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLHeadElement2(_oaidl.IDispatch):
    put_profile: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_profile: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLTitleElement(_oaidl.IDispatch):
    put_text: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLMetaElement(_oaidl.IDispatch):
    put_httpEquiv: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_httpEquiv: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_content: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_content: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_url: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_charset: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLMetaElement2(_oaidl.IDispatch):
    put_scheme: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_scheme: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLMetaElement3(_oaidl.IDispatch):
    put_url: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]


class IHTMLBaseElement(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_target: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLBaseElement2(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLHtmlElement(_oaidl.IDispatch):
    pass


class DispHTMLHeadElement(_oaidl.IDispatch):
    pass


class DispHTMLTitleElement(_oaidl.IDispatch):
    pass


class DispHTMLMetaElement(_oaidl.IDispatch):
    pass


class DispHTMLBaseElement(_oaidl.IDispatch):
    pass


class IHTMLIsIndexElement(_oaidl.IDispatch):
    put_prompt: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_prompt: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_action: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_action: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLIsIndexElement2(_oaidl.IDispatch):
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class IHTMLNextIdElement(_oaidl.IDispatch):
    put_n: _Callable[[_type.BSTR],  # v
                     _type.HRESULT]
    get_n: _Callable[[_Pointer[_type.BSTR]],  # p
                     _type.HRESULT]


class DispHTMLIsIndexElement(_oaidl.IDispatch):
    pass


class DispHTMLNextIdElement(_oaidl.IDispatch):
    pass


class IHTMLBaseFontElement(_oaidl.IDispatch):
    put_color: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_color: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_face: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_face: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_size: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_size: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]


class DispHTMLBaseFontElement(_oaidl.IDispatch):
    pass


class IHTMLUnknownElement(_oaidl.IDispatch):
    pass


class DispHTMLUnknownElement(_oaidl.IDispatch):
    pass


class IWebGeolocation(_oaidl.IDispatch):
    getCurrentPosition: _Callable[[_oaidl.IDispatch,  # successCallback
                                   _oaidl.IDispatch,  # errorCallback
                                   _oaidl.IDispatch],  # options
                                  _type.HRESULT]
    watchPosition: _Callable[[_oaidl.IDispatch,  # successCallback
                              _oaidl.IDispatch,  # errorCallback
                              _oaidl.IDispatch,  # options
                              _Pointer[_type.c_long]],  # watchId
                             _type.HRESULT]
    clearWatch: _Callable[[_type.c_long],  # watchId
                          _type.HRESULT]


class IHTMLMimeTypesCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLPluginsCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    refresh: _Callable[[_type.VARIANT_BOOL],  # reload
                       _type.HRESULT]


class IOmHistory(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_short]],  # p
                          _type.HRESULT]
    back: _Callable[[_Pointer[_struct.VARIANT]],  # pvargdistance
                    _type.HRESULT]
    forward: _Callable[[_Pointer[_struct.VARIANT]],  # pvargdistance
                       _type.HRESULT]
    go: _Callable[[_Pointer[_struct.VARIANT]],  # pvargdistance
                  _type.HRESULT]


class IHTMLOpsProfile(_oaidl.IDispatch):
    addRequest: _Callable[[_type.BSTR,  # name
                           _struct.VARIANT,  # reserved
                           _Pointer[_type.VARIANT_BOOL]],  # success
                          _type.HRESULT]
    clearRequest: _Callable[[],
                            _type.HRESULT]
    doRequest: _Callable[[_struct.VARIANT,  # usage
                          _struct.VARIANT,  # fname
                          _struct.VARIANT,  # domain
                          _struct.VARIANT,  # path
                          _struct.VARIANT,  # expire
                          _struct.VARIANT],  # reserved
                         _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # name
                             _Pointer[_type.BSTR]],  # value
                            _type.HRESULT]
    setAttribute: _Callable[[_type.BSTR,  # name
                             _type.BSTR,  # value
                             _struct.VARIANT,  # prefs
                             _Pointer[_type.VARIANT_BOOL]],  # success
                            _type.HRESULT]
    commitChanges: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # success
                             _type.HRESULT]
    addReadRequest: _Callable[[_type.BSTR,  # name
                               _struct.VARIANT,  # reserved
                               _Pointer[_type.VARIANT_BOOL]],  # success
                              _type.HRESULT]
    doReadRequest: _Callable[[_struct.VARIANT,  # usage
                              _struct.VARIANT,  # fname
                              _struct.VARIANT,  # domain
                              _struct.VARIANT,  # path
                              _struct.VARIANT,  # expire
                              _struct.VARIANT],  # reserved
                             _type.HRESULT]
    doWriteRequest: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # success
                              _type.HRESULT]


class IOmNavigator(_oaidl.IDispatch):
    get_appCodeName: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    get_appName: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_appVersion: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_userAgent: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    javaEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # enabled
                           _type.HRESULT]
    taintEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # enabled
                            _type.HRESULT]
    get_mimeTypes: _Callable[[_Pointer[IHTMLMimeTypesCollection]],  # p
                             _type.HRESULT]
    get_plugins: _Callable[[_Pointer[IHTMLPluginsCollection]],  # p
                           _type.HRESULT]
    get_cookieEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    get_opsProfile: _Callable[[_Pointer[IHTMLOpsProfile]],  # p
                              _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # string
                        _type.HRESULT]
    get_cpuClass: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_systemLanguage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_browserLanguage: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_userLanguage: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_platform: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_appMinorVersion: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_connectionSpeed: _Callable[[_Pointer[_type.c_long]],  # p
                                   _type.HRESULT]
    get_onLine: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_userProfile: _Callable[[_Pointer[IHTMLOpsProfile]],  # p
                               _type.HRESULT]


class INavigatorGeolocation(_oaidl.IDispatch):
    get_geolocation: _Callable[[_Pointer[IWebGeolocation]],  # p
                               _type.HRESULT]


class INavigatorDoNotTrack(_oaidl.IDispatch):
    get_msDoNotTrack: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]


class IHTMLLocation(_oaidl.IDispatch):
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_protocol: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_protocol: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_host: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_host: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_hostname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_hostname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_port: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_port: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_pathname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_pathname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_search: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_search: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_hash: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_hash: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    reload: _Callable[[_type.VARIANT_BOOL],  # flag
                      _type.HRESULT]
    replace: _Callable[[_type.BSTR],  # bstr
                       _type.HRESULT]
    assign: _Callable[[_type.BSTR],  # bstr
                      _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # string
                        _type.HRESULT]


class DispHTMLHistory(_oaidl.IDispatch):
    pass


class DispHTMLNavigator(_oaidl.IDispatch):
    pass


class DispHTMLLocation(_oaidl.IDispatch):
    pass


class DispCPlugins(_oaidl.IDispatch):
    pass


class IHTMLBookmarkCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_struct.VARIANT]],  # pVarBookmark
                    _type.HRESULT]


class IHTMLDataTransfer(_oaidl.IDispatch):
    setData: _Callable[[_type.BSTR,  # format
                        _Pointer[_struct.VARIANT],  # data
                        _Pointer[_type.VARIANT_BOOL]],  # pret
                       _type.HRESULT]
    getData: _Callable[[_type.BSTR,  # format
                        _Pointer[_struct.VARIANT]],  # pvarRet
                       _type.HRESULT]
    clearData: _Callable[[_type.BSTR,  # format
                          _Pointer[_type.VARIANT_BOOL]],  # pret
                         _type.HRESULT]
    put_dropEffect: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_dropEffect: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_effectAllowed: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_effectAllowed: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]


class IHTMLEventObj2(_oaidl.IDispatch):
    setAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _struct.VARIANT,  # AttributeValue
                             _type.LONG],  # lFlags
                            _type.HRESULT]
    getAttribute: _Callable[[_type.BSTR,  # strAttributeName
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # AttributeValue
                            _type.HRESULT]
    removeAttribute: _Callable[[_type.BSTR,  # strAttributeName
                                _type.LONG,  # lFlags
                                _Pointer[_type.VARIANT_BOOL]],  # pfSuccess
                               _type.HRESULT]
    put_propertyName: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_propertyName: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    putref_bookmarks: _Callable[[IHTMLBookmarkCollection],  # v
                                _type.HRESULT]
    get_bookmarks: _Callable[[_Pointer[IHTMLBookmarkCollection]],  # p
                             _type.HRESULT]
    putref_recordset: _Callable[[_oaidl.IDispatch],  # v
                                _type.HRESULT]
    get_recordset: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    put_dataFld: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_dataFld: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    putref_boundElements: _Callable[[IHTMLElementCollection],  # v
                                    _type.HRESULT]
    get_boundElements: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                                 _type.HRESULT]
    put_repeat: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_repeat: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_srcUrn: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_srcUrn: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    putref_srcElement: _Callable[[IHTMLElement],  # v
                                 _type.HRESULT]
    get_srcElement: _Callable[[_Pointer[IHTMLElement]],  # p
                              _type.HRESULT]
    put_altKey: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_altKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_ctrlKey: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_ctrlKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_shiftKey: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_shiftKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    putref_fromElement: _Callable[[IHTMLElement],  # v
                                  _type.HRESULT]
    get_fromElement: _Callable[[_Pointer[IHTMLElement]],  # p
                               _type.HRESULT]
    putref_toElement: _Callable[[IHTMLElement],  # v
                                _type.HRESULT]
    get_toElement: _Callable[[_Pointer[IHTMLElement]],  # p
                             _type.HRESULT]
    put_button: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_button: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_qualifier: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_qualifier: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_reason: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_reason: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_x: _Callable[[_type.c_long],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_long],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    put_clientX: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_clientX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_clientY: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_clientY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_offsetX: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_offsetX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_offsetY: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_offsetY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_screenX: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_screenX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_screenY: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_screenY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    putref_srcFilter: _Callable[[_oaidl.IDispatch],  # v
                                _type.HRESULT]
    get_srcFilter: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_dataTransfer: _Callable[[_Pointer[IHTMLDataTransfer]],  # p
                                _type.HRESULT]


class IHTMLEventObj3(_oaidl.IDispatch):
    get_contentOverflow: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]
    put_shiftLeft: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_shiftLeft: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    put_altLeft: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_altLeft: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_ctrlLeft: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_ctrlLeft: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_imeCompositionChange: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                                        _type.HRESULT]
    get_imeNotifyCommand: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                                    _type.HRESULT]
    get_imeNotifyData: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                                 _type.HRESULT]
    get_imeRequest: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                              _type.HRESULT]
    get_imeRequestData: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                                  _type.HRESULT]
    get_keyboardLayout: _Callable[[_Pointer[_type.LONG_PTR]],  # p
                                  _type.HRESULT]
    get_behaviorCookie: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    get_behaviorPart: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_nextPage: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class IHTMLEventObj4(_oaidl.IDispatch):
    get_wheelDelta: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLEventObj5(_oaidl.IDispatch):
    put_url: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_source: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    put_origin: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_origin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_issession: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_issession: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]


class IHTMLEventObj6(_oaidl.IDispatch):
    get_actionURL: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_buttonID: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]


class DispCEventObj(_oaidl.IDispatch):
    pass


class IHTMLStyleMedia(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    matchMedium: _Callable[[_type.BSTR,  # mediaQuery
                            _Pointer[_type.VARIANT_BOOL]],  # matches
                           _type.HRESULT]


class DispHTMLStyleMedia(_oaidl.IDispatch):
    pass


class IHTMLFramesCollection2(_oaidl.IDispatch):
    item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_struct.VARIANT]],  # pvarResult
                    _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class HTMLWindowEvents3(_oaidl.IDispatch):
    pass


class HTMLWindowEvents2(_oaidl.IDispatch):
    pass


class HTMLWindowEvents(_oaidl.IDispatch):
    pass


class IHTMLDocument2(IHTMLDocument):
    get_all: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                       _type.HRESULT]
    get_body: _Callable[[_Pointer[IHTMLElement]],  # p
                        _type.HRESULT]
    get_activeElement: _Callable[[_Pointer[IHTMLElement]],  # p
                                 _type.HRESULT]
    get_images: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                          _type.HRESULT]
    get_applets: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                           _type.HRESULT]
    get_links: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                         _type.HRESULT]
    get_forms: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                         _type.HRESULT]
    get_anchors: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                           _type.HRESULT]
    put_title: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_title: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    get_scripts: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                           _type.HRESULT]
    put_designMode: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_designMode: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_selection: _Callable[[_Pointer[IHTMLSelectionObject]],  # p
                             _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_frames: _Callable[[_Pointer[IHTMLFramesCollection2]],  # p
                          _type.HRESULT]
    get_embeds: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                          _type.HRESULT]
    get_plugins: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                           _type.HRESULT]
    put_alinkColor: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_alinkColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_fgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_fgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_linkColor: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_linkColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_vlinkColor: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_vlinkColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_referrer: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_location: _Callable[[_Pointer[IHTMLLocation]],  # p
                            _type.HRESULT]
    get_lastModified: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_URL: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_URL: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_domain: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_domain: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_cookie: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_cookie: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_expando: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_expando: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_charset: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_defaultCharset: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_defaultCharset: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_mimeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileSize: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_fileCreatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_fileModifiedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    get_fileUpdatedDate: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    get_security: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_protocol: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_nameProp: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    write: _Callable[[_Pointer[_struct.SAFEARRAY]],  # psarray
                     _type.HRESULT]
    writeln: _Callable[[_Pointer[_struct.SAFEARRAY]],  # psarray
                       _type.HRESULT]
    open: _Callable[[_type.BSTR,  # url
                     _struct.VARIANT,  # name
                     _struct.VARIANT,  # features
                     _struct.VARIANT,  # replace
                     _Pointer[_oaidl.IDispatch]],  # pomWindowResult
                    _type.HRESULT]
    close: _Callable[[],
                     _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    queryCommandSupported: _Callable[[_type.BSTR,  # cmdID
                                      _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                     _type.HRESULT]
    queryCommandEnabled: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]
    queryCommandState: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                 _type.HRESULT]
    queryCommandIndeterm: _Callable[[_type.BSTR,  # cmdID
                                     _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                    _type.HRESULT]
    queryCommandText: _Callable[[_type.BSTR,  # cmdID
                                 _Pointer[_type.BSTR]],  # pcmdText
                                _type.HRESULT]
    queryCommandValue: _Callable[[_type.BSTR,  # cmdID
                                  _Pointer[_struct.VARIANT]],  # pcmdValue
                                 _type.HRESULT]
    execCommand: _Callable[[_type.BSTR,  # cmdID
                            _type.VARIANT_BOOL,  # showUI
                            _struct.VARIANT,  # value
                            _Pointer[_type.VARIANT_BOOL]],  # pfRet
                           _type.HRESULT]
    execCommandShowHelp: _Callable[[_type.BSTR,  # cmdID
                                    _Pointer[_type.VARIANT_BOOL]],  # pfRet
                                   _type.HRESULT]
    createElement: _Callable[[_type.BSTR,  # eTag
                              _Pointer[IHTMLElement]],  # newElem
                             _type.HRESULT]
    put_onhelp: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onhelp: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onclick: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_ondblclick: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondblclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onkeyup: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onkeyup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onkeydown: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onkeydown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onkeypress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onkeypress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmouseup: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmouseup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onmousedown: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousedown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmousemove: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousemove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmouseout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onmouseout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmouseover: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmouseover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onafterupdate: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onafterupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onrowexit: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onrowexit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onrowenter: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onrowenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondragstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onselectstart: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onselectstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    elementFromPoint: _Callable[[_type.c_long,  # x
                                 _type.c_long,  # y
                                 _Pointer[IHTMLElement]],  # elementHit
                                _type.HRESULT]
    get_parentWindow: _Callable[[_Pointer[IHTMLWindow2]],  # p
                                _type.HRESULT]
    get_styleSheets: _Callable[[_Pointer[IHTMLStyleSheetsCollection]],  # p
                               _type.HRESULT]
    put_onbeforeupdate: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onbeforeupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onerrorupdate: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onerrorupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]
    createStyleSheet: _Callable[[_type.BSTR,  # bstrHref
                                 _type.c_long,  # lIndex
                                 _Pointer[IHTMLStyleSheet]],  # ppnewStyleSheet
                                _type.HRESULT]


class IHTMLWindow2(IHTMLFramesCollection2):
    get_frames: _Callable[[_Pointer[IHTMLFramesCollection2]],  # p
                          _type.HRESULT]
    put_defaultStatus: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_defaultStatus: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    put_status: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    setTimeout: _Callable[[_type.BSTR,  # expression
                           _type.c_long,  # msec
                           _Pointer[_struct.VARIANT],  # language
                           _Pointer[_type.c_long]],  # timerID
                          _type.HRESULT]
    clearTimeout: _Callable[[_type.c_long],  # timerID
                            _type.HRESULT]
    alert: _Callable[[_type.BSTR],  # message
                     _type.HRESULT]
    confirm: _Callable[[_type.BSTR,  # message
                        _Pointer[_type.VARIANT_BOOL]],  # confirmed
                       _type.HRESULT]
    prompt: _Callable[[_type.BSTR,  # message
                       _type.BSTR,  # defstr
                       _Pointer[_struct.VARIANT]],  # textdata
                      _type.HRESULT]
    get_Image: _Callable[[_Pointer[IHTMLImageElementFactory]],  # p
                         _type.HRESULT]
    get_location: _Callable[[_Pointer[IHTMLLocation]],  # p
                            _type.HRESULT]
    get_history: _Callable[[_Pointer[IOmHistory]],  # p
                           _type.HRESULT]
    close: _Callable[[],
                     _type.HRESULT]
    put_opener: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_opener: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_navigator: _Callable[[_Pointer[IOmNavigator]],  # p
                             _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_parent: _Callable[[_Pointer[IHTMLWindow2]],  # p
                          _type.HRESULT]
    open: _Callable[[_type.BSTR,  # url
                     _type.BSTR,  # name
                     _type.BSTR,  # features
                     _type.VARIANT_BOOL,  # replace
                     _Pointer[IHTMLWindow2]],  # pomWindowResult
                    _type.HRESULT]
    get_self: _Callable[[_Pointer[IHTMLWindow2]],  # p
                        _type.HRESULT]
    get_top: _Callable[[_Pointer[IHTMLWindow2]],  # p
                       _type.HRESULT]
    get_window: _Callable[[_Pointer[IHTMLWindow2]],  # p
                          _type.HRESULT]
    navigate: _Callable[[_type.BSTR],  # url
                        _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onbeforeunload: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onbeforeunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onunload: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onhelp: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onhelp: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onresize: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onresize: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onscroll: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onscroll: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_document: _Callable[[_Pointer[IHTMLDocument2]],  # p
                            _type.HRESULT]
    get_event: _Callable[[_Pointer[IHTMLEventObj]],  # p
                         _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    showModalDialog: _Callable[[_type.BSTR,  # dialog
                                _Pointer[_struct.VARIANT],  # varArgIn
                                _Pointer[_struct.VARIANT],  # varOptions
                                _Pointer[_struct.VARIANT]],  # varArgOut
                               _type.HRESULT]
    showHelp: _Callable[[_type.BSTR,  # helpURL
                         _struct.VARIANT,  # helpArg
                         _type.BSTR],  # features
                        _type.HRESULT]
    get_screen: _Callable[[_Pointer[IHTMLScreen]],  # p
                          _type.HRESULT]
    get_Option: _Callable[[_Pointer[IHTMLOptionElementFactory]],  # p
                          _type.HRESULT]
    focus: _Callable[[],
                     _type.HRESULT]
    get_closed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    blur: _Callable[[],
                    _type.HRESULT]
    scroll: _Callable[[_type.c_long,  # x
                       _type.c_long],  # y
                      _type.HRESULT]
    get_clientInformation: _Callable[[_Pointer[IOmNavigator]],  # p
                                     _type.HRESULT]
    setInterval: _Callable[[_type.BSTR,  # expression
                            _type.c_long,  # msec
                            _Pointer[_struct.VARIANT],  # language
                            _Pointer[_type.c_long]],  # timerID
                           _type.HRESULT]
    clearInterval: _Callable[[_type.c_long],  # timerID
                             _type.HRESULT]
    put_offscreenBuffering: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_offscreenBuffering: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    execScript: _Callable[[_type.BSTR,  # code
                           _type.BSTR,  # language
                           _Pointer[_struct.VARIANT]],  # pvarRet
                          _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]
    scrollBy: _Callable[[_type.c_long,  # x
                         _type.c_long],  # y
                        _type.HRESULT]
    scrollTo: _Callable[[_type.c_long,  # x
                         _type.c_long],  # y
                        _type.HRESULT]
    moveTo: _Callable[[_type.c_long,  # x
                       _type.c_long],  # y
                      _type.HRESULT]
    moveBy: _Callable[[_type.c_long,  # x
                       _type.c_long],  # y
                      _type.HRESULT]
    resizeTo: _Callable[[_type.c_long,  # x
                         _type.c_long],  # y
                        _type.HRESULT]
    resizeBy: _Callable[[_type.c_long,  # x
                         _type.c_long],  # y
                        _type.HRESULT]
    get_external: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]


class IHTMLWindow3(_oaidl.IDispatch):
    get_screenLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_screenTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    attachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch,  # pDisp
                            _Pointer[_type.VARIANT_BOOL]],  # pfResult
                           _type.HRESULT]
    detachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch],  # pDisp
                           _type.HRESULT]
    setTimeout: _Callable[[_Pointer[_struct.VARIANT],  # expression
                           _type.c_long,  # msec
                           _Pointer[_struct.VARIANT],  # language
                           _Pointer[_type.c_long]],  # timerID
                          _type.HRESULT]
    setInterval: _Callable[[_Pointer[_struct.VARIANT],  # expression
                            _type.c_long,  # msec
                            _Pointer[_struct.VARIANT],  # language
                            _Pointer[_type.c_long]],  # timerID
                           _type.HRESULT]
    print: _Callable[[],
                     _type.HRESULT]
    put_onbeforeprint: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onbeforeprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onafterprint: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onafterprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_clipboardData: _Callable[[_Pointer[IHTMLDataTransfer]],  # p
                                 _type.HRESULT]
    showModelessDialog: _Callable[[_type.BSTR,  # url
                                   _Pointer[_struct.VARIANT],  # varArgIn
                                   _Pointer[_struct.VARIANT],  # options
                                   _Pointer[IHTMLWindow2]],  # pDialog
                                  _type.HRESULT]


class IHTMLFrameBase(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_frameBorder: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_frameBorder: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_frameSpacing: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_frameSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_marginWidth: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_marginWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_marginHeight: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_marginHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_noResize: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_noResize: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_scrolling: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_scrolling: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class IHTMLStorage(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_remainingSpace: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    key: _Callable[[_type.c_long,  # lIndex
                    _Pointer[_type.BSTR]],  # __MIDL__IHTMLStorage0000
                   _type.HRESULT]
    getItem: _Callable[[_type.BSTR,  # bstrKey
                        _Pointer[_struct.VARIANT]],  # __MIDL__IHTMLStorage0001
                       _type.HRESULT]
    setItem: _Callable[[_type.BSTR,  # bstrKey
                        _type.BSTR],  # bstrValue
                       _type.HRESULT]
    removeItem: _Callable[[_type.BSTR],  # bstrKey
                          _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]


class IHTMLPerformance(_oaidl.IDispatch):
    get_navigation: _Callable[[_Pointer[IHTMLPerformanceNavigation]],  # p
                              _type.HRESULT]
    get_timing: _Callable[[_Pointer[IHTMLPerformanceTiming]],  # p
                          _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # string
                        _type.HRESULT]
    toJSON: _Callable[[_Pointer[_struct.VARIANT]],  # pVar
                      _type.HRESULT]


class IHTMLApplicationCache(_oaidl.IDispatch):
    get_status: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_onchecking: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onchecking: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onnoupdate: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onnoupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondownloading: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_ondownloading: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onprogress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onprogress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onupdateready: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onupdateready: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_oncached: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_oncached: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onobsolete: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onobsolete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    update: _Callable[[],
                      _type.HRESULT]
    swapCache: _Callable[[],
                         _type.HRESULT]
    abort: _Callable[[],
                     _type.HRESULT]


class IHTMLScreen(_oaidl.IDispatch):
    get_colorDepth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_bufferDepth: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_bufferDepth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_updateInterval: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_updateInterval: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    get_availHeight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_availWidth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_fontSmoothingEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                        _type.HRESULT]


class IHTMLScreen2(_oaidl.IDispatch):
    get_logicalXDPI: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_logicalYDPI: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_deviceXDPI: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_deviceYDPI: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLScreen3(_oaidl.IDispatch):
    get_systemXDPI: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_systemYDPI: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLScreen4(_oaidl.IDispatch):
    get_pixelDepth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLWindow4(_oaidl.IDispatch):
    createPopup: _Callable[[_Pointer[_struct.VARIANT],  # varArgIn
                            _Pointer[_oaidl.IDispatch]],  # ppPopup
                           _type.HRESULT]
    get_frameElement: _Callable[[_Pointer[IHTMLFrameBase]],  # p
                                _type.HRESULT]


class IHTMLWindow5(_oaidl.IDispatch):
    put_XMLHttpRequest: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_XMLHttpRequest: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]


class IHTMLWindow6(_oaidl.IDispatch):
    put_XDomainRequest: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_XDomainRequest: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    get_sessionStorage: _Callable[[_Pointer[IHTMLStorage]],  # p
                                  _type.HRESULT]
    get_localStorage: _Callable[[_Pointer[IHTMLStorage]],  # p
                                _type.HRESULT]
    put_onhashchange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onhashchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_maxConnectionsPerServer: _Callable[[_Pointer[_type.c_long]],  # p
                                           _type.HRESULT]
    postMessage: _Callable[[_type.BSTR,  # msg
                            _struct.VARIANT],  # targetOrigin
                           _type.HRESULT]
    toStaticHTML: _Callable[[_type.BSTR,  # bstrHTML
                             _Pointer[_type.BSTR]],  # pbstrStaticHTML
                            _type.HRESULT]
    put_onmessage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmessage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    msWriteProfilerMark: _Callable[[_type.BSTR],  # bstrProfilerMarkName
                                   _type.HRESULT]


class IHTMLWindow7(_oaidl.IDispatch):
    getSelection: _Callable[[_Pointer[IHTMLSelection]],  # ppIHTMLSelection
                            _type.HRESULT]
    getComputedStyle: _Callable[[IHTMLDOMNode,  # varArgIn
                                 _type.BSTR,  # bstrPseudoElt
                                 _Pointer[IHTMLCSSStyleDeclaration]],  # ppComputedStyle
                                _type.HRESULT]
    get_styleMedia: _Callable[[_Pointer[IHTMLStyleMedia]],  # p
                              _type.HRESULT]
    put_performance: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_performance: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    get_innerWidth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_innerHeight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_pageXOffset: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_pageYOffset: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_screenX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_screenY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_outerWidth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_outerHeight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_onabort: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onabort: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_oncanplay: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_oncanplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_oncanplaythrough: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_oncanplaythrough: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onchange: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onclick: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_oncontextmenu: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_oncontextmenu: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_ondblclick: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondblclick: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondrag: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrag: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_ondragend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_ondragend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ondragenter: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondragleave: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragleave: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondragover: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_ondragover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondragstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_ondragstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_ondrop: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_ondrop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_ondurationchange: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_ondurationchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onfocusin: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onfocusin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onfocusout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onfocusout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_oninput: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_oninput: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onemptied: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onemptied: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onended: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onended: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onkeydown: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onkeydown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onkeypress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onkeypress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onkeyup: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onkeyup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onloadeddata: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onloadeddata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onloadedmetadata: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onloadedmetadata: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onloadstart: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onloadstart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmousedown: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousedown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmouseenter: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmouseenter: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onmouseleave: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmouseleave: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onmousemove: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmousemove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmouseout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onmouseout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onmouseover: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_onmouseover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_onmouseup: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmouseup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onmousewheel: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmousewheel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onoffline: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onoffline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ononline: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_ononline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onprogress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onprogress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onratechange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onratechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onreset: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onreset: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onseeked: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onseeked: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onseeking: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onseeking: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onselect: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onstalled: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstalled: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onstorage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstorage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onsubmit: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onsubmit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onsuspend: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onsuspend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ontimeupdate: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_ontimeupdate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onpause: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onpause: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_onplay: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onplay: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onplaying: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onplaying: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onvolumechange: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onvolumechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onwaiting: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onwaiting: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class IHTMLWindow8(_oaidl.IDispatch):
    put_onmspointerdown: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerdown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointermove: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointermove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerup: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onmspointerup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onmspointerover: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerout: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmspointerout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmspointercancel: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmspointercancel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmspointerhover: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmspointerhover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsgesturestart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsgesturestart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsgesturechange: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmsgesturechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmsgestureend: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgestureend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturehold: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmsgesturehold: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmsgesturetap: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgesturetap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturedoubletap: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_onmsgesturedoubletap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_onmsinertiastart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsinertiastart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    get_applicationCache: _Callable[[_Pointer[IHTMLApplicationCache]],  # p
                                    _type.HRESULT]
    put_onpopstate: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onpopstate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]


class DispHTMLScreen(_oaidl.IDispatch):
    pass


class DispHTMLWindow2(_oaidl.IDispatch):
    pass


class DispHTMLWindowProxy(_oaidl.IDispatch):
    pass


class IHTMLDocumentCompatibleInfo(_oaidl.IDispatch):
    get_userAgent: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLDocumentCompatibleInfoCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLDocumentCompatibleInfo]],  # compatibleInfo
                    _type.HRESULT]


class DispHTMLDocumentCompatibleInfo(_oaidl.IDispatch):
    pass


class DispHTMLDocumentCompatibleInfoCollection(_oaidl.IDispatch):
    pass


class HTMLDocumentEvents4(_oaidl.IDispatch):
    pass


class HTMLDocumentEvents3(_oaidl.IDispatch):
    pass


class HTMLDocumentEvents2(_oaidl.IDispatch):
    pass


class HTMLDocumentEvents(_oaidl.IDispatch):
    pass


class ISVGSVGElement(_oaidl.IDispatch):
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]
    put_contentScriptType: _Callable[[_type.BSTR],  # v
                                     _type.HRESULT]
    get_contentScriptType: _Callable[[_Pointer[_type.BSTR]],  # p
                                     _type.HRESULT]
    put_contentStyleType: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_contentStyleType: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    putref_viewport: _Callable[[ISVGRect],  # v
                               _type.HRESULT]
    get_viewport: _Callable[[_Pointer[ISVGRect]],  # p
                            _type.HRESULT]
    put_pixelUnitToMillimeterX: _Callable[[_type.c_float],  # v
                                          _type.HRESULT]
    get_pixelUnitToMillimeterX: _Callable[[_Pointer[_type.c_float]],  # p
                                          _type.HRESULT]
    put_pixelUnitToMillimeterY: _Callable[[_type.c_float],  # v
                                          _type.HRESULT]
    get_pixelUnitToMillimeterY: _Callable[[_Pointer[_type.c_float]],  # p
                                          _type.HRESULT]
    put_screenPixelToMillimeterX: _Callable[[_type.c_float],  # v
                                            _type.HRESULT]
    get_screenPixelToMillimeterX: _Callable[[_Pointer[_type.c_float]],  # p
                                            _type.HRESULT]
    put_screenPixelToMillimeterY: _Callable[[_type.c_float],  # v
                                            _type.HRESULT]
    get_screenPixelToMillimeterY: _Callable[[_Pointer[_type.c_float]],  # p
                                            _type.HRESULT]
    put_useCurrentView: _Callable[[_type.VARIANT_BOOL],  # v
                                  _type.HRESULT]
    get_useCurrentView: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    putref_currentView: _Callable[[ISVGViewSpec],  # v
                                  _type.HRESULT]
    get_currentView: _Callable[[_Pointer[ISVGViewSpec]],  # p
                               _type.HRESULT]
    put_currentScale: _Callable[[_type.c_float],  # v
                                _type.HRESULT]
    get_currentScale: _Callable[[_Pointer[_type.c_float]],  # p
                                _type.HRESULT]
    putref_currentTranslate: _Callable[[ISVGPoint],  # v
                                       _type.HRESULT]
    get_currentTranslate: _Callable[[_Pointer[ISVGPoint]],  # p
                                    _type.HRESULT]
    suspendRedraw: _Callable[[_type.ULONG,  # maxWaitMilliseconds
                              _Pointer[_type.ULONG]],  # pResult
                             _type.HRESULT]
    unsuspendRedraw: _Callable[[_type.ULONG],  # suspendHandeID
                               _type.HRESULT]
    unsuspendRedrawAll: _Callable[[],
                                  _type.HRESULT]
    forceRedraw: _Callable[[],
                           _type.HRESULT]
    pauseAnimations: _Callable[[],
                               _type.HRESULT]
    unpauseAnimations: _Callable[[],
                                 _type.HRESULT]
    animationsPaused: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pResult
                                _type.HRESULT]
    getCurrentTime: _Callable[[_Pointer[_type.c_float]],  # pResult
                              _type.HRESULT]
    setCurrentTime: _Callable[[_type.c_float],  # seconds
                              _type.HRESULT]
    getIntersectionList: _Callable[[ISVGRect,  # rect
                                    ISVGElement,  # referenceElement
                                    _Pointer[_struct.VARIANT]],  # pResult
                                   _type.HRESULT]
    getEnclosureList: _Callable[[ISVGRect,  # rect
                                 ISVGElement,  # referenceElement
                                 _Pointer[_struct.VARIANT]],  # pResult
                                _type.HRESULT]
    checkIntersection: _Callable[[ISVGElement,  # element
                                  ISVGRect,  # rect
                                  _Pointer[_type.VARIANT_BOOL]],  # pResult
                                 _type.HRESULT]
    checkEnclosure: _Callable[[ISVGElement,  # element
                               ISVGRect,  # rect
                               _Pointer[_type.VARIANT_BOOL]],  # pResult
                              _type.HRESULT]
    deselectAll: _Callable[[],
                           _type.HRESULT]
    createSVGNumber: _Callable[[_Pointer[ISVGNumber]],  # pResult
                               _type.HRESULT]
    createSVGLength: _Callable[[_Pointer[ISVGLength]],  # pResult
                               _type.HRESULT]
    createSVGAngle: _Callable[[_Pointer[ISVGAngle]],  # pResult
                              _type.HRESULT]
    createSVGPoint: _Callable[[_Pointer[ISVGPoint]],  # pResult
                              _type.HRESULT]
    createSVGMatrix: _Callable[[_Pointer[ISVGMatrix]],  # pResult
                               _type.HRESULT]
    createSVGRect: _Callable[[_Pointer[ISVGRect]],  # pResult
                             _type.HRESULT]
    createSVGTransform: _Callable[[_Pointer[ISVGTransform]],  # pResult
                                  _type.HRESULT]
    createSVGTransformFromMatrix: _Callable[[ISVGMatrix,  # matrix
                                             _Pointer[ISVGTransform]],  # pResult
                                            _type.HRESULT]
    getElementById: _Callable[[_type.BSTR,  # elementId
                               _Pointer[IHTMLElement]],  # pResult
                              _type.HRESULT]


class IDOMNodeIterator(_oaidl.IDispatch):
    get_root: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                        _type.HRESULT]
    get_whatToShow: _Callable[[_Pointer[_type.ULONG]],  # p
                              _type.HRESULT]
    get_filter: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_expandEntityReferences: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                          _type.HRESULT]
    nextNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                        _type.HRESULT]
    previousNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                            _type.HRESULT]
    detach: _Callable[[],
                      _type.HRESULT]


class IDOMTreeWalker(_oaidl.IDispatch):
    get_root: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                        _type.HRESULT]
    get_whatToShow: _Callable[[_Pointer[_type.ULONG]],  # p
                              _type.HRESULT]
    get_filter: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_expandEntityReferences: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                          _type.HRESULT]
    putref_currentNode: _Callable[[_oaidl.IDispatch],  # v
                                  _type.HRESULT]
    get_currentNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                               _type.HRESULT]
    parentNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                          _type.HRESULT]
    firstChild: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                          _type.HRESULT]
    lastChild: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                         _type.HRESULT]
    previousSibling: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                               _type.HRESULT]
    nextSibling: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                           _type.HRESULT]
    previousNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                            _type.HRESULT]
    nextNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppRetNode
                        _type.HRESULT]


class IDOMProcessingInstruction(_oaidl.IDispatch):
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLDocument3(_oaidl.IDispatch):
    releaseCapture: _Callable[[],
                              _type.HRESULT]
    recalc: _Callable[[_type.VARIANT_BOOL],  # fForce
                      _type.HRESULT]
    createTextNode: _Callable[[_type.BSTR,  # text
                               _Pointer[IHTMLDOMNode]],  # newTextNode
                              _type.HRESULT]
    get_documentElement: _Callable[[_Pointer[IHTMLElement]],  # p
                                   _type.HRESULT]
    get_uniqueID: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    attachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch,  # pDisp
                            _Pointer[_type.VARIANT_BOOL]],  # pfResult
                           _type.HRESULT]
    detachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch],  # pDisp
                           _type.HRESULT]
    put_onrowsdelete: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onrowsdelete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onrowsinserted: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onrowsinserted: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_oncellchange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_oncellchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_ondatasetchanged: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_ondatasetchanged: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_ondataavailable: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_ondataavailable: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_ondatasetcomplete: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_ondatasetcomplete: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onpropertychange: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onpropertychange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_dir: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_dir: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_oncontextmenu: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_oncontextmenu: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onstop: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onstop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    createDocumentFragment: _Callable[[_Pointer[IHTMLDocument2]],  # pNewDoc
                                      _type.HRESULT]
    get_parentDocument: _Callable[[_Pointer[IHTMLDocument2]],  # p
                                  _type.HRESULT]
    put_enableDownload: _Callable[[_type.VARIANT_BOOL],  # v
                                  _type.HRESULT]
    get_enableDownload: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    put_baseUrl: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_baseUrl: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    put_inheritStyleSheets: _Callable[[_type.VARIANT_BOOL],  # v
                                      _type.HRESULT]
    get_inheritStyleSheets: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]
    put_onbeforeeditfocus: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onbeforeeditfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    getElementsByName: _Callable[[_type.BSTR,  # v
                                  _Pointer[IHTMLElementCollection]],  # pelColl
                                 _type.HRESULT]
    getElementById: _Callable[[_type.BSTR,  # v
                               _Pointer[IHTMLElement]],  # pel
                              _type.HRESULT]
    getElementsByTagName: _Callable[[_type.BSTR,  # v
                                     _Pointer[IHTMLElementCollection]],  # pelColl
                                    _type.HRESULT]


class IHTMLDocument4(_oaidl.IDispatch):
    focus: _Callable[[],
                     _type.HRESULT]
    hasFocus: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfFocus
                        _type.HRESULT]
    put_onselectionchange: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onselectionchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    get_namespaces: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                              _type.HRESULT]
    createDocumentFromUrl: _Callable[[_type.BSTR,  # bstrUrl
                                      _type.BSTR,  # bstrOptions
                                      _Pointer[IHTMLDocument2]],  # newDoc
                                     _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    createEventObject: _Callable[[_Pointer[_struct.VARIANT],  # pvarEventObject
                                  _Pointer[IHTMLEventObj]],  # ppEventObj
                                 _type.HRESULT]
    fireEvent: _Callable[[_type.BSTR,  # bstrEventName
                          _Pointer[_struct.VARIANT],  # pvarEventObject
                          _Pointer[_type.VARIANT_BOOL]],  # pfCancelled
                         _type.HRESULT]
    createRenderStyle: _Callable[[_type.BSTR,  # v
                                  _Pointer[IHTMLRenderStyle]],  # ppIHTMLRenderStyle
                                 _type.HRESULT]
    put_oncontrolselect: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_oncontrolselect: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_URLUnencoded: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]


class IHTMLDocument5(_oaidl.IDispatch):
    put_onmousewheel: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onmousewheel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_doctype: _Callable[[_Pointer[IHTMLDOMNode]],  # p
                           _type.HRESULT]
    get_implementation: _Callable[[_Pointer[IHTMLDOMImplementation]],  # p
                                  _type.HRESULT]
    createAttribute: _Callable[[_type.BSTR,  # bstrattrName
                                _Pointer[IHTMLDOMAttribute]],  # ppattribute
                               _type.HRESULT]
    createComment: _Callable[[_type.BSTR,  # bstrdata
                              _Pointer[IHTMLDOMNode]],  # ppRetNode
                             _type.HRESULT]
    put_onfocusin: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onfocusin: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onfocusout: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onfocusout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onactivate: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_ondeactivate: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_ondeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onbeforeactivate: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onbeforeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onbeforedeactivate: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onbeforedeactivate: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    get_compatMode: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]


class IHTMLDocument6(_oaidl.IDispatch):
    get_compatible: _Callable[[_Pointer[IHTMLDocumentCompatibleInfoCollection]],  # p
                              _type.HRESULT]
    get_documentMode: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onstorage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstorage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onstoragecommit: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onstoragecommit: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    getElementById: _Callable[[_type.BSTR,  # bstrId
                               _Pointer[IHTMLElement2]],  # ppRetElement
                              _type.HRESULT]
    updateSettings: _Callable[[],
                              _type.HRESULT]


class IHTMLDocument8(_oaidl.IDispatch):
    put_onmscontentzoom: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmscontentzoom: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerdown: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerdown: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointermove: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointermove: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerup: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onmspointerup: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onmspointerover: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmspointerover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmspointerout: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmspointerout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmspointercancel: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmspointercancel: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmspointerhover: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmspointerhover: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsgesturestart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsgesturestart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_onmsgesturechange: _Callable[[_struct.VARIANT],  # v
                                     _type.HRESULT]
    get_onmsgesturechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                     _type.HRESULT]
    put_onmsgestureend: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgestureend: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturehold: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_onmsgesturehold: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_onmsgesturetap: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onmsgesturetap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]
    put_onmsgesturedoubletap: _Callable[[_struct.VARIANT],  # v
                                        _type.HRESULT]
    get_onmsgesturedoubletap: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                        _type.HRESULT]
    put_onmsinertiastart: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_onmsinertiastart: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    elementsFromPoint: _Callable[[_type.c_float,  # x
                                  _type.c_float,  # y
                                  _Pointer[IHTMLDOMChildrenCollection]],  # elementsHit
                                 _type.HRESULT]
    elementsFromRect: _Callable[[_type.c_float,  # left
                                 _type.c_float,  # top
                                 _type.c_float,  # width
                                 _type.c_float,  # height
                                 _Pointer[IHTMLDOMChildrenCollection]],  # elementsHit
                                _type.HRESULT]
    put_onmsmanipulationstatechanged: _Callable[[_struct.VARIANT],  # v
                                                _type.HRESULT]
    get_onmsmanipulationstatechanged: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                                _type.HRESULT]
    put_msCapsLockWarningOff: _Callable[[_type.VARIANT_BOOL],  # v
                                        _type.HRESULT]
    get_msCapsLockWarningOff: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                        _type.HRESULT]


class IDocumentEvent(_oaidl.IDispatch):
    createEvent: _Callable[[_type.BSTR,  # eventType
                            _Pointer[IDOMEvent]],  # ppEvent
                           _type.HRESULT]


class IDocumentRange(_oaidl.IDispatch):
    createRange: _Callable[[_Pointer[IHTMLDOMRange]],  # ppIHTMLDOMRange
                           _type.HRESULT]


class IDocumentSelector(_oaidl.IDispatch):
    querySelector: _Callable[[_type.BSTR,  # v
                              _Pointer[IHTMLElement]],  # pel
                             _type.HRESULT]
    querySelectorAll: _Callable[[_type.BSTR,  # v
                                 _Pointer[IHTMLDOMChildrenCollection]],  # pel
                                _type.HRESULT]


class IDocumentTraversal(_oaidl.IDispatch):
    createNodeIterator: _Callable[[_oaidl.IDispatch,  # pRootNode
                                   _type.c_long,  # ulWhatToShow
                                   _Pointer[_struct.VARIANT],  # pFilter
                                   _type.VARIANT_BOOL,  # fEntityReferenceExpansion
                                   _Pointer[IDOMNodeIterator]],  # ppNodeIterator
                                  _type.HRESULT]
    createTreeWalker: _Callable[[_oaidl.IDispatch,  # pRootNode
                                 _type.c_long,  # ulWhatToShow
                                 _Pointer[_struct.VARIANT],  # pFilter
                                 _type.VARIANT_BOOL,  # fEntityReferenceExpansion
                                 _Pointer[IDOMTreeWalker]],  # ppTreeWalker
                                _type.HRESULT]


class DispHTMLDocument(_oaidl.IDispatch):
    pass


class DWebBridgeEvents(_oaidl.IDispatch):
    pass


class IWebBridge(_oaidl.IDispatch):
    put_URL: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_URL: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_Scrollbar: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_Scrollbar: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    put_embed: _Callable[[_type.VARIANT_BOOL],  # v
                         _type.HRESULT]
    get_embed: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                         _type.HRESULT]
    get_event: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                         _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    AboutBox: _Callable[[],
                        _type.HRESULT]


class IWBScriptControl(_oaidl.IDispatch):
    raiseEvent: _Callable[[_type.BSTR,  # name
                           _struct.VARIANT],  # eventData
                          _type.HRESULT]
    bubbleEvent: _Callable[[],
                           _type.HRESULT]
    setContextMenu: _Callable[[_struct.VARIANT],  # menuItemPairs
                              _type.HRESULT]
    put_selectableContent: _Callable[[_type.VARIANT_BOOL],  # v
                                     _type.HRESULT]
    get_selectableContent: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                     _type.HRESULT]
    get_frozen: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_scrollbar: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_scrollbar: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_visibility: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    put_onvisibilitychange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onvisibilitychange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]


class IHTMLEmbedElement(_oaidl.IDispatch):
    put_hidden: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_hidden: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_palette: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_pluginspage: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_units: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_units: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]


class IHTMLEmbedElement2(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_pluginspage: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class DispHTMLEmbed(_oaidl.IDispatch):
    pass


class HTMLMapEvents2(_oaidl.IDispatch):
    pass


class HTMLMapEvents(_oaidl.IDispatch):
    pass


class IHTMLAreasCollection(_oaidl.IDispatch):
    put_length: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # name
                     _struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]
    tags: _Callable[[_struct.VARIANT,  # tagName
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]
    add: _Callable[[IHTMLElement,  # element
                    _struct.VARIANT],  # before
                   _type.HRESULT]
    remove: _Callable[[_type.c_long],  # index
                      _type.HRESULT]


class IHTMLAreasCollection2(_oaidl.IDispatch):
    urns: _Callable[[_struct.VARIANT,  # urn
                     _Pointer[_oaidl.IDispatch]],  # pdisp
                    _type.HRESULT]


class IHTMLAreasCollection3(_oaidl.IDispatch):
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[_oaidl.IDispatch]],  # pdisp
                         _type.HRESULT]


class IHTMLAreasCollection4(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLElement2]],  # pNode
                    _type.HRESULT]
    namedItem: _Callable[[_type.BSTR,  # name
                          _Pointer[IHTMLElement2]],  # pNode
                         _type.HRESULT]


class IHTMLMapElement(_oaidl.IDispatch):
    get_areas: _Callable[[_Pointer[IHTMLAreasCollection]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLAreasCollection(_oaidl.IDispatch):
    pass


class DispHTMLMapElement(_oaidl.IDispatch):
    pass


class HTMLAreaEvents2(_oaidl.IDispatch):
    pass


class HTMLAreaEvents(_oaidl.IDispatch):
    pass


class IHTMLAreaElement(_oaidl.IDispatch):
    put_shape: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_shape: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_coords: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_coords: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_target: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_target: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_noHref: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noHref: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_host: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_host: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_hostname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_hostname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_pathname: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_pathname: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_port: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_port: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_protocol: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_protocol: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_search: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_search: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_hash: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_hash: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_onblur: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onblur: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onfocus: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onfocus: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_tabIndex: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_tabIndex: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    focus: _Callable[[],
                     _type.HRESULT]
    blur: _Callable[[],
                    _type.HRESULT]


class IHTMLAreaElement2(_oaidl.IDispatch):
    put_shape: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_shape: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_coords: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_coords: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_href: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_href: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispHTMLAreaElement(_oaidl.IDispatch):
    pass


class IHTMLTableCaption(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_vAlign: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_vAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispHTMLTableCaption(_oaidl.IDispatch):
    pass


class IHTMLCommentElement(_oaidl.IDispatch):
    put_text: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_atomic: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_atomic: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLCommentElement2(_oaidl.IDispatch):
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    substringData: _Callable[[_type.c_long,  # offset
                              _type.c_long,  # Count
                              _Pointer[_type.BSTR]],  # pbstrsubString
                             _type.HRESULT]
    appendData: _Callable[[_type.BSTR],  # bstrstring
                          _type.HRESULT]
    insertData: _Callable[[_type.c_long,  # offset
                           _type.BSTR],  # bstrstring
                          _type.HRESULT]
    deleteData: _Callable[[_type.c_long,  # offset
                           _type.c_long],  # Count
                          _type.HRESULT]
    replaceData: _Callable[[_type.c_long,  # offset
                            _type.c_long,  # Count
                            _type.BSTR],  # bstrstring
                           _type.HRESULT]


class IHTMLCommentElement3(_oaidl.IDispatch):
    substringData: _Callable[[_type.c_long,  # offset
                              _type.c_long,  # Count
                              _Pointer[_type.BSTR]],  # pbstrsubString
                             _type.HRESULT]
    insertData: _Callable[[_type.c_long,  # offset
                           _type.BSTR],  # bstrstring
                          _type.HRESULT]
    deleteData: _Callable[[_type.c_long,  # offset
                           _type.c_long],  # Count
                          _type.HRESULT]
    replaceData: _Callable[[_type.c_long,  # offset
                            _type.c_long,  # Count
                            _type.BSTR],  # bstrstring
                           _type.HRESULT]


class DispHTMLCommentElement(_oaidl.IDispatch):
    pass


class IHTMLPhraseElement(_oaidl.IDispatch):
    pass


class IHTMLPhraseElement2(_oaidl.IDispatch):
    put_cite: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_cite: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_dateTime: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_dateTime: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class IHTMLPhraseElement3(_oaidl.IDispatch):
    put_cite: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_cite: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLSpanElement(_oaidl.IDispatch):
    pass


class DispHTMLPhraseElement(_oaidl.IDispatch):
    pass


class DispHTMLSpanElement(_oaidl.IDispatch):
    pass


class HTMLTableEvents2(_oaidl.IDispatch):
    pass


class HTMLTableEvents(_oaidl.IDispatch):
    pass


class IHTMLTableSection(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_vAlign: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_vAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_rows: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                        _type.HRESULT]
    insertRow: _Callable[[_type.c_long,  # index
                          _Pointer[_oaidl.IDispatch]],  # row
                         _type.HRESULT]
    deleteRow: _Callable[[_type.c_long],  # index
                         _type.HRESULT]


class IHTMLTable(_oaidl.IDispatch):
    put_cols: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_cols: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_frame: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_frame: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_rules: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_rules: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_cellSpacing: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_cellSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_cellPadding: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_cellPadding: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_borderColor: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_borderColorLight: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderColorLight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderColorDark: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderColorDark: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    refresh: _Callable[[],
                       _type.HRESULT]
    get_rows: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_dataPageSize: _Callable[[_type.c_long],  # v
                                _type.HRESULT]
    get_dataPageSize: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    nextPage: _Callable[[],
                        _type.HRESULT]
    previousPage: _Callable[[],
                            _type.HRESULT]
    get_tHead: _Callable[[_Pointer[IHTMLTableSection]],  # p
                         _type.HRESULT]
    get_tFoot: _Callable[[_Pointer[IHTMLTableSection]],  # p
                         _type.HRESULT]
    get_tBodies: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                           _type.HRESULT]
    get_caption: _Callable[[_Pointer[IHTMLTableCaption]],  # p
                           _type.HRESULT]
    createTHead: _Callable[[_Pointer[_oaidl.IDispatch]],  # head
                           _type.HRESULT]
    deleteTHead: _Callable[[],
                           _type.HRESULT]
    createTFoot: _Callable[[_Pointer[_oaidl.IDispatch]],  # foot
                           _type.HRESULT]
    deleteTFoot: _Callable[[],
                           _type.HRESULT]
    createCaption: _Callable[[_Pointer[IHTMLTableCaption]],  # caption
                             _type.HRESULT]
    deleteCaption: _Callable[[],
                             _type.HRESULT]
    insertRow: _Callable[[_type.c_long,  # index
                          _Pointer[_oaidl.IDispatch]],  # row
                         _type.HRESULT]
    deleteRow: _Callable[[_type.c_long],  # index
                         _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]


class IHTMLTable2(_oaidl.IDispatch):
    firstPage: _Callable[[],
                         _type.HRESULT]
    lastPage: _Callable[[],
                        _type.HRESULT]
    get_cells: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                         _type.HRESULT]
    moveRow: _Callable[[_type.c_long,  # indexFrom
                        _type.c_long,  # indexTo
                        _Pointer[_oaidl.IDispatch]],  # row
                       _type.HRESULT]


class IHTMLTable3(_oaidl.IDispatch):
    put_summary: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_summary: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLTable4(_oaidl.IDispatch):
    putref_tHead: _Callable[[IHTMLTableSection],  # v
                            _type.HRESULT]
    get_tHead: _Callable[[_Pointer[IHTMLTableSection]],  # p
                         _type.HRESULT]
    putref_tFoot: _Callable[[IHTMLTableSection],  # v
                            _type.HRESULT]
    get_tFoot: _Callable[[_Pointer[IHTMLTableSection]],  # p
                         _type.HRESULT]
    putref_caption: _Callable[[IHTMLTableCaption],  # v
                              _type.HRESULT]
    get_caption: _Callable[[_Pointer[IHTMLTableCaption]],  # p
                           _type.HRESULT]
    insertRow: _Callable[[_type.c_long,  # index
                          _Pointer[_oaidl.IDispatch]],  # row
                         _type.HRESULT]
    deleteRow: _Callable[[_type.c_long],  # index
                         _type.HRESULT]
    createTBody: _Callable[[_Pointer[IHTMLTableSection]],  # tbody
                           _type.HRESULT]


class IHTMLTableCol(_oaidl.IDispatch):
    put_span: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_span: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_vAlign: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_vAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLTableCol2(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLTableCol3(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLTableSection2(_oaidl.IDispatch):
    moveRow: _Callable[[_type.c_long,  # indexFrom
                        _type.c_long,  # indexTo
                        _Pointer[_oaidl.IDispatch]],  # row
                       _type.HRESULT]


class IHTMLTableSection3(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLTableSection4(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    insertRow: _Callable[[_type.c_long,  # index
                          _Pointer[_oaidl.IDispatch]],  # row
                         _type.HRESULT]
    deleteRow: _Callable[[_type.c_long],  # index
                         _type.HRESULT]


class IHTMLTableRow(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_vAlign: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_vAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_borderColor: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_borderColorLight: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderColorLight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderColorDark: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderColorDark: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_rowIndex: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_sectionRowIndex: _Callable[[_Pointer[_type.c_long]],  # p
                                   _type.HRESULT]
    get_cells: _Callable[[_Pointer[IHTMLElementCollection]],  # p
                         _type.HRESULT]
    insertCell: _Callable[[_type.c_long,  # index
                           _Pointer[_oaidl.IDispatch]],  # row
                          _type.HRESULT]
    deleteCell: _Callable[[_type.c_long],  # index
                          _type.HRESULT]


class IHTMLTableRow2(_oaidl.IDispatch):
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]


class IHTMLTableRow3(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLTableRow4(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    insertCell: _Callable[[_type.c_long,  # index
                           _Pointer[_oaidl.IDispatch]],  # row
                          _type.HRESULT]
    deleteCell: _Callable[[_type.c_long],  # index
                          _type.HRESULT]


class IHTMLTableRowMetrics(_oaidl.IDispatch):
    get_clientHeight: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_clientWidth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_clientTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_clientLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]


class IHTMLTableCell(_oaidl.IDispatch):
    put_rowSpan: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_rowSpan: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_colSpan: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_colSpan: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_vAlign: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_vAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_bgColor: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_bgColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_noWrap: _Callable[[_type.VARIANT_BOOL],  # v
                          _type.HRESULT]
    get_noWrap: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_background: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_background: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_borderColor: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_borderColorLight: _Callable[[_struct.VARIANT],  # v
                                    _type.HRESULT]
    get_borderColorLight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    put_borderColorDark: _Callable[[_struct.VARIANT],  # v
                                   _type.HRESULT]
    get_borderColorDark: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_cellIndex: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]


class IHTMLTableCell2(_oaidl.IDispatch):
    put_abbr: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_abbr: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_axis: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_axis: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_headers: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_headers: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_scope: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_scope: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLTableCell3(_oaidl.IDispatch):
    put_ch: _Callable[[_type.BSTR],  # v
                      _type.HRESULT]
    get_ch: _Callable[[_Pointer[_type.BSTR]],  # p
                      _type.HRESULT]
    put_chOff: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_chOff: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLTable(_oaidl.IDispatch):
    pass


class DispHTMLTableCol(_oaidl.IDispatch):
    pass


class DispHTMLTableSection(_oaidl.IDispatch):
    pass


class DispHTMLTableRow(_oaidl.IDispatch):
    pass


class DispHTMLTableCell(_oaidl.IDispatch):
    pass


class HTMLScriptEvents2(_oaidl.IDispatch):
    pass


class HTMLScriptEvents(_oaidl.IDispatch):
    pass


class IHTMLScriptElement(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_htmlFor: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_htmlFor: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_event: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_event: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_text: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_text: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_defer: _Callable[[_type.VARIANT_BOOL],  # v
                         _type.HRESULT]
    get_defer: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                         _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLScriptElement2(_oaidl.IDispatch):
    put_charset: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_charset: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLScriptElement3(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]


class IHTMLScriptElement4(_oaidl.IDispatch):
    get_usedCharset: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class DispHTMLScriptElement(_oaidl.IDispatch):
    pass


class IHTMLNoShowElement(_oaidl.IDispatch):
    pass


class DispHTMLNoShowElement(_oaidl.IDispatch):
    pass


class HTMLObjectElementEvents2(_oaidl.IDispatch):
    pass


class HTMLObjectElementEvents(_oaidl.IDispatch):
    pass


class IHTMLObjectElement(_oaidl.IDispatch):
    get_object: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_classid: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    putref_recordset: _Callable[[_oaidl.IDispatch],  # v
                                _type.HRESULT]
    get_recordset: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_codeBase: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_codeBase: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_codeType: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_codeType: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_code: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_code: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_BaseHref: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_altHtml: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_altHtml: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]


class IHTMLObjectElement2(_oaidl.IDispatch):
    namedRecordset: _Callable[[_type.BSTR,  # dataMember
                               _Pointer[_struct.VARIANT],  # hierarchy
                               _Pointer[_oaidl.IDispatch]],  # ppRecordset
                              _type.HRESULT]
    put_classid: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_classid: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLObjectElement3(_oaidl.IDispatch):
    put_archive: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_archive: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_alt: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_alt: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_declare: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_declare: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_standby: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_standby: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_useMap: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_useMap: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLObjectElement4(_oaidl.IDispatch):
    get_contentDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    put_codeBase: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_codeBase: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_data: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class IHTMLObjectElement5(_oaidl.IDispatch):
    put_object: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_object: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLParamElement(_oaidl.IDispatch):
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_valueType: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_valueType: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class IHTMLParamElement2(_oaidl.IDispatch):
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_value: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]
    put_valueType: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_valueType: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class DispHTMLObjectElement(_oaidl.IDispatch):
    pass


class DispHTMLParamElement(_oaidl.IDispatch):
    pass


class HTMLFrameSiteEvents2(_oaidl.IDispatch):
    pass


class HTMLFrameSiteEvents(_oaidl.IDispatch):
    pass


class IHTMLFrameBase2(_oaidl.IDispatch):
    get_contentWindow: _Callable[[_Pointer[IHTMLWindow2]],  # p
                                 _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_allowTransparency: _Callable[[_type.VARIANT_BOOL],  # v
                                     _type.HRESULT]
    get_allowTransparency: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                     _type.HRESULT]


class IHTMLFrameBase3(_oaidl.IDispatch):
    put_longDesc: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_longDesc: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class DispHTMLFrameBase(_oaidl.IDispatch):
    pass


class IHTMLFrameElement(_oaidl.IDispatch):
    put_borderColor: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]


class IHTMLFrameElement2(_oaidl.IDispatch):
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]


class IHTMLFrameElement3(_oaidl.IDispatch):
    get_contentDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_longDesc: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_longDesc: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_frameBorder: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_frameBorder: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class DispHTMLFrameElement(_oaidl.IDispatch):
    pass


class IHTMLIFrameElement(_oaidl.IDispatch):
    put_vspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_vspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_hspace: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_hspace: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLIFrameElement2(_oaidl.IDispatch):
    put_height: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_width: _Callable[[_struct.VARIANT],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]


class IHTMLIFrameElement3(_oaidl.IDispatch):
    get_contentDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_longDesc: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_longDesc: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_frameBorder: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_frameBorder: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class DispHTMLIFrame(_oaidl.IDispatch):
    pass


class IHTMLDivPosition(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLFieldSetElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLFieldSetElement2(_oaidl.IDispatch):
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class IHTMLLegendElement(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLLegendElement2(_oaidl.IDispatch):
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class DispHTMLDivPosition(_oaidl.IDispatch):
    pass


class DispHTMLFieldSetElement(_oaidl.IDispatch):
    pass


class DispHTMLLegendElement(_oaidl.IDispatch):
    pass


class IHTMLSpanFlow(_oaidl.IDispatch):
    put_align: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispHTMLSpanFlow(_oaidl.IDispatch):
    pass


class IHTMLFrameSetElement(_oaidl.IDispatch):
    put_rows: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_rows: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_cols: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_cols: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_border: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_borderColor: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_borderColor: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_frameBorder: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_frameBorder: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_frameSpacing: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_frameSpacing: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_name: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onunload: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_onunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onbeforeunload: _Callable[[_struct.VARIANT],  # v
                                  _type.HRESULT]
    get_onbeforeunload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                  _type.HRESULT]


class IHTMLFrameSetElement2(_oaidl.IDispatch):
    put_onbeforeprint: _Callable[[_struct.VARIANT],  # v
                                 _type.HRESULT]
    get_onbeforeprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_onafterprint: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onafterprint: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]


class IHTMLFrameSetElement3(_oaidl.IDispatch):
    put_onhashchange: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_onhashchange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    put_onmessage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onmessage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onoffline: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onoffline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_ononline: _Callable[[_struct.VARIANT],  # v
                            _type.HRESULT]
    get_ononline: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    put_onstorage: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_onstorage: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class DispHTMLFrameSetSite(_oaidl.IDispatch):
    pass


class IHTMLBGsound(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_loop: _Callable[[_struct.VARIANT],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]
    put_volume: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_volume: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_balance: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_balance: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]


class DispHTMLBGsound(_oaidl.IDispatch):
    pass


class IHTMLFontNamesCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_type.BSTR]],  # pBstr
                    _type.HRESULT]


class IHTMLFontSizesCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    get_forFont: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_type.c_long]],  # plSize
                    _type.HRESULT]


class IHTMLOptionsHolder(_oaidl.IDispatch):
    get_document: _Callable[[_Pointer[IHTMLDocument2]],  # p
                            _type.HRESULT]
    get_fonts: _Callable[[_Pointer[IHTMLFontNamesCollection]],  # p
                         _type.HRESULT]
    put_execArg: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_execArg: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_errorLine: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_errorLine: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_errorCharacter: _Callable[[_type.c_long],  # v
                                  _type.HRESULT]
    get_errorCharacter: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    put_errorCode: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_errorCode: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_errorMessage: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_errorMessage: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_errorDebug: _Callable[[_type.VARIANT_BOOL],  # v
                              _type.HRESULT]
    get_errorDebug: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    get_unsecuredWindowOfDocument: _Callable[[_Pointer[IHTMLWindow2]],  # p
                                             _type.HRESULT]
    put_findText: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_findText: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_anythingAfterFrameset: _Callable[[_type.VARIANT_BOOL],  # v
                                         _type.HRESULT]
    get_anythingAfterFrameset: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                         _type.HRESULT]
    sizes: _Callable[[_type.BSTR,  # fontName
                      _Pointer[IHTMLFontSizesCollection]],  # pSizesCollection
                     _type.HRESULT]
    openfiledlg: _Callable[[_struct.VARIANT,  # initFile
                            _struct.VARIANT,  # initDir
                            _struct.VARIANT,  # filter
                            _struct.VARIANT,  # title
                            _Pointer[_type.BSTR]],  # pathName
                           _type.HRESULT]
    savefiledlg: _Callable[[_struct.VARIANT,  # initFile
                            _struct.VARIANT,  # initDir
                            _struct.VARIANT,  # filter
                            _struct.VARIANT,  # title
                            _Pointer[_type.BSTR]],  # pathName
                           _type.HRESULT]
    choosecolordlg: _Callable[[_struct.VARIANT,  # initColor
                               _Pointer[_type.c_long]],  # rgbColor
                              _type.HRESULT]
    showSecurityInfo: _Callable[[],
                                _type.HRESULT]
    isApartmentModel: _Callable[[IHTMLObjectElement,  # object
                                 _Pointer[_type.VARIANT_BOOL]],  # fApartment
                                _type.HRESULT]
    getCharset: _Callable[[_type.BSTR,  # fontName
                           _Pointer[_type.c_long]],  # charset
                          _type.HRESULT]
    get_secureConnectionInfo: _Callable[[_Pointer[_type.BSTR]],  # p
                                        _type.HRESULT]


class HTMLStyleElementEvents2(_oaidl.IDispatch):
    pass


class HTMLStyleElementEvents(_oaidl.IDispatch):
    pass


class IHTMLStyleElement(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_styleSheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                              _type.HRESULT]
    put_disabled: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_disabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLStyleElement2(_oaidl.IDispatch):
    get_sheet: _Callable[[_Pointer[IHTMLStyleSheet]],  # p
                         _type.HRESULT]


class DispHTMLStyleElement(_oaidl.IDispatch):
    pass


class IHTMLStyleFontFace(_oaidl.IDispatch):
    put_fontsrc: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_fontsrc: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IHTMLStyleFontFace2(_oaidl.IDispatch):
    get_style: _Callable[[_Pointer[IHTMLRuleStyle]],  # p
                         _type.HRESULT]


class DispHTMLStyleFontFace(_oaidl.IDispatch):
    pass


class IHTMLXDomainRequest(_oaidl.IDispatch):
    get_responseText: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    put_timeout: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_timeout: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_contentType: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_onprogress: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_onprogress: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onerror: _Callable[[_struct.VARIANT],  # v
                           _type.HRESULT]
    get_onerror: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    put_ontimeout: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_ontimeout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_onload: _Callable[[_struct.VARIANT],  # v
                          _type.HRESULT]
    get_onload: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    abort: _Callable[[],
                     _type.HRESULT]
    open: _Callable[[_type.BSTR,  # bstrMethod
                     _type.BSTR],  # bstrUrl
                    _type.HRESULT]
    send: _Callable[[_struct.VARIANT],  # varBody
                    _type.HRESULT]


class IHTMLXDomainRequestFactory(_oaidl.IDispatch):
    create: _Callable[[_Pointer[IHTMLXDomainRequest]],  # __MIDL__IHTMLXDomainRequestFactory0000
                      _type.HRESULT]


class DispXDomainRequest(_oaidl.IDispatch):
    pass


class IHTMLStorage2(_oaidl.IDispatch):
    setItem: _Callable[[_type.BSTR,  # bstrKey
                        _type.BSTR],  # bstrValue
                       _type.HRESULT]


class DispHTMLStorage(_oaidl.IDispatch):
    pass


class IEventTarget(_oaidl.IDispatch):
    addEventListener: _Callable[[_type.BSTR,  # type
                                 _oaidl.IDispatch,  # listener
                                 _type.VARIANT_BOOL],  # useCapture
                                _type.HRESULT]
    removeEventListener: _Callable[[_type.BSTR,  # type
                                    _oaidl.IDispatch,  # listener
                                    _type.VARIANT_BOOL],  # useCapture
                                   _type.HRESULT]
    dispatchEvent: _Callable[[IDOMEvent,  # evt
                              _Pointer[_type.VARIANT_BOOL]],  # pfResult
                             _type.HRESULT]


class DispDOMEvent(_oaidl.IDispatch):
    pass


class IDOMUIEvent(_oaidl.IDispatch):
    get_view: _Callable[[_Pointer[IHTMLWindow2]],  # p
                        _type.HRESULT]
    get_detail: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    initUIEvent: _Callable[[_type.BSTR,  # eventType
                            _type.VARIANT_BOOL,  # canBubble
                            _type.VARIANT_BOOL,  # cancelable
                            IHTMLWindow2,  # view
                            _type.c_long],  # detail
                           _type.HRESULT]


class DispDOMUIEvent(_oaidl.IDispatch):
    pass


class IDOMMouseEvent(_oaidl.IDispatch):
    get_screenX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_screenY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_clientX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_clientY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_ctrlKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_shiftKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_altKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_metaKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_button: _Callable[[_Pointer[_type.USHORT]],  # p
                          _type.HRESULT]
    get_relatedTarget: _Callable[[_Pointer[IEventTarget]],  # p
                                 _type.HRESULT]
    initMouseEvent: _Callable[[_type.BSTR,  # eventType
                               _type.VARIANT_BOOL,  # canBubble
                               _type.VARIANT_BOOL,  # cancelable
                               IHTMLWindow2,  # viewArg
                               _type.c_long,  # detailArg
                               _type.c_long,  # screenXArg
                               _type.c_long,  # screenYArg
                               _type.c_long,  # clientXArg
                               _type.c_long,  # clientYArg
                               _type.VARIANT_BOOL,  # ctrlKeyArg
                               _type.VARIANT_BOOL,  # altKeyArg
                               _type.VARIANT_BOOL,  # shiftKeyArg
                               _type.VARIANT_BOOL,  # metaKeyArg
                               _type.USHORT,  # buttonArg
                               IEventTarget],  # relatedTargetArg
                              _type.HRESULT]
    getModifierState: _Callable[[_type.BSTR,  # keyArg
                                 _Pointer[_type.VARIANT_BOOL]],  # activated
                                _type.HRESULT]
    get_buttons: _Callable[[_Pointer[_type.USHORT]],  # p
                           _type.HRESULT]
    get_fromElement: _Callable[[_Pointer[IHTMLElement]],  # p
                               _type.HRESULT]
    get_toElement: _Callable[[_Pointer[IHTMLElement]],  # p
                             _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    get_offsetX: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_offsetY: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_pageX: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    get_pageY: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    get_layerX: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_layerY: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_which: _Callable[[_Pointer[_type.USHORT]],  # p
                         _type.HRESULT]


class DispDOMMouseEvent(_oaidl.IDispatch):
    pass


class IDOMDragEvent(_oaidl.IDispatch):
    get_dataTransfer: _Callable[[_Pointer[IHTMLDataTransfer]],  # p
                                _type.HRESULT]
    initDragEvent: _Callable[[_type.BSTR,  # eventType
                              _type.VARIANT_BOOL,  # canBubble
                              _type.VARIANT_BOOL,  # cancelable
                              IHTMLWindow2,  # viewArg
                              _type.c_long,  # detailArg
                              _type.c_long,  # screenXArg
                              _type.c_long,  # screenYArg
                              _type.c_long,  # clientXArg
                              _type.c_long,  # clientYArg
                              _type.VARIANT_BOOL,  # ctrlKeyArg
                              _type.VARIANT_BOOL,  # altKeyArg
                              _type.VARIANT_BOOL,  # shiftKeyArg
                              _type.VARIANT_BOOL,  # metaKeyArg
                              _type.USHORT,  # buttonArg
                              IEventTarget,  # relatedTargetArg
                              IHTMLDataTransfer],  # dataTransferArg
                             _type.HRESULT]


class DispDOMDragEvent(_oaidl.IDispatch):
    pass


class IDOMMouseWheelEvent(_oaidl.IDispatch):
    get_wheelDelta: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    initMouseWheelEvent: _Callable[[_type.BSTR,  # eventType
                                    _type.VARIANT_BOOL,  # canBubble
                                    _type.VARIANT_BOOL,  # cancelable
                                    IHTMLWindow2,  # viewArg
                                    _type.c_long,  # detailArg
                                    _type.c_long,  # screenXArg
                                    _type.c_long,  # screenYArg
                                    _type.c_long,  # clientXArg
                                    _type.c_long,  # clientYArg
                                    _type.USHORT,  # buttonArg
                                    IEventTarget,  # relatedTargetArg
                                    _type.BSTR,  # modifiersListArg
                                    _type.c_long],  # wheelDeltaArg
                                   _type.HRESULT]


class DispDOMMouseWheelEvent(_oaidl.IDispatch):
    pass


class IDOMWheelEvent(_oaidl.IDispatch):
    get_deltaX: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_deltaY: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_deltaZ: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_deltaMode: _Callable[[_Pointer[_type.ULONG]],  # p
                             _type.HRESULT]
    initWheelEvent: _Callable[[_type.BSTR,  # eventType
                               _type.VARIANT_BOOL,  # canBubble
                               _type.VARIANT_BOOL,  # cancelable
                               IHTMLWindow2,  # viewArg
                               _type.c_long,  # detailArg
                               _type.c_long,  # screenXArg
                               _type.c_long,  # screenYArg
                               _type.c_long,  # clientXArg
                               _type.c_long,  # clientYArg
                               _type.USHORT,  # buttonArg
                               IEventTarget,  # relatedTargetArg
                               _type.BSTR,  # modifiersListArg
                               _type.c_long,  # deltaX
                               _type.c_long,  # deltaY
                               _type.c_long,  # deltaZ
                               _type.ULONG],  # deltaMode
                              _type.HRESULT]


class DispDOMWheelEvent(_oaidl.IDispatch):
    pass


class IDOMTextEvent(_oaidl.IDispatch):
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_inputMethod: _Callable[[_Pointer[_type.ULONG]],  # p
                               _type.HRESULT]
    initTextEvent: _Callable[[_type.BSTR,  # eventType
                              _type.VARIANT_BOOL,  # canBubble
                              _type.VARIANT_BOOL,  # cancelable
                              IHTMLWindow2,  # viewArg
                              _type.BSTR,  # dataArg
                              _type.ULONG,  # inputMethod
                              _type.BSTR],  # locale
                             _type.HRESULT]
    get_locale: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispDOMTextEvent(_oaidl.IDispatch):
    pass


class IDOMKeyboardEvent(_oaidl.IDispatch):
    get_key: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_location: _Callable[[_Pointer[_type.ULONG]],  # p
                            _type.HRESULT]
    get_ctrlKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_shiftKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_altKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_metaKey: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_repeat: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    getModifierState: _Callable[[_type.BSTR,  # keyArg
                                 _Pointer[_type.VARIANT_BOOL]],  # state
                                _type.HRESULT]
    initKeyboardEvent: _Callable[[_type.BSTR,  # eventType
                                  _type.VARIANT_BOOL,  # canBubble
                                  _type.VARIANT_BOOL,  # cancelable
                                  IHTMLWindow2,  # viewArg
                                  _type.BSTR,  # keyArg
                                  _type.ULONG,  # locationArg
                                  _type.BSTR,  # modifiersListArg
                                  _type.VARIANT_BOOL,  # repeat
                                  _type.BSTR],  # locale
                                 _type.HRESULT]
    get_keyCode: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    get_charCode: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_which: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    get_ie9_char: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_locale: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispDOMKeyboardEvent(_oaidl.IDispatch):
    pass


class IDOMCompositionEvent(_oaidl.IDispatch):
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    initCompositionEvent: _Callable[[_type.BSTR,  # eventType
                                     _type.VARIANT_BOOL,  # canBubble
                                     _type.VARIANT_BOOL,  # cancelable
                                     IHTMLWindow2,  # viewArg
                                     _type.BSTR,  # data
                                     _type.BSTR],  # locale
                                    _type.HRESULT]
    get_locale: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class DispDOMCompositionEvent(_oaidl.IDispatch):
    pass


class IDOMMutationEvent(_oaidl.IDispatch):
    get_relatedNode: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                               _type.HRESULT]
    get_prevValue: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    get_newValue: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_attrName: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_attrChange: _Callable[[_Pointer[_type.USHORT]],  # p
                              _type.HRESULT]
    initMutationEvent: _Callable[[_type.BSTR,  # eventType
                                  _type.VARIANT_BOOL,  # canBubble
                                  _type.VARIANT_BOOL,  # cancelable
                                  _oaidl.IDispatch,  # relatedNodeArg
                                  _type.BSTR,  # prevValueArg
                                  _type.BSTR,  # newValueArg
                                  _type.BSTR,  # attrNameArg
                                  _type.USHORT],  # attrChangeArg
                                 _type.HRESULT]


class DispDOMMutationEvent(_oaidl.IDispatch):
    pass


class IDOMBeforeUnloadEvent(_oaidl.IDispatch):
    put_returnValue: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_returnValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]


class DispDOMBeforeUnloadEvent(_oaidl.IDispatch):
    pass


class IDOMFocusEvent(_oaidl.IDispatch):
    get_relatedTarget: _Callable[[_Pointer[IEventTarget]],  # p
                                 _type.HRESULT]
    initFocusEvent: _Callable[[_type.BSTR,  # eventType
                               _type.VARIANT_BOOL,  # canBubble
                               _type.VARIANT_BOOL,  # cancelable
                               IHTMLWindow2,  # view
                               _type.c_long,  # detail
                               IEventTarget],  # relatedTargetArg
                              _type.HRESULT]


class DispDOMFocusEvent(_oaidl.IDispatch):
    pass


class IDOMCustomEvent(_oaidl.IDispatch):
    get_detail: _Callable[[_Pointer[_struct.VARIANT]],  # p
                          _type.HRESULT]
    initCustomEvent: _Callable[[_type.BSTR,  # eventType
                                _type.VARIANT_BOOL,  # canBubble
                                _type.VARIANT_BOOL,  # cancelable
                                _Pointer[_struct.VARIANT]],  # detail
                               _type.HRESULT]


class DispDOMCustomEvent(_oaidl.IDispatch):
    pass


class ICanvasGradient(_oaidl.IDispatch):
    addColorStop: _Callable[[_type.c_float,  # offset
                             _type.BSTR],  # color
                            _type.HRESULT]


class ICanvasPattern(_oaidl.IDispatch):
    pass


class ICanvasTextMetrics(_oaidl.IDispatch):
    get_width: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]


class ICanvasImageData(_oaidl.IDispatch):
    get_width: _Callable[[_Pointer[_type.ULONG]],  # p
                         _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.ULONG]],  # p
                          _type.HRESULT]
    get_data: _Callable[[_Pointer[_struct.VARIANT]],  # p
                        _type.HRESULT]


class ICanvasPixelArray(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.ULONG]],  # p
                          _type.HRESULT]


class IHTMLCanvasElement(_oaidl.IDispatch):
    put_width: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    getContext: _Callable[[_type.BSTR,  # contextId
                           _Pointer[ICanvasRenderingContext2D]],  # ppContext
                          _type.HRESULT]
    toDataURL: _Callable[[_type.BSTR,  # type
                          _struct.VARIANT,  # jpegquality
                          _Pointer[_type.BSTR]],  # pUrl
                         _type.HRESULT]


class ICanvasRenderingContext2D(_oaidl.IDispatch):
    get_canvas: _Callable[[_Pointer[IHTMLCanvasElement]],  # p
                          _type.HRESULT]
    restore: _Callable[[],
                       _type.HRESULT]
    save: _Callable[[],
                    _type.HRESULT]
    rotate: _Callable[[_type.c_float],  # angle
                      _type.HRESULT]
    scale: _Callable[[_type.c_float,  # x
                      _type.c_float],  # y
                     _type.HRESULT]
    setTransform: _Callable[[_type.c_float,  # m11
                             _type.c_float,  # m12
                             _type.c_float,  # m21
                             _type.c_float,  # m22
                             _type.c_float,  # dx
                             _type.c_float],  # dy
                            _type.HRESULT]
    transform: _Callable[[_type.c_float,  # m11
                          _type.c_float,  # m12
                          _type.c_float,  # m21
                          _type.c_float,  # m22
                          _type.c_float,  # dx
                          _type.c_float],  # dy
                         _type.HRESULT]
    translate: _Callable[[_type.c_float,  # x
                          _type.c_float],  # y
                         _type.HRESULT]
    put_globalAlpha: _Callable[[_type.c_float],  # v
                               _type.HRESULT]
    get_globalAlpha: _Callable[[_Pointer[_type.c_float]],  # p
                               _type.HRESULT]
    put_globalCompositeOperation: _Callable[[_type.BSTR],  # v
                                            _type.HRESULT]
    get_globalCompositeOperation: _Callable[[_Pointer[_type.BSTR]],  # p
                                            _type.HRESULT]
    put_fillStyle: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_fillStyle: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_strokeStyle: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_strokeStyle: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    createLinearGradient: _Callable[[_type.c_float,  # x0
                                     _type.c_float,  # y0
                                     _type.c_float,  # x1
                                     _type.c_float,  # y1
                                     _Pointer[ICanvasGradient]],  # ppCanvasGradient
                                    _type.HRESULT]
    createRadialGradient: _Callable[[_type.c_float,  # x0
                                     _type.c_float,  # y0
                                     _type.c_float,  # r0
                                     _type.c_float,  # x1
                                     _type.c_float,  # y1
                                     _type.c_float,  # r1
                                     _Pointer[ICanvasGradient]],  # ppCanvasGradient
                                    _type.HRESULT]
    createPattern: _Callable[[_oaidl.IDispatch,  # image
                              _struct.VARIANT,  # repetition
                              _Pointer[ICanvasPattern]],  # ppCanvasPattern
                             _type.HRESULT]
    put_lineCap: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_lineCap: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_lineJoin: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_lineJoin: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    put_lineWidth: _Callable[[_type.c_float],  # v
                             _type.HRESULT]
    get_lineWidth: _Callable[[_Pointer[_type.c_float]],  # p
                             _type.HRESULT]
    put_miterLimit: _Callable[[_type.c_float],  # v
                              _type.HRESULT]
    get_miterLimit: _Callable[[_Pointer[_type.c_float]],  # p
                              _type.HRESULT]
    put_shadowBlur: _Callable[[_type.c_float],  # v
                              _type.HRESULT]
    get_shadowBlur: _Callable[[_Pointer[_type.c_float]],  # p
                              _type.HRESULT]
    put_shadowColor: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_shadowColor: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_shadowOffsetX: _Callable[[_type.c_float],  # v
                                 _type.HRESULT]
    get_shadowOffsetX: _Callable[[_Pointer[_type.c_float]],  # p
                                 _type.HRESULT]
    put_shadowOffsetY: _Callable[[_type.c_float],  # v
                                 _type.HRESULT]
    get_shadowOffsetY: _Callable[[_Pointer[_type.c_float]],  # p
                                 _type.HRESULT]
    clearRect: _Callable[[_type.c_float,  # x
                          _type.c_float,  # y
                          _type.c_float,  # w
                          _type.c_float],  # h
                         _type.HRESULT]
    fillRect: _Callable[[_type.c_float,  # x
                         _type.c_float,  # y
                         _type.c_float,  # w
                         _type.c_float],  # h
                        _type.HRESULT]
    strokeRect: _Callable[[_type.c_float,  # x
                           _type.c_float,  # y
                           _type.c_float,  # w
                           _type.c_float],  # h
                          _type.HRESULT]
    arc: _Callable[[_type.c_float,  # x
                    _type.c_float,  # y
                    _type.c_float,  # radius
                    _type.c_float,  # startAngle
                    _type.c_float,  # endAngle
                    _type.BOOL],  # anticlockwise
                   _type.HRESULT]
    arcTo: _Callable[[_type.c_float,  # x1
                      _type.c_float,  # y1
                      _type.c_float,  # x2
                      _type.c_float,  # y2
                      _type.c_float],  # radius
                     _type.HRESULT]
    beginPath: _Callable[[],
                         _type.HRESULT]
    bezierCurveTo: _Callable[[_type.c_float,  # cp1x
                              _type.c_float,  # cp1y
                              _type.c_float,  # cp2x
                              _type.c_float,  # cp2y
                              _type.c_float,  # x
                              _type.c_float],  # y
                             _type.HRESULT]
    clip: _Callable[[],
                    _type.HRESULT]
    closePath: _Callable[[],
                         _type.HRESULT]
    fill: _Callable[[],
                    _type.HRESULT]
    lineTo: _Callable[[_type.c_float,  # x
                       _type.c_float],  # y
                      _type.HRESULT]
    moveTo: _Callable[[_type.c_float,  # x
                       _type.c_float],  # y
                      _type.HRESULT]
    quadraticCurveTo: _Callable[[_type.c_float,  # cpx
                                 _type.c_float,  # cpy
                                 _type.c_float,  # x
                                 _type.c_float],  # y
                                _type.HRESULT]
    rect: _Callable[[_type.c_float,  # x
                     _type.c_float,  # y
                     _type.c_float,  # w
                     _type.c_float],  # h
                    _type.HRESULT]
    stroke: _Callable[[],
                      _type.HRESULT]
    isPointInPath: _Callable[[_type.c_float,  # x
                              _type.c_float,  # y
                              _Pointer[_type.VARIANT_BOOL]],  # pResult
                             _type.HRESULT]
    put_font: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_font: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_textAlign: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_textAlign: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_textBaseline: _Callable[[_type.BSTR],  # v
                                _type.HRESULT]
    get_textBaseline: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    fillText: _Callable[[_type.BSTR,  # text
                         _type.c_float,  # x
                         _type.c_float,  # y
                         _struct.VARIANT],  # maxWidth
                        _type.HRESULT]
    measureText: _Callable[[_type.BSTR,  # text
                            _Pointer[ICanvasTextMetrics]],  # ppCanvasTextMetrics
                           _type.HRESULT]
    strokeText: _Callable[[_type.BSTR,  # text
                           _type.c_float,  # x
                           _type.c_float,  # y
                           _struct.VARIANT],  # maxWidth
                          _type.HRESULT]
    drawImage: _Callable[[_oaidl.IDispatch,  # pSrc
                          _struct.VARIANT,  # a1
                          _struct.VARIANT,  # a2
                          _struct.VARIANT,  # a3
                          _struct.VARIANT,  # a4
                          _struct.VARIANT,  # a5
                          _struct.VARIANT,  # a6
                          _struct.VARIANT,  # a7
                          _struct.VARIANT],  # a8
                         _type.HRESULT]
    createImageData: _Callable[[_struct.VARIANT,  # a1
                                _struct.VARIANT,  # a2
                                _Pointer[ICanvasImageData]],  # ppCanvasImageData
                               _type.HRESULT]
    getImageData: _Callable[[_type.c_float,  # sx
                             _type.c_float,  # sy
                             _type.c_float,  # sw
                             _type.c_float,  # sh
                             _Pointer[ICanvasImageData]],  # ppCanvasImageData
                            _type.HRESULT]
    putImageData: _Callable[[ICanvasImageData,  # imagedata
                             _type.c_float,  # dx
                             _type.c_float,  # dy
                             _struct.VARIANT,  # dirtyX
                             _struct.VARIANT,  # dirtyY
                             _struct.VARIANT,  # dirtyWidth
                             _struct.VARIANT],  # dirtyHeight
                            _type.HRESULT]


class DispCanvasGradient(_oaidl.IDispatch):
    pass


class DispCanvasPattern(_oaidl.IDispatch):
    pass


class DispCanvasTextMetrics(_oaidl.IDispatch):
    pass


class DispCanvasImageData(_oaidl.IDispatch):
    pass


class DispCanvasRenderingContext2D(_oaidl.IDispatch):
    pass


class DispHTMLCanvasElement(_oaidl.IDispatch):
    pass


class IDOMProgressEvent(_oaidl.IDispatch):
    get_lengthComputable: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    get_loaded: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                          _type.HRESULT]
    get_total: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                         _type.HRESULT]
    initProgressEvent: _Callable[[_type.BSTR,  # eventType
                                  _type.VARIANT_BOOL,  # canBubble
                                  _type.VARIANT_BOOL,  # cancelable
                                  _type.VARIANT_BOOL,  # lengthComputableArg
                                  _type.ULONGLONG,  # loadedArg
                                  _type.ULONGLONG],  # totalArg
                                 _type.HRESULT]


class DispDOMProgressEvent(_oaidl.IDispatch):
    pass


class IDOMMessageEvent(_oaidl.IDispatch):
    get_data: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_origin: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    get_source: _Callable[[_Pointer[IHTMLWindow2]],  # p
                          _type.HRESULT]
    initMessageEvent: _Callable[[_type.BSTR,  # eventType
                                 _type.VARIANT_BOOL,  # canBubble
                                 _type.VARIANT_BOOL,  # cancelable
                                 _type.BSTR,  # data
                                 _type.BSTR,  # origin
                                 _type.BSTR,  # lastEventId
                                 IHTMLWindow2],  # source
                                _type.HRESULT]


class DispDOMMessageEvent(_oaidl.IDispatch):
    pass


class IDOMSiteModeEvent(_oaidl.IDispatch):
    get_buttonID: _Callable[[_Pointer[_type.LONG]],  # p
                            _type.HRESULT]
    get_actionURL: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class DispDOMSiteModeEvent(_oaidl.IDispatch):
    pass


class IDOMStorageEvent(_oaidl.IDispatch):
    get_key: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_oldValue: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_newValue: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_url: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_storageArea: _Callable[[_Pointer[IHTMLStorage]],  # p
                               _type.HRESULT]
    initStorageEvent: _Callable[[_type.BSTR,  # eventType
                                 _type.VARIANT_BOOL,  # canBubble
                                 _type.VARIANT_BOOL,  # cancelable
                                 _type.BSTR,  # keyArg
                                 _type.BSTR,  # oldValueArg
                                 _type.BSTR,  # newValueArg
                                 _type.BSTR,  # urlArg
                                 IHTMLStorage],  # storageAreaArg
                                _type.HRESULT]


class DispDOMStorageEvent(_oaidl.IDispatch):
    pass


class IXMLHttpRequestEventTarget(_oaidl.IDispatch):
    pass


class DispXMLHttpRequestEventTarget(_oaidl.IDispatch):
    pass


class HTMLXMLHttpRequestEvents(_oaidl.IDispatch):
    pass


class IHTMLXMLHttpRequest(_oaidl.IDispatch):
    get_readyState: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_responseBody: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_responseText: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_responseXML: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                               _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_statusText: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    abort: _Callable[[],
                     _type.HRESULT]
    open: _Callable[[_type.BSTR,  # bstrMethod
                     _type.BSTR,  # bstrUrl
                     _struct.VARIANT,  # varAsync
                     _struct.VARIANT,  # varUser
                     _struct.VARIANT],  # varPassword
                    _type.HRESULT]
    send: _Callable[[_struct.VARIANT],  # varBody
                    _type.HRESULT]
    getAllResponseHeaders: _Callable[[_Pointer[_type.BSTR]],  # __MIDL__IHTMLXMLHttpRequest0000
                                     _type.HRESULT]
    getResponseHeader: _Callable[[_type.BSTR,  # bstrHeader
                                  _Pointer[_type.BSTR]],  # __MIDL__IHTMLXMLHttpRequest0001
                                 _type.HRESULT]
    setRequestHeader: _Callable[[_type.BSTR,  # bstrHeader
                                 _type.BSTR],  # bstrValue
                                _type.HRESULT]


class IHTMLXMLHttpRequest2(_oaidl.IDispatch):
    put_timeout: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_timeout: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_ontimeout: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_ontimeout: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]


class IHTMLXMLHttpRequestFactory(_oaidl.IDispatch):
    create: _Callable[[_Pointer[IHTMLXMLHttpRequest]],  # __MIDL__IHTMLXMLHttpRequestFactory0000
                      _type.HRESULT]


class DispHTMLXMLHttpRequest(_oaidl.IDispatch):
    pass


class ISVGAngle(_oaidl.IDispatch):
    put_unitType: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_unitType: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    put_value: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_valueInSpecifiedUnits: _Callable[[_type.c_float],  # v
                                         _type.HRESULT]
    get_valueInSpecifiedUnits: _Callable[[_Pointer[_type.c_float]],  # p
                                         _type.HRESULT]
    put_valueAsString: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_valueAsString: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    newValueSpecifiedUnits: _Callable[[_type.c_short,  # unitType
                                       _type.c_float],  # valueInSpecifiedUnits
                                      _type.HRESULT]
    convertToSpecifiedUnits: _Callable[[_type.c_short],  # unitType
                                       _type.HRESULT]


class ISVGElement(_oaidl.IDispatch):
    put_xmlbase: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_xmlbase: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    putref_ownerSVGElement: _Callable[[ISVGSVGElement],  # v
                                      _type.HRESULT]
    get_ownerSVGElement: _Callable[[_Pointer[ISVGSVGElement]],  # p
                                   _type.HRESULT]
    putref_viewportElement: _Callable[[ISVGElement],  # v
                                      _type.HRESULT]
    get_viewportElement: _Callable[[_Pointer[ISVGElement]],  # p
                                   _type.HRESULT]
    putref_focusable: _Callable[[ISVGAnimatedEnumeration],  # v
                                _type.HRESULT]
    get_focusable: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                             _type.HRESULT]


class ISVGRect(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_width: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_float],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_float]],  # p
                          _type.HRESULT]


class ISVGMatrix(_oaidl.IDispatch):
    put_a: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_a: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_b: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_b: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_c: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_c: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_d: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_d: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_e: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_e: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_f: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_f: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    multiply: _Callable[[ISVGMatrix,  # secondMatrix
                         _Pointer[ISVGMatrix]],  # ppResult
                        _type.HRESULT]
    inverse: _Callable[[_Pointer[ISVGMatrix]],  # ppResult
                       _type.HRESULT]
    translate: _Callable[[_type.c_float,  # x
                          _type.c_float,  # y
                          _Pointer[ISVGMatrix]],  # ppResult
                         _type.HRESULT]
    scale: _Callable[[_type.c_float,  # scaleFactor
                      _Pointer[ISVGMatrix]],  # ppResult
                     _type.HRESULT]
    scaleNonUniform: _Callable[[_type.c_float,  # scaleFactorX
                                _type.c_float,  # scaleFactorY
                                _Pointer[ISVGMatrix]],  # ppResult
                               _type.HRESULT]
    rotate: _Callable[[_type.c_float,  # angle
                       _Pointer[ISVGMatrix]],  # ppResult
                      _type.HRESULT]
    rotateFromVector: _Callable[[_type.c_float,  # x
                                 _type.c_float,  # y
                                 _Pointer[ISVGMatrix]],  # ppResult
                                _type.HRESULT]
    flipX: _Callable[[_Pointer[ISVGMatrix]],  # ppResult
                     _type.HRESULT]
    flipY: _Callable[[_Pointer[ISVGMatrix]],  # ppResult
                     _type.HRESULT]
    skewX: _Callable[[_type.c_float,  # angle
                      _Pointer[ISVGMatrix]],  # ppResult
                     _type.HRESULT]
    skewY: _Callable[[_type.c_float,  # angle
                      _Pointer[ISVGMatrix]],  # ppResult
                     _type.HRESULT]


class ISVGStringList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[_type.BSTR,  # newItem
                           _Pointer[_type.BSTR]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[_type.BSTR]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[_type.BSTR,  # newItem
                                 _type.c_long,  # index
                                 _Pointer[_type.BSTR]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[_type.BSTR,  # newItem
                            _type.c_long,  # index
                            _Pointer[_type.BSTR]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[_type.BSTR]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[_type.BSTR,  # newItem
                           _Pointer[_type.BSTR]],  # ppResult
                          _type.HRESULT]


class ISVGAnimatedRect(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGRect],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGRect]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGRect],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGRect]],  # p
                           _type.HRESULT]


class ISVGAnimatedString(_oaidl.IDispatch):
    put_baseVal: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_animVal: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class ISVGAnimatedBoolean(_oaidl.IDispatch):
    put_baseVal: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_animVal: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_animVal: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]


class ISVGAnimatedTransformList(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGTransformList],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGTransformList]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGTransformList],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGTransformList]],  # p
                           _type.HRESULT]


class ISVGAnimatedPreserveAspectRatio(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGPreserveAspectRatio],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGPreserveAspectRatio]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGPreserveAspectRatio],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGPreserveAspectRatio]],  # p
                           _type.HRESULT]


class ISVGStylable(_oaidl.IDispatch):
    get_className: _Callable[[_Pointer[ISVGAnimatedString]],  # p
                             _type.HRESULT]


class ISVGLocatable(_oaidl.IDispatch):
    get_nearestViewportElement: _Callable[[_Pointer[ISVGElement]],  # p
                                          _type.HRESULT]
    get_farthestViewportElement: _Callable[[_Pointer[ISVGElement]],  # p
                                           _type.HRESULT]
    getBBox: _Callable[[_Pointer[ISVGRect]],  # ppResult
                       _type.HRESULT]
    getCTM: _Callable[[_Pointer[ISVGMatrix]],  # ppResult
                      _type.HRESULT]
    getScreenCTM: _Callable[[_Pointer[ISVGMatrix]],  # ppResult
                            _type.HRESULT]
    getTransformToElement: _Callable[[ISVGElement,  # pElement
                                      _Pointer[ISVGMatrix]],  # ppResult
                                     _type.HRESULT]


class ISVGTransformable(_oaidl.IDispatch):
    get_transform: _Callable[[_Pointer[ISVGAnimatedTransformList]],  # p
                             _type.HRESULT]


class ISVGTests(_oaidl.IDispatch):
    get_requiredFeatures: _Callable[[_Pointer[ISVGStringList]],  # p
                                    _type.HRESULT]
    get_requiredExtensions: _Callable[[_Pointer[ISVGStringList]],  # p
                                      _type.HRESULT]
    get_systemLanguage: _Callable[[_Pointer[ISVGStringList]],  # p
                                  _type.HRESULT]
    hasExtension: _Callable[[_type.BSTR,  # extension
                             _Pointer[_type.VARIANT_BOOL]],  # pResult
                            _type.HRESULT]


class ISVGLangSpace(_oaidl.IDispatch):
    put_xmllang: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_xmllang: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_xmlspace: _Callable[[_type.BSTR],  # v
                            _type.HRESULT]
    get_xmlspace: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]


class ISVGExternalResourcesRequired(_oaidl.IDispatch):
    get_externalResourcesRequired: _Callable[[_Pointer[ISVGAnimatedBoolean]],  # p
                                             _type.HRESULT]


class ISVGFitToViewBox(_oaidl.IDispatch):
    get_viewBox: _Callable[[_Pointer[ISVGAnimatedRect]],  # p
                           _type.HRESULT]
    putref_preserveAspectRatio: _Callable[[ISVGAnimatedPreserveAspectRatio],  # v
                                          _type.HRESULT]
    get_preserveAspectRatio: _Callable[[_Pointer[ISVGAnimatedPreserveAspectRatio]],  # p
                                       _type.HRESULT]


class ISVGZoomAndPan(_oaidl.IDispatch):
    get_zoomAndPan: _Callable[[_Pointer[_type.c_short]],  # p
                              _type.HRESULT]


class ISVGURIReference(_oaidl.IDispatch):
    get_href: _Callable[[_Pointer[ISVGAnimatedString]],  # p
                        _type.HRESULT]


class ISVGAnimatedAngle(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGAngle],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGAngle]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGAngle],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGAngle]],  # p
                           _type.HRESULT]


class ISVGTransformList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[ISVGTransform,  # newItem
                           _Pointer[ISVGTransform]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[ISVGTransform]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[ISVGTransform,  # newItem
                                 _type.c_long,  # index
                                 _Pointer[ISVGTransform]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[ISVGTransform,  # newItem
                            _type.c_long,  # index
                            _Pointer[ISVGTransform]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[ISVGTransform]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[ISVGTransform,  # newItem
                           _Pointer[ISVGTransform]],  # ppResult
                          _type.HRESULT]
    createSVGTransformFromMatrix: _Callable[[ISVGMatrix,  # newItem
                                             _Pointer[ISVGTransform]],  # ppResult
                                            _type.HRESULT]
    consolidate: _Callable[[_Pointer[ISVGTransform]],  # ppResult
                           _type.HRESULT]


class ISVGAnimatedEnumeration(_oaidl.IDispatch):
    put_baseVal: _Callable[[_type.USHORT],  # v
                           _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[_type.USHORT]],  # p
                           _type.HRESULT]
    put_animVal: _Callable[[_type.USHORT],  # v
                           _type.HRESULT]
    get_animVal: _Callable[[_Pointer[_type.USHORT]],  # p
                           _type.HRESULT]


class ISVGAnimatedInteger(_oaidl.IDispatch):
    put_baseVal: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]
    put_animVal: _Callable[[_type.c_long],  # v
                           _type.HRESULT]
    get_animVal: _Callable[[_Pointer[_type.c_long]],  # p
                           _type.HRESULT]


class ISVGLength(_oaidl.IDispatch):
    put_unitType: _Callable[[_type.c_short],  # v
                            _type.HRESULT]
    get_unitType: _Callable[[_Pointer[_type.c_short]],  # p
                            _type.HRESULT]
    put_value: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_valueInSpecifiedUnits: _Callable[[_type.c_float],  # v
                                         _type.HRESULT]
    get_valueInSpecifiedUnits: _Callable[[_Pointer[_type.c_float]],  # p
                                         _type.HRESULT]
    put_valueAsString: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_valueAsString: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    newValueSpecifiedUnits: _Callable[[_type.c_short,  # unitType
                                       _type.c_float],  # valueInSpecifiedUnits
                                      _type.HRESULT]
    convertToSpecifiedUnits: _Callable[[_type.c_short],  # unitType
                                       _type.HRESULT]


class ISVGAnimatedLength(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGLength],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGLength]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGLength],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGLength]],  # p
                           _type.HRESULT]


class ISVGLengthList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[ISVGLength,  # newItem
                           _Pointer[ISVGLength]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[ISVGLength]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[ISVGLength,  # newItem
                                 _type.c_long,  # index
                                 _Pointer[ISVGLength]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[ISVGLength,  # newItem
                            _type.c_long,  # index
                            _Pointer[ISVGLength]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[ISVGLength]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[ISVGLength,  # newItem
                           _Pointer[ISVGLength]],  # ppResult
                          _type.HRESULT]


class ISVGAnimatedLengthList(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGLengthList],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGLengthList]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGLengthList],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGLengthList]],  # p
                           _type.HRESULT]


class ISVGNumber(_oaidl.IDispatch):
    put_value: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]


class ISVGAnimatedNumber(_oaidl.IDispatch):
    put_baseVal: _Callable[[_type.c_float],  # v
                           _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[_type.c_float]],  # p
                           _type.HRESULT]
    put_animVal: _Callable[[_type.c_float],  # v
                           _type.HRESULT]
    get_animVal: _Callable[[_Pointer[_type.c_float]],  # p
                           _type.HRESULT]


class ISVGNumberList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[ISVGNumber,  # newItem
                           _Pointer[ISVGNumber]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[ISVGNumber]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[ISVGNumber,  # newItem
                                 _type.c_long,  # index
                                 _Pointer[ISVGNumber]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[ISVGNumber,  # newItem
                            _type.c_long,  # index
                            _Pointer[ISVGNumber]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[ISVGNumber]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[ISVGNumber,  # newItem
                           _Pointer[ISVGNumber]],  # ppResult
                          _type.HRESULT]


class ISVGAnimatedNumberList(_oaidl.IDispatch):
    putref_baseVal: _Callable[[ISVGNumberList],  # v
                              _type.HRESULT]
    get_baseVal: _Callable[[_Pointer[ISVGNumberList]],  # p
                           _type.HRESULT]
    putref_animVal: _Callable[[ISVGNumberList],  # v
                              _type.HRESULT]
    get_animVal: _Callable[[_Pointer[ISVGNumberList]],  # p
                           _type.HRESULT]


class ISVGClipPathElement(_oaidl.IDispatch):
    putref_clipPathUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                    _type.HRESULT]
    get_clipPathUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                 _type.HRESULT]


class DispSVGClipPathElement(_oaidl.IDispatch):
    pass


class ISVGDocument(_oaidl.IDispatch):
    get_rootElement: _Callable[[_Pointer[ISVGSVGElement]],  # p
                               _type.HRESULT]


class IGetSVGDocument(_oaidl.IDispatch):
    getSVGDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppSVGDocument
                              _type.HRESULT]


class DispSVGElement(_oaidl.IDispatch):
    pass


class IICCSVGColor(_oaidl.IDispatch):
    pass


class ISVGPaint(_oaidl.IDispatch):
    pass


class ISVGPatternElement(_oaidl.IDispatch):
    putref_patternUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                   _type.HRESULT]
    get_patternUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                _type.HRESULT]
    putref_patternContentUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                          _type.HRESULT]
    get_patternContentUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                       _type.HRESULT]
    putref_patternTransform: _Callable[[ISVGAnimatedTransformList],  # v
                                       _type.HRESULT]
    get_patternTransform: _Callable[[_Pointer[ISVGAnimatedTransformList]],  # p
                                    _type.HRESULT]
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]


class DispSVGPatternElement(_oaidl.IDispatch):
    pass


class ISVGPathSeg(_oaidl.IDispatch):
    put_pathSegType: _Callable[[_type.c_short],  # v
                               _type.HRESULT]
    get_pathSegType: _Callable[[_Pointer[_type.c_short]],  # p
                               _type.HRESULT]
    get_pathSegTypeAsLetter: _Callable[[_Pointer[_type.BSTR]],  # p
                                       _type.HRESULT]


class ISVGPathSegArcAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_r1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_r1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_r2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_r2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_angle: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_angle: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_largeArcFlag: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_largeArcFlag: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    put_sweepFlag: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_sweepFlag: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]


class ISVGPathSegArcRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_r1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_r1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_r2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_r2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_angle: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_angle: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_largeArcFlag: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_largeArcFlag: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    put_sweepFlag: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_sweepFlag: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]


class ISVGPathSegClosePath(_oaidl.IDispatch):
    pass


class ISVGPathSegMovetoAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegMovetoRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegCurvetoCubicAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_x2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoCubicRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_x2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoCubicSmoothAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoCubicSmoothRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y2: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y2: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoQuadraticAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoQuadraticRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_x1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_x1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]
    put_y1: _Callable[[_type.c_float],  # v
                      _type.HRESULT]
    get_y1: _Callable[[_Pointer[_type.c_float]],  # p
                      _type.HRESULT]


class ISVGPathSegCurvetoQuadraticSmoothAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegCurvetoQuadraticSmoothRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoHorizontalAbs(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoHorizontalRel(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoVerticalAbs(_oaidl.IDispatch):
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class ISVGPathSegLinetoVerticalRel(_oaidl.IDispatch):
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]


class DispSVGPathSegArcAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegArcRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegClosePath(_oaidl.IDispatch):
    pass


class DispSVGPathSegMovetoAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegMovetoRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoCubicAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoCubicRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoCubicSmoothAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoCubicSmoothRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoQuadraticAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoQuadraticRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoQuadraticSmoothAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegCurvetoQuadraticSmoothRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoHorizontalAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoHorizontalRel(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoVerticalAbs(_oaidl.IDispatch):
    pass


class DispSVGPathSegLinetoVerticalRel(_oaidl.IDispatch):
    pass


class ISVGPathSegList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[ISVGPathSeg,  # newItem
                           _Pointer[ISVGPathSeg]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[ISVGPathSeg]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[ISVGPathSeg,  # newItem
                                 _type.c_long,  # index
                                 _Pointer[ISVGPathSeg]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[ISVGPathSeg,  # newItem
                            _type.c_long,  # index
                            _Pointer[ISVGPathSeg]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[ISVGPathSeg]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[ISVGPathSeg,  # newItem
                           _Pointer[ISVGPathSeg]],  # ppResult
                          _type.HRESULT]


class ISVGPoint(_oaidl.IDispatch):
    put_x: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_x: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    put_y: _Callable[[_type.c_float],  # v
                     _type.HRESULT]
    get_y: _Callable[[_Pointer[_type.c_float]],  # p
                     _type.HRESULT]
    matrixTransform: _Callable[[ISVGMatrix,  # pMatrix
                                _Pointer[ISVGPoint]],  # ppResult
                               _type.HRESULT]


class ISVGPointList(_oaidl.IDispatch):
    put_numberOfItems: _Callable[[_type.c_long],  # v
                                 _type.HRESULT]
    get_numberOfItems: _Callable[[_Pointer[_type.c_long]],  # p
                                 _type.HRESULT]
    clear: _Callable[[],
                     _type.HRESULT]
    initialize: _Callable[[ISVGPoint,  # pNewItem
                           _Pointer[ISVGPoint]],  # ppResult
                          _type.HRESULT]
    getItem: _Callable[[_type.c_long,  # index
                        _Pointer[ISVGPoint]],  # ppResult
                       _type.HRESULT]
    insertItemBefore: _Callable[[ISVGPoint,  # pNewItem
                                 _type.c_long,  # index
                                 _Pointer[ISVGPoint]],  # ppResult
                                _type.HRESULT]
    replaceItem: _Callable[[ISVGPoint,  # pNewItem
                            _type.c_long,  # index
                            _Pointer[ISVGPoint]],  # ppResult
                           _type.HRESULT]
    removeItem: _Callable[[_type.c_long,  # index
                           _Pointer[ISVGPoint]],  # ppResult
                          _type.HRESULT]
    appendItem: _Callable[[ISVGPoint,  # pNewItem
                           _Pointer[ISVGPoint]],  # ppResult
                          _type.HRESULT]


class ISVGViewSpec(_oaidl.IDispatch):
    pass


class ISVGTransform(_oaidl.IDispatch):
    put_type: _Callable[[_type.c_short],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.c_short]],  # p
                        _type.HRESULT]
    putref_matrix: _Callable[[ISVGMatrix],  # v
                             _type.HRESULT]
    get_matrix: _Callable[[_Pointer[ISVGMatrix]],  # p
                          _type.HRESULT]
    put_angle: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_angle: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    setMatrix: _Callable[[ISVGMatrix],  # matrix
                         _type.HRESULT]
    setTranslate: _Callable[[_type.c_float,  # tx
                             _type.c_float],  # ty
                            _type.HRESULT]
    setScale: _Callable[[_type.c_float,  # sx
                         _type.c_float],  # sy
                        _type.HRESULT]
    setRotate: _Callable[[_type.c_float,  # angle
                          _type.c_float,  # cx
                          _type.c_float],  # cy
                         _type.HRESULT]
    setSkewX: _Callable[[_type.c_float],  # angle
                        _type.HRESULT]
    setSkewY: _Callable[[_type.c_float],  # angle
                        _type.HRESULT]


class DispSVGSVGElement(_oaidl.IDispatch):
    pass


class ISVGElementInstance(_oaidl.IDispatch):
    get_correspondingElement: _Callable[[_Pointer[ISVGElement]],  # p
                                        _type.HRESULT]
    get_correspondingUseElement: _Callable[[_Pointer[ISVGUseElement]],  # p
                                           _type.HRESULT]
    get_parentNode: _Callable[[_Pointer[ISVGElementInstance]],  # p
                              _type.HRESULT]
    get_childNodes: _Callable[[_Pointer[ISVGElementInstanceList]],  # p
                              _type.HRESULT]
    get_firstChild: _Callable[[_Pointer[ISVGElementInstance]],  # p
                              _type.HRESULT]
    get_lastChild: _Callable[[_Pointer[ISVGElementInstance]],  # p
                             _type.HRESULT]
    get_previousSibling: _Callable[[_Pointer[ISVGElementInstance]],  # p
                                   _type.HRESULT]
    get_nextSibling: _Callable[[_Pointer[ISVGElementInstance]],  # p
                               _type.HRESULT]


class ISVGUseElement(_oaidl.IDispatch):
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]
    putref_instanceRoot: _Callable[[ISVGElementInstance],  # v
                                   _type.HRESULT]
    get_instanceRoot: _Callable[[_Pointer[ISVGElementInstance]],  # p
                                _type.HRESULT]
    putref_animatedInstanceRoot: _Callable[[ISVGElementInstance],  # v
                                           _type.HRESULT]
    get_animatedInstanceRoot: _Callable[[_Pointer[ISVGElementInstance]],  # p
                                        _type.HRESULT]


class DispSVGUseElement(_oaidl.IDispatch):
    pass


class IHTMLStyleSheetRulesAppliedCollection(_oaidl.IDispatch):
    item: _Callable[[_type.c_long,  # index
                     _Pointer[IHTMLStyleSheetRule]],  # ppHTMLStyleSheetRule
                    _type.HRESULT]
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    propertyAppliedBy: _Callable[[_type.BSTR,  # name
                                  _Pointer[IHTMLStyleSheetRule]],  # ppRule
                                 _type.HRESULT]
    propertyAppliedTrace: _Callable[[_type.BSTR,  # name
                                     _type.c_long,  # index
                                     _Pointer[IHTMLStyleSheetRule]],  # ppRule
                                    _type.HRESULT]
    propertyAppliedTraceLength: _Callable[[_type.BSTR,  # name
                                           _Pointer[_type.c_long]],  # pLength
                                          _type.HRESULT]


class IRulesApplied(_oaidl.IDispatch):
    get_element: _Callable[[_Pointer[IHTMLElement]],  # p
                           _type.HRESULT]
    get_inlineStyles: _Callable[[_Pointer[IHTMLStyle]],  # p
                                _type.HRESULT]
    get_appliedRules: _Callable[[_Pointer[IHTMLStyleSheetRulesAppliedCollection]],  # p
                                _type.HRESULT]
    propertyIsInline: _Callable[[_type.BSTR,  # name
                                 _Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    propertyIsInheritable: _Callable[[_type.BSTR,  # name
                                      _Pointer[_type.VARIANT_BOOL]],  # p
                                     _type.HRESULT]
    hasInheritableProperty: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]


class DispHTMLStyleSheetRulesAppliedCollection(_oaidl.IDispatch):
    pass


class DispRulesApplied(_oaidl.IDispatch):
    pass


class DispRulesAppliedCollection(_oaidl.IDispatch):
    pass


class DispHTMLW3CComputedStyle(_oaidl.IDispatch):
    pass


class ISVGAnimatedPoints(_oaidl.IDispatch):
    putref_points: _Callable[[ISVGPointList],  # v
                             _type.HRESULT]
    get_points: _Callable[[_Pointer[ISVGPointList]],  # p
                          _type.HRESULT]
    putref_animatedPoints: _Callable[[ISVGPointList],  # v
                                     _type.HRESULT]
    get_animatedPoints: _Callable[[_Pointer[ISVGPointList]],  # p
                                  _type.HRESULT]


class ISVGCircleElement(_oaidl.IDispatch):
    putref_cx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_cy: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cy: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_r: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_r: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]


class ISVGEllipseElement(_oaidl.IDispatch):
    putref_cx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_cy: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cy: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_rx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_rx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_ry: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_ry: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]


class ISVGLineElement(_oaidl.IDispatch):
    putref_x1: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_x1: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_y1: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_y1: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_x2: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_x2: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_y2: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_y2: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]


class ISVGRectElement(_oaidl.IDispatch):
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]
    putref_rx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_rx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_ry: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_ry: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]


class ISVGPolygonElement(_oaidl.IDispatch):
    pass


class ISVGPolylineElement(_oaidl.IDispatch):
    pass


class DispSVGCircleElement(_oaidl.IDispatch):
    pass


class DispSVGEllipseElement(_oaidl.IDispatch):
    pass


class DispSVGLineElement(_oaidl.IDispatch):
    pass


class DispSVGRectElement(_oaidl.IDispatch):
    pass


class DispSVGPolygonElement(_oaidl.IDispatch):
    pass


class DispSVGPolylineElement(_oaidl.IDispatch):
    pass


class ISVGGElement(_oaidl.IDispatch):
    pass


class DispSVGGElement(_oaidl.IDispatch):
    pass


class ISVGSymbolElement(_oaidl.IDispatch):
    pass


class DispSVGSymbolElement(_oaidl.IDispatch):
    pass


class ISVGDefsElement(_oaidl.IDispatch):
    pass


class DispSVGDefsElement(_oaidl.IDispatch):
    pass


class ISVGAnimatedPathData(_oaidl.IDispatch):
    putref_pathSegList: _Callable[[ISVGPathSegList],  # v
                                  _type.HRESULT]
    get_pathSegList: _Callable[[_Pointer[ISVGPathSegList]],  # p
                               _type.HRESULT]
    putref_normalizedPathSegList: _Callable[[ISVGPathSegList],  # v
                                            _type.HRESULT]
    get_normalizedPathSegList: _Callable[[_Pointer[ISVGPathSegList]],  # p
                                         _type.HRESULT]
    putref_animatedPathSegList: _Callable[[ISVGPathSegList],  # v
                                          _type.HRESULT]
    get_animatedPathSegList: _Callable[[_Pointer[ISVGPathSegList]],  # p
                                       _type.HRESULT]
    putref_animatedNormalizedPathSegList: _Callable[[ISVGPathSegList],  # v
                                                    _type.HRESULT]
    get_animatedNormalizedPathSegList: _Callable[[_Pointer[ISVGPathSegList]],  # p
                                                 _type.HRESULT]


class ISVGPathElement(_oaidl.IDispatch):
    putref_pathLength: _Callable[[ISVGAnimatedNumber],  # v
                                 _type.HRESULT]
    get_pathLength: _Callable[[_Pointer[ISVGAnimatedNumber]],  # p
                              _type.HRESULT]
    getTotalLength: _Callable[[_Pointer[_type.c_float]],  # pfltResult
                              _type.HRESULT]
    getPointAtLength: _Callable[[_type.c_float,  # fltdistance
                                 _Pointer[ISVGPoint]],  # ppPointResult
                                _type.HRESULT]
    getPathSegAtLength: _Callable[[_type.c_float,  # fltdistance
                                   _Pointer[_type.c_long]],  # plResult
                                  _type.HRESULT]
    createSVGPathSegClosePath: _Callable[[_Pointer[ISVGPathSegClosePath]],  # ppResult
                                         _type.HRESULT]
    createSVGPathSegMovetoAbs: _Callable[[_type.c_float,  # x
                                          _type.c_float,  # y
                                          _Pointer[ISVGPathSegMovetoAbs]],  # ppResult
                                         _type.HRESULT]
    createSVGPathSegMovetoRel: _Callable[[_type.c_float,  # x
                                          _type.c_float,  # y
                                          _Pointer[ISVGPathSegMovetoRel]],  # ppResult
                                         _type.HRESULT]
    createSVGPathSegLinetoAbs: _Callable[[_type.c_float,  # x
                                          _type.c_float,  # y
                                          _Pointer[ISVGPathSegLinetoAbs]],  # ppResult
                                         _type.HRESULT]
    createSVGPathSegLinetoRel: _Callable[[_type.c_float,  # x
                                          _type.c_float,  # y
                                          _Pointer[ISVGPathSegLinetoRel]],  # ppResult
                                         _type.HRESULT]
    createSVGPathSegCurvetoCubicAbs: _Callable[[_type.c_float,  # x
                                                _type.c_float,  # y
                                                _type.c_float,  # x1
                                                _type.c_float,  # y1
                                                _type.c_float,  # x2
                                                _type.c_float,  # y2
                                                _Pointer[ISVGPathSegCurvetoCubicAbs]],  # ppResult
                                               _type.HRESULT]
    createSVGPathSegCurvetoCubicRel: _Callable[[_type.c_float,  # x
                                                _type.c_float,  # y
                                                _type.c_float,  # x1
                                                _type.c_float,  # y1
                                                _type.c_float,  # x2
                                                _type.c_float,  # y2
                                                _Pointer[ISVGPathSegCurvetoCubicRel]],  # ppResult
                                               _type.HRESULT]
    createSVGPathSegCurvetoQuadraticAbs: _Callable[[_type.c_float,  # x
                                                    _type.c_float,  # y
                                                    _type.c_float,  # x1
                                                    _type.c_float,  # y1
                                                    _Pointer[ISVGPathSegCurvetoQuadraticAbs]],  # ppResult
                                                   _type.HRESULT]
    createSVGPathSegCurvetoQuadraticRel: _Callable[[_type.c_float,  # x
                                                    _type.c_float,  # y
                                                    _type.c_float,  # x1
                                                    _type.c_float,  # y1
                                                    _Pointer[ISVGPathSegCurvetoQuadraticRel]],  # ppResult
                                                   _type.HRESULT]
    createSVGPathSegArcAbs: _Callable[[_type.c_float,  # x
                                       _type.c_float,  # y
                                       _type.c_float,  # r1
                                       _type.c_float,  # r2
                                       _type.c_float,  # angle
                                       _type.VARIANT_BOOL,  # largeArcFlag
                                       _type.VARIANT_BOOL,  # sweepFlag
                                       _Pointer[ISVGPathSegArcAbs]],  # ppResult
                                      _type.HRESULT]
    createSVGPathSegArcRel: _Callable[[_type.c_float,  # x
                                       _type.c_float,  # y
                                       _type.c_float,  # r1
                                       _type.c_float,  # r2
                                       _type.c_float,  # angle
                                       _type.VARIANT_BOOL,  # largeArcFlag
                                       _type.VARIANT_BOOL,  # sweepFlag
                                       _Pointer[ISVGPathSegArcRel]],  # ppResult
                                      _type.HRESULT]
    createSVGPathSegLinetoHorizontalAbs: _Callable[[_type.c_float,  # x
                                                    _Pointer[ISVGPathSegLinetoHorizontalAbs]],  # ppResult
                                                   _type.HRESULT]
    createSVGPathSegLinetoHorizontalRel: _Callable[[_type.c_float,  # x
                                                    _Pointer[ISVGPathSegLinetoHorizontalRel]],  # ppResult
                                                   _type.HRESULT]
    createSVGPathSegLinetoVerticalAbs: _Callable[[_type.c_float,  # y
                                                  _Pointer[ISVGPathSegLinetoVerticalAbs]],  # ppResult
                                                 _type.HRESULT]
    createSVGPathSegLinetoVerticalRel: _Callable[[_type.c_float,  # y
                                                  _Pointer[ISVGPathSegLinetoVerticalRel]],  # ppResult
                                                 _type.HRESULT]
    createSVGPathSegCurvetoCubicSmoothAbs: _Callable[[_type.c_float,  # x
                                                      _type.c_float,  # y
                                                      _type.c_float,  # x2
                                                      _type.c_float,  # y2
                                                      _Pointer[ISVGPathSegCurvetoCubicSmoothAbs]],  # ppResult
                                                     _type.HRESULT]
    createSVGPathSegCurvetoCubicSmoothRel: _Callable[[_type.c_float,  # x
                                                      _type.c_float,  # y
                                                      _type.c_float,  # x2
                                                      _type.c_float,  # y2
                                                      _Pointer[ISVGPathSegCurvetoCubicSmoothRel]],  # ppResult
                                                     _type.HRESULT]
    createSVGPathSegCurvetoQuadraticSmoothAbs: _Callable[[_type.c_float,  # x
                                                          _type.c_float,  # y
                                                          _Pointer[ISVGPathSegCurvetoQuadraticSmoothAbs]],  # ppResult
                                                         _type.HRESULT]
    createSVGPathSegCurvetoQuadraticSmoothRel: _Callable[[_type.c_float,  # x
                                                          _type.c_float,  # y
                                                          _Pointer[ISVGPathSegCurvetoQuadraticSmoothRel]],  # ppResult
                                                         _type.HRESULT]


class DispSVGPathElement(_oaidl.IDispatch):
    pass


class ISVGPreserveAspectRatio(_oaidl.IDispatch):
    put_align: _Callable[[_type.c_short],  # v
                         _type.HRESULT]
    get_align: _Callable[[_Pointer[_type.c_short]],  # p
                         _type.HRESULT]
    put_meetOrSlice: _Callable[[_type.c_short],  # v
                               _type.HRESULT]
    get_meetOrSlice: _Callable[[_Pointer[_type.c_short]],  # p
                               _type.HRESULT]


class ISVGTextElement(_oaidl.IDispatch):
    pass


class DispSVGTextElement(_oaidl.IDispatch):
    pass


class ISVGImageElement(_oaidl.IDispatch):
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]


class DispSVGImageElement(_oaidl.IDispatch):
    pass


class ISVGStopElement(_oaidl.IDispatch):
    putref_offset: _Callable[[ISVGAnimatedNumber],  # v
                             _type.HRESULT]
    get_offset: _Callable[[_Pointer[ISVGAnimatedNumber]],  # p
                          _type.HRESULT]


class DispSVGStopElement(_oaidl.IDispatch):
    pass


class ISVGGradientElement(_oaidl.IDispatch):
    putref_gradientUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                    _type.HRESULT]
    get_gradientUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                 _type.HRESULT]
    putref_gradientTransform: _Callable[[ISVGAnimatedTransformList],  # v
                                        _type.HRESULT]
    get_gradientTransform: _Callable[[_Pointer[ISVGAnimatedTransformList]],  # p
                                     _type.HRESULT]
    putref_spreadMethod: _Callable[[ISVGAnimatedEnumeration],  # v
                                   _type.HRESULT]
    get_spreadMethod: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                _type.HRESULT]


class DispSVGGradientElement(_oaidl.IDispatch):
    pass


class ISVGLinearGradientElement(_oaidl.IDispatch):
    putref_x1: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_x1: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_y1: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_y1: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_x2: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_x2: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_y2: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_y2: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]


class DispSVGLinearGradientElement(_oaidl.IDispatch):
    pass


class ISVGRadialGradientElement(_oaidl.IDispatch):
    putref_cx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_cy: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_cy: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_r: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_r: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_fx: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_fx: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]
    putref_fy: _Callable[[ISVGAnimatedLength],  # v
                         _type.HRESULT]
    get_fy: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                      _type.HRESULT]


class DispSVGRadialGradientElement(_oaidl.IDispatch):
    pass


class ISVGMaskElement(_oaidl.IDispatch):
    putref_maskUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                _type.HRESULT]
    get_maskUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                             _type.HRESULT]
    putref_maskContentUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                       _type.HRESULT]
    get_maskContentUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                    _type.HRESULT]
    putref_x: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLength],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                     _type.HRESULT]
    putref_width: _Callable[[ISVGAnimatedLength],  # v
                            _type.HRESULT]
    get_width: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                         _type.HRESULT]
    putref_height: _Callable[[ISVGAnimatedLength],  # v
                             _type.HRESULT]
    get_height: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                          _type.HRESULT]


class DispSVGMaskElement(_oaidl.IDispatch):
    pass


class ISVGMarkerElement(_oaidl.IDispatch):
    putref_refX: _Callable[[ISVGAnimatedLength],  # v
                           _type.HRESULT]
    get_refX: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                        _type.HRESULT]
    putref_refY: _Callable[[ISVGAnimatedLength],  # v
                           _type.HRESULT]
    get_refY: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                        _type.HRESULT]
    putref_markerUnits: _Callable[[ISVGAnimatedEnumeration],  # v
                                  _type.HRESULT]
    get_markerUnits: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                               _type.HRESULT]
    putref_markerWidth: _Callable[[ISVGAnimatedLength],  # v
                                  _type.HRESULT]
    get_markerWidth: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                               _type.HRESULT]
    putref_markerHeight: _Callable[[ISVGAnimatedLength],  # v
                                   _type.HRESULT]
    get_markerHeight: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                                _type.HRESULT]
    putref_orientType: _Callable[[ISVGAnimatedEnumeration],  # v
                                 _type.HRESULT]
    get_orientType: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                              _type.HRESULT]
    putref_orientAngle: _Callable[[ISVGAnimatedAngle],  # v
                                  _type.HRESULT]
    get_orientAngle: _Callable[[_Pointer[ISVGAnimatedAngle]],  # p
                               _type.HRESULT]
    setOrientToAuto: _Callable[[],
                               _type.HRESULT]
    setOrientToAngle: _Callable[[ISVGAngle],  # pSVGAngle
                                _type.HRESULT]


class DispSVGMarkerElement(_oaidl.IDispatch):
    pass


class ISVGZoomEvent(_oaidl.IDispatch):
    get_zoomRectScreen: _Callable[[_Pointer[ISVGRect]],  # p
                                  _type.HRESULT]
    get_previousScale: _Callable[[_Pointer[_type.c_float]],  # p
                                 _type.HRESULT]
    get_previousTranslate: _Callable[[_Pointer[ISVGPoint]],  # p
                                     _type.HRESULT]
    get_newScale: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    get_newTranslate: _Callable[[_Pointer[ISVGPoint]],  # p
                                _type.HRESULT]


class DispSVGZoomEvent(_oaidl.IDispatch):
    pass


class ISVGAElement(_oaidl.IDispatch):
    putref_target: _Callable[[ISVGAnimatedString],  # v
                             _type.HRESULT]
    get_target: _Callable[[_Pointer[ISVGAnimatedString]],  # p
                          _type.HRESULT]


class DispSVGAElement(_oaidl.IDispatch):
    pass


class ISVGViewElement(_oaidl.IDispatch):
    putref_viewTarget: _Callable[[ISVGStringList],  # v
                                 _type.HRESULT]
    get_viewTarget: _Callable[[_Pointer[ISVGStringList]],  # p
                              _type.HRESULT]


class DispSVGViewElement(_oaidl.IDispatch):
    pass


class IHTMLMediaError(_oaidl.IDispatch):
    get_code: _Callable[[_Pointer[_type.c_short]],  # p
                        _type.HRESULT]


class IHTMLTimeRanges(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    start: _Callable[[_type.c_long,  # index
                      _Pointer[_type.c_float]],  # startTime
                     _type.HRESULT]
    end: _Callable[[_type.c_long,  # index
                    _Pointer[_type.c_float]],  # endTime
                   _type.HRESULT]


class IHTMLTimeRanges2(_oaidl.IDispatch):
    startDouble: _Callable[[_type.c_long,  # index
                            _Pointer[_type.c_double]],  # startTime
                           _type.HRESULT]
    endDouble: _Callable[[_type.c_long,  # index
                          _Pointer[_type.c_double]],  # endTime
                         _type.HRESULT]


class IHTMLMediaElement(_oaidl.IDispatch):
    get_error: _Callable[[_Pointer[IHTMLMediaError]],  # p
                         _type.HRESULT]
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_currentSrc: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    get_networkState: _Callable[[_Pointer[_type.USHORT]],  # p
                                _type.HRESULT]
    put_preload: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_preload: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    get_buffered: _Callable[[_Pointer[IHTMLTimeRanges]],  # p
                            _type.HRESULT]
    load: _Callable[[],
                    _type.HRESULT]
    canPlayType: _Callable[[_type.BSTR,  # type
                            _Pointer[_type.BSTR]],  # canPlay
                           _type.HRESULT]
    get_seeking: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    put_currentTime: _Callable[[_type.c_float],  # v
                               _type.HRESULT]
    get_currentTime: _Callable[[_Pointer[_type.c_float]],  # p
                               _type.HRESULT]
    get_initialTime: _Callable[[_Pointer[_type.c_float]],  # p
                               _type.HRESULT]
    get_duration: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    get_paused: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_defaultPlaybackRate: _Callable[[_type.c_float],  # v
                                       _type.HRESULT]
    get_defaultPlaybackRate: _Callable[[_Pointer[_type.c_float]],  # p
                                       _type.HRESULT]
    put_playbackRate: _Callable[[_type.c_float],  # v
                                _type.HRESULT]
    get_playbackRate: _Callable[[_Pointer[_type.c_float]],  # p
                                _type.HRESULT]
    get_played: _Callable[[_Pointer[IHTMLTimeRanges]],  # p
                          _type.HRESULT]
    get_seekable: _Callable[[_Pointer[IHTMLTimeRanges]],  # p
                            _type.HRESULT]
    get_ended: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                         _type.HRESULT]
    put_autoplay: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_autoplay: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_loop: _Callable[[_type.VARIANT_BOOL],  # v
                        _type.HRESULT]
    get_loop: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                        _type.HRESULT]
    play: _Callable[[],
                    _type.HRESULT]
    pause: _Callable[[],
                     _type.HRESULT]
    put_controls: _Callable[[_type.VARIANT_BOOL],  # v
                            _type.HRESULT]
    get_controls: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    put_volume: _Callable[[_type.c_float],  # v
                          _type.HRESULT]
    get_volume: _Callable[[_Pointer[_type.c_float]],  # p
                          _type.HRESULT]
    put_muted: _Callable[[_type.VARIANT_BOOL],  # v
                         _type.HRESULT]
    get_muted: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                         _type.HRESULT]
    put_autobuffer: _Callable[[_type.VARIANT_BOOL],  # v
                              _type.HRESULT]
    get_autobuffer: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]


class IHTMLMediaElement2(_oaidl.IDispatch):
    put_currentTimeDouble: _Callable[[_type.c_double],  # v
                                     _type.HRESULT]
    get_currentTimeDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                     _type.HRESULT]
    get_initialTimeDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                     _type.HRESULT]
    get_durationDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                  _type.HRESULT]
    put_defaultPlaybackRateDouble: _Callable[[_type.c_double],  # v
                                             _type.HRESULT]
    get_defaultPlaybackRateDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                             _type.HRESULT]
    put_playbackRateDouble: _Callable[[_type.c_double],  # v
                                      _type.HRESULT]
    get_playbackRateDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                      _type.HRESULT]
    put_volumeDouble: _Callable[[_type.c_double],  # v
                                _type.HRESULT]
    get_volumeDouble: _Callable[[_Pointer[_type.c_double]],  # p
                                _type.HRESULT]


class IHTMLMSMediaElement(_oaidl.IDispatch):
    put_msPlayToDisabled: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_msPlayToDisabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_msPlayToPrimary: _Callable[[_type.VARIANT_BOOL],  # v
                                   _type.HRESULT]
    get_msPlayToPrimary: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]


class IHTMLSourceElement(_oaidl.IDispatch):
    put_src: _Callable[[_type.BSTR],  # v
                       _type.HRESULT]
    get_src: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class IHTMLAudioElement(_oaidl.IDispatch):
    pass


class IHTMLVideoElement(_oaidl.IDispatch):
    put_width: _Callable[[_type.c_long],  # v
                         _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    put_height: _Callable[[_type.c_long],  # v
                          _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_videoWidth: _Callable[[_Pointer[_type.ULONG]],  # p
                              _type.HRESULT]
    get_videoHeight: _Callable[[_Pointer[_type.ULONG]],  # p
                               _type.HRESULT]
    put_poster: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_poster: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]


class IHTMLAudioElementFactory(_oaidl.IDispatch):
    create: _Callable[[_struct.VARIANT,  # src
                       _Pointer[IHTMLAudioElement]],  # __MIDL__IHTMLAudioElementFactory0000
                      _type.HRESULT]


class DispHTMLMediaError(_oaidl.IDispatch):
    pass


class DispHTMLTimeRanges(_oaidl.IDispatch):
    pass


class DispHTMLMediaElement(_oaidl.IDispatch):
    pass


class DispHTMLSourceElement(_oaidl.IDispatch):
    pass


class DispHTMLAudioElement(_oaidl.IDispatch):
    pass


class DispHTMLVideoElement(_oaidl.IDispatch):
    pass


class ISVGSwitchElement(_oaidl.IDispatch):
    pass


class DispSVGSwitchElement(_oaidl.IDispatch):
    pass


class ISVGDescElement(_oaidl.IDispatch):
    pass


class DispSVGDescElement(_oaidl.IDispatch):
    pass


class ISVGTitleElement(_oaidl.IDispatch):
    pass


class DispSVGTitleElement(_oaidl.IDispatch):
    pass


class ISVGMetadataElement(_oaidl.IDispatch):
    pass


class DispSVGMetadataElement(_oaidl.IDispatch):
    pass


class ISVGElementInstanceList(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[ISVGElementInstance]],  # ppResult
                    _type.HRESULT]


class DispSVGElementInstance(_oaidl.IDispatch):
    pass


class DispSVGElementInstanceList(_oaidl.IDispatch):
    pass


class IDOMException(_oaidl.IDispatch):
    put_code: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_code: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    get_message: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class DispDOMException(_oaidl.IDispatch):
    pass


class IRangeException(_oaidl.IDispatch):
    put_code: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_code: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    get_message: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class DispRangeException(_oaidl.IDispatch):
    pass


class ISVGException(_oaidl.IDispatch):
    put_code: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_code: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    get_message: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class DispSVGException(_oaidl.IDispatch):
    pass


class IEventException(_oaidl.IDispatch):
    put_code: _Callable[[_type.c_long],  # v
                        _type.HRESULT]
    get_code: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    get_message: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class DispEventException(_oaidl.IDispatch):
    pass


class ISVGScriptElement(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]


class DispSVGScriptElement(_oaidl.IDispatch):
    pass


class ISVGStyleElement(_oaidl.IDispatch):
    put_type: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_type: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_media: _Callable[[_type.BSTR],  # v
                         _type.HRESULT]
    get_media: _Callable[[_Pointer[_type.BSTR]],  # p
                         _type.HRESULT]


class DispSVGStyleElement(_oaidl.IDispatch):
    pass


class ISVGTextContentElement(_oaidl.IDispatch):
    putref_textLength: _Callable[[ISVGAnimatedLength],  # v
                                 _type.HRESULT]
    get_textLength: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                              _type.HRESULT]
    putref_lengthAdjust: _Callable[[ISVGAnimatedEnumeration],  # v
                                   _type.HRESULT]
    get_lengthAdjust: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                                _type.HRESULT]
    getNumberOfChars: _Callable[[_Pointer[_type.c_long]],  # pResult
                                _type.HRESULT]
    getComputedTextLength: _Callable[[_Pointer[_type.c_float]],  # pResult
                                     _type.HRESULT]
    getSubStringLength: _Callable[[_type.c_long,  # charnum
                                   _type.c_long,  # nchars
                                   _Pointer[_type.c_float]],  # pResult
                                  _type.HRESULT]
    getStartPositionOfChar: _Callable[[_type.c_long,  # charnum
                                       _Pointer[ISVGPoint]],  # ppResult
                                      _type.HRESULT]
    getEndPositionOfChar: _Callable[[_type.c_long,  # charnum
                                     _Pointer[ISVGPoint]],  # ppResult
                                    _type.HRESULT]
    getExtentOfChar: _Callable[[_type.c_long,  # charnum
                                _Pointer[ISVGRect]],  # ppResult
                               _type.HRESULT]
    getRotationOfChar: _Callable[[_type.c_long,  # charnum
                                  _Pointer[_type.c_float]],  # pResult
                                 _type.HRESULT]
    getCharNumAtPosition: _Callable[[ISVGPoint,  # point
                                     _Pointer[_type.c_long]],  # pResult
                                    _type.HRESULT]
    selectSubString: _Callable[[_type.c_long,  # charnum
                                _type.c_long],  # nchars
                               _type.HRESULT]


class DispSVGTextContentElement(_oaidl.IDispatch):
    pass


class ISVGTextPositioningElement(_oaidl.IDispatch):
    putref_x: _Callable[[ISVGAnimatedLengthList],  # v
                        _type.HRESULT]
    get_x: _Callable[[_Pointer[ISVGAnimatedLengthList]],  # p
                     _type.HRESULT]
    putref_y: _Callable[[ISVGAnimatedLengthList],  # v
                        _type.HRESULT]
    get_y: _Callable[[_Pointer[ISVGAnimatedLengthList]],  # p
                     _type.HRESULT]
    putref_dx: _Callable[[ISVGAnimatedLengthList],  # v
                         _type.HRESULT]
    get_dx: _Callable[[_Pointer[ISVGAnimatedLengthList]],  # p
                      _type.HRESULT]
    putref_dy: _Callable[[ISVGAnimatedLengthList],  # v
                         _type.HRESULT]
    get_dy: _Callable[[_Pointer[ISVGAnimatedLengthList]],  # p
                      _type.HRESULT]
    putref_rotate: _Callable[[ISVGAnimatedNumberList],  # v
                             _type.HRESULT]
    get_rotate: _Callable[[_Pointer[ISVGAnimatedNumberList]],  # p
                          _type.HRESULT]


class DispSVGTextPositioningElement(_oaidl.IDispatch):
    pass


class DispDOMDocumentType(_oaidl.IDispatch):
    pass


class DispNodeIterator(_oaidl.IDispatch):
    pass


class DispTreeWalker(_oaidl.IDispatch):
    pass


class DispDOMProcessingInstruction(_oaidl.IDispatch):
    pass


class IHTMLPerformanceNavigation(_oaidl.IDispatch):
    get_type: _Callable[[_Pointer[_type.ULONG]],  # p
                        _type.HRESULT]
    get_redirectCount: _Callable[[_Pointer[_type.ULONG]],  # p
                                 _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # string
                        _type.HRESULT]
    toJSON: _Callable[[_Pointer[_struct.VARIANT]],  # pVar
                      _type.HRESULT]


class IHTMLPerformanceTiming(_oaidl.IDispatch):
    get_navigationStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                   _type.HRESULT]
    get_unloadEventStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                    _type.HRESULT]
    get_unloadEventEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                  _type.HRESULT]
    get_redirectStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                 _type.HRESULT]
    get_redirectEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                               _type.HRESULT]
    get_fetchStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                              _type.HRESULT]
    get_domainLookupStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                     _type.HRESULT]
    get_domainLookupEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                   _type.HRESULT]
    get_connectStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                _type.HRESULT]
    get_connectEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                              _type.HRESULT]
    get_requestStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                _type.HRESULT]
    get_responseStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                 _type.HRESULT]
    get_responseEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                               _type.HRESULT]
    get_domLoading: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                              _type.HRESULT]
    get_domInteractive: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                  _type.HRESULT]
    get_domContentLoadedEventStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                              _type.HRESULT]
    get_domContentLoadedEventEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                            _type.HRESULT]
    get_domComplete: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                               _type.HRESULT]
    get_loadEventStart: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                  _type.HRESULT]
    get_loadEventEnd: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                _type.HRESULT]
    get_msFirstPaint: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                                _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # string
                        _type.HRESULT]
    toJSON: _Callable[[_Pointer[_struct.VARIANT]],  # pVar
                      _type.HRESULT]


class DispHTMLPerformance(_oaidl.IDispatch):
    pass


class DispHTMLPerformanceNavigation(_oaidl.IDispatch):
    pass


class DispHTMLPerformanceTiming(_oaidl.IDispatch):
    pass


class ISVGTSpanElement(_oaidl.IDispatch):
    pass


class DispSVGTSpanElement(_oaidl.IDispatch):
    pass


class ITemplatePrinter(_oaidl.IDispatch):
    startDoc: _Callable[[_type.BSTR,  # bstrTitle
                         _Pointer[_type.VARIANT_BOOL]],  # p
                        _type.HRESULT]
    stopDoc: _Callable[[],
                       _type.HRESULT]
    printBlankPage: _Callable[[],
                              _type.HRESULT]
    printPage: _Callable[[_oaidl.IDispatch],  # pElemDisp
                         _type.HRESULT]
    ensurePrintDialogDefaults: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                         _type.HRESULT]
    showPrintDialog: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    showPageSetupDialog: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                   _type.HRESULT]
    printNonNative: _Callable[[_Unknwnbase.IUnknown,  # pMarkup
                               _Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    printNonNativeFrames: _Callable[[_Unknwnbase.IUnknown,  # pMarkup
                                     _type.VARIANT_BOOL],  # fActiveFrame
                                    _type.HRESULT]
    put_framesetDocument: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_framesetDocument: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_frameActive: _Callable[[_type.VARIANT_BOOL],  # v
                               _type.HRESULT]
    get_frameActive: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    put_frameAsShown: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_frameAsShown: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    put_selection: _Callable[[_type.VARIANT_BOOL],  # v
                             _type.HRESULT]
    get_selection: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    put_selectedPages: _Callable[[_type.VARIANT_BOOL],  # v
                                 _type.HRESULT]
    get_selectedPages: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    put_currentPage: _Callable[[_type.VARIANT_BOOL],  # v
                               _type.HRESULT]
    get_currentPage: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    put_currentPageAvail: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_currentPageAvail: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_collate: _Callable[[_type.VARIANT_BOOL],  # v
                           _type.HRESULT]
    get_collate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                           _type.HRESULT]
    get_duplex: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    put_copies: _Callable[[_type.USHORT],  # v
                          _type.HRESULT]
    get_copies: _Callable[[_Pointer[_type.USHORT]],  # p
                          _type.HRESULT]
    put_pageFrom: _Callable[[_type.USHORT],  # v
                            _type.HRESULT]
    get_pageFrom: _Callable[[_Pointer[_type.USHORT]],  # p
                            _type.HRESULT]
    put_pageTo: _Callable[[_type.USHORT],  # v
                          _type.HRESULT]
    get_pageTo: _Callable[[_Pointer[_type.USHORT]],  # p
                          _type.HRESULT]
    put_tableOfLinks: _Callable[[_type.VARIANT_BOOL],  # v
                                _type.HRESULT]
    get_tableOfLinks: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    put_allLinkedDocuments: _Callable[[_type.VARIANT_BOOL],  # v
                                      _type.HRESULT]
    get_allLinkedDocuments: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]
    put_header: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_header: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_footer: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_footer: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_marginLeft: _Callable[[_type.c_long],  # v
                              _type.HRESULT]
    get_marginLeft: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    put_marginRight: _Callable[[_type.c_long],  # v
                               _type.HRESULT]
    get_marginRight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    put_marginTop: _Callable[[_type.c_long],  # v
                             _type.HRESULT]
    get_marginTop: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    put_marginBottom: _Callable[[_type.c_long],  # v
                                _type.HRESULT]
    get_marginBottom: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    get_pageWidth: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_pageHeight: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_unprintableLeft: _Callable[[_Pointer[_type.c_long]],  # p
                                   _type.HRESULT]
    get_unprintableTop: _Callable[[_Pointer[_type.c_long]],  # p
                                  _type.HRESULT]
    get_unprintableRight: _Callable[[_Pointer[_type.c_long]],  # p
                                    _type.HRESULT]
    get_unprintableBottom: _Callable[[_Pointer[_type.c_long]],  # p
                                     _type.HRESULT]
    updatePageStatus: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]


class ITemplatePrinter2(ITemplatePrinter):
    put_selectionEnabled: _Callable[[_type.VARIANT_BOOL],  # v
                                    _type.HRESULT]
    get_selectionEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    put_frameActiveEnabled: _Callable[[_type.VARIANT_BOOL],  # v
                                      _type.HRESULT]
    get_frameActiveEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                      _type.HRESULT]
    put_orientation: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_orientation: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_usePrinterCopyCollate: _Callable[[_type.VARIANT_BOOL],  # v
                                         _type.HRESULT]
    get_usePrinterCopyCollate: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                         _type.HRESULT]
    deviceSupports: _Callable[[_type.BSTR,  # bstrProperty
                               _Pointer[_struct.VARIANT]],  # pvar
                              _type.HRESULT]


class ITemplatePrinter3(ITemplatePrinter2):
    put_headerFooterFont: _Callable[[_type.BSTR],  # v
                                    _type.HRESULT]
    get_headerFooterFont: _Callable[[_Pointer[_type.BSTR]],  # p
                                    _type.HRESULT]
    getPageMarginTop: _Callable[[_oaidl.IDispatch,  # pageRule
                                 _type.c_long,  # pageWidth
                                 _type.c_long,  # pageHeight
                                 _Pointer[_struct.VARIANT]],  # pMargin
                                _type.HRESULT]
    getPageMarginRight: _Callable[[_oaidl.IDispatch,  # pageRule
                                   _type.c_long,  # pageWidth
                                   _type.c_long,  # pageHeight
                                   _Pointer[_struct.VARIANT]],  # pMargin
                                  _type.HRESULT]
    getPageMarginBottom: _Callable[[_oaidl.IDispatch,  # pageRule
                                    _type.c_long,  # pageWidth
                                    _type.c_long,  # pageHeight
                                    _Pointer[_struct.VARIANT]],  # pMargin
                                   _type.HRESULT]
    getPageMarginLeft: _Callable[[_oaidl.IDispatch,  # pageRule
                                  _type.c_long,  # pageWidth
                                  _type.c_long,  # pageHeight
                                  _Pointer[_struct.VARIANT]],  # pMargin
                                 _type.HRESULT]
    getPageMarginTopImportant: _Callable[[_oaidl.IDispatch,  # pageRule
                                          _Pointer[_type.VARIANT_BOOL]],  # pbImportant
                                         _type.HRESULT]
    getPageMarginRightImportant: _Callable[[_oaidl.IDispatch,  # pageRule
                                            _Pointer[_type.VARIANT_BOOL]],  # pbImportant
                                           _type.HRESULT]
    getPageMarginBottomImportant: _Callable[[_oaidl.IDispatch,  # pageRule
                                             _Pointer[_type.VARIANT_BOOL]],  # pbImportant
                                            _type.HRESULT]
    getPageMarginLeftImportant: _Callable[[_oaidl.IDispatch,  # pageRule
                                           _Pointer[_type.VARIANT_BOOL]],  # pbImportant
                                          _type.HRESULT]


class IPrintManagerTemplatePrinter(_oaidl.IDispatch):
    startPrint: _Callable[[],
                          _type.HRESULT]
    drawPreviewPage: _Callable[[_oaidl.IDispatch,  # pElemDisp
                                _type.c_long],  # nPage
                               _type.HRESULT]
    setPageCount: _Callable[[_type.c_long],  # nPage
                            _type.HRESULT]
    invalidatePreview: _Callable[[],
                                 _type.HRESULT]
    getPrintTaskOptionValue: _Callable[[_type.BSTR,  # bstrKey
                                        _Pointer[_struct.VARIANT]],  # pvarin
                                       _type.HRESULT]
    endPrint: _Callable[[],
                        _type.HRESULT]


class IPrintManagerTemplatePrinter2(IPrintManagerTemplatePrinter):
    get_showHeaderFooter: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    get_shrinkToFit: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    get_percentScale: _Callable[[_Pointer[_type.c_float]],  # p
                                _type.HRESULT]


class DispCPrintManagerTemplatePrinter(_oaidl.IDispatch):
    pass


class ISVGTextPathElement(_oaidl.IDispatch):
    putref_startOffset: _Callable[[ISVGAnimatedLength],  # v
                                  _type.HRESULT]
    get_startOffset: _Callable[[_Pointer[ISVGAnimatedLength]],  # p
                               _type.HRESULT]
    putref_method: _Callable[[ISVGAnimatedEnumeration],  # v
                             _type.HRESULT]
    get_method: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                          _type.HRESULT]
    putref_spacing: _Callable[[ISVGAnimatedEnumeration],  # v
                              _type.HRESULT]
    get_spacing: _Callable[[_Pointer[ISVGAnimatedEnumeration]],  # p
                           _type.HRESULT]


class DispSVGTextPathElement(_oaidl.IDispatch):
    pass


class IDOMXmlSerializer(_oaidl.IDispatch):
    serializeToString: _Callable[[IHTMLDOMNode,  # pNode
                                  _Pointer[_type.BSTR]],  # pString
                                 _type.HRESULT]


class IDOMParser(_oaidl.IDispatch):
    parseFromString: _Callable[[_type.BSTR,  # xmlSource
                                _type.BSTR,  # mimeType
                                _Pointer[IHTMLDocument2]],  # ppNode
                               _type.HRESULT]


class DispXMLSerializer(_oaidl.IDispatch):
    pass


class DispDOMParser(_oaidl.IDispatch):
    pass


class IDOMXmlSerializerFactory(_oaidl.IDispatch):
    create: _Callable[[_Pointer[IDOMXmlSerializer]],  # __MIDL__IDOMXmlSerializerFactory0000
                      _type.HRESULT]


class IDOMParserFactory(_oaidl.IDispatch):
    create: _Callable[[_Pointer[IDOMParser]],  # __MIDL__IDOMParserFactory0000
                      _type.HRESULT]


class DispHTMLSemanticElement(_oaidl.IDispatch):
    pass


class IHTMLProgressElement(_oaidl.IDispatch):
    put_value: _Callable[[_type.c_float],  # v
                         _type.HRESULT]
    get_value: _Callable[[_Pointer[_type.c_float]],  # p
                         _type.HRESULT]
    put_max: _Callable[[_type.c_float],  # v
                       _type.HRESULT]
    get_max: _Callable[[_Pointer[_type.c_float]],  # p
                       _type.HRESULT]
    get_position: _Callable[[_Pointer[_type.c_float]],  # p
                            _type.HRESULT]
    get_form: _Callable[[_Pointer[IHTMLFormElement]],  # p
                        _type.HRESULT]


class DispHTMLProgressElement(_oaidl.IDispatch):
    pass


class IDOMMSTransitionEvent(_oaidl.IDispatch):
    get_propertyName: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_elapsedTime: _Callable[[_Pointer[_type.c_float]],  # p
                               _type.HRESULT]
    initMSTransitionEvent: _Callable[[_type.BSTR,  # eventType
                                      _type.VARIANT_BOOL,  # canBubble
                                      _type.VARIANT_BOOL,  # cancelable
                                      _type.BSTR,  # propertyName
                                      _type.c_float],  # elapsedTime
                                     _type.HRESULT]


class DispDOMMSTransitionEvent(_oaidl.IDispatch):
    pass


class IDOMMSAnimationEvent(_oaidl.IDispatch):
    get_animationName: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_elapsedTime: _Callable[[_Pointer[_type.c_float]],  # p
                               _type.HRESULT]
    initMSAnimationEvent: _Callable[[_type.BSTR,  # eventType
                                     _type.VARIANT_BOOL,  # canBubble
                                     _type.VARIANT_BOOL,  # cancelable
                                     _type.BSTR,  # animationName
                                     _type.c_float],  # elapsedTime
                                    _type.HRESULT]


class DispDOMMSAnimationEvent(_oaidl.IDispatch):
    pass


class IWebGeocoordinates(_oaidl.IDispatch):
    get_latitude: _Callable[[_Pointer[_type.c_double]],  # p
                            _type.HRESULT]
    get_longitude: _Callable[[_Pointer[_type.c_double]],  # p
                             _type.HRESULT]
    get_altitude: _Callable[[_Pointer[_struct.VARIANT]],  # p
                            _type.HRESULT]
    get_accuracy: _Callable[[_Pointer[_type.c_double]],  # p
                            _type.HRESULT]
    get_altitudeAccuracy: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                    _type.HRESULT]
    get_heading: _Callable[[_Pointer[_struct.VARIANT]],  # p
                           _type.HRESULT]
    get_speed: _Callable[[_Pointer[_struct.VARIANT]],  # p
                         _type.HRESULT]


class IWebGeopositionError(_oaidl.IDispatch):
    get_code: _Callable[[_Pointer[_type.c_long]],  # p
                        _type.HRESULT]
    get_message: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]


class IWebGeoposition(_oaidl.IDispatch):
    get_coords: _Callable[[_Pointer[IWebGeocoordinates]],  # p
                          _type.HRESULT]
    get_timestamp: _Callable[[_Pointer[_type.ULONGLONG]],  # p
                             _type.HRESULT]


class DispWebGeolocation(_oaidl.IDispatch):
    pass


class DispWebGeocoordinates(_oaidl.IDispatch):
    pass


class DispWebGeopositionError(_oaidl.IDispatch):
    pass


class DispWebGeoposition(_oaidl.IDispatch):
    pass


class IClientCaps(_oaidl.IDispatch):
    get_javaEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    get_cookieEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                 _type.HRESULT]
    get_cpuClass: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_systemLanguage: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    get_userLanguage: _Callable[[_Pointer[_type.BSTR]],  # p
                                _type.HRESULT]
    get_platform: _Callable[[_Pointer[_type.BSTR]],  # p
                            _type.HRESULT]
    get_connectionSpeed: _Callable[[_Pointer[_type.c_long]],  # p
                                   _type.HRESULT]
    get_onLine: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_colorDepth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_bufferDepth: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_width: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    get_height: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get_availHeight: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_availWidth: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_connectionType: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    isComponentInstalled: _Callable[[_type.BSTR,  # bstrName
                                     _type.BSTR,  # bstrUrl
                                     _type.BSTR,  # bStrVer
                                     _Pointer[_type.VARIANT_BOOL]],  # p
                                    _type.HRESULT]
    getComponentVersion: _Callable[[_type.BSTR,  # bstrName
                                    _type.BSTR,  # bstrUrl
                                    _Pointer[_type.BSTR]],  # pbstrVer
                                   _type.HRESULT]
    compareVersions: _Callable[[_type.BSTR,  # bstrVer1
                                _type.BSTR,  # bstrVer2
                                _Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    addComponentRequest: _Callable[[_type.BSTR,  # bstrName
                                    _type.BSTR,  # bstrUrl
                                    _type.BSTR],  # bStrVer
                                   _type.HRESULT]
    doComponentRequest: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    clearComponentRequest: _Callable[[],
                                     _type.HRESULT]


class IDOMMSManipulationEvent(_oaidl.IDispatch):
    get_lastState: _Callable[[_Pointer[_type.c_long]],  # p
                             _type.HRESULT]
    get_currentState: _Callable[[_Pointer[_type.c_long]],  # p
                                _type.HRESULT]
    initMSManipulationEvent: _Callable[[_type.BSTR,  # eventType
                                        _type.VARIANT_BOOL,  # canBubble
                                        _type.VARIANT_BOOL,  # cancelable
                                        IHTMLWindow2,  # viewArg
                                        _type.c_long,  # detailArg
                                        _type.c_long,  # lastState
                                        _type.c_long],  # currentState
                                       _type.HRESULT]


class DispDOMMSManipulationEvent(_oaidl.IDispatch):
    pass


class IDOMCloseEvent(_oaidl.IDispatch):
    get_wasClean: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    initCloseEvent: _Callable[[_type.BSTR,  # eventType
                               _type.VARIANT_BOOL,  # canBubble
                               _type.VARIANT_BOOL,  # cancelable
                               _type.VARIANT_BOOL,  # wasClean
                               _type.c_long,  # code
                               _type.BSTR],  # reason
                              _type.HRESULT]


class DispDOMCloseEvent(_oaidl.IDispatch):
    pass


class DispApplicationCache(_oaidl.IDispatch):
    pass


class ICSSFilterSite(_Unknwnbase.IUnknown):
    GetElement: _Callable[[_Pointer[IHTMLElement]],  # Element
                          _type.HRESULT]
    FireOnFilterChangeEvent: _Callable[[],
                                       _type.HRESULT]


class IMarkupPointer(_Unknwnbase.IUnknown):
    OwningDoc: _Callable[[_Pointer[IHTMLDocument2]],  # ppDoc
                         _type.HRESULT]
    Gravity: _Callable[[_Pointer[_enum.POINTER_GRAVITY]],  # pGravity
                       _type.HRESULT]
    SetGravity: _Callable[[_enum.POINTER_GRAVITY],  # Gravity
                          _type.HRESULT]
    Cling: _Callable[[_Pointer[_type.BOOL]],  # pfCling
                     _type.HRESULT]
    SetCling: _Callable[[_type.BOOL],  # fCLing
                        _type.HRESULT]
    Unposition: _Callable[[],
                          _type.HRESULT]
    IsPositioned: _Callable[[_Pointer[_type.BOOL]],  # pfPositioned
                            _type.HRESULT]
    GetContainer: _Callable[[_Pointer[IMarkupContainer]],  # ppContainer
                            _type.HRESULT]
    MoveAdjacentToElement: _Callable[[IHTMLElement,  # pElement
                                      _enum.ELEMENT_ADJACENCY],  # eAdj
                                     _type.HRESULT]
    MoveToPointer: _Callable[[IMarkupPointer],  # pPointer
                             _type.HRESULT]
    MoveToContainer: _Callable[[IMarkupContainer,  # pContainer
                                _type.BOOL],  # fAtStart
                               _type.HRESULT]
    Left: _Callable[[_type.BOOL,  # fMove
                     _Pointer[_enum.MARKUP_CONTEXT_TYPE],  # pContext
                     _Pointer[IHTMLElement],  # ppElement
                     _Pointer[_type.c_long],  # pcch
                     _Pointer[_type.OLECHAR]],  # pchText
                    _type.HRESULT]
    Right: _Callable[[_type.BOOL,  # fMove
                      _Pointer[_enum.MARKUP_CONTEXT_TYPE],  # pContext
                      _Pointer[IHTMLElement],  # ppElement
                      _Pointer[_type.c_long],  # pcch
                      _Pointer[_type.OLECHAR]],  # pchText
                     _type.HRESULT]
    CurrentScope: _Callable[[_Pointer[IHTMLElement]],  # ppElemCurrent
                            _type.HRESULT]
    IsLeftOf: _Callable[[IMarkupPointer,  # pPointerThat
                         _Pointer[_type.BOOL]],  # pfResult
                        _type.HRESULT]
    IsLeftOfOrEqualTo: _Callable[[IMarkupPointer,  # pPointerThat
                                  _Pointer[_type.BOOL]],  # pfResult
                                 _type.HRESULT]
    IsRightOf: _Callable[[IMarkupPointer,  # pPointerThat
                          _Pointer[_type.BOOL]],  # pfResult
                         _type.HRESULT]
    IsRightOfOrEqualTo: _Callable[[IMarkupPointer,  # pPointerThat
                                   _Pointer[_type.BOOL]],  # pfResult
                                  _type.HRESULT]
    IsEqualTo: _Callable[[IMarkupPointer,  # pPointerThat
                          _Pointer[_type.BOOL]],  # pfAreEqual
                         _type.HRESULT]
    MoveUnit: _Callable[[_enum.MOVEUNIT_ACTION],  # muAction
                        _type.HRESULT]
    FindTextA: _Callable[[_Pointer[_type.OLECHAR],  # pchFindText
                          _type.DWORD,  # dwFlags
                          IMarkupPointer,  # pIEndMatch
                          IMarkupPointer],  # pIEndSearch
                         _type.HRESULT]


class IMarkupContainer(_Unknwnbase.IUnknown):
    OwningDoc: _Callable[[_Pointer[IHTMLDocument2]],  # ppDoc
                         _type.HRESULT]


class IMarkupContainer2(IMarkupContainer):
    CreateChangeLog: _Callable[[IHTMLChangeSink,  # pChangeSink
                                _Pointer[IHTMLChangeLog],  # ppChangeLog
                                _type.BOOL,  # fForward
                                _type.BOOL],  # fBackward
                               _type.HRESULT]
    RegisterForDirtyRange: _Callable[[IHTMLChangeSink,  # pChangeSink
                                      _Pointer[_type.DWORD]],  # pdwCookie
                                     _type.HRESULT]
    UnRegisterForDirtyRange: _Callable[[_type.DWORD],  # dwCookie
                                       _type.HRESULT]
    GetAndClearDirtyRange: _Callable[[_type.DWORD,  # dwCookie
                                      IMarkupPointer,  # pIPointerBegin
                                      IMarkupPointer],  # pIPointerEnd
                                     _type.HRESULT]
    GetVersionNumber: _Callable[[],
                                _type.c_long]
    GetMasterElement: _Callable[[_Pointer[IHTMLElement]],  # ppElementMaster
                                _type.HRESULT]


class IHTMLChangeLog(_Unknwnbase.IUnknown):
    GetNextChange: _Callable[[_Pointer[_type.BYTE],  # pbBuffer
                              _type.c_long,  # nBufferSize
                              _Pointer[_type.c_long]],  # pnRecordLength
                             _type.HRESULT]


class IHTMLChangeSink(_Unknwnbase.IUnknown):
    Notify: _Callable[[],
                      _type.HRESULT]


class ISegmentList(_Unknwnbase.IUnknown):
    CreateIterator: _Callable[[_Pointer[ISegmentListIterator]],  # ppIIter
                              _type.HRESULT]
    GetType: _Callable[[_Pointer[_enum.SELECTION_TYPE]],  # peType
                       _type.HRESULT]
    IsEmpty: _Callable[[_Pointer[_type.BOOL]],  # pfEmpty
                       _type.HRESULT]


class ISegmentListIterator(_Unknwnbase.IUnknown):
    Current: _Callable[[_Pointer[ISegment]],  # ppISegment
                       _type.HRESULT]
    First: _Callable[[],
                     _type.HRESULT]
    IsDone: _Callable[[],
                      _type.HRESULT]
    Advance: _Callable[[],
                       _type.HRESULT]


class IHTMLCaret(_Unknwnbase.IUnknown):
    MoveCaretToPointer: _Callable[[IDisplayPointer,  # pDispPointer
                                   _type.BOOL,  # fScrollIntoView
                                   _enum.CARET_DIRECTION],  # eDir
                                  _type.HRESULT]
    MoveCaretToPointerEx: _Callable[[IDisplayPointer,  # pDispPointer
                                     _type.BOOL,  # fVisible
                                     _type.BOOL,  # fScrollIntoView
                                     _enum.CARET_DIRECTION],  # eDir
                                    _type.HRESULT]
    MoveMarkupPointerToCaret: _Callable[[IMarkupPointer],  # pIMarkupPointer
                                        _type.HRESULT]
    MoveDisplayPointerToCaret: _Callable[[IDisplayPointer],  # pDispPointer
                                         _type.HRESULT]
    IsVisible: _Callable[[_Pointer[_type.BOOL]],  # pIsVisible
                         _type.HRESULT]
    Show: _Callable[[_type.BOOL],  # fScrollIntoView
                    _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    InsertText: _Callable[[_Pointer[_type.OLECHAR],  # pText
                           _type.LONG],  # lLen
                          _type.HRESULT]
    ScrollIntoView: _Callable[[],
                              _type.HRESULT]
    GetLocation: _Callable[[_Pointer[_struct.POINT],  # pPoint
                            _type.BOOL],  # fTranslate
                           _type.HRESULT]
    GetCaretDirection: _Callable[[_Pointer[_enum.CARET_DIRECTION]],  # peDir
                                 _type.HRESULT]
    SetCaretDirection: _Callable[[_enum.CARET_DIRECTION],  # eDir
                                 _type.HRESULT]


class ISegment(_Unknwnbase.IUnknown):
    GetPointers: _Callable[[IMarkupPointer,  # pIStart
                            IMarkupPointer],  # pIEnd
                           _type.HRESULT]


class IElementSegment(ISegment):
    GetElement: _Callable[[_Pointer[IHTMLElement]],  # ppIElement
                          _type.HRESULT]
    SetPrimary: _Callable[[_type.BOOL],  # fPrimary
                          _type.HRESULT]
    IsPrimary: _Callable[[_Pointer[_type.BOOL]],  # pfPrimary
                         _type.HRESULT]


class IHighlightSegment(ISegment):
    pass


class IHighlightRenderingServices(_Unknwnbase.IUnknown):
    AddSegment: _Callable[[IDisplayPointer,  # pDispPointerStart
                           IDisplayPointer,  # pDispPointerEnd
                           IHTMLRenderStyle,  # pIRenderStyle
                           _Pointer[IHighlightSegment]],  # ppISegment
                          _type.HRESULT]
    MoveSegmentToPointers: _Callable[[IHighlightSegment,  # pISegment
                                      IDisplayPointer,  # pDispPointerStart
                                      IDisplayPointer],  # pDispPointerEnd
                                     _type.HRESULT]
    RemoveSegment: _Callable[[IHighlightSegment],  # pISegment
                             _type.HRESULT]


class ILineInfo(_Unknwnbase.IUnknown):
    get_x: _Callable[[_Pointer[_type.c_long]],  # p
                     _type.HRESULT]
    get_baseLine: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_textDescent: _Callable[[_Pointer[_type.c_long]],  # p
                               _type.HRESULT]
    get_textHeight: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_lineDirection: _Callable[[_Pointer[_type.LONG]],  # p
                                 _type.HRESULT]


class IDisplayPointer(_Unknwnbase.IUnknown):
    MoveToPoint: _Callable[[_struct.POINT,  # ptPoint
                            _enum.COORD_SYSTEM,  # eCoordSystem
                            IHTMLElement,  # pElementContext
                            _type.DWORD,  # dwHitTestOptions
                            _Pointer[_type.DWORD]],  # pdwHitTestResults
                           _type.HRESULT]
    MoveUnit: _Callable[[_enum.DISPLAY_MOVEUNIT,  # eMoveUnit
                         _type.LONG],  # lXPos
                        _type.HRESULT]
    PositionMarkupPointer: _Callable[[IMarkupPointer],  # pMarkupPointer
                                     _type.HRESULT]
    MoveToPointer: _Callable[[IDisplayPointer],  # pDispPointer
                             _type.HRESULT]
    SetPointerGravity: _Callable[[_enum.POINTER_GRAVITY],  # eGravity
                                 _type.HRESULT]
    GetPointerGravity: _Callable[[_Pointer[_enum.POINTER_GRAVITY]],  # peGravity
                                 _type.HRESULT]
    SetDisplayGravity: _Callable[[_enum.DISPLAY_GRAVITY],  # eGravity
                                 _type.HRESULT]
    GetDisplayGravity: _Callable[[_Pointer[_enum.DISPLAY_GRAVITY]],  # peGravity
                                 _type.HRESULT]
    IsPositioned: _Callable[[_Pointer[_type.BOOL]],  # pfPositioned
                            _type.HRESULT]
    Unposition: _Callable[[],
                          _type.HRESULT]
    IsEqualTo: _Callable[[IDisplayPointer,  # pDispPointer
                          _Pointer[_type.BOOL]],  # pfIsEqual
                         _type.HRESULT]
    IsLeftOf: _Callable[[IDisplayPointer,  # pDispPointer
                         _Pointer[_type.BOOL]],  # pfIsLeftOf
                        _type.HRESULT]
    IsRightOf: _Callable[[IDisplayPointer,  # pDispPointer
                          _Pointer[_type.BOOL]],  # pfIsRightOf
                         _type.HRESULT]
    IsAtBOL: _Callable[[_Pointer[_type.BOOL]],  # pfBOL
                       _type.HRESULT]
    MoveToMarkupPointer: _Callable[[IMarkupPointer,  # pPointer
                                    IDisplayPointer],  # pDispLineContext
                                   _type.HRESULT]
    ScrollIntoView: _Callable[[],
                              _type.HRESULT]
    GetLineInfo: _Callable[[_Pointer[ILineInfo]],  # ppLineInfo
                           _type.HRESULT]
    GetFlowElement: _Callable[[_Pointer[IHTMLElement]],  # ppLayoutElement
                              _type.HRESULT]
    QueryBreaks: _Callable[[_Pointer[_type.DWORD]],  # pdwBreaks
                           _type.HRESULT]


class IDisplayServices(_Unknwnbase.IUnknown):
    CreateDisplayPointer: _Callable[[_Pointer[IDisplayPointer]],  # ppDispPointer
                                    _type.HRESULT]
    TransformRect: _Callable[[_Pointer[_struct.RECT],  # pRect
                              _enum.COORD_SYSTEM,  # eSource
                              _enum.COORD_SYSTEM,  # eDestination
                              IHTMLElement],  # pIElement
                             _type.HRESULT]
    TransformPoint: _Callable[[_Pointer[_struct.POINT],  # pPoint
                               _enum.COORD_SYSTEM,  # eSource
                               _enum.COORD_SYSTEM,  # eDestination
                               IHTMLElement],  # pIElement
                              _type.HRESULT]
    GetCaret: _Callable[[_Pointer[IHTMLCaret]],  # ppCaret
                        _type.HRESULT]
    GetComputedStyle: _Callable[[IMarkupPointer,  # pPointer
                                 _Pointer[IHTMLComputedStyle]],  # ppComputedStyle
                                _type.HRESULT]
    ScrollRectIntoView: _Callable[[IHTMLElement,  # pIElement
                                   _struct.RECT],  # rect
                                  _type.HRESULT]
    HasFlowLayout: _Callable[[IHTMLElement,  # pIElement
                              _Pointer[_type.BOOL]],  # pfHasFlowLayout
                             _type.HRESULT]


class IHtmlDlgSafeHelper(_oaidl.IDispatch):
    choosecolordlg: _Callable[[_struct.VARIANT,  # initColor
                               _Pointer[_struct.VARIANT]],  # rgbColor
                              _type.HRESULT]
    getCharset: _Callable[[_type.BSTR,  # fontName
                           _Pointer[_struct.VARIANT]],  # charset
                          _type.HRESULT]
    get_Fonts: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                         _type.HRESULT]
    get_BlockFormats: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]


class IBlockFormats(_oaidl.IDispatch):
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    Item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_type.BSTR]],  # pbstrBlockFormat
                    _type.HRESULT]


class IFontNames(_oaidl.IDispatch):
    get__NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    get_Count: _Callable[[_Pointer[_type.c_long]],  # p
                         _type.HRESULT]
    Item: _Callable[[_Pointer[_struct.VARIANT],  # pvarIndex
                     _Pointer[_type.BSTR]],  # pbstrFontName
                    _type.HRESULT]


class ICSSFilter(_Unknwnbase.IUnknown):
    SetSite: _Callable[[ICSSFilterSite],  # pSink
                       _type.HRESULT]
    OnAmbientPropertyChange: _Callable[[_type.LONG],  # dispid
                                       _type.HRESULT]


class ISecureUrlHost(_Unknwnbase.IUnknown):
    ValidateSecureUrl: _Callable[[_Pointer[_type.BOOL],  # pfAllow
                                  _Pointer[_type.OLECHAR],  # pchUrlInQuestion
                                  _type.DWORD],  # dwFlags
                                 _type.HRESULT]


class IMarkupServices(_Unknwnbase.IUnknown):
    CreateMarkupPointer: _Callable[[_Pointer[IMarkupPointer]],  # ppPointer
                                   _type.HRESULT]
    CreateMarkupContainer: _Callable[[_Pointer[IMarkupContainer]],  # ppMarkupContainer
                                     _type.HRESULT]
    CreateElement: _Callable[[_enum.ELEMENT_TAG_ID,  # tagID
                              _Pointer[_type.OLECHAR],  # pchAttributes
                              _Pointer[IHTMLElement]],  # ppElement
                             _type.HRESULT]
    CloneElement: _Callable[[IHTMLElement,  # pElemCloneThis
                             _Pointer[IHTMLElement]],  # ppElementTheClone
                            _type.HRESULT]
    InsertElement: _Callable[[IHTMLElement,  # pElementInsert
                              IMarkupPointer,  # pPointerStart
                              IMarkupPointer],  # pPointerFinish
                             _type.HRESULT]
    RemoveElement: _Callable[[IHTMLElement],  # pElementRemove
                             _type.HRESULT]
    Remove: _Callable[[IMarkupPointer,  # pPointerStart
                       IMarkupPointer],  # pPointerFinish
                      _type.HRESULT]
    Copy: _Callable[[IMarkupPointer,  # pPointerSourceStart
                     IMarkupPointer,  # pPointerSourceFinish
                     IMarkupPointer],  # pPointerTarget
                    _type.HRESULT]
    Move: _Callable[[IMarkupPointer,  # pPointerSourceStart
                     IMarkupPointer,  # pPointerSourceFinish
                     IMarkupPointer],  # pPointerTarget
                    _type.HRESULT]
    InsertText: _Callable[[_Pointer[_type.OLECHAR],  # pchText
                           _type.c_long,  # cch
                           IMarkupPointer],  # pPointerTarget
                          _type.HRESULT]
    ParseString: _Callable[[_Pointer[_type.OLECHAR],  # pchHTML
                            _type.DWORD,  # dwFlags
                            _Pointer[IMarkupContainer],  # ppContainerResult
                            IMarkupPointer,  # ppPointerStart
                            IMarkupPointer],  # ppPointerFinish
                           _type.HRESULT]
    ParseGlobal: _Callable[[_type.HGLOBAL,  # hglobalHTML
                            _type.DWORD,  # dwFlags
                            _Pointer[IMarkupContainer],  # ppContainerResult
                            IMarkupPointer,  # pPointerStart
                            IMarkupPointer],  # pPointerFinish
                           _type.HRESULT]
    IsScopedElement: _Callable[[IHTMLElement,  # pElement
                                _Pointer[_type.BOOL]],  # pfScoped
                               _type.HRESULT]
    GetElementTagId: _Callable[[IHTMLElement,  # pElement
                                _Pointer[_enum.ELEMENT_TAG_ID]],  # ptagId
                               _type.HRESULT]
    GetTagIDForName: _Callable[[_type.BSTR,  # bstrName
                                _Pointer[_enum.ELEMENT_TAG_ID]],  # ptagId
                               _type.HRESULT]
    GetNameForTagID: _Callable[[_enum.ELEMENT_TAG_ID,  # tagId
                                _Pointer[_type.BSTR]],  # pbstrName
                               _type.HRESULT]
    MovePointersToRange: _Callable[[IHTMLTxtRange,  # pIRange
                                    IMarkupPointer,  # pPointerStart
                                    IMarkupPointer],  # pPointerFinish
                                   _type.HRESULT]
    MoveRangeToPointers: _Callable[[IMarkupPointer,  # pPointerStart
                                    IMarkupPointer,  # pPointerFinish
                                    IHTMLTxtRange],  # pIRange
                                   _type.HRESULT]
    BeginUndoUnit: _Callable[[_Pointer[_type.OLECHAR]],  # pchTitle
                             _type.HRESULT]
    EndUndoUnit: _Callable[[],
                           _type.HRESULT]


class IMarkupServices2(IMarkupServices):
    ParseGlobalEx: _Callable[[_type.HGLOBAL,  # hglobalHTML
                              _type.DWORD,  # dwFlags
                              IMarkupContainer,  # pContext
                              _Pointer[IMarkupContainer],  # ppContainerResult
                              IMarkupPointer,  # pPointerStart
                              IMarkupPointer],  # pPointerFinish
                             _type.HRESULT]
    ValidateElements: _Callable[[IMarkupPointer,  # pPointerStart
                                 IMarkupPointer,  # pPointerFinish
                                 IMarkupPointer,  # pPointerTarget
                                 IMarkupPointer,  # pPointerStatus
                                 _Pointer[IHTMLElement],  # ppElemFailBottom
                                 _Pointer[IHTMLElement]],  # ppElemFailTop
                                _type.HRESULT]
    SaveSegmentsToClipboard: _Callable[[ISegmentList,  # pSegmentList
                                        _type.DWORD],  # dwFlags
                                       _type.HRESULT]


class IHTMLChangePlayback(_Unknwnbase.IUnknown):
    ExecChange: _Callable[[_Pointer[_type.BYTE],  # pbRecord
                           _type.BOOL],  # fForward
                          _type.HRESULT]


class IMarkupPointer2(IMarkupPointer):
    IsAtWordBreak: _Callable[[_Pointer[_type.BOOL]],  # pfAtBreak
                             _type.HRESULT]
    GetMarkupPosition: _Callable[[_Pointer[_type.c_long]],  # plMP
                                 _type.HRESULT]
    MoveToMarkupPosition: _Callable[[IMarkupContainer,  # pContainer
                                     _type.c_long],  # lMP
                                    _type.HRESULT]
    MoveUnitBounded: _Callable[[_enum.MOVEUNIT_ACTION,  # muAction
                                IMarkupPointer],  # pIBoundary
                               _type.HRESULT]
    IsInsideURL: _Callable[[IMarkupPointer,  # pRight
                            _Pointer[_type.BOOL]],  # pfResult
                           _type.HRESULT]
    MoveToContent: _Callable[[IHTMLElement,  # pIElement
                              _type.BOOL],  # fAtStart
                             _type.HRESULT]


class IMarkupTextFrags(_Unknwnbase.IUnknown):
    GetTextFragCount: _Callable[[_Pointer[_type.c_long]],  # pcFrags
                                _type.HRESULT]
    GetTextFrag: _Callable[[_type.c_long,  # iFrag
                            _Pointer[_type.BSTR],  # pbstrFrag
                            IMarkupPointer],  # pPointerFrag
                           _type.HRESULT]
    RemoveTextFrag: _Callable[[_type.c_long],  # iFrag
                              _type.HRESULT]
    InsertTextFrag: _Callable[[_type.c_long,  # iFrag
                               _type.BSTR,  # bstrInsert
                               IMarkupPointer],  # pPointerInsert
                              _type.HRESULT]
    FindTextFragFromMarkupPointer: _Callable[[IMarkupPointer,  # pPointerFind
                                              _Pointer[_type.c_long],  # piFrag
                                              _Pointer[_type.BOOL]],  # pfFragFound
                                             _type.HRESULT]


class IXMLGenericParse(_Unknwnbase.IUnknown):
    SetGenericParse: _Callable[[_type.VARIANT_BOOL],  # fDoGeneric
                               _type.HRESULT]


class IHTMLEditHost(_Unknwnbase.IUnknown):
    SnapRect: _Callable[[IHTMLElement,  # pIElement
                         _Pointer[_struct.RECT],  # prcNew
                         _enum.ELEMENT_CORNER],  # eHandle
                        _type.HRESULT]


class IHTMLEditHost2(IHTMLEditHost):
    PreDrag: _Callable[[],
                       _type.HRESULT]


class ISequenceNumber(_Unknwnbase.IUnknown):
    GetSequenceNumber: _Callable[[_type.c_long,  # nCurrent
                                  _Pointer[_type.c_long]],  # pnNew
                                 _type.HRESULT]


class IIMEServices(_Unknwnbase.IUnknown):
    GetActiveIMM: _Callable[[_Pointer[_Dimm.IActiveIMMApp]],  # ppActiveIMM
                            _type.HRESULT]


class ISelectionServicesListener(_Unknwnbase.IUnknown):
    BeginSelectionUndo: _Callable[[],
                                  _type.HRESULT]
    EndSelectionUndo: _Callable[[],
                                _type.HRESULT]
    OnSelectedElementExit: _Callable[[IMarkupPointer,  # pIElementStart
                                      IMarkupPointer,  # pIElementEnd
                                      IMarkupPointer,  # pIElementContentStart
                                      IMarkupPointer],  # pIElementContentEnd
                                     _type.HRESULT]
    OnChangeType: _Callable[[_enum.SELECTION_TYPE,  # eType
                             ISelectionServicesListener],  # pIListener
                            _type.HRESULT]
    GetTypeDetail: _Callable[[_Pointer[_type.BSTR]],  # pTypeDetail
                             _type.HRESULT]


class ISelectionServices(_Unknwnbase.IUnknown):
    SetSelectionType: _Callable[[_enum.SELECTION_TYPE,  # eType
                                 ISelectionServicesListener],  # pIListener
                                _type.HRESULT]
    GetMarkupContainer: _Callable[[_Pointer[IMarkupContainer]],  # ppIContainer
                                  _type.HRESULT]
    AddSegment: _Callable[[IMarkupPointer,  # pIStart
                           IMarkupPointer,  # pIEnd
                           _Pointer[ISegment]],  # ppISegmentAdded
                          _type.HRESULT]
    AddElementSegment: _Callable[[IHTMLElement,  # pIElement
                                  _Pointer[IElementSegment]],  # ppISegmentAdded
                                 _type.HRESULT]
    RemoveSegment: _Callable[[ISegment],  # pISegment
                             _type.HRESULT]
    GetSelectionServicesListener: _Callable[[_Pointer[ISelectionServicesListener]],  # ppISelectionServicesListener
                                            _type.HRESULT]


class IHTMLEditDesigner(_Unknwnbase.IUnknown):
    PreHandleEvent: _Callable[[_type.DISPID,  # inEvtDispId
                               IHTMLEventObj],  # pIEventObj
                              _type.HRESULT]
    PostHandleEvent: _Callable[[_type.DISPID,  # inEvtDispId
                                IHTMLEventObj],  # pIEventObj
                               _type.HRESULT]
    TranslateAcceleratorA: _Callable[[_type.DISPID,  # inEvtDispId
                                      IHTMLEventObj],  # pIEventObj
                                     _type.HRESULT]
    PostEditorEventNotify: _Callable[[_type.DISPID,  # inEvtDispId
                                      IHTMLEventObj],  # pIEventObj
                                     _type.HRESULT]


class IHTMLEditServices(_Unknwnbase.IUnknown):
    AddDesigner: _Callable[[IHTMLEditDesigner],  # pIDesigner
                           _type.HRESULT]
    RemoveDesigner: _Callable[[IHTMLEditDesigner],  # pIDesigner
                              _type.HRESULT]
    GetSelectionServices: _Callable[[IMarkupContainer,  # pIContainer
                                     _Pointer[ISelectionServices]],  # ppSelSvc
                                    _type.HRESULT]
    MoveToSelectionAnchor: _Callable[[IMarkupPointer],  # pIStartAnchor
                                     _type.HRESULT]
    MoveToSelectionEnd: _Callable[[IMarkupPointer],  # pIEndAnchor
                                  _type.HRESULT]
    SelectRange: _Callable[[IMarkupPointer,  # pStart
                            IMarkupPointer,  # pEnd
                            _enum.SELECTION_TYPE],  # eType
                           _type.HRESULT]


class IHTMLEditServices2(IHTMLEditServices):
    MoveToSelectionAnchorEx: _Callable[[IDisplayPointer],  # pIStartAnchor
                                       _type.HRESULT]
    MoveToSelectionEndEx: _Callable[[IDisplayPointer],  # pIEndAnchor
                                    _type.HRESULT]
    FreezeVirtualCaretPos: _Callable[[_type.BOOL],  # fReCompute
                                     _type.HRESULT]
    UnFreezeVirtualCaretPos: _Callable[[_type.BOOL],  # fReset
                                       _type.HRESULT]


class IHTMLComputedStyle(_Unknwnbase.IUnknown):
    get_bold: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                        _type.HRESULT]
    get_italic: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]
    get_underline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_overline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                            _type.HRESULT]
    get_strikeOut: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_subScript: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_superScript: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                               _type.HRESULT]
    get_explicitFace: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    get_fontWeight: _Callable[[_Pointer[_type.c_long]],  # p
                              _type.HRESULT]
    get_fontSize: _Callable[[_Pointer[_type.c_long]],  # p
                            _type.HRESULT]
    get_fontName: _Callable[[_Pointer[_type.TCHAR]],  # p
                            _type.HRESULT]
    get_hasBgColor: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                              _type.HRESULT]
    get_textColor: _Callable[[_Pointer[_type.DWORD]],  # p
                             _type.HRESULT]
    get_backgroundColor: _Callable[[_Pointer[_type.DWORD]],  # p
                                   _type.HRESULT]
    get_preFormatted: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                _type.HRESULT]
    get_direction: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                             _type.HRESULT]
    get_blockDirection: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                                  _type.HRESULT]
    get_OL: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                      _type.HRESULT]
    IsEqual: _Callable[[IHTMLComputedStyle,  # pComputedStyle
                        _Pointer[_type.VARIANT_BOOL]],  # pfEqual
                       _type.HRESULT]


class IDeveloperConsoleMessageReceiver(_Unknwnbase.IUnknown):
    Write: _Callable[[_type.LPCWSTR,  # source
                      _enum.DEV_CONSOLE_MESSAGE_LEVEL,  # level
                      _type.c_int,  # messageId
                      _type.LPCWSTR],  # messageText
                     _type.HRESULT]
    WriteWithUrl: _Callable[[_type.LPCWSTR,  # source
                             _enum.DEV_CONSOLE_MESSAGE_LEVEL,  # level
                             _type.c_int,  # messageId
                             _type.LPCWSTR,  # messageText
                             _type.LPCWSTR],  # fileUrl
                            _type.HRESULT]
    WriteWithUrlAndLine: _Callable[[_type.LPCWSTR,  # source
                                    _enum.DEV_CONSOLE_MESSAGE_LEVEL,  # level
                                    _type.c_int,  # messageId
                                    _type.LPCWSTR,  # messageText
                                    _type.LPCWSTR,  # fileUrl
                                    _type.ULONG],  # line
                                   _type.HRESULT]
    WriteWithUrlLineAndColumn: _Callable[[_type.LPCWSTR,  # source
                                          _enum.DEV_CONSOLE_MESSAGE_LEVEL,  # level
                                          _type.c_int,  # messageId
                                          _type.LPCWSTR,  # messageText
                                          _type.LPCWSTR,  # fileUrl
                                          _type.ULONG,  # line
                                          _type.ULONG],  # column
                                         _type.HRESULT]


class IScriptEventHandler(_Unknwnbase.IUnknown):
    FunctionName: _Callable[[_Pointer[_type.BSTR]],  # pbstrFunctionName
                            _type.HRESULT]
    DebugDocumentContext: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppDebugDocumentContext
                                    _type.HRESULT]
    EventHandlerDispatch: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDispHandler
                                    _type.HRESULT]
    UsesCapture: _Callable[[_Pointer[_type.BOOL]],  # pfUsesCapture
                           _type.HRESULT]
    Cookie: _Callable[[_Pointer[_type.ULONGLONG]],  # pullCookie
                      _type.HRESULT]


class IDebugCallbackNotificationHandler(_Unknwnbase.IUnknown):
    RequestedCallbackTypes: _Callable[[_Pointer[_type.DWORD]],  # pCallbackMask
                                      _type.HRESULT]
    BeforeDispatchEvent: _Callable[[_Unknwnbase.IUnknown],  # pEvent
                                   _type.HRESULT]
    DispatchEventComplete: _Callable[[_Unknwnbase.IUnknown,  # pEvent
                                      _type.DWORD],  # propagationStatus
                                     _type.HRESULT]
    BeforeInvokeDomCallback: _Callable[[_Unknwnbase.IUnknown,  # pEvent
                                        IScriptEventHandler,  # pCallback
                                        _enum.DOM_EVENT_PHASE,  # eStage
                                        _type.DWORD],  # propagationStatus
                                       _type.HRESULT]
    InvokeDomCallbackComplete: _Callable[[_Unknwnbase.IUnknown,  # pEvent
                                          IScriptEventHandler,  # pCallback
                                          _enum.DOM_EVENT_PHASE,  # eStage
                                          _type.DWORD],  # propagationStatus
                                         _type.HRESULT]
    BeforeInvokeCallback: _Callable[[_enum.SCRIPT_TIMER_TYPE,  # eCallbackType
                                     _type.DWORD,  # callbackCookie
                                     _oaidl.IDispatch,  # pDispHandler
                                     _type.ULONGLONG,  # ullHandlerCookie
                                     _type.BSTR,  # functionName
                                     _type.UINT32,  # line
                                     _type.UINT32,  # column
                                     _type.UINT32,  # cchLength
                                     _Unknwnbase.IUnknown],  # pDebugDocumentContext
                                    _type.HRESULT]
    InvokeCallbackComplete: _Callable[[_enum.SCRIPT_TIMER_TYPE,  # eCallbackType
                                       _type.DWORD,  # callbackCookie
                                       _oaidl.IDispatch,  # pDispHandler
                                       _type.ULONGLONG,  # ullHandlerCookie
                                       _type.BSTR,  # functionName
                                       _type.UINT32,  # line
                                       _type.UINT32,  # column
                                       _type.UINT32,  # cchLength
                                       _Unknwnbase.IUnknown],  # pDebugDocumentContext
                                      _type.HRESULT]


class IScriptEventHandlerSourceInfo(_Unknwnbase.IUnknown):
    GetSourceInfo: _Callable[[_Pointer[_type.BSTR],  # pbstrFunctionName
                              _Pointer[_type.UINT32],  # line
                              _Pointer[_type.UINT32],  # column
                              _Pointer[_type.UINT32]],  # cchLength
                             _type.HRESULT]


class IDOMEventRegistrationCallback(_Unknwnbase.IUnknown):
    OnDOMEventListenerAdded: _Callable[[_type.LPCWSTR,  # pszEventType
                                        IScriptEventHandler],  # pHandler
                                       _type.HRESULT]
    OnDOMEventListenerRemoved: _Callable[[_type.ULONGLONG],  # ullCookie
                                         _type.HRESULT]


class IEventTarget2(_Unknwnbase.IUnknown):
    GetRegisteredEventTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # ppEventTypeArray
                                       _type.HRESULT]
    GetListenersForType: _Callable[[_type.LPCWSTR,  # pszEventType
                                    _Pointer[_Pointer[_struct.SAFEARRAY]]],  # ppEventHandlerArray
                                   _type.HRESULT]
    RegisterForDOMEventListeners: _Callable[[IDOMEventRegistrationCallback],  # pCallback
                                            _type.HRESULT]
    UnregisterForDOMEventListeners: _Callable[[IDOMEventRegistrationCallback],  # pCallback
                                              _type.HRESULT]


class HTMLNamespaceEvents(_oaidl.IDispatch):
    pass


class IHTMLNamespace(_oaidl.IDispatch):
    get_name: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    get_urn: _Callable[[_Pointer[_type.BSTR]],  # p
                       _type.HRESULT]
    get_tagNames: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_readyState: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_onreadystatechange: _Callable[[_struct.VARIANT],  # v
                                      _type.HRESULT]
    get_onreadystatechange: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                      _type.HRESULT]
    doImport: _Callable[[_type.BSTR],  # bstrImplementationUrl
                        _type.HRESULT]
    attachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch,  # pDisp
                            _Pointer[_type.VARIANT_BOOL]],  # pfResult
                           _type.HRESULT]
    detachEvent: _Callable[[_type.BSTR,  # event
                            _oaidl.IDispatch],  # pDisp
                           _type.HRESULT]


class IHTMLNamespaceCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    item: _Callable[[_struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # ppNamespace
                    _type.HRESULT]
    add: _Callable[[_type.BSTR,  # bstrNamespace
                    _type.BSTR,  # bstrUrn
                    _struct.VARIANT,  # implementationUrl
                    _Pointer[_oaidl.IDispatch]],  # ppNamespace
                   _type.HRESULT]


class DispHTMLNamespace(_oaidl.IDispatch):
    pass


class DispHTMLNamespaceCollection(_oaidl.IDispatch):
    pass


class IHTMLPainter(_Unknwnbase.IUnknown):
    Draw: _Callable[[_struct.RECT,  # rcBounds
                     _struct.RECT,  # rcUpdate
                     _type.LONG,  # lDrawFlags
                     _type.HDC,  # hdc
                     _type.LPVOID],  # pvDrawObject
                    _type.HRESULT]
    OnResize: _Callable[[_struct.SIZE],  # size
                        _type.HRESULT]
    GetPainterInfo: _Callable[[_Pointer[_struct.HTML_PAINTER_INFO]],  # pInfo
                              _type.HRESULT]
    HitTestPoint: _Callable[[_struct.POINT,  # pt
                             _Pointer[_type.BOOL],  # pbHit
                             _Pointer[_type.LONG]],  # plPartID
                            _type.HRESULT]


class IHTMLPaintSite(_Unknwnbase.IUnknown):
    InvalidatePainterInfo: _Callable[[],
                                     _type.HRESULT]
    InvalidateRect: _Callable[[_Pointer[_struct.RECT]],  # prcInvalid
                              _type.HRESULT]
    InvalidateRegion: _Callable[[_type.HRGN],  # rgnInvalid
                                _type.HRESULT]
    GetDrawInfo: _Callable[[_type.LONG,  # lFlags
                            _Pointer[_struct.HTML_PAINT_DRAW_INFO]],  # pDrawInfo
                           _type.HRESULT]
    TransformGlobalToLocal: _Callable[[_struct.POINT,  # ptGlobal
                                       _Pointer[_struct.POINT]],  # pptLocal
                                      _type.HRESULT]
    TransformLocalToGlobal: _Callable[[_struct.POINT,  # ptLocal
                                       _Pointer[_struct.POINT]],  # pptGlobal
                                      _type.HRESULT]
    GetHitTestCookie: _Callable[[_Pointer[_type.LONG]],  # plCookie
                                _type.HRESULT]


class IHTMLPainterEventInfo(_Unknwnbase.IUnknown):
    GetEventInfoFlags: _Callable[[_Pointer[_type.c_long]],  # plEventInfoFlags
                                 _type.HRESULT]
    GetEventTarget: _Callable[[_Pointer[IHTMLElement]],  # ppElement
                              _type.HRESULT]
    SetCursor: _Callable[[_type.LONG],  # lPartID
                         _type.HRESULT]
    StringFromPartID: _Callable[[_type.LONG,  # lPartID
                                 _Pointer[_type.BSTR]],  # pbstrPart
                                _type.HRESULT]


class IHTMLPainterOverlay(_Unknwnbase.IUnknown):
    OnMove: _Callable[[_struct.RECT],  # rcDevice
                      _type.HRESULT]


class IHTMLIPrintCollection(_oaidl.IDispatch):
    get_length: _Callable[[_Pointer[_type.c_long]],  # p
                          _type.HRESULT]
    get__newEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]
    item: _Callable[[_type.c_long,  # index
                     _Pointer[_Unknwnbase.IUnknown]],  # ppIPrint
                    _type.HRESULT]


class IEnumPrivacyRecords(_Unknwnbase.IUnknown):
    Reset: _Callable[[],
                     _type.HRESULT]
    GetSize: _Callable[[_Pointer[_type.ULONG]],  # pSize
                       _type.HRESULT]
    GetPrivacyImpacted: _Callable[[_Pointer[_type.BOOL]],  # pState
                                  _type.HRESULT]
    Next: _Callable[[_Pointer[_type.BSTR],  # pbstrUrl
                     _Pointer[_type.BSTR],  # pbstrPolicyRef
                     _Pointer[_type.LONG],  # pdwReserved
                     _Pointer[_type.DWORD]],  # pdwPrivacyFlags
                    _type.HRESULT]


class IWPCBlockedUrls(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.DWORD]],  # pdwCount
                        _type.HRESULT]
    GetUrl: _Callable[[_type.DWORD,  # dwIdx
                       _Pointer[_type.BSTR]],  # pbstrUrl
                      _type.HRESULT]


class IHTMLDOMConstructorCollection(_oaidl.IDispatch):
    get_Attr: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                        _type.HRESULT]
    get_BehaviorUrnsCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                          _type.HRESULT]
    get_BookmarkCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_CompatibleInfo: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_CompatibleInfoCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                            _type.HRESULT]
    get_ControlRangeCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                          _type.HRESULT]
    get_CSSCurrentStyleDeclaration: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                              _type.HRESULT]
    get_CSSRuleList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                               _type.HRESULT]
    get_CSSRuleStyleDeclaration: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                           _type.HRESULT]
    get_CSSStyleDeclaration: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_CSSStyleRule: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]
    get_CSSStyleSheet: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_DataTransfer: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]
    get_DOMImplementation: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_Element: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                           _type.HRESULT]
    get_Event: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                         _type.HRESULT]
    get_History: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                           _type.HRESULT]
    get_HTCElementBehaviorDefaults: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                              _type.HRESULT]
    get_HTMLAnchorElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLAreaElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLAreasCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLBaseElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLBaseFontElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLBGSoundElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLBlockElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLBodyElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLBRElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_HTMLButtonElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_HTMLCommentElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLDDElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_HTMLDivElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_HTMLDocument: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]
    get_HTMLDListElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLDTElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_HTMLEmbedElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLFieldSetElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLFontElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLFormElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLFrameElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLFrameSetElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLGenericElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLHeadElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLHeadingElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLHRElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_HTMLHtmlElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLIFrameElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLImageElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLInputElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLIsIndexElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLLabelElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLLegendElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLLIElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_HTMLLinkElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLMapElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_HTMLMarqueeElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLMetaElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLModelessDialog: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_HTMLNamespaceInfo: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLNamespaceInfoCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                               _type.HRESULT]
    get_HTMLNextIdElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLNoShowElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLObjectElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLOListElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLOptionElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLParagraphElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                        _type.HRESULT]
    get_HTMLParamElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLPhraseElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLPluginsCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                         _type.HRESULT]
    get_HTMLPopup: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_HTMLScriptElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLSelectElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_HTMLSpanElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLStyleElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLTableCaptionElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                           _type.HRESULT]
    get_HTMLTableCellElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                        _type.HRESULT]
    get_HTMLTableColElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLTableElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLTableRowElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLTableSectionElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                           _type.HRESULT]
    get_HTMLTextAreaElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_HTMLTextElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                   _type.HRESULT]
    get_HTMLTitleElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLUListElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                    _type.HRESULT]
    get_HTMLUnknownElement: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_Image: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                         _type.HRESULT]
    get_Location: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_NamedNodeMap: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                _type.HRESULT]
    get_Navigator: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_NodeList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                            _type.HRESULT]
    get_Option: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_Screen: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_Selection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_StaticNodeList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_Storage: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                           _type.HRESULT]
    get_StyleSheetList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_StyleSheetPage: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_StyleSheetPageList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                      _type.HRESULT]
    get_Text: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                        _type.HRESULT]
    get_TextRange: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                             _type.HRESULT]
    get_TextRangeCollection: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                       _type.HRESULT]
    get_TextRectangle: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                 _type.HRESULT]
    get_TextRectangleList: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                     _type.HRESULT]
    get_Window: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                          _type.HRESULT]
    get_XDomainRequest: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]
    get_XMLHttpRequest: _Callable[[_Pointer[_oaidl.IDispatch]],  # p
                                  _type.HRESULT]


class IHTMLDialog(_oaidl.IDispatch):
    put_dialogTop: _Callable[[_struct.VARIANT],  # v
                             _type.HRESULT]
    get_dialogTop: _Callable[[_Pointer[_struct.VARIANT]],  # p
                             _type.HRESULT]
    put_dialogLeft: _Callable[[_struct.VARIANT],  # v
                              _type.HRESULT]
    get_dialogLeft: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    put_dialogWidth: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_dialogWidth: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    put_dialogHeight: _Callable[[_struct.VARIANT],  # v
                                _type.HRESULT]
    get_dialogHeight: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_dialogArguments: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                   _type.HRESULT]
    get_menuArguments: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                 _type.HRESULT]
    put_returnValue: _Callable[[_struct.VARIANT],  # v
                               _type.HRESULT]
    get_returnValue: _Callable[[_Pointer[_struct.VARIANT]],  # p
                               _type.HRESULT]
    close: _Callable[[],
                     _type.HRESULT]
    toString: _Callable[[_Pointer[_type.BSTR]],  # String
                        _type.HRESULT]


class IHTMLDialog2(_oaidl.IDispatch):
    put_status: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_status: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_resizable: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_resizable: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class IHTMLDialog3(_oaidl.IDispatch):
    put_unadorned: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_unadorned: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]
    put_dialogHide: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_dialogHide: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]


class IHTMLModelessInit(_oaidl.IDispatch):
    get_parameters: _Callable[[_Pointer[_struct.VARIANT]],  # p
                              _type.HRESULT]
    get_optionString: _Callable[[_Pointer[_struct.VARIANT]],  # p
                                _type.HRESULT]
    get_moniker: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                           _type.HRESULT]
    get_document: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # p
                            _type.HRESULT]


class IHTMLPopup(_oaidl.IDispatch):
    show: _Callable[[_type.c_long,  # x
                     _type.c_long,  # y
                     _type.c_long,  # w
                     _type.c_long,  # h
                     _Pointer[_struct.VARIANT]],  # pElement
                    _type.HRESULT]
    hide: _Callable[[],
                    _type.HRESULT]
    get_document: _Callable[[_Pointer[IHTMLDocument]],  # p
                            _type.HRESULT]
    get_isOpen: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # p
                          _type.HRESULT]


class DispHTMLPopup(_oaidl.IDispatch):
    pass


class IHTMLAppBehavior(_oaidl.IDispatch):
    put_applicationName: _Callable[[_type.BSTR],  # v
                                   _type.HRESULT]
    get_applicationName: _Callable[[_Pointer[_type.BSTR]],  # p
                                   _type.HRESULT]
    put_version: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_version: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_icon: _Callable[[_type.BSTR],  # v
                        _type.HRESULT]
    get_icon: _Callable[[_Pointer[_type.BSTR]],  # p
                        _type.HRESULT]
    put_singleInstance: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_singleInstance: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_minimizeButton: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_minimizeButton: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_maximizeButton: _Callable[[_type.BSTR],  # v
                                  _type.HRESULT]
    get_maximizeButton: _Callable[[_Pointer[_type.BSTR]],  # p
                                  _type.HRESULT]
    put_border: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_border: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_borderStyle: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_borderStyle: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_sysMenu: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_sysMenu: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_caption: _Callable[[_type.BSTR],  # v
                           _type.HRESULT]
    get_caption: _Callable[[_Pointer[_type.BSTR]],  # p
                           _type.HRESULT]
    put_windowState: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_windowState: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_showInTaskBar: _Callable[[_type.BSTR],  # v
                                 _type.HRESULT]
    get_showInTaskBar: _Callable[[_Pointer[_type.BSTR]],  # p
                                 _type.HRESULT]
    get_commandLine: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]


class IHTMLAppBehavior2(_oaidl.IDispatch):
    put_contextMenu: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_contextMenu: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_innerBorder: _Callable[[_type.BSTR],  # v
                               _type.HRESULT]
    get_innerBorder: _Callable[[_Pointer[_type.BSTR]],  # p
                               _type.HRESULT]
    put_scroll: _Callable[[_type.BSTR],  # v
                          _type.HRESULT]
    get_scroll: _Callable[[_Pointer[_type.BSTR]],  # p
                          _type.HRESULT]
    put_scrollFlat: _Callable[[_type.BSTR],  # v
                              _type.HRESULT]
    get_scrollFlat: _Callable[[_Pointer[_type.BSTR]],  # p
                              _type.HRESULT]
    put_selection: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_selection: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class IHTMLAppBehavior3(_oaidl.IDispatch):
    put_navigable: _Callable[[_type.BSTR],  # v
                             _type.HRESULT]
    get_navigable: _Callable[[_Pointer[_type.BSTR]],  # p
                             _type.HRESULT]


class DispHTMLAppBehavior(_oaidl.IDispatch):
    pass


class DispIHTMLInputButtonElement(_oaidl.IDispatch):
    pass


class DispIHTMLInputTextElement(_oaidl.IDispatch):
    pass


class DispIHTMLInputFileElement(_oaidl.IDispatch):
    pass


class DispIHTMLOptionButtonElement(_oaidl.IDispatch):
    pass


class DispIHTMLInputImage(_oaidl.IDispatch):
    pass


class IElementNamespace(_Unknwnbase.IUnknown):
    AddTag: _Callable[[_type.BSTR,  # bstrTagName
                       _type.LONG],  # lFlags
                      _type.HRESULT]


class IElementNamespaceTable(_Unknwnbase.IUnknown):
    AddNamespace: _Callable[[_type.BSTR,  # bstrNamespace
                             _type.BSTR,  # bstrUrn
                             _type.LONG,  # lFlags
                             _Pointer[_struct.VARIANT]],  # pvarFactory
                            _type.HRESULT]


class IElementNamespaceFactory(_Unknwnbase.IUnknown):
    Create: _Callable[[IElementNamespace],  # pNamespace
                      _type.HRESULT]


class IElementNamespaceFactory2(IElementNamespaceFactory):
    CreateWithImplementation: _Callable[[IElementNamespace,  # pNamespace
                                         _type.BSTR],  # bstrImplementation
                                        _type.HRESULT]


class IElementNamespaceFactoryCallback(_Unknwnbase.IUnknown):
    Resolve: _Callable[[_type.BSTR,  # bstrNamespace
                        _type.BSTR,  # bstrTagName
                        _type.BSTR,  # bstrAttrs
                        IElementNamespace],  # pNamespace
                       _type.HRESULT]


class IElementBehaviorSiteOM2(IElementBehaviorSiteOM):
    GetDefaults: _Callable[[_Pointer[IHTMLElementDefaults]],  # ppDefaults
                           _type.HRESULT]


class IElementBehaviorCategory(_Unknwnbase.IUnknown):
    GetCategory: _Callable[[_Pointer[_type.LPOLESTR]],  # ppchCategory
                           _type.HRESULT]


class IElementBehaviorSiteCategory(_Unknwnbase.IUnknown):
    GetRelatedBehaviors: _Callable[[_type.LONG,  # lDirection
                                    _type.LPOLESTR,  # pchCategory
                                    _Pointer[_objidlbase.IEnumUnknown]],  # ppEnumerator
                                   _type.HRESULT]


class IElementBehaviorSubmit(_Unknwnbase.IUnknown):
    GetSubmitInfo: _Callable[[IHTMLSubmitData],  # pSubmitData
                             _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IElementBehaviorFocus(_Unknwnbase.IUnknown):
    GetFocusRect: _Callable[[_Pointer[_struct.RECT]],  # pRect
                            _type.HRESULT]


class IElementBehaviorLayout(_Unknwnbase.IUnknown):
    GetSize: _Callable[[_type.LONG,  # dwFlags
                        _struct.SIZE,  # sizeContent
                        _Pointer[_struct.POINT],  # pptTranslateBy
                        _Pointer[_struct.POINT],  # pptTopLeft
                        _Pointer[_struct.SIZE]],  # psizeProposed
                       _type.HRESULT]
    GetLayoutInfo: _Callable[[_Pointer[_type.LONG]],  # plLayoutInfo
                             _type.HRESULT]
    GetPosition: _Callable[[_type.LONG,  # lFlags
                            _Pointer[_struct.POINT]],  # pptTopLeft
                           _type.HRESULT]
    MapSize: _Callable[[_Pointer[_struct.SIZE],  # psizeIn
                        _Pointer[_struct.RECT]],  # prcOut
                       _type.HRESULT]


class IElementBehaviorLayout2(_Unknwnbase.IUnknown):
    GetTextDescent: _Callable[[_Pointer[_type.LONG]],  # plDescent
                              _type.HRESULT]


class IElementBehaviorSiteLayout(_Unknwnbase.IUnknown):
    InvalidateLayoutInfo: _Callable[[],
                                    _type.HRESULT]
    InvalidateSize: _Callable[[],
                              _type.HRESULT]
    GetMediaResolution: _Callable[[_Pointer[_struct.SIZE]],  # psizeResolution
                                  _type.HRESULT]


class IElementBehaviorSiteLayout2(_Unknwnbase.IUnknown):
    GetFontInfo: _Callable[[_Pointer[_struct.LOGFONTW]],  # plf
                           _type.HRESULT]


class IHostBehaviorInit(_Unknwnbase.IUnknown):
    PopulateNamespaceTable: _Callable[[],
                                      _type.HRESULT]


class ISurfacePresenter(_Unknwnbase.IUnknown):
    Present: _Callable[[_type.UINT,  # uBuffer
                        _Pointer[_struct.RECT]],  # pDirty
                       _type.HRESULT]
    GetBuffer: _Callable[[_type.UINT,  # backBufferIndex
                          _Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppBuffer
                         _type.HRESULT]
    IsCurrent: _Callable[[_Pointer[_type.BOOL]],  # pIsCurrent
                         _type.HRESULT]


class IViewObjectPresentSite(_Unknwnbase.IUnknown):
    CreateSurfacePresenter: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                       _type.UINT,  # width
                                       _type.UINT,  # height
                                       _type.UINT,  # backBufferCount
                                       _enum.DXGI_FORMAT,  # format
                                       _enum.VIEW_OBJECT_ALPHA_MODE,  # mode
                                       _Pointer[ISurfacePresenter]],  # ppQueue
                                      _type.HRESULT]
    IsHardwareComposition: _Callable[[_Pointer[_type.BOOL]],  # pIsHardwareComposition
                                     _type.HRESULT]
    SetCompositionMode: _Callable[[_enum.VIEW_OBJECT_COMPOSITION_MODE],  # mode
                                  _type.HRESULT]


class ICanvasPixelArrayData(_Unknwnbase.IUnknown):
    GetBufferPointer: _Callable[[_Pointer[_Pointer[_type.BYTE]],  # ppBuffer
                                 _Pointer[_type.ULONG]],  # pBufferLength
                                _type.HRESULT]


class IViewObjectPrint(_Unknwnbase.IUnknown):
    GetPrintBitmap: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppPrintBitmap
                              _type.HRESULT]


class IViewObjectPresentNotifySite(IViewObjectPresentSite):
    RequestFrame: _Callable[[],
                            _type.HRESULT]


class IViewObjectPresentNotify(_Unknwnbase.IUnknown):
    OnPreRender: _Callable[[],
                           _type.HRESULT]


class ITrackingProtection(_Unknwnbase.IUnknown):
    EvaluateUrl: _Callable[[_type.BSTR,  # bstrUrl
                            _Pointer[_type.BOOL]],  # pfAllowed
                           _type.HRESULT]
    GetEnabled: _Callable[[_Pointer[_type.BOOL]],  # pfEnabled
                          _type.HRESULT]


class IBFCacheable(_Unknwnbase.IUnknown):
    EnterBFCache: _Callable[[],
                            _type.HRESULT]
    ExitBFCache: _Callable[[],
                           _type.HRESULT]
