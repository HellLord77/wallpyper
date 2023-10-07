from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oleacc as _oleacc
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IRawElementProviderSimple(_Unknwnbase.IUnknown):
    get_ProviderOptions: _Callable[[_Pointer[_enum.ProviderOptions]],  # pRetVal
                                   _type.HRESULT]
    GetPatternProvider: _Callable[[_type.PATTERNID,  # patternId
                                   _Pointer[_Unknwnbase.IUnknown]],  # pRetVal
                                  _type.HRESULT]
    GetPropertyValue: _Callable[[_type.PROPERTYID,  # propertyId
                                 _Pointer[_struct.VARIANT]],  # pRetVal
                                _type.HRESULT]
    get_HostRawElementProvider: _Callable[[_Pointer[IRawElementProviderSimple]],  # pRetVal
                                          _type.HRESULT]


class IAccessibleEx(_Unknwnbase.IUnknown):
    GetObjectForChild: _Callable[[_type.c_long,  # idChild
                                  _Pointer[IAccessibleEx]],  # pRetVal
                                 _type.HRESULT]
    GetIAccessiblePair: _Callable[[_Pointer[_oleacc.IAccessible],  # ppAcc
                                   _Pointer[_type.c_long]],  # pidChild
                                  _type.HRESULT]
    GetRuntimeId: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                            _type.HRESULT]
    ConvertReturnedElement: _Callable[[IRawElementProviderSimple,  # pIn
                                       _Pointer[IAccessibleEx]],  # ppRetValOut
                                      _type.HRESULT]


class IRawElementProviderSimple2(IRawElementProviderSimple):
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]


class IRawElementProviderSimple3(IRawElementProviderSimple2):
    GetMetadataValue: _Callable[[_type.c_int,  # targetId
                                 _type.METADATAID,  # metadataId
                                 _Pointer[_struct.VARIANT]],  # returnVal
                                _type.HRESULT]


class IRawElementProviderFragmentRoot(_Unknwnbase.IUnknown):
    ElementProviderFromPoint: _Callable[[_type.c_double,  # x
                                         _type.c_double,  # y
                                         _Pointer[IRawElementProviderFragment]],  # pRetVal
                                        _type.HRESULT]
    GetFocus: _Callable[[_Pointer[IRawElementProviderFragment]],  # pRetVal
                        _type.HRESULT]


class IRawElementProviderFragment(_Unknwnbase.IUnknown):
    Navigate: _Callable[[_enum.NavigateDirection,  # direction
                         _Pointer[IRawElementProviderFragment]],  # pRetVal
                        _type.HRESULT]
    GetRuntimeId: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                            _type.HRESULT]
    get_BoundingRectangle: _Callable[[_Pointer[_struct.UiaRect]],  # pRetVal
                                     _type.HRESULT]
    GetEmbeddedFragmentRoots: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                        _type.HRESULT]
    SetFocus: _Callable[[],
                        _type.HRESULT]
    get_FragmentRoot: _Callable[[_Pointer[IRawElementProviderFragmentRoot]],  # pRetVal
                                _type.HRESULT]


class IRawElementProviderAdviseEvents(_Unknwnbase.IUnknown):
    AdviseEventAdded: _Callable[[_type.EVENTID,  # eventId
                                 _Pointer[_struct.SAFEARRAY]],  # propertyIDs
                                _type.HRESULT]
    AdviseEventRemoved: _Callable[[_type.EVENTID,  # eventId
                                   _Pointer[_struct.SAFEARRAY]],  # propertyIDs
                                  _type.HRESULT]


class IRawElementProviderHwndOverride(_Unknwnbase.IUnknown):
    GetOverrideProviderForHwnd: _Callable[[_type.HWND,  # hwnd
                                           _Pointer[IRawElementProviderSimple]],  # pRetVal
                                          _type.HRESULT]


class IProxyProviderWinEventSink(_Unknwnbase.IUnknown):
    AddAutomationPropertyChangedEvent: _Callable[[IRawElementProviderSimple,  # pProvider
                                                  _type.PROPERTYID,  # id
                                                  _struct.VARIANT],  # newValue
                                                 _type.HRESULT]
    AddAutomationEvent: _Callable[[IRawElementProviderSimple,  # pProvider
                                   _type.EVENTID],  # id
                                  _type.HRESULT]
    AddStructureChangedEvent: _Callable[[IRawElementProviderSimple,  # pProvider
                                         _enum.StructureChangeType,  # structureChangeType
                                         _Pointer[_struct.SAFEARRAY]],  # runtimeId
                                        _type.HRESULT]


