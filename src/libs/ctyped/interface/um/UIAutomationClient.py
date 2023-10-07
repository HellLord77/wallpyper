from __future__ import annotations as _

from typing import Callable as _Callable

from . import UIAutomationCore as _UIAutomationCore
from . import Unknwnbase as _Unknwnbase
from . import oleacc as _oleacc
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IUIAutomationElement(_Unknwnbase.IUnknown):
    SetFocus: _Callable[[],
                        _type.HRESULT]
    GetRuntimeId: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # runtimeId
                            _type.HRESULT]
    FindFirst: _Callable[[_enum.TreeScope,  # scope
                          IUIAutomationCondition,  # condition
                          _Pointer[IUIAutomationElement]],  # found
                         _type.HRESULT]
    FindAll: _Callable[[_enum.TreeScope,  # scope
                        IUIAutomationCondition,  # condition
                        _Pointer[IUIAutomationElementArray]],  # found
                       _type.HRESULT]
    FindFirstBuildCache: _Callable[[_enum.TreeScope,  # scope
                                    IUIAutomationCondition,  # condition
                                    IUIAutomationCacheRequest,  # cacheRequest
                                    _Pointer[IUIAutomationElement]],  # found
                                   _type.HRESULT]
    FindAllBuildCache: _Callable[[_enum.TreeScope,  # scope
                                  IUIAutomationCondition,  # condition
                                  IUIAutomationCacheRequest,  # cacheRequest
                                  _Pointer[IUIAutomationElementArray]],  # found
                                 _type.HRESULT]
    BuildUpdatedCache: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                  _Pointer[IUIAutomationElement]],  # updatedElement
                                 _type.HRESULT]
    GetCurrentPropertyValue: _Callable[[_type.PROPERTYID,  # propertyId
                                        _Pointer[_struct.VARIANT]],  # retVal
                                       _type.HRESULT]
    GetCurrentPropertyValueEx: _Callable[[_type.PROPERTYID,  # propertyId
                                          _type.BOOL,  # ignoreDefaultValue
                                          _Pointer[_struct.VARIANT]],  # retVal
                                         _type.HRESULT]
    GetCachedPropertyValue: _Callable[[_type.PROPERTYID,  # propertyId
                                       _Pointer[_struct.VARIANT]],  # retVal
                                      _type.HRESULT]
    GetCachedPropertyValueEx: _Callable[[_type.PROPERTYID,  # propertyId
                                         _type.BOOL,  # ignoreDefaultValue
                                         _Pointer[_struct.VARIANT]],  # retVal
                                        _type.HRESULT]
    GetCurrentPatternAs: _Callable[[_type.PATTERNID,  # patternId
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # patternObject
                                   _type.HRESULT]
    GetCachedPatternAs: _Callable[[_type.PATTERNID,  # patternId
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # patternObject
                                  _type.HRESULT]
    GetCurrentPattern: _Callable[[_type.PATTERNID,  # patternId
                                  _Pointer[_Unknwnbase.IUnknown]],  # patternObject
                                 _type.HRESULT]
    GetCachedPattern: _Callable[[_type.PATTERNID,  # patternId
                                 _Pointer[_Unknwnbase.IUnknown]],  # patternObject
                                _type.HRESULT]
    GetCachedParent: _Callable[[_Pointer[IUIAutomationElement]],  # parent
                               _type.HRESULT]
    GetCachedChildren: _Callable[[_Pointer[IUIAutomationElementArray]],  # children
                                 _type.HRESULT]
    get_CurrentProcessId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_CurrentControlType: _Callable[[_Pointer[_type.CONTROLTYPEID]],  # retVal
                                      _type.HRESULT]
    get_CurrentLocalizedControlType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                               _type.HRESULT]
    get_CurrentName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                               _type.HRESULT]
    get_CurrentAcceleratorKey: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                         _type.HRESULT]
    get_CurrentAccessKey: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_CurrentHasKeyboardFocus: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                           _type.HRESULT]
    get_CurrentIsKeyboardFocusable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                              _type.HRESULT]
    get_CurrentIsEnabled: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CurrentAutomationId: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                       _type.HRESULT]
    get_CurrentClassName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_CurrentHelpText: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CurrentCulture: _Callable[[_Pointer[_type.c_int]],  # retVal
                                  _type.HRESULT]
    get_CurrentIsControlElement: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                           _type.HRESULT]
    get_CurrentIsContentElement: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                           _type.HRESULT]
    get_CurrentIsPassword: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CurrentNativeWindowHandle: _Callable[[_Pointer[_type.UIA_HWND]],  # retVal
                                             _type.HRESULT]
    get_CurrentItemType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CurrentIsOffscreen: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                      _type.HRESULT]
    get_CurrentOrientation: _Callable[[_Pointer[_enum.OrientationType]],  # retVal
                                      _type.HRESULT]
    get_CurrentFrameworkId: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                      _type.HRESULT]
    get_CurrentIsRequiredForForm: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                            _type.HRESULT]
    get_CurrentItemStatus: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                     _type.HRESULT]
    get_CurrentBoundingRectangle: _Callable[[_Pointer[_struct.RECT]],  # retVal
                                            _type.HRESULT]
    get_CurrentLabeledBy: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                    _type.HRESULT]
    get_CurrentAriaRole: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CurrentAriaProperties: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                         _type.HRESULT]
    get_CurrentIsDataValidForForm: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                             _type.HRESULT]
    get_CurrentControllerFor: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                        _type.HRESULT]
    get_CurrentDescribedBy: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                      _type.HRESULT]
    get_CurrentFlowsTo: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                  _type.HRESULT]
    get_CurrentProviderDescription: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                              _type.HRESULT]
    get_CachedProcessId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                   _type.HRESULT]
    get_CachedControlType: _Callable[[_Pointer[_type.CONTROLTYPEID]],  # retVal
                                     _type.HRESULT]
    get_CachedLocalizedControlType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                              _type.HRESULT]
    get_CachedName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                              _type.HRESULT]
    get_CachedAcceleratorKey: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                        _type.HRESULT]
    get_CachedAccessKey: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CachedHasKeyboardFocus: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                          _type.HRESULT]
    get_CachedIsKeyboardFocusable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                             _type.HRESULT]
    get_CachedIsEnabled: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]
    get_CachedAutomationId: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                      _type.HRESULT]
    get_CachedClassName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CachedHelpText: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                  _type.HRESULT]
    get_CachedCulture: _Callable[[_Pointer[_type.c_int]],  # retVal
                                 _type.HRESULT]
    get_CachedIsControlElement: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                          _type.HRESULT]
    get_CachedIsContentElement: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                          _type.HRESULT]
    get_CachedIsPassword: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CachedNativeWindowHandle: _Callable[[_Pointer[_type.UIA_HWND]],  # retVal
                                            _type.HRESULT]
    get_CachedItemType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                  _type.HRESULT]
    get_CachedIsOffscreen: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CachedOrientation: _Callable[[_Pointer[_enum.OrientationType]],  # retVal
                                     _type.HRESULT]
    get_CachedFrameworkId: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                     _type.HRESULT]
    get_CachedIsRequiredForForm: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                           _type.HRESULT]
    get_CachedItemStatus: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_CachedBoundingRectangle: _Callable[[_Pointer[_struct.RECT]],  # retVal
                                           _type.HRESULT]
    get_CachedLabeledBy: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                   _type.HRESULT]
    get_CachedAriaRole: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                  _type.HRESULT]
    get_CachedAriaProperties: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                        _type.HRESULT]
    get_CachedIsDataValidForForm: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                            _type.HRESULT]
    get_CachedControllerFor: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                       _type.HRESULT]
    get_CachedDescribedBy: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                     _type.HRESULT]
    get_CachedFlowsTo: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                 _type.HRESULT]
    get_CachedProviderDescription: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                             _type.HRESULT]
    GetClickablePoint: _Callable[[_Pointer[_struct.POINT],  # clickable
                                  _Pointer[_type.BOOL]],  # gotClickable
                                 _type.HRESULT]


class IUIAutomationElementArray(_Unknwnbase.IUnknown):
    get_Length: _Callable[[_Pointer[_type.c_int]],  # length
                          _type.HRESULT]
    GetElement: _Callable[[_type.c_int,  # index
                           _Pointer[IUIAutomationElement]],  # element
                          _type.HRESULT]


class IUIAutomationCondition(_Unknwnbase.IUnknown):
    pass


class IUIAutomationBoolCondition(IUIAutomationCondition):
    get_BooleanValue: _Callable[[_Pointer[_type.BOOL]],  # boolVal
                                _type.HRESULT]


