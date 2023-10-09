from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IWidgetActionInvokedArgs(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_CustomState: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IWidgetAnalyticsInfoReportedArgs(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]
    get_AnalyticsJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IWidgetContext(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DefinitionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Size: _Callable[[_Pointer[_enum.Microsoft.Windows.Widgets.WidgetSize]],  # value
                        _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IWidgetContextChangedArgs(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]


class IWidgetCustomizationRequestedArgs(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]
    get_CustomState: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IWidgetErrorInfoReportedArgs(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]
    get_ErrorJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IWidgetInfo(_inspectable.IInspectable):
    get_WidgetContext: _Callable[[_Pointer[IWidgetContext]],  # value
                                 _type.HRESULT]
    get_Template: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_CustomState: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LastUpdateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]


class IWidgetManager(_inspectable.IInspectable):
    UpdateWidget: _Callable[[IWidgetUpdateRequestOptions],  # widgetUpdateRequestOptions
                            _type.HRESULT]
    GetWidgetIds: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                             _Pointer[_Pointer[_type.HSTRING]]],  # result
                            _type.HRESULT]
    GetWidgetInfo: _Callable[[_type.HSTRING,  # widgetId
                              _Pointer[IWidgetInfo]],  # result
                             _type.HRESULT]
    GetWidgetInfos: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                               _Pointer[_Pointer[IWidgetInfo]]],  # result
                              _type.HRESULT]
    DeleteWidget: _Callable[[_type.HSTRING],  # widgetId
                            _type.HRESULT]


class IWidgetManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IWidgetManager]],  # result
                          _type.HRESULT]


class IWidgetProvider(_inspectable.IInspectable):
    CreateWidget: _Callable[[IWidgetContext],  # widgetContext
                            _type.HRESULT]
    DeleteWidget: _Callable[[_type.HSTRING,  # widgetId
                             _type.HSTRING],  # customState
                            _type.HRESULT]
    OnActionInvoked: _Callable[[IWidgetActionInvokedArgs],  # actionInvokedArgs
                               _type.HRESULT]
    OnWidgetContextChanged: _Callable[[IWidgetContextChangedArgs],  # contextChangedArgs
                                      _type.HRESULT]
    Activate: _Callable[[IWidgetContext],  # widgetContext
                        _type.HRESULT]
    Deactivate: _Callable[[_type.HSTRING],  # widgetId
                          _type.HRESULT]


class IWidgetProvider2(_inspectable.IInspectable):
    OnCustomizationRequested: _Callable[[IWidgetCustomizationRequestedArgs],  # customizationRequestedArgs
                                        _type.HRESULT]


class IWidgetProviderAnalytics(_inspectable.IInspectable):
    OnAnalyticsInfoReported: _Callable[[IWidgetAnalyticsInfoReportedArgs],  # args
                                       _type.HRESULT]


class IWidgetProviderErrors(_inspectable.IInspectable):
    OnErrorInfoReported: _Callable[[IWidgetErrorInfoReportedArgs],  # args
                                   _type.HRESULT]


class IWidgetUpdateRequestOptions(_inspectable.IInspectable):
    get_WidgetId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Template: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Template: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Data: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_CustomState: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_CustomState: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IWidgetUpdateRequestOptionsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # widgetId
                               _Pointer[IWidgetUpdateRequestOptions]],  # value
                              _type.HRESULT]


class IWidgetUpdateRequestOptionsStatics(_inspectable.IInspectable, factory=True):
    get_UnsetValue: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