class IProxyProviderWinEventHandler(_Unknwnbase.IUnknown):
    RespondToWinEvent: _Callable[[_type.DWORD,  # idWinEvent
                                  _type.HWND,  # hwnd
                                  _type.LONG,  # idObject
                                  _type.LONG,  # idChild
                                  IProxyProviderWinEventSink],  # pSink
                                 _type.HRESULT]


class IRawElementProviderWindowlessSite(_Unknwnbase.IUnknown):
    GetAdjacentFragment: _Callable[[_enum.NavigateDirection,  # direction
                                    _Pointer[IRawElementProviderFragment]],  # ppParent
                                   _type.HRESULT]
    GetRuntimeIdPrefix: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                  _type.HRESULT]


class IAccessibleHostingElementProviders(_Unknwnbase.IUnknown):
    GetEmbeddedFragmentRoots: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                        _type.HRESULT]
    GetObjectIdForProvider: _Callable[[IRawElementProviderSimple,  # pProvider
                                       _Pointer[_type.c_long]],  # pidObject
                                      _type.HRESULT]


class IRawElementProviderHostingAccessibles(_Unknwnbase.IUnknown):
    GetEmbeddedAccessibles: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                      _type.HRESULT]


class IDockProvider(_Unknwnbase.IUnknown):
    SetDockPosition: _Callable[[_enum.DockPosition],  # dockPosition
                               _type.HRESULT]
    get_DockPosition: _Callable[[_Pointer[_enum.DockPosition]],  # pRetVal
                                _type.HRESULT]


class IExpandCollapseProvider(_Unknwnbase.IUnknown):
    Expand: _Callable[[],
                      _type.HRESULT]
    Collapse: _Callable[[],
                        _type.HRESULT]
    get_ExpandCollapseState: _Callable[[_Pointer[_enum.ExpandCollapseState]],  # pRetVal
                                       _type.HRESULT]


class IGridProvider(_Unknwnbase.IUnknown):
    GetItem: _Callable[[_type.c_int,  # row
                        _type.c_int,  # column
                        _Pointer[IRawElementProviderSimple]],  # pRetVal
                       _type.HRESULT]
    get_RowCount: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                            _type.HRESULT]
    get_ColumnCount: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                               _type.HRESULT]


class IGridItemProvider(_Unknwnbase.IUnknown):
    get_Row: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                       _type.HRESULT]
    get_Column: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                          _type.HRESULT]
    get_RowSpan: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                           _type.HRESULT]
    get_ColumnSpan: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                              _type.HRESULT]
    get_ContainingGrid: _Callable[[_Pointer[IRawElementProviderSimple]],  # pRetVal
                                  _type.HRESULT]


class _IInvokeProvider:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IInvokeProvider(_IInvokeProvider, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IInvokeProvider_impl(_IInvokeProvider, _Unknwnbase.IUnknown_impl):
    pass


class IMultipleViewProvider(_Unknwnbase.IUnknown):
    GetViewName: _Callable[[_type.c_int,  # viewId
                            _Pointer[_type.BSTR]],  # pRetVal
                           _type.HRESULT]
    SetCurrentView: _Callable[[_type.c_int],  # viewId
                              _type.HRESULT]
    get_CurrentView: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                               _type.HRESULT]
    GetSupportedViews: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                 _type.HRESULT]


class IRangeValueProvider(_Unknwnbase.IUnknown):
    SetValue: _Callable[[_type.c_double],  # val
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                         _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                              _type.HRESULT]
    get_Maximum: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                           _type.HRESULT]
    get_Minimum: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                           _type.HRESULT]
    get_LargeChange: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                               _type.HRESULT]
    get_SmallChange: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                               _type.HRESULT]


class IScrollItemProvider(_Unknwnbase.IUnknown):
    ScrollIntoView: _Callable[[],
                              _type.HRESULT]