class IUIAutomationPropertyCondition(IUIAutomationCondition):
    get_PropertyId: _Callable[[_Pointer[_type.PROPERTYID]],  # propertyId
                              _type.HRESULT]
    get_PropertyValue: _Callable[[_Pointer[_struct.VARIANT]],  # propertyValue
                                 _type.HRESULT]
    get_PropertyConditionFlags: _Callable[[_Pointer[_enum.PropertyConditionFlags]],  # flags
                                          _type.HRESULT]


class IUIAutomationAndCondition(IUIAutomationCondition):
    get_ChildCount: _Callable[[_Pointer[_type.c_int]],  # childCount
                              _type.HRESULT]
    GetChildrenAsNativeArray: _Callable[[_Pointer[_Pointer[IUIAutomationCondition]],  # childArray
                                         _Pointer[_type.c_int]],  # childArrayCount
                                        _type.HRESULT]
    GetChildren: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # childArray
                           _type.HRESULT]


class IUIAutomationOrCondition(IUIAutomationCondition):
    get_ChildCount: _Callable[[_Pointer[_type.c_int]],  # childCount
                              _type.HRESULT]
    GetChildrenAsNativeArray: _Callable[[_Pointer[_Pointer[IUIAutomationCondition]],  # childArray
                                         _Pointer[_type.c_int]],  # childArrayCount
                                        _type.HRESULT]
    GetChildren: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # childArray
                           _type.HRESULT]


class IUIAutomationNotCondition(IUIAutomationCondition):
    GetChild: _Callable[[_Pointer[IUIAutomationCondition]],  # condition
                        _type.HRESULT]


class IUIAutomationCacheRequest(_Unknwnbase.IUnknown):
    AddProperty: _Callable[[_type.PROPERTYID],  # propertyId
                           _type.HRESULT]
    AddPattern: _Callable[[_type.PATTERNID],  # patternId
                          _type.HRESULT]
    Clone: _Callable[[_Pointer[IUIAutomationCacheRequest]],  # clonedRequest
                     _type.HRESULT]
    get_TreeScope: _Callable[[_Pointer[_enum.TreeScope]],  # scope
                             _type.HRESULT]
    put_TreeScope: _Callable[[_enum.TreeScope],  # scope
                             _type.HRESULT]
    get_TreeFilter: _Callable[[_Pointer[IUIAutomationCondition]],  # filter
                              _type.HRESULT]
    put_TreeFilter: _Callable[[IUIAutomationCondition],  # filter
                              _type.HRESULT]
    get_AutomationElementMode: _Callable[[_Pointer[_enum.AutomationElementMode]],  # mode
                                         _type.HRESULT]
    put_AutomationElementMode: _Callable[[_enum.AutomationElementMode],  # mode
                                         _type.HRESULT]


class IUIAutomationTreeWalker(_Unknwnbase.IUnknown):
    GetParentElement: _Callable[[IUIAutomationElement,  # element
                                 _Pointer[IUIAutomationElement]],  # parent
                                _type.HRESULT]
    GetFirstChildElement: _Callable[[IUIAutomationElement,  # element
                                     _Pointer[IUIAutomationElement]],  # first
                                    _type.HRESULT]
    GetLastChildElement: _Callable[[IUIAutomationElement,  # element
                                    _Pointer[IUIAutomationElement]],  # last
                                   _type.HRESULT]
    GetNextSiblingElement: _Callable[[IUIAutomationElement,  # element
                                      _Pointer[IUIAutomationElement]],  # next
                                     _type.HRESULT]
    GetPreviousSiblingElement: _Callable[[IUIAutomationElement,  # element
                                          _Pointer[IUIAutomationElement]],  # previous
                                         _type.HRESULT]
    NormalizeElement: _Callable[[IUIAutomationElement,  # element
                                 _Pointer[IUIAutomationElement]],  # normalized
                                _type.HRESULT]
    GetParentElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                           IUIAutomationCacheRequest,  # cacheRequest
                                           _Pointer[IUIAutomationElement]],  # parent
                                          _type.HRESULT]
    GetFirstChildElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                               IUIAutomationCacheRequest,  # cacheRequest
                                               _Pointer[IUIAutomationElement]],  # first
                                              _type.HRESULT]
    GetLastChildElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                              IUIAutomationCacheRequest,  # cacheRequest
                                              _Pointer[IUIAutomationElement]],  # last
                                             _type.HRESULT]
    GetNextSiblingElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                                IUIAutomationCacheRequest,  # cacheRequest
                                                _Pointer[IUIAutomationElement]],  # next
                                               _type.HRESULT]
    GetPreviousSiblingElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                                    IUIAutomationCacheRequest,  # cacheRequest
                                                    _Pointer[IUIAutomationElement]],  # previous
                                                   _type.HRESULT]
    NormalizeElementBuildCache: _Callable[[IUIAutomationElement,  # element
                                           IUIAutomationCacheRequest,  # cacheRequest
                                           _Pointer[IUIAutomationElement]],  # normalized
                                          _type.HRESULT]
    get_Condition: _Callable[[_Pointer[IUIAutomationCondition]],  # condition
                             _type.HRESULT]


class IUIAutomationEventHandler(_Unknwnbase.IUnknown):
    HandleAutomationEvent: _Callable[[IUIAutomationElement,  # sender
                                      _type.EVENTID],  # eventId
                                     _type.HRESULT]


class IUIAutomationPropertyChangedEventHandler(_Unknwnbase.IUnknown):
    HandlePropertyChangedEvent: _Callable[[IUIAutomationElement,  # sender
                                           _type.PROPERTYID,  # propertyId
                                           _struct.VARIANT],  # newValue
                                          _type.HRESULT]


class IUIAutomationStructureChangedEventHandler(_Unknwnbase.IUnknown):
    HandleStructureChangedEvent: _Callable[[IUIAutomationElement,  # sender
                                            _enum.StructureChangeType,  # changeType
                                            _Pointer[_struct.SAFEARRAY]],  # runtimeId
                                           _type.HRESULT]


class IUIAutomationFocusChangedEventHandler(_Unknwnbase.IUnknown):
    HandleFocusChangedEvent: _Callable[[IUIAutomationElement],  # sender
                                       _type.HRESULT]


class IUIAutomationTextEditTextChangedEventHandler(_Unknwnbase.IUnknown):
    HandleTextEditTextChangedEvent: _Callable[[IUIAutomationElement,  # sender
                                               _enum.TextEditChangeType,  # textEditChangeType
                                               _Pointer[_struct.SAFEARRAY]],  # eventStrings
                                              _type.HRESULT]


class IUIAutomationChangesEventHandler(_Unknwnbase.IUnknown):
    HandleChangesEvent: _Callable[[IUIAutomationElement,  # sender
                                   _Pointer[_struct.UiaChangeInfo],  # uiaChanges
                                   _type.c_int],  # changesCount
                                  _type.HRESULT]


class IUIAutomationNotificationEventHandler(_Unknwnbase.IUnknown):
    HandleNotificationEvent: _Callable[[IUIAutomationElement,  # sender
                                        _enum.NotificationKind,  # notificationKind
                                        _enum.NotificationProcessing,  # notificationProcessing
                                        _type.BSTR,  # displayString
                                        _type.BSTR],  # activityId
                                       _type.HRESULT]


class _IUIAutomationInvokePattern:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IUIAutomationInvokePattern(_IUIAutomationInvokePattern, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IUIAutomationInvokePattern_impl(_IUIAutomationInvokePattern, _Unknwnbase.IUnknown_impl):
    pass


class IUIAutomationDockPattern(_Unknwnbase.IUnknown):
    SetDockPosition: _Callable[[_enum.DockPosition],  # dockPos
                               _type.HRESULT]
    get_CurrentDockPosition: _Callable[[_Pointer[_enum.DockPosition]],  # retVal
                                       _type.HRESULT]
    get_CachedDockPosition: _Callable[[_Pointer[_enum.DockPosition]],  # retVal
                                      _type.HRESULT]


class IUIAutomationExpandCollapsePattern(_Unknwnbase.IUnknown):
    Expand: _Callable[[],
                      _type.HRESULT]
    Collapse: _Callable[[],
                        _type.HRESULT]
    get_CurrentExpandCollapseState: _Callable[[_Pointer[_enum.ExpandCollapseState]],  # retVal
                                              _type.HRESULT]
    get_CachedExpandCollapseState: _Callable[[_Pointer[_enum.ExpandCollapseState]],  # retVal
                                             _type.HRESULT]


class IUIAutomationGridPattern(_Unknwnbase.IUnknown):
    GetItem: _Callable[[_type.c_int,  # row
                        _type.c_int,  # column
                        _Pointer[IUIAutomationElement]],  # element
                       _type.HRESULT]
    get_CurrentRowCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                   _type.HRESULT]
    get_CurrentColumnCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                      _type.HRESULT]
    get_CachedRowCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                  _type.HRESULT]
    get_CachedColumnCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                     _type.HRESULT]


class IUIAutomationGridItemPattern(_Unknwnbase.IUnknown):
    get_CurrentContainingGrid: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                         _type.HRESULT]
    get_CurrentRow: _Callable[[_Pointer[_type.c_int]],  # retVal
                              _type.HRESULT]
    get_CurrentColumn: _Callable[[_Pointer[_type.c_int]],  # retVal
                                 _type.HRESULT]
    get_CurrentRowSpan: _Callable[[_Pointer[_type.c_int]],  # retVal
                                  _type.HRESULT]
    get_CurrentColumnSpan: _Callable[[_Pointer[_type.c_int]],  # retVal
                                     _type.HRESULT]
    get_CachedContainingGrid: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                        _type.HRESULT]
    get_CachedRow: _Callable[[_Pointer[_type.c_int]],  # retVal
                             _type.HRESULT]
    get_CachedColumn: _Callable[[_Pointer[_type.c_int]],  # retVal
                                _type.HRESULT]
    get_CachedRowSpan: _Callable[[_Pointer[_type.c_int]],  # retVal
                                 _type.HRESULT]
    get_CachedColumnSpan: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]


class IUIAutomationMultipleViewPattern(_Unknwnbase.IUnknown):
    GetViewName: _Callable[[_type.c_int,  # view
                            _Pointer[_type.BSTR]],  # name
                           _type.HRESULT]
    SetCurrentView: _Callable[[_type.c_int],  # view
                              _type.HRESULT]
    get_CurrentCurrentView: _Callable[[_Pointer[_type.c_int]],  # retVal
                                      _type.HRESULT]
    GetCurrentSupportedViews: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                        _type.HRESULT]
    get_CachedCurrentView: _Callable[[_Pointer[_type.c_int]],  # retVal
                                     _type.HRESULT]
    GetCachedSupportedViews: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                       _type.HRESULT]


class IUIAutomationObjectModelPattern(_Unknwnbase.IUnknown):
    GetUnderlyingObjectModel: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # retVal
                                        _type.HRESULT]


class IUIAutomationRangeValuePattern(_Unknwnbase.IUnknown):
    SetValue: _Callable[[_type.c_double],  # val
                        _type.HRESULT]
    get_CurrentValue: _Callable[[_Pointer[_type.c_double]],  # retVal
                                _type.HRESULT]
    get_CurrentIsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CurrentMaximum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                  _type.HRESULT]
    get_CurrentMinimum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                  _type.HRESULT]
    get_CurrentLargeChange: _Callable[[_Pointer[_type.c_double]],  # retVal
                                      _type.HRESULT]
    get_CurrentSmallChange: _Callable[[_Pointer[_type.c_double]],  # retVal
                                      _type.HRESULT]
    get_CachedValue: _Callable[[_Pointer[_type.c_double]],  # retVal
                               _type.HRESULT]
    get_CachedIsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CachedMaximum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                 _type.HRESULT]
    get_CachedMinimum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                 _type.HRESULT]
    get_CachedLargeChange: _Callable[[_Pointer[_type.c_double]],  # retVal
                                     _type.HRESULT]
    get_CachedSmallChange: _Callable[[_Pointer[_type.c_double]],  # retVal
                                     _type.HRESULT]


class IUIAutomationScrollPattern(_Unknwnbase.IUnknown):
    Scroll: _Callable[[_enum.ScrollAmount,  # horizontalAmount
                       _enum.ScrollAmount],  # verticalAmount
                      _type.HRESULT]
    SetScrollPercent: _Callable[[_type.c_double,  # horizontalPercent
                                 _type.c_double],  # verticalPercent
                                _type.HRESULT]
    get_CurrentHorizontalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # retVal
                                                  _type.HRESULT]
    get_CurrentVerticalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # retVal
                                                _type.HRESULT]
    get_CurrentHorizontalViewSize: _Callable[[_Pointer[_type.c_double]],  # retVal
                                             _type.HRESULT]
    get_CurrentVerticalViewSize: _Callable[[_Pointer[_type.c_double]],  # retVal
                                           _type.HRESULT]
    get_CurrentHorizontallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                                 _type.HRESULT]
    get_CurrentVerticallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                               _type.HRESULT]
    get_CachedHorizontalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # retVal
                                                 _type.HRESULT]
    get_CachedVerticalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # retVal
                                               _type.HRESULT]
    get_CachedHorizontalViewSize: _Callable[[_Pointer[_type.c_double]],  # retVal
                                            _type.HRESULT]
    get_CachedVerticalViewSize: _Callable[[_Pointer[_type.c_double]],  # retVal
                                          _type.HRESULT]
    get_CachedHorizontallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                                _type.HRESULT]
    get_CachedVerticallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                              _type.HRESULT]


class IUIAutomationScrollItemPattern(_Unknwnbase.IUnknown):
    ScrollIntoView: _Callable[[],
                              _type.HRESULT]


class IUIAutomationSelectionPattern(_Unknwnbase.IUnknown):
    GetCurrentSelection: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                   _type.HRESULT]
    get_CurrentCanSelectMultiple: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                            _type.HRESULT]
    get_CurrentIsSelectionRequired: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                              _type.HRESULT]
    GetCachedSelection: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                  _type.HRESULT]
    get_CachedCanSelectMultiple: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                           _type.HRESULT]
    get_CachedIsSelectionRequired: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                             _type.HRESULT]


class IUIAutomationSelectionPattern2(IUIAutomationSelectionPattern):
    get_CurrentFirstSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                            _type.HRESULT]
    get_CurrentLastSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                           _type.HRESULT]
    get_CurrentCurrentSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                              _type.HRESULT]
    get_CurrentItemCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_CachedFirstSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                           _type.HRESULT]
    get_CachedLastSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                          _type.HRESULT]
    get_CachedCurrentSelectedItem: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                             _type.HRESULT]
    get_CachedItemCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                                   _type.HRESULT]


class IUIAutomationSelectionItemPattern(_Unknwnbase.IUnknown):
    Select: _Callable[[],
                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    get_CurrentIsSelected: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CurrentSelectionContainer: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                             _type.HRESULT]
    get_CachedIsSelected: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CachedSelectionContainer: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                            _type.HRESULT]


class IUIAutomationSynchronizedInputPattern(_Unknwnbase.IUnknown):
    StartListening: _Callable[[_enum.SynchronizedInputType],  # inputType
                              _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]


class IUIAutomationTablePattern(_Unknwnbase.IUnknown):
    GetCurrentRowHeaders: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                    _type.HRESULT]
    GetCurrentColumnHeaders: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                       _type.HRESULT]
    get_CurrentRowOrColumnMajor: _Callable[[_Pointer[_enum.RowOrColumnMajor]],  # retVal
                                           _type.HRESULT]
    GetCachedRowHeaders: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                   _type.HRESULT]
    GetCachedColumnHeaders: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                      _type.HRESULT]
    get_CachedRowOrColumnMajor: _Callable[[_Pointer[_enum.RowOrColumnMajor]],  # retVal
                                          _type.HRESULT]


class IUIAutomationTableItemPattern(_Unknwnbase.IUnknown):
    GetCurrentRowHeaderItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                        _type.HRESULT]
    GetCurrentColumnHeaderItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                           _type.HRESULT]
    GetCachedRowHeaderItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                       _type.HRESULT]
    GetCachedColumnHeaderItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                          _type.HRESULT]


class IUIAutomationTogglePattern(_Unknwnbase.IUnknown):
    Toggle: _Callable[[],
                      _type.HRESULT]
    get_CurrentToggleState: _Callable[[_Pointer[_enum.ToggleState]],  # retVal
                                      _type.HRESULT]
    get_CachedToggleState: _Callable[[_Pointer[_enum.ToggleState]],  # retVal
                                     _type.HRESULT]


class IUIAutomationTransformPattern(_Unknwnbase.IUnknown):
    Move: _Callable[[_type.c_double,  # x
                     _type.c_double],  # y
                    _type.HRESULT]
    Resize: _Callable[[_type.c_double,  # width
                       _type.c_double],  # height
                      _type.HRESULT]
    Rotate: _Callable[[_type.c_double],  # degrees
                      _type.HRESULT]
    get_CurrentCanMove: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                  _type.HRESULT]
    get_CurrentCanResize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CurrentCanRotate: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CachedCanMove: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                 _type.HRESULT]
    get_CachedCanResize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]
    get_CachedCanRotate: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]