class ISelectionProvider(_Unknwnbase.IUnknown):
    GetSelection: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                            _type.HRESULT]
    get_CanSelectMultiple: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                                     _type.HRESULT]
    get_IsSelectionRequired: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                                       _type.HRESULT]


class ISelectionProvider2(ISelectionProvider):
    get_FirstSelectedItem: _Callable[[_Pointer[IRawElementProviderSimple]],  # retVal
                                     _type.HRESULT]
    get_LastSelectedItem: _Callable[[_Pointer[IRawElementProviderSimple]],  # retVal
                                    _type.HRESULT]
    get_CurrentSelectedItem: _Callable[[_Pointer[IRawElementProviderSimple]],  # retVal
                                       _type.HRESULT]
    get_ItemCount: _Callable[[_Pointer[_type.c_int]],  # retVal
                             _type.HRESULT]


class IScrollProvider(_Unknwnbase.IUnknown):
    Scroll: _Callable[[_enum.ScrollAmount,  # horizontalAmount
                       _enum.ScrollAmount],  # verticalAmount
                      _type.HRESULT]
    SetScrollPercent: _Callable[[_type.c_double,  # horizontalPercent
                                 _type.c_double],  # verticalPercent
                                _type.HRESULT]
    get_HorizontalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                                           _type.HRESULT]
    get_VerticalScrollPercent: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                                         _type.HRESULT]
    get_HorizontalViewSize: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                                      _type.HRESULT]
    get_VerticalViewSize: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                                    _type.HRESULT]
    get_HorizontallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                                          _type.HRESULT]
    get_VerticallyScrollable: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                                        _type.HRESULT]


class ISelectionItemProvider(_Unknwnbase.IUnknown):
    Select: _Callable[[],
                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    get_IsSelected: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                              _type.HRESULT]
    get_SelectionContainer: _Callable[[_Pointer[IRawElementProviderSimple]],  # pRetVal
                                      _type.HRESULT]


class ISynchronizedInputProvider(_Unknwnbase.IUnknown):
    StartListening: _Callable[[_enum.SynchronizedInputType],  # inputType
                              _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]


class ITableProvider(_Unknwnbase.IUnknown):
    GetRowHeaders: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                             _type.HRESULT]
    GetColumnHeaders: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                _type.HRESULT]
    get_RowOrColumnMajor: _Callable[[_Pointer[_enum.RowOrColumnMajor]],  # pRetVal
                                    _type.HRESULT]


class ITableItemProvider(_Unknwnbase.IUnknown):
    GetRowHeaderItems: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                 _type.HRESULT]
    GetColumnHeaderItems: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                    _type.HRESULT]


class IToggleProvider(_Unknwnbase.IUnknown):
    Toggle: _Callable[[],
                      _type.HRESULT]
    get_ToggleState: _Callable[[_Pointer[_enum.ToggleState]],  # pRetVal
                               _type.HRESULT]


class ITransformProvider(_Unknwnbase.IUnknown):
    Move: _Callable[[_type.c_double,  # x
                     _type.c_double],  # y
                    _type.HRESULT]
    Resize: _Callable[[_type.c_double,  # width
                       _type.c_double],  # height
                      _type.HRESULT]
    Rotate: _Callable[[_type.c_double],  # degrees
                      _type.HRESULT]
    get_CanMove: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                           _type.HRESULT]
    get_CanResize: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                             _type.HRESULT]
    get_CanRotate: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                             _type.HRESULT]


class IValueProvider(_Unknwnbase.IUnknown):
    SetValue: _Callable[[_type.LPCWSTR],  # val
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.BSTR]],  # pRetVal
                         _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                              _type.HRESULT]


class IWindowProvider(_Unknwnbase.IUnknown):
    SetVisualState: _Callable[[_enum.WindowVisualState],  # state
                              _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    WaitForInputIdle: _Callable[[_type.c_int,  # milliseconds
                                 _Pointer[_type.BOOL]],  # pRetVal
                                _type.HRESULT]
    get_CanMaximize: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                               _type.HRESULT]
    get_CanMinimize: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                               _type.HRESULT]
    get_IsModal: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                           _type.HRESULT]
    get_WindowVisualState: _Callable[[_Pointer[_enum.WindowVisualState]],  # pRetVal
                                     _type.HRESULT]
    get_WindowInteractionState: _Callable[[_Pointer[_enum.WindowInteractionState]],  # pRetVal
                                          _type.HRESULT]
    get_IsTopmost: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                             _type.HRESULT]