class IUIAutomationValuePattern(_Unknwnbase.IUnknown):
    SetValue: _Callable[[_type.BSTR],  # val
                        _type.HRESULT]
    get_CurrentValue: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                _type.HRESULT]
    get_CurrentIsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CachedValue: _Callable[[_Pointer[_type.BSTR]],  # retVal
                               _type.HRESULT]
    get_CachedIsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]


class IUIAutomationWindowPattern(_Unknwnbase.IUnknown):
    Close: _Callable[[],
                     _type.HRESULT]
    WaitForInputIdle: _Callable[[_type.c_int,  # milliseconds
                                 _Pointer[_type.BOOL]],  # success
                                _type.HRESULT]
    SetWindowVisualState: _Callable[[_enum.WindowVisualState],  # state
                                    _type.HRESULT]
    get_CurrentCanMaximize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                      _type.HRESULT]
    get_CurrentCanMinimize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                      _type.HRESULT]
    get_CurrentIsModal: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                  _type.HRESULT]
    get_CurrentIsTopmost: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CurrentWindowVisualState: _Callable[[_Pointer[_enum.WindowVisualState]],  # retVal
                                            _type.HRESULT]
    get_CurrentWindowInteractionState: _Callable[[_Pointer[_enum.WindowInteractionState]],  # retVal
                                                 _type.HRESULT]
    get_CachedCanMaximize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CachedCanMinimize: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                     _type.HRESULT]
    get_CachedIsModal: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                 _type.HRESULT]
    get_CachedIsTopmost: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]
    get_CachedWindowVisualState: _Callable[[_Pointer[_enum.WindowVisualState]],  # retVal
                                           _type.HRESULT]
    get_CachedWindowInteractionState: _Callable[[_Pointer[_enum.WindowInteractionState]],  # retVal
                                                _type.HRESULT]


class IUIAutomationTextRange(_Unknwnbase.IUnknown):
    Clone: _Callable[[_Pointer[IUIAutomationTextRange]],  # clonedRange
                     _type.HRESULT]
    Compare: _Callable[[IUIAutomationTextRange,  # range
                        _Pointer[_type.BOOL]],  # areSame
                       _type.HRESULT]
    CompareEndpoints: _Callable[[_enum.TextPatternRangeEndpoint,  # srcEndPoint
                                 IUIAutomationTextRange,  # range
                                 _enum.TextPatternRangeEndpoint,  # targetEndPoint
                                 _Pointer[_type.c_int]],  # compValue
                                _type.HRESULT]
    ExpandToEnclosingUnit: _Callable[[_enum.TextUnit],  # textUnit
                                     _type.HRESULT]
    FindAttribute: _Callable[[_type.TEXTATTRIBUTEID,  # attr
                              _struct.VARIANT,  # val
                              _type.BOOL,  # backward
                              _Pointer[IUIAutomationTextRange]],  # found
                             _type.HRESULT]
    FindText: _Callable[[_type.BSTR,  # text
                         _type.BOOL,  # backward
                         _type.BOOL,  # ignoreCase
                         _Pointer[IUIAutomationTextRange]],  # found
                        _type.HRESULT]
    GetAttributeValue: _Callable[[_type.TEXTATTRIBUTEID,  # attr
                                  _Pointer[_struct.VARIANT]],  # value
                                 _type.HRESULT]
    GetBoundingRectangles: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # boundingRects
                                     _type.HRESULT]
    GetEnclosingElement: _Callable[[_Pointer[IUIAutomationElement]],  # enclosingElement
                                   _type.HRESULT]
    GetText: _Callable[[_type.c_int,  # maxLength
                        _Pointer[_type.BSTR]],  # text
                       _type.HRESULT]
    Move: _Callable[[_enum.TextUnit,  # unit
                     _type.c_int,  # count
                     _Pointer[_type.c_int]],  # moved
                    _type.HRESULT]
    MoveEndpointByUnit: _Callable[[_enum.TextPatternRangeEndpoint,  # endpoint
                                   _enum.TextUnit,  # unit
                                   _type.c_int,  # count
                                   _Pointer[_type.c_int]],  # moved
                                  _type.HRESULT]
    MoveEndpointByRange: _Callable[[_enum.TextPatternRangeEndpoint,  # srcEndPoint
                                    IUIAutomationTextRange,  # range
                                    _enum.TextPatternRangeEndpoint],  # targetEndPoint
                                   _type.HRESULT]
    Select: _Callable[[],
                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    ScrollIntoView: _Callable[[_type.BOOL],  # alignToTop
                              _type.HRESULT]
    GetChildren: _Callable[[_Pointer[IUIAutomationElementArray]],  # children
                           _type.HRESULT]


class IUIAutomationTextRange2(IUIAutomationTextRange):
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]


class IUIAutomationTextRange3(IUIAutomationTextRange2):
    GetEnclosingElementBuildCache: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                              _Pointer[IUIAutomationElement]],  # enclosingElement
                                             _type.HRESULT]
    GetChildrenBuildCache: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                      _Pointer[IUIAutomationElementArray]],  # children
                                     _type.HRESULT]
    GetAttributeValues: _Callable[[_Pointer[_type.TEXTATTRIBUTEID],  # attributeIds
                                   _type.c_int,  # attributeIdCount
                                   _Pointer[_Pointer[_struct.SAFEARRAY]]],  # attributeValues
                                  _type.HRESULT]


class IUIAutomationTextRangeArray(_Unknwnbase.IUnknown):
    get_Length: _Callable[[_Pointer[_type.c_int]],  # length
                          _type.HRESULT]
    GetElement: _Callable[[_type.c_int,  # index
                           _Pointer[IUIAutomationTextRange]],  # element
                          _type.HRESULT]


class IUIAutomationTextPattern(_Unknwnbase.IUnknown):
    RangeFromPoint: _Callable[[_struct.POINT,  # pt
                               _Pointer[IUIAutomationTextRange]],  # range
                              _type.HRESULT]
    RangeFromChild: _Callable[[IUIAutomationElement,  # child
                               _Pointer[IUIAutomationTextRange]],  # range
                              _type.HRESULT]
    GetSelection: _Callable[[_Pointer[IUIAutomationTextRangeArray]],  # ranges
                            _type.HRESULT]
    GetVisibleRanges: _Callable[[_Pointer[IUIAutomationTextRangeArray]],  # ranges
                                _type.HRESULT]
    get_DocumentRange: _Callable[[_Pointer[IUIAutomationTextRange]],  # range
                                 _type.HRESULT]
    get_SupportedTextSelection: _Callable[[_Pointer[_enum.SupportedTextSelection]],  # supportedTextSelection
                                          _type.HRESULT]


class IUIAutomationTextPattern2(IUIAutomationTextPattern):
    RangeFromAnnotation: _Callable[[IUIAutomationElement,  # annotation
                                    _Pointer[IUIAutomationTextRange]],  # range
                                   _type.HRESULT]
    GetCaretRange: _Callable[[_Pointer[_type.BOOL],  # isActive
                              _Pointer[IUIAutomationTextRange]],  # range
                             _type.HRESULT]


class IUIAutomationTextEditPattern(IUIAutomationTextPattern):
    GetActiveComposition: _Callable[[_Pointer[IUIAutomationTextRange]],  # range
                                    _type.HRESULT]
    GetConversionTarget: _Callable[[_Pointer[IUIAutomationTextRange]],  # range
                                   _type.HRESULT]


class IUIAutomationCustomNavigationPattern(_Unknwnbase.IUnknown):
    Navigate: _Callable[[_enum.NavigateDirection,  # direction
                         _Pointer[IUIAutomationElement]],  # pRetVal
                        _type.HRESULT]


class IUIAutomationActiveTextPositionChangedEventHandler(_Unknwnbase.IUnknown):
    HandleActiveTextPositionChangedEvent: _Callable[[IUIAutomationElement,  # sender
                                                     IUIAutomationTextRange],  # range
                                                    _type.HRESULT]


class IUIAutomationLegacyIAccessiblePattern(_Unknwnbase.IUnknown):
    Select: _Callable[[_type.c_long],  # flagsSelect
                      _type.HRESULT]
    DoDefaultAction: _Callable[[],
                               _type.HRESULT]
    SetValue: _Callable[[_type.LPCWSTR],  # szValue
                        _type.HRESULT]
    get_CurrentChildId: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                                  _type.HRESULT]
    get_CurrentName: _Callable[[_Pointer[_type.BSTR]],  # pszName
                               _type.HRESULT]
    get_CurrentValue: _Callable[[_Pointer[_type.BSTR]],  # pszValue
                                _type.HRESULT]
    get_CurrentDescription: _Callable[[_Pointer[_type.BSTR]],  # pszDescription
                                      _type.HRESULT]
    get_CurrentRole: _Callable[[_Pointer[_type.DWORD]],  # pdwRole
                               _type.HRESULT]
    get_CurrentState: _Callable[[_Pointer[_type.DWORD]],  # pdwState
                                _type.HRESULT]
    get_CurrentHelp: _Callable[[_Pointer[_type.BSTR]],  # pszHelp
                               _type.HRESULT]
    get_CurrentKeyboardShortcut: _Callable[[_Pointer[_type.BSTR]],  # pszKeyboardShortcut
                                           _type.HRESULT]
    GetCurrentSelection: _Callable[[_Pointer[IUIAutomationElementArray]],  # pvarSelectedChildren
                                   _type.HRESULT]
    get_CurrentDefaultAction: _Callable[[_Pointer[_type.BSTR]],  # pszDefaultAction
                                        _type.HRESULT]
    get_CachedChildId: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                                 _type.HRESULT]
    get_CachedName: _Callable[[_Pointer[_type.BSTR]],  # pszName
                              _type.HRESULT]
    get_CachedValue: _Callable[[_Pointer[_type.BSTR]],  # pszValue
                               _type.HRESULT]
    get_CachedDescription: _Callable[[_Pointer[_type.BSTR]],  # pszDescription
                                     _type.HRESULT]
    get_CachedRole: _Callable[[_Pointer[_type.DWORD]],  # pdwRole
                              _type.HRESULT]
    get_CachedState: _Callable[[_Pointer[_type.DWORD]],  # pdwState
                               _type.HRESULT]
    get_CachedHelp: _Callable[[_Pointer[_type.BSTR]],  # pszHelp
                              _type.HRESULT]
    get_CachedKeyboardShortcut: _Callable[[_Pointer[_type.BSTR]],  # pszKeyboardShortcut
                                          _type.HRESULT]
    GetCachedSelection: _Callable[[_Pointer[IUIAutomationElementArray]],  # pvarSelectedChildren
                                  _type.HRESULT]
    get_CachedDefaultAction: _Callable[[_Pointer[_type.BSTR]],  # pszDefaultAction
                                       _type.HRESULT]
    GetIAccessible: _Callable[[_Pointer[_oleacc.IAccessible]],  # ppAccessible
                              _type.HRESULT]


class IUIAutomationItemContainerPattern(_Unknwnbase.IUnknown):
    FindItemByProperty: _Callable[[IUIAutomationElement,  # pStartAfter
                                   _type.PROPERTYID,  # propertyId
                                   _struct.VARIANT,  # value
                                   _Pointer[IUIAutomationElement]],  # pFound
                                  _type.HRESULT]


class IUIAutomationVirtualizedItemPattern(_Unknwnbase.IUnknown):
    Realize: _Callable[[],
                       _type.HRESULT]


class IUIAutomationAnnotationPattern(_Unknwnbase.IUnknown):
    get_CurrentAnnotationTypeId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                           _type.HRESULT]
    get_CurrentAnnotationTypeName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                             _type.HRESULT]
    get_CurrentAuthor: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                 _type.HRESULT]
    get_CurrentDateTime: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CurrentTarget: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                 _type.HRESULT]
    get_CachedAnnotationTypeId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                          _type.HRESULT]
    get_CachedAnnotationTypeName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                            _type.HRESULT]
    get_CachedAuthor: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                _type.HRESULT]
    get_CachedDateTime: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                  _type.HRESULT]
    get_CachedTarget: _Callable[[_Pointer[IUIAutomationElement]],  # retVal
                                _type.HRESULT]


class IUIAutomationStylesPattern(_Unknwnbase.IUnknown):
    get_CurrentStyleId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                  _type.HRESULT]
    get_CurrentStyleName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_CurrentFillColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_CurrentFillPatternStyle: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                           _type.HRESULT]
    get_CurrentShape: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                _type.HRESULT]
    get_CurrentFillPatternColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                                           _type.HRESULT]
    get_CurrentExtendedProperties: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                             _type.HRESULT]
    GetCurrentExtendedPropertiesAsArray: _Callable[[_Pointer[_Pointer[_struct.ExtendedProperty]],  # propertyArray
                                                    _Pointer[_type.c_int]],  # propertyCount
                                                   _type.HRESULT]
    get_CachedStyleId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                 _type.HRESULT]
    get_CachedStyleName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                   _type.HRESULT]
    get_CachedFillColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                                   _type.HRESULT]
    get_CachedFillPatternStyle: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                          _type.HRESULT]
    get_CachedShape: _Callable[[_Pointer[_type.BSTR]],  # retVal
                               _type.HRESULT]
    get_CachedFillPatternColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                                          _type.HRESULT]
    get_CachedExtendedProperties: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                            _type.HRESULT]
    GetCachedExtendedPropertiesAsArray: _Callable[[_Pointer[_Pointer[_struct.ExtendedProperty]],  # propertyArray
                                                   _Pointer[_type.c_int]],  # propertyCount
                                                  _type.HRESULT]


class IUIAutomationSpreadsheetPattern(_Unknwnbase.IUnknown):
    GetItemByName: _Callable[[_type.BSTR,  # name
                              _Pointer[IUIAutomationElement]],  # element
                             _type.HRESULT]


class IUIAutomationSpreadsheetItemPattern(_Unknwnbase.IUnknown):
    get_CurrentFormula: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                  _type.HRESULT]
    GetCurrentAnnotationObjects: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                           _type.HRESULT]
    GetCurrentAnnotationTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                         _type.HRESULT]
    get_CachedFormula: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                 _type.HRESULT]
    GetCachedAnnotationObjects: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                          _type.HRESULT]
    GetCachedAnnotationTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                        _type.HRESULT]


class IUIAutomationTransformPattern2(IUIAutomationTransformPattern):
    Zoom: _Callable[[_type.c_double],  # zoomValue
                    _type.HRESULT]
    ZoomByUnit: _Callable[[_enum.ZoomUnit],  # zoomUnit
                          _type.HRESULT]
    get_CurrentCanZoom: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                  _type.HRESULT]
    get_CachedCanZoom: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                 _type.HRESULT]
    get_CurrentZoomLevel: _Callable[[_Pointer[_type.c_double]],  # retVal
                                    _type.HRESULT]
    get_CachedZoomLevel: _Callable[[_Pointer[_type.c_double]],  # retVal
                                   _type.HRESULT]
    get_CurrentZoomMinimum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                      _type.HRESULT]
    get_CachedZoomMinimum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                     _type.HRESULT]
    get_CurrentZoomMaximum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                      _type.HRESULT]
    get_CachedZoomMaximum: _Callable[[_Pointer[_type.c_double]],  # retVal
                                     _type.HRESULT]


class IUIAutomationTextChildPattern(_Unknwnbase.IUnknown):
    get_TextContainer: _Callable[[_Pointer[IUIAutomationElement]],  # container
                                 _type.HRESULT]
    get_TextRange: _Callable[[_Pointer[IUIAutomationTextRange]],  # range
                             _type.HRESULT]


class IUIAutomationDragPattern(_Unknwnbase.IUnknown):
    get_CurrentIsGrabbed: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                    _type.HRESULT]
    get_CachedIsGrabbed: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]
    get_CurrentDropEffect: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                     _type.HRESULT]
    get_CachedDropEffect: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_CurrentDropEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                      _type.HRESULT]
    get_CachedDropEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                     _type.HRESULT]
    GetCurrentGrabbedItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                      _type.HRESULT]
    GetCachedGrabbedItems: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                     _type.HRESULT]


class IUIAutomationDropTargetPattern(_Unknwnbase.IUnknown):
    get_CurrentDropTargetEffect: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                           _type.HRESULT]
    get_CachedDropTargetEffect: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                          _type.HRESULT]
    get_CurrentDropTargetEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                            _type.HRESULT]
    get_CachedDropTargetEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                           _type.HRESULT]