class ILegacyIAccessibleProvider(_Unknwnbase.IUnknown):
    Select: _Callable[[_type.c_long],  # flagsSelect
                      _type.HRESULT]
    DoDefaultAction: _Callable[[],
                               _type.HRESULT]
    SetValue: _Callable[[_type.LPCWSTR],  # szValue
                        _type.HRESULT]
    GetIAccessible: _Callable[[_Pointer[_oleacc.IAccessible]],  # ppAccessible
                              _type.HRESULT]
    get_ChildId: _Callable[[_Pointer[_type.c_int]],  # pRetVal
                           _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # pszName
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.BSTR]],  # pszValue
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.BSTR]],  # pszDescription
                               _type.HRESULT]
    get_Role: _Callable[[_Pointer[_type.DWORD]],  # pdwRole
                        _type.HRESULT]
    get_State: _Callable[[_Pointer[_type.DWORD]],  # pdwState
                         _type.HRESULT]
    get_Help: _Callable[[_Pointer[_type.BSTR]],  # pszHelp
                        _type.HRESULT]
    get_KeyboardShortcut: _Callable[[_Pointer[_type.BSTR]],  # pszKeyboardShortcut
                                    _type.HRESULT]
    GetSelection: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pvarSelectedChildren
                            _type.HRESULT]
    get_DefaultAction: _Callable[[_Pointer[_type.BSTR]],  # pszDefaultAction
                                 _type.HRESULT]


class IItemContainerProvider(_Unknwnbase.IUnknown):
    FindItemByProperty: _Callable[[IRawElementProviderSimple,  # pStartAfter
                                   _type.PROPERTYID,  # propertyId
                                   _struct.VARIANT,  # value
                                   _Pointer[IRawElementProviderSimple]],  # pFound
                                  _type.HRESULT]


class IVirtualizedItemProvider(_Unknwnbase.IUnknown):
    Realize: _Callable[[],
                       _type.HRESULT]


class IObjectModelProvider(_Unknwnbase.IUnknown):
    GetUnderlyingObjectModel: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppUnknown
                                        _type.HRESULT]


class IAnnotationProvider(_Unknwnbase.IUnknown):
    get_AnnotationTypeId: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_AnnotationTypeName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                      _type.HRESULT]
    get_Author: _Callable[[_Pointer[_type.BSTR]],  # retVal
                          _type.HRESULT]
    get_DateTime: _Callable[[_Pointer[_type.BSTR]],  # retVal
                            _type.HRESULT]
    get_Target: _Callable[[_Pointer[IRawElementProviderSimple]],  # retVal
                          _type.HRESULT]


class IStylesProvider(_Unknwnbase.IUnknown):
    get_StyleId: _Callable[[_Pointer[_type.c_int]],  # retVal
                           _type.HRESULT]
    get_StyleName: _Callable[[_Pointer[_type.BSTR]],  # retVal
                             _type.HRESULT]
    get_FillColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                             _type.HRESULT]
    get_FillPatternStyle: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                    _type.HRESULT]
    get_Shape: _Callable[[_Pointer[_type.BSTR]],  # retVal
                         _type.HRESULT]
    get_FillPatternColor: _Callable[[_Pointer[_type.c_int]],  # retVal
                                    _type.HRESULT]
    get_ExtendedProperties: _Callable[[_Pointer[_type.BSTR]],  # retVal
                                      _type.HRESULT]


class ISpreadsheetProvider(_Unknwnbase.IUnknown):
    GetItemByName: _Callable[[_type.LPCWSTR,  # name
                              _Pointer[IRawElementProviderSimple]],  # pRetVal
                             _type.HRESULT]


class ISpreadsheetItemProvider(_Unknwnbase.IUnknown):
    get_Formula: _Callable[[_Pointer[_type.BSTR]],  # pRetVal
                           _type.HRESULT]
    GetAnnotationObjects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                    _type.HRESULT]
    GetAnnotationTypes: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                  _type.HRESULT]