class IUIAutomationElement2(IUIAutomationElement):
    get_CurrentOptimizeForVisualContent: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                                   _type.HRESULT]
    get_CachedOptimizeForVisualContent: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                                  _type.HRESULT]
    get_CurrentLiveSetting: _Callable[[_Pointer[_enum.LiveSetting]],  # retVal
                                      _type.HRESULT]
    get_CachedLiveSetting: _Callable[[_Pointer[_enum.LiveSetting]],  # retVal
                                     _type.HRESULT]
    get_CurrentFlowsFrom: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                    _type.HRESULT]
    get_CachedFlowsFrom: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                   _type.HRESULT]


class IUIAutomationElement3(IUIAutomationElement2):
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]
    get_CurrentIsPeripheral: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                       _type.HRESULT]
    get_CachedIsPeripheral: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                      _type.HRESULT]


class IUIAutomationElement4(IUIAutomationElement3):
    get_CurrentPositionInSet: _Callable[[_Pointer[_type.c_int]],  # retVal
                                        _type.HRESULT]
    get_CurrentSizeOfSet: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_CurrentLevel: _Callable[[_Pointer[_type.c_int]],  # retVal
                                _type.HRESULT]
    get_CurrentAnnotationTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                          _type.HRESULT]
    get_CurrentAnnotationObjects: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                            _type.HRESULT]
    get_CachedPositionInSet: _Callable[[_Pointer[_type.c_int]],  # retVal
                                       _type.HRESULT]
    get_CachedSizeOfSet: _Callable[[_Pointer[_type.c_int]],  # retVal
                                   _type.HRESULT]
    get_CachedLevel: _Callable[[_Pointer[_type.c_int]],  # retVal
                               _type.HRESULT]
    get_CachedAnnotationTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # retVal
                                         _type.HRESULT]
    get_CachedAnnotationObjects: _Callable[[_Pointer[IUIAutomationElementArray]],  # retVal
                                           _type.HRESULT]


class IUIAutomationElement5(IUIAutomationElement4):
    get_CurrentLandmarkType: _Callable[[_Pointer[_type.LANDMARKTYPEID]],  # retVal
                                       _type.HRESULT]
    get_CurrentLocalizedLandmarkType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                                _type.HRESULT]
    get_CachedLandmarkType: _Callable[[_Pointer[_type.LANDMARKTYPEID]],  # retVal
                                      _type.HRESULT]
    get_CachedLocalizedLandmarkType: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                               _type.HRESULT]


class IUIAutomationElement6(IUIAutomationElement5):
    get_CurrentFullDescription: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                          _type.HRESULT]
    get_CachedFullDescription: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                         _type.HRESULT]


class IUIAutomationElement7(IUIAutomationElement6):
    FindFirstWithOptions: _Callable[[_enum.TreeScope,  # scope
                                     IUIAutomationCondition,  # condition
                                     _enum.TreeTraversalOptions,  # traversalOptions
                                     IUIAutomationElement,  # root
                                     _Pointer[IUIAutomationElement]],  # found
                                    _type.HRESULT]
    FindAllWithOptions: _Callable[[_enum.TreeScope,  # scope
                                   IUIAutomationCondition,  # condition
                                   _enum.TreeTraversalOptions,  # traversalOptions
                                   IUIAutomationElement,  # root
                                   _Pointer[IUIAutomationElementArray]],  # found
                                  _type.HRESULT]
    FindFirstWithOptionsBuildCache: _Callable[[_enum.TreeScope,  # scope
                                               IUIAutomationCondition,  # condition
                                               IUIAutomationCacheRequest,  # cacheRequest
                                               _enum.TreeTraversalOptions,  # traversalOptions
                                               IUIAutomationElement,  # root
                                               _Pointer[IUIAutomationElement]],  # found
                                              _type.HRESULT]
    FindAllWithOptionsBuildCache: _Callable[[_enum.TreeScope,  # scope
                                             IUIAutomationCondition,  # condition
                                             IUIAutomationCacheRequest,  # cacheRequest
                                             _enum.TreeTraversalOptions,  # traversalOptions
                                             IUIAutomationElement,  # root
                                             _Pointer[IUIAutomationElementArray]],  # found
                                            _type.HRESULT]
    GetCurrentMetadataValue: _Callable[[_type.c_int,  # targetId
                                        _type.METADATAID,  # metadataId
                                        _Pointer[_struct.VARIANT]],  # returnVal
                                       _type.HRESULT]


class IUIAutomationElement8(IUIAutomationElement7):
    get_CurrentHeadingLevel: _Callable[[_Pointer[_type.HEADINGLEVELID]],  # retVal
                                       _type.HRESULT]
    get_CachedHeadingLevel: _Callable[[_Pointer[_type.HEADINGLEVELID]],  # retVal
                                      _type.HRESULT]


class IUIAutomationElement9(IUIAutomationElement8):
    get_CurrentIsDialog: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                   _type.HRESULT]
    get_CachedIsDialog: _Callable[[_Pointer[_type.BOOL]],  # retVal
                                  _type.HRESULT]


class IUIAutomationProxyFactory(_Unknwnbase.IUnknown):
    CreateProvider: _Callable[[_type.UIA_HWND,  # hwnd
                               _type.LONG,  # idObject
                               _type.LONG,  # idChild
                               _Pointer[_UIAutomationCore.IRawElementProviderSimple]],  # provider
                              _type.HRESULT]
    get_ProxyFactoryId: _Callable[[_Pointer[_type.BSTR]],  # factoryId
                                  _type.HRESULT]


class IUIAutomationProxyFactoryEntry(_Unknwnbase.IUnknown):
    get_ProxyFactory: _Callable[[_Pointer[IUIAutomationProxyFactory]],  # factory
                                _type.HRESULT]
    get_ClassName: _Callable[[_Pointer[_type.BSTR]],  # className
                             _type.HRESULT]
    get_ImageName: _Callable[[_Pointer[_type.BSTR]],  # imageName
                             _type.HRESULT]
    get_AllowSubstringMatch: _Callable[[_Pointer[_type.BOOL]],  # allowSubstringMatch
                                       _type.HRESULT]
    get_CanCheckBaseClass: _Callable[[_Pointer[_type.BOOL]],  # canCheckBaseClass
                                     _type.HRESULT]
    get_NeedsAdviseEvents: _Callable[[_Pointer[_type.BOOL]],  # adviseEvents
                                     _type.HRESULT]
    put_ClassName: _Callable[[_type.LPCWSTR],  # className
                             _type.HRESULT]
    put_ImageName: _Callable[[_type.LPCWSTR],  # imageName
                             _type.HRESULT]
    put_AllowSubstringMatch: _Callable[[_type.BOOL],  # allowSubstringMatch
                                       _type.HRESULT]
    put_CanCheckBaseClass: _Callable[[_type.BOOL],  # canCheckBaseClass
                                     _type.HRESULT]
    put_NeedsAdviseEvents: _Callable[[_type.BOOL],  # adviseEvents
                                     _type.HRESULT]
    SetWinEventsForAutomationEvent: _Callable[[_type.EVENTID,  # eventId
                                               _type.PROPERTYID,  # propertyId
                                               _Pointer[_struct.SAFEARRAY]],  # winEvents
                                              _type.HRESULT]
    GetWinEventsForAutomationEvent: _Callable[[_type.EVENTID,  # eventId
                                               _type.PROPERTYID,  # propertyId
                                               _Pointer[_Pointer[_struct.SAFEARRAY]]],  # winEvents
                                              _type.HRESULT]


class IUIAutomationProxyFactoryMapping(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT]],  # count
                         _type.HRESULT]
    GetTable: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # table
                        _type.HRESULT]
    GetEntry: _Callable[[_type.UINT,  # index
                         _Pointer[IUIAutomationProxyFactoryEntry]],  # entry
                        _type.HRESULT]
    SetTable: _Callable[[_Pointer[_struct.SAFEARRAY]],  # factoryList
                        _type.HRESULT]
    InsertEntries: _Callable[[_type.UINT,  # before
                              _Pointer[_struct.SAFEARRAY]],  # factoryList
                             _type.HRESULT]
    InsertEntry: _Callable[[_type.UINT,  # before
                            IUIAutomationProxyFactoryEntry],  # factory
                           _type.HRESULT]
    RemoveEntry: _Callable[[_type.UINT],  # index
                           _type.HRESULT]
    ClearTable: _Callable[[],
                          _type.HRESULT]
    RestoreDefaultTable: _Callable[[],
                                   _type.HRESULT]


class IUIAutomationEventHandlerGroup(_Unknwnbase.IUnknown):
    AddActiveTextPositionChangedEventHandler: _Callable[[_enum.TreeScope,  # scope
                                                         IUIAutomationCacheRequest,  # cacheRequest
                                                         IUIAutomationActiveTextPositionChangedEventHandler],  # handler
                                                        _type.HRESULT]
    AddAutomationEventHandler: _Callable[[_type.EVENTID,  # eventId
                                          _enum.TreeScope,  # scope
                                          IUIAutomationCacheRequest,  # cacheRequest
                                          IUIAutomationEventHandler],  # handler
                                         _type.HRESULT]
    AddChangesEventHandler: _Callable[[_enum.TreeScope,  # scope
                                       _Pointer[_type.c_int],  # changeTypes
                                       _type.c_int,  # changesCount
                                       IUIAutomationCacheRequest,  # cacheRequest
                                       IUIAutomationChangesEventHandler],  # handler
                                      _type.HRESULT]
    AddNotificationEventHandler: _Callable[[_enum.TreeScope,  # scope
                                            IUIAutomationCacheRequest,  # cacheRequest
                                            IUIAutomationNotificationEventHandler],  # handler
                                           _type.HRESULT]
    AddPropertyChangedEventHandler: _Callable[[_enum.TreeScope,  # scope
                                               IUIAutomationCacheRequest,  # cacheRequest
                                               IUIAutomationPropertyChangedEventHandler,  # handler
                                               _Pointer[_type.PROPERTYID],  # propertyArray
                                               _type.c_int],  # propertyCount
                                              _type.HRESULT]
    AddStructureChangedEventHandler: _Callable[[_enum.TreeScope,  # scope
                                                IUIAutomationCacheRequest,  # cacheRequest
                                                IUIAutomationStructureChangedEventHandler],  # handler
                                               _type.HRESULT]
    AddTextEditTextChangedEventHandler: _Callable[[_enum.TreeScope,  # scope
                                                   _enum.TextEditChangeType,  # textEditChangeType
                                                   IUIAutomationCacheRequest,  # cacheRequest
                                                   IUIAutomationTextEditTextChangedEventHandler],  # handler
                                                  _type.HRESULT]


class IUIAutomation(_Unknwnbase.IUnknown):
    CompareElements: _Callable[[IUIAutomationElement,  # el1
                                IUIAutomationElement,  # el2
                                _Pointer[_type.BOOL]],  # areSame
                               _type.HRESULT]
    CompareRuntimeIds: _Callable[[_Pointer[_struct.SAFEARRAY],  # runtimeId1
                                  _Pointer[_struct.SAFEARRAY],  # runtimeId2
                                  _Pointer[_type.BOOL]],  # areSame
                                 _type.HRESULT]
    GetRootElement: _Callable[[_Pointer[IUIAutomationElement]],  # root
                              _type.HRESULT]
    ElementFromHandle: _Callable[[_type.UIA_HWND,  # hwnd
                                  _Pointer[IUIAutomationElement]],  # element
                                 _type.HRESULT]
    ElementFromPoint: _Callable[[_struct.POINT,  # pt
                                 _Pointer[IUIAutomationElement]],  # element
                                _type.HRESULT]
    GetFocusedElement: _Callable[[_Pointer[IUIAutomationElement]],  # element
                                 _type.HRESULT]
    GetRootElementBuildCache: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                         _Pointer[IUIAutomationElement]],  # root
                                        _type.HRESULT]
    ElementFromHandleBuildCache: _Callable[[_type.UIA_HWND,  # hwnd
                                            IUIAutomationCacheRequest,  # cacheRequest
                                            _Pointer[IUIAutomationElement]],  # element
                                           _type.HRESULT]
    ElementFromPointBuildCache: _Callable[[_struct.POINT,  # pt
                                           IUIAutomationCacheRequest,  # cacheRequest
                                           _Pointer[IUIAutomationElement]],  # element
                                          _type.HRESULT]
    GetFocusedElementBuildCache: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                            _Pointer[IUIAutomationElement]],  # element
                                           _type.HRESULT]
    CreateTreeWalker: _Callable[[IUIAutomationCondition,  # pCondition
                                 _Pointer[IUIAutomationTreeWalker]],  # walker
                                _type.HRESULT]
    get_ControlViewWalker: _Callable[[_Pointer[IUIAutomationTreeWalker]],  # walker
                                     _type.HRESULT]
    get_ContentViewWalker: _Callable[[_Pointer[IUIAutomationTreeWalker]],  # walker
                                     _type.HRESULT]
    get_RawViewWalker: _Callable[[_Pointer[IUIAutomationTreeWalker]],  # walker
                                 _type.HRESULT]
    get_RawViewCondition: _Callable[[_Pointer[IUIAutomationCondition]],  # condition
                                    _type.HRESULT]
    get_ControlViewCondition: _Callable[[_Pointer[IUIAutomationCondition]],  # condition
                                        _type.HRESULT]
    get_ContentViewCondition: _Callable[[_Pointer[IUIAutomationCondition]],  # condition
                                        _type.HRESULT]
    CreateCacheRequest: _Callable[[_Pointer[IUIAutomationCacheRequest]],  # cacheRequest
                                  _type.HRESULT]
    CreateTrueCondition: _Callable[[_Pointer[IUIAutomationCondition]],  # newCondition
                                   _type.HRESULT]
    CreateFalseCondition: _Callable[[_Pointer[IUIAutomationCondition]],  # newCondition
                                    _type.HRESULT]
    CreatePropertyCondition: _Callable[[_type.PROPERTYID,  # propertyId
                                        _struct.VARIANT,  # value
                                        _Pointer[IUIAutomationCondition]],  # newCondition
                                       _type.HRESULT]
    CreatePropertyConditionEx: _Callable[[_type.PROPERTYID,  # propertyId
                                          _struct.VARIANT,  # value
                                          _enum.PropertyConditionFlags,  # flags
                                          _Pointer[IUIAutomationCondition]],  # newCondition
                                         _type.HRESULT]
    CreateAndCondition: _Callable[[IUIAutomationCondition,  # condition1
                                   IUIAutomationCondition,  # condition2
                                   _Pointer[IUIAutomationCondition]],  # newCondition
                                  _type.HRESULT]
    CreateAndConditionFromArray: _Callable[[_Pointer[_struct.SAFEARRAY],  # conditions
                                            _Pointer[IUIAutomationCondition]],  # newCondition
                                           _type.HRESULT]
    CreateAndConditionFromNativeArray: _Callable[[_Pointer[IUIAutomationCondition],  # conditions
                                                  _type.c_int,  # conditionCount
                                                  _Pointer[IUIAutomationCondition]],  # newCondition
                                                 _type.HRESULT]
    CreateOrCondition: _Callable[[IUIAutomationCondition,  # condition1
                                  IUIAutomationCondition,  # condition2
                                  _Pointer[IUIAutomationCondition]],  # newCondition
                                 _type.HRESULT]
    CreateOrConditionFromArray: _Callable[[_Pointer[_struct.SAFEARRAY],  # conditions
                                           _Pointer[IUIAutomationCondition]],  # newCondition
                                          _type.HRESULT]
    CreateOrConditionFromNativeArray: _Callable[[_Pointer[IUIAutomationCondition],  # conditions
                                                 _type.c_int,  # conditionCount
                                                 _Pointer[IUIAutomationCondition]],  # newCondition
                                                _type.HRESULT]
    CreateNotCondition: _Callable[[IUIAutomationCondition,  # condition
                                   _Pointer[IUIAutomationCondition]],  # newCondition
                                  _type.HRESULT]
    AddAutomationEventHandler: _Callable[[_type.EVENTID,  # eventId
                                          IUIAutomationElement,  # element
                                          _enum.TreeScope,  # scope
                                          IUIAutomationCacheRequest,  # cacheRequest
                                          IUIAutomationEventHandler],  # handler
                                         _type.HRESULT]
    RemoveAutomationEventHandler: _Callable[[_type.EVENTID,  # eventId
                                             IUIAutomationElement,  # element
                                             IUIAutomationEventHandler],  # handler
                                            _type.HRESULT]
    AddPropertyChangedEventHandlerNativeArray: _Callable[[IUIAutomationElement,  # element
                                                          _enum.TreeScope,  # scope
                                                          IUIAutomationCacheRequest,  # cacheRequest
                                                          IUIAutomationPropertyChangedEventHandler,  # handler
                                                          _Pointer[_type.PROPERTYID],  # propertyArray
                                                          _type.c_int],  # propertyCount
                                                         _type.HRESULT]
    AddPropertyChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                               _enum.TreeScope,  # scope
                                               IUIAutomationCacheRequest,  # cacheRequest
                                               IUIAutomationPropertyChangedEventHandler,  # handler
                                               _Pointer[_struct.SAFEARRAY]],  # propertyArray
                                              _type.HRESULT]
    RemovePropertyChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                  IUIAutomationPropertyChangedEventHandler],  # handler
                                                 _type.HRESULT]
    AddStructureChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                _enum.TreeScope,  # scope
                                                IUIAutomationCacheRequest,  # cacheRequest
                                                IUIAutomationStructureChangedEventHandler],  # handler
                                               _type.HRESULT]
    RemoveStructureChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                   IUIAutomationStructureChangedEventHandler],  # handler
                                                  _type.HRESULT]
    AddFocusChangedEventHandler: _Callable[[IUIAutomationCacheRequest,  # cacheRequest
                                            IUIAutomationFocusChangedEventHandler],  # handler
                                           _type.HRESULT]
    RemoveFocusChangedEventHandler: _Callable[[IUIAutomationFocusChangedEventHandler],  # handler
                                              _type.HRESULT]
    RemoveAllEventHandlers: _Callable[[],
                                      _type.HRESULT]
    IntNativeArrayToSafeArray: _Callable[[_Pointer[_type.c_int],  # array
                                          _type.c_int,  # arrayCount
                                          _Pointer[_Pointer[_struct.SAFEARRAY]]],  # safeArray
                                         _type.HRESULT]
    IntSafeArrayToNativeArray: _Callable[[_Pointer[_struct.SAFEARRAY],  # intArray
                                          _Pointer[_Pointer[_type.c_int]],  # array
                                          _Pointer[_type.c_int]],  # arrayCount
                                         _type.HRESULT]
    RectToVariant: _Callable[[_struct.RECT,  # rc
                              _Pointer[_struct.VARIANT]],  # var
                             _type.HRESULT]
    VariantToRect: _Callable[[_struct.VARIANT,  # var
                              _Pointer[_struct.RECT]],  # rc
                             _type.HRESULT]
    SafeArrayToRectNativeArray: _Callable[[_Pointer[_struct.SAFEARRAY],  # rects
                                           _Pointer[_Pointer[_struct.RECT]],  # rectArray
                                           _Pointer[_type.c_int]],  # rectArrayCount
                                          _type.HRESULT]
    CreateProxyFactoryEntry: _Callable[[IUIAutomationProxyFactory,  # factory
                                        _Pointer[IUIAutomationProxyFactoryEntry]],  # factoryEntry
                                       _type.HRESULT]
    get_ProxyFactoryMapping: _Callable[[_Pointer[IUIAutomationProxyFactoryMapping]],  # factoryMapping
                                       _type.HRESULT]
    GetPropertyProgrammaticName: _Callable[[_type.PROPERTYID,  # property
                                            _Pointer[_type.BSTR]],  # name
                                           _type.HRESULT]
    GetPatternProgrammaticName: _Callable[[_type.PATTERNID,  # pattern
                                           _Pointer[_type.BSTR]],  # name
                                          _type.HRESULT]
    PollForPotentialSupportedPatterns: _Callable[[IUIAutomationElement,  # pElement
                                                  _Pointer[_Pointer[_struct.SAFEARRAY]],  # patternIds
                                                  _Pointer[_Pointer[_struct.SAFEARRAY]]],  # patternNames
                                                 _type.HRESULT]
    PollForPotentialSupportedProperties: _Callable[[IUIAutomationElement,  # pElement
                                                    _Pointer[_Pointer[_struct.SAFEARRAY]],  # propertyIds
                                                    _Pointer[_Pointer[_struct.SAFEARRAY]]],  # propertyNames
                                                   _type.HRESULT]
    CheckNotSupported: _Callable[[_struct.VARIANT,  # value
                                  _Pointer[_type.BOOL]],  # isNotSupported
                                 _type.HRESULT]
    get_ReservedNotSupportedValue: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # notSupportedValue
                                             _type.HRESULT]
    get_ReservedMixedAttributeValue: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # mixedAttributeValue
                                               _type.HRESULT]
    ElementFromIAccessible: _Callable[[_oleacc.IAccessible,  # accessible
                                       _type.c_int,  # childId
                                       _Pointer[IUIAutomationElement]],  # element
                                      _type.HRESULT]
    ElementFromIAccessibleBuildCache: _Callable[[_oleacc.IAccessible,  # accessible
                                                 _type.c_int,  # childId
                                                 IUIAutomationCacheRequest,  # cacheRequest
                                                 _Pointer[IUIAutomationElement]],  # element
                                                _type.HRESULT]