class ITransformProvider2(ITransformProvider):
    Zoom: _Callable[[_type.c_double],  # zoom
                    _type.HRESULT]
    get_CanZoom: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                           _type.HRESULT]
    get_ZoomLevel: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                             _type.HRESULT]
    get_ZoomMinimum: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                               _type.HRESULT]
    get_ZoomMaximum: _Callable[[_Pointer[_type.c_double]],  # pRetVal
                               _type.HRESULT]
    ZoomByUnit: _Callable[[_enum.ZoomUnit],  # zoomUnit
                          _type.HRESULT]


class IDragProvider(_Unknwnbase.IUnknown):
    get_IsGrabbed: _Callable[[_Pointer[_type.BOOL]],  # pRetVal
                             _type.HRESULT]
    get_DropEffect: _Callable[[_Pointer[_type.BSTR]],  # pRetVal
                              _type.HRESULT]
    get_DropEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                               _type.HRESULT]
    GetGrabbedItems: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                               _type.HRESULT]


class IDropTargetProvider(_Unknwnbase.IUnknown):
    get_DropTargetEffect: _Callable[[_Pointer[_type.BSTR]],  # pRetVal
                                    _type.HRESULT]
    get_DropTargetEffects: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                     _type.HRESULT]


class ITextRangeProvider(_Unknwnbase.IUnknown):
    Clone: _Callable[[_Pointer[ITextRangeProvider]],  # pRetVal
                     _type.HRESULT]
    Compare: _Callable[[ITextRangeProvider,  # range
                        _Pointer[_type.BOOL]],  # pRetVal
                       _type.HRESULT]
    CompareEndpoints: _Callable[[_enum.TextPatternRangeEndpoint,  # endpoint
                                 ITextRangeProvider,  # targetRange
                                 _enum.TextPatternRangeEndpoint,  # targetEndpoint
                                 _Pointer[_type.c_int]],  # pRetVal
                                _type.HRESULT]
    ExpandToEnclosingUnit: _Callable[[_enum.TextUnit],  # unit
                                     _type.HRESULT]
    FindAttribute: _Callable[[_type.TEXTATTRIBUTEID,  # attributeId
                              _struct.VARIANT,  # val
                              _type.BOOL,  # backward
                              _Pointer[ITextRangeProvider]],  # pRetVal
                             _type.HRESULT]
    FindText: _Callable[[_type.BSTR,  # text
                         _type.BOOL,  # backward
                         _type.BOOL,  # ignoreCase
                         _Pointer[ITextRangeProvider]],  # pRetVal
                        _type.HRESULT]
    GetAttributeValue: _Callable[[_type.TEXTATTRIBUTEID,  # attributeId
                                  _Pointer[_struct.VARIANT]],  # pRetVal
                                 _type.HRESULT]
    GetBoundingRectangles: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                     _type.HRESULT]
    GetEnclosingElement: _Callable[[_Pointer[IRawElementProviderSimple]],  # pRetVal
                                   _type.HRESULT]
    GetText: _Callable[[_type.c_int,  # maxLength
                        _Pointer[_type.BSTR]],  # pRetVal
                       _type.HRESULT]
    Move: _Callable[[_enum.TextUnit,  # unit
                     _type.c_int,  # count
                     _Pointer[_type.c_int]],  # pRetVal
                    _type.HRESULT]
    MoveEndpointByUnit: _Callable[[_enum.TextPatternRangeEndpoint,  # endpoint
                                   _enum.TextUnit,  # unit
                                   _type.c_int,  # count
                                   _Pointer[_type.c_int]],  # pRetVal
                                  _type.HRESULT]
    MoveEndpointByRange: _Callable[[_enum.TextPatternRangeEndpoint,  # endpoint
                                    ITextRangeProvider,  # targetRange
                                    _enum.TextPatternRangeEndpoint],  # targetEndpoint
                                   _type.HRESULT]
    Select: _Callable[[],
                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    ScrollIntoView: _Callable[[_type.BOOL],  # alignToTop
                              _type.HRESULT]
    GetChildren: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                           _type.HRESULT]