class IUIAutomation2(IUIAutomation):
    get_AutoSetFocus: _Callable[[_Pointer[_type.BOOL]],  # autoSetFocus
                                _type.HRESULT]
    put_AutoSetFocus: _Callable[[_type.BOOL],  # autoSetFocus
                                _type.HRESULT]
    get_ConnectionTimeout: _Callable[[_Pointer[_type.DWORD]],  # timeout
                                     _type.HRESULT]
    put_ConnectionTimeout: _Callable[[_type.DWORD],  # timeout
                                     _type.HRESULT]
    get_TransactionTimeout: _Callable[[_Pointer[_type.DWORD]],  # timeout
                                      _type.HRESULT]
    put_TransactionTimeout: _Callable[[_type.DWORD],  # timeout
                                      _type.HRESULT]


class IUIAutomation3(IUIAutomation2):
    AddTextEditTextChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                   _enum.TreeScope,  # scope
                                                   _enum.TextEditChangeType,  # textEditChangeType
                                                   IUIAutomationCacheRequest,  # cacheRequest
                                                   IUIAutomationTextEditTextChangedEventHandler],  # handler
                                                  _type.HRESULT]
    RemoveTextEditTextChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                      IUIAutomationTextEditTextChangedEventHandler],  # handler
                                                     _type.HRESULT]


class IUIAutomation4(IUIAutomation3):
    AddChangesEventHandler: _Callable[[IUIAutomationElement,  # element
                                       _enum.TreeScope,  # scope
                                       _Pointer[_type.c_int],  # changeTypes
                                       _type.c_int,  # changesCount
                                       IUIAutomationCacheRequest,  # pCacheRequest
                                       IUIAutomationChangesEventHandler],  # handler
                                      _type.HRESULT]
    RemoveChangesEventHandler: _Callable[[IUIAutomationElement,  # element
                                          IUIAutomationChangesEventHandler],  # handler
                                         _type.HRESULT]


class IUIAutomation5(IUIAutomation4):
    AddNotificationEventHandler: _Callable[[IUIAutomationElement,  # element
                                            _enum.TreeScope,  # scope
                                            IUIAutomationCacheRequest,  # cacheRequest
                                            IUIAutomationNotificationEventHandler],  # handler
                                           _type.HRESULT]
    RemoveNotificationEventHandler: _Callable[[IUIAutomationElement,  # element
                                               IUIAutomationNotificationEventHandler],  # handler
                                              _type.HRESULT]


class IUIAutomation6(IUIAutomation5):
    CreateEventHandlerGroup: _Callable[[_Pointer[IUIAutomationEventHandlerGroup]],  # handlerGroup
                                       _type.HRESULT]
    AddEventHandlerGroup: _Callable[[IUIAutomationElement,  # element
                                     IUIAutomationEventHandlerGroup],  # handlerGroup
                                    _type.HRESULT]
    RemoveEventHandlerGroup: _Callable[[IUIAutomationElement,  # element
                                        IUIAutomationEventHandlerGroup],  # handlerGroup
                                       _type.HRESULT]
    get_ConnectionRecoveryBehavior: _Callable[[_Pointer[_enum.ConnectionRecoveryBehaviorOptions]],  # connectionRecoveryBehaviorOptions
                                              _type.HRESULT]
    put_ConnectionRecoveryBehavior: _Callable[[_enum.ConnectionRecoveryBehaviorOptions],  # connectionRecoveryBehaviorOptions
                                              _type.HRESULT]
    get_CoalesceEvents: _Callable[[_Pointer[_enum.CoalesceEventsOptions]],  # coalesceEventsOptions
                                  _type.HRESULT]
    put_CoalesceEvents: _Callable[[_enum.CoalesceEventsOptions],  # coalesceEventsOptions
                                  _type.HRESULT]
    AddActiveTextPositionChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                         _enum.TreeScope,  # scope
                                                         IUIAutomationCacheRequest,  # cacheRequest
                                                         IUIAutomationActiveTextPositionChangedEventHandler],  # handler
                                                        _type.HRESULT]
    RemoveActiveTextPositionChangedEventHandler: _Callable[[IUIAutomationElement,  # element
                                                            IUIAutomationActiveTextPositionChangedEventHandler],  # handler
                                                           _type.HRESULT]