class ITextProvider(_Unknwnbase.IUnknown):
    GetSelection: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                            _type.HRESULT]
    GetVisibleRanges: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]]],  # pRetVal
                                _type.HRESULT]
    RangeFromChild: _Callable[[IRawElementProviderSimple,  # childElement
                               _Pointer[ITextRangeProvider]],  # pRetVal
                              _type.HRESULT]
    RangeFromPoint: _Callable[[_struct.UiaPoint,  # point
                               _Pointer[ITextRangeProvider]],  # pRetVal
                              _type.HRESULT]
    get_DocumentRange: _Callable[[_Pointer[ITextRangeProvider]],  # pRetVal
                                 _type.HRESULT]
    get_SupportedTextSelection: _Callable[[_Pointer[_enum.SupportedTextSelection]],  # pRetVal
                                          _type.HRESULT]


class ITextProvider2(ITextProvider):
    RangeFromAnnotation: _Callable[[IRawElementProviderSimple,  # annotationElement
                                    _Pointer[ITextRangeProvider]],  # pRetVal
                                   _type.HRESULT]
    GetCaretRange: _Callable[[_Pointer[_type.BOOL],  # isActive
                              _Pointer[ITextRangeProvider]],  # pRetVal
                             _type.HRESULT]


class ITextEditProvider(ITextProvider):
    GetActiveComposition: _Callable[[_Pointer[ITextRangeProvider]],  # pRetVal
                                    _type.HRESULT]
    GetConversionTarget: _Callable[[_Pointer[ITextRangeProvider]],  # pRetVal
                                   _type.HRESULT]


class ITextRangeProvider2(ITextRangeProvider):
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]


class ITextChildProvider(_Unknwnbase.IUnknown):
    get_TextContainer: _Callable[[_Pointer[IRawElementProviderSimple]],  # pRetVal
                                 _type.HRESULT]
    get_TextRange: _Callable[[_Pointer[ITextRangeProvider]],  # pRetVal
                             _type.HRESULT]


class ICustomNavigationProvider(_Unknwnbase.IUnknown):
    Navigate: _Callable[[_enum.NavigateDirection,  # direction
                         _Pointer[IRawElementProviderSimple]],  # pRetVal
                        _type.HRESULT]


class IUIAutomationPatternInstance(_Unknwnbase.IUnknown):
    GetProperty: _Callable[[_type.UINT,  # index
                            _type.BOOL,  # cached
                            _enum.UIAutomationType,  # type
                            _type.c_void_p],  # pPtr
                           _type.HRESULT]
    CallMethod: _Callable[[_type.UINT,  # index
                           _Pointer[_struct.UIAutomationParameter],  # pParams
                           _type.UINT],  # cParams
                          _type.HRESULT]


class IUIAutomationPatternHandler(_Unknwnbase.IUnknown):
    CreateClientWrapper: _Callable[[IUIAutomationPatternInstance,  # pPatternInstance
                                    _Pointer[_Unknwnbase.IUnknown]],  # pClientWrapper
                                   _type.HRESULT]
    Dispatch: _Callable[[_Unknwnbase.IUnknown,  # pTarget
                         _type.UINT,  # index
                         _Pointer[_struct.UIAutomationParameter],  # pParams
                         _type.UINT],  # cParams
                        _type.HRESULT]


class IUIAutomationRegistrar(_Unknwnbase.IUnknown):
    RegisterProperty: _Callable[[_Pointer[_struct.UIAutomationPropertyInfo],  # property
                                 _Pointer[_type.PROPERTYID]],  # propertyId
                                _type.HRESULT]
    RegisterEvent: _Callable[[_Pointer[_struct.UIAutomationEventInfo],  # event
                              _Pointer[_type.EVENTID]],  # eventId
                             _type.HRESULT]
    RegisterPattern: _Callable[[_Pointer[_struct.UIAutomationPatternInfo],  # pattern
                                _Pointer[_type.PATTERNID],  # pPatternId
                                _Pointer[_type.PROPERTYID],  # pPatternAvailablePropertyId
                                _type.UINT,  # propertyIdCount
                                _Pointer[_type.PROPERTYID],  # pPropertyIds
                                _type.UINT,  # eventIdCount
                                _Pointer[_type.EVENTID]],  # pEventIds
                               _type.HRESULT]
