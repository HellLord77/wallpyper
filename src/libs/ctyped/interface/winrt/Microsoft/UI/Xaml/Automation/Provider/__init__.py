from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Automation as _Microsoft_UI_Xaml_Automation
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IAnnotationProvider(_inspectable.IInspectable):
    get_AnnotationTypeId: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_AnnotationTypeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_DateTime: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Target: _Callable[[_Pointer[IIRawElementProviderSimple]],  # value
                          _type.HRESULT]


class ICustomNavigationProvider(_inspectable.IInspectable):
    NavigateCustom: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection,  # direction
                               _Pointer[_inspectable.IInspectable]],  # result
                              _type.HRESULT]


class IDockProvider(_inspectable.IInspectable):
    get_DockPosition: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.DockPosition]],  # value
                                _type.HRESULT]
    SetDockPosition: _Callable[[_enum.Microsoft.UI.Xaml.Automation.DockPosition],  # dockPosition
                               _type.HRESULT]


class IDragProvider(_inspectable.IInspectable):
    get_IsGrabbed: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_DropEffect: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_DropEffects: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                _Pointer[_Pointer[_type.HSTRING]]],  # value
                               _type.HRESULT]
    GetGrabbedItems: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                               _type.HRESULT]


class IDropTargetProvider(_inspectable.IInspectable):
    get_DropEffect: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_DropEffects: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                _Pointer[_Pointer[_type.HSTRING]]],  # value
                               _type.HRESULT]


class IExpandCollapseProvider(_inspectable.IInspectable):
    get_ExpandCollapseState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.ExpandCollapseState]],  # value
                                       _type.HRESULT]
    Collapse: _Callable[[],
                        _type.HRESULT]
    Expand: _Callable[[],
                      _type.HRESULT]


class IGridItemProvider(_inspectable.IInspectable):
    get_Column: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_ColumnSpan: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_ContainingGrid: _Callable[[_Pointer[IIRawElementProviderSimple]],  # value
                                  _type.HRESULT]
    get_Row: _Callable[[_Pointer[_type.INT32]],  # value
                       _type.HRESULT]
    get_RowSpan: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]


class IGridProvider(_inspectable.IInspectable):
    get_ColumnCount: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_RowCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    GetItem: _Callable[[_type.INT32,  # row
                        _type.INT32,  # column
                        _Pointer[IIRawElementProviderSimple]],  # result
                       _type.HRESULT]


class IIRawElementProviderSimple(_inspectable.IInspectable):
    pass


class IInvokeProvider(_inspectable.IInspectable):
    Invoke: _Callable[[],
                      _type.HRESULT]


class IItemContainerProvider(_inspectable.IInspectable):
    FindItemByProperty: _Callable[[IIRawElementProviderSimple,  # startAfter
                                   _Microsoft_UI_Xaml_Automation.IAutomationProperty,  # automationProperty
                                   _inspectable.IInspectable,  # value
                                   _Pointer[IIRawElementProviderSimple]],  # result
                                  _type.HRESULT]


class IMultipleViewProvider(_inspectable.IInspectable):
    get_CurrentView: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    GetSupportedViews: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                  _Pointer[_Pointer[_type.INT32]]],  # result
                                 _type.HRESULT]
    GetViewName: _Callable[[_type.INT32,  # viewId
                            _Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    SetCurrentView: _Callable[[_type.INT32],  # viewId
                              _type.HRESULT]


class IObjectModelProvider(_inspectable.IInspectable):
    GetUnderlyingObjectModel: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                        _type.HRESULT]


class IRangeValueProvider(_inspectable.IInspectable):
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_LargeChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_Maximum: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_Minimum: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_SmallChange: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    SetValue: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]


class IScrollItemProvider(_inspectable.IInspectable):
    ScrollIntoView: _Callable[[],
                              _type.HRESULT]


class IScrollProvider(_inspectable.IInspectable):
    get_HorizontallyScrollable: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_HorizontalScrollPercent: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                           _type.HRESULT]
    get_HorizontalViewSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    get_VerticallyScrollable: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_VerticalScrollPercent: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    get_VerticalViewSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    Scroll: _Callable[[_enum.Microsoft.UI.Xaml.Automation.ScrollAmount,  # horizontalAmount
                       _enum.Microsoft.UI.Xaml.Automation.ScrollAmount],  # verticalAmount
                      _type.HRESULT]
    SetScrollPercent: _Callable[[_type.DOUBLE,  # horizontalPercent
                                 _type.DOUBLE],  # verticalPercent
                                _type.HRESULT]


class ISelectionItemProvider(_inspectable.IInspectable):
    get_IsSelected: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_SelectionContainer: _Callable[[_Pointer[IIRawElementProviderSimple]],  # value
                                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    Select: _Callable[[],
                      _type.HRESULT]


class ISelectionProvider(_inspectable.IInspectable):
    get_CanSelectMultiple: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsSelectionRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    GetSelection: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                             _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                            _type.HRESULT]


class ISpreadsheetItemProvider(_inspectable.IInspectable):
    get_Formula: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    GetAnnotationObjects: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                     _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                                    _type.HRESULT]
    GetAnnotationTypes: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                   _Pointer[_Pointer[_enum.Microsoft.UI.Xaml.Automation.AnnotationType]]],  # result
                                  _type.HRESULT]


class ISpreadsheetProvider(_inspectable.IInspectable):
    GetItemByName: _Callable[[_type.HSTRING,  # name
                              _Pointer[IIRawElementProviderSimple]],  # result
                             _type.HRESULT]


class IStylesProvider(_inspectable.IInspectable):
    get_ExtendedProperties: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_FillColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_FillPatternColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                    _type.HRESULT]
    get_FillPatternStyle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Shape: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_StyleId: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_StyleName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class ISynchronizedInputProvider(_inspectable.IInspectable):
    Cancel: _Callable[[],
                      _type.HRESULT]
    StartListening: _Callable[[_enum.Microsoft.UI.Xaml.Automation.SynchronizedInputType],  # inputType
                              _type.HRESULT]


class ITableItemProvider(_inspectable.IInspectable):
    GetColumnHeaderItems: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                     _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                                    _type.HRESULT]
    GetRowHeaderItems: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                  _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                                 _type.HRESULT]


class ITableProvider(_inspectable.IInspectable):
    get_RowOrColumnMajor: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.RowOrColumnMajor]],  # value
                                    _type.HRESULT]
    GetColumnHeaders: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                 _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                                _type.HRESULT]
    GetRowHeaders: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                              _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                             _type.HRESULT]


class ITextChildProvider(_inspectable.IInspectable):
    get_TextContainer: _Callable[[_Pointer[IIRawElementProviderSimple]],  # value
                                 _type.HRESULT]
    get_TextRange: _Callable[[_Pointer[ITextRangeProvider]],  # value
                             _type.HRESULT]


class ITextEditProvider(_inspectable.IInspectable):
    GetActiveComposition: _Callable[[_Pointer[ITextRangeProvider]],  # result
                                    _type.HRESULT]
    GetConversionTarget: _Callable[[_Pointer[ITextRangeProvider]],  # result
                                   _type.HRESULT]


class ITextProvider(_inspectable.IInspectable):
    get_DocumentRange: _Callable[[_Pointer[ITextRangeProvider]],  # value
                                 _type.HRESULT]
    get_SupportedTextSelection: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.SupportedTextSelection]],  # value
                                          _type.HRESULT]
    GetSelection: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                             _Pointer[_Pointer[ITextRangeProvider]]],  # result
                            _type.HRESULT]
    GetVisibleRanges: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                 _Pointer[_Pointer[ITextRangeProvider]]],  # result
                                _type.HRESULT]
    RangeFromChild: _Callable[[IIRawElementProviderSimple,  # childElement
                               _Pointer[ITextRangeProvider]],  # result
                              _type.HRESULT]
    RangeFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # screenLocation
                               _Pointer[ITextRangeProvider]],  # result
                              _type.HRESULT]


class ITextProvider2(_inspectable.IInspectable):
    RangeFromAnnotation: _Callable[[IIRawElementProviderSimple,  # annotationElement
                                    _Pointer[ITextRangeProvider]],  # result
                                   _type.HRESULT]
    GetCaretRange: _Callable[[_Pointer[_type.boolean],  # isActive
                              _Pointer[ITextRangeProvider]],  # returnValue
                             _type.HRESULT]


class ITextRangeProvider(_inspectable.IInspectable):
    Clone: _Callable[[_Pointer[ITextRangeProvider]],  # result
                     _type.HRESULT]
    Compare: _Callable[[ITextRangeProvider,  # textRangeProvider
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    CompareEndpoints: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint,  # endpoint
                                 ITextRangeProvider,  # textRangeProvider
                                 _enum.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint,  # targetEndpoint
                                 _Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    ExpandToEnclosingUnit: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Text.TextUnit],  # unit
                                     _type.HRESULT]
    FindAttribute: _Callable[[_type.INT32,  # attributeId
                              _inspectable.IInspectable,  # value
                              _type.boolean,  # backward
                              _Pointer[ITextRangeProvider]],  # result
                             _type.HRESULT]
    FindText: _Callable[[_type.HSTRING,  # text
                         _type.boolean,  # backward
                         _type.boolean,  # ignoreCase
                         _Pointer[ITextRangeProvider]],  # result
                        _type.HRESULT]
    GetAttributeValue: _Callable[[_type.INT32,  # attributeId
                                  _Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    GetBoundingRectangles: _Callable[[_Pointer[_type.UINT32],  # __returnValueSize
                                      _Pointer[_Pointer[_type.DOUBLE]]],  # returnValue
                                     _type.HRESULT]
    GetEnclosingElement: _Callable[[_Pointer[IIRawElementProviderSimple]],  # result
                                   _type.HRESULT]
    GetText: _Callable[[_type.INT32,  # maxLength
                        _Pointer[_type.HSTRING]],  # result
                       _type.HRESULT]
    Move: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Text.TextUnit,  # unit
                     _type.INT32,  # count
                     _Pointer[_type.INT32]],  # result
                    _type.HRESULT]
    MoveEndpointByUnit: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint,  # endpoint
                                   _enum.Microsoft.UI.Xaml.Automation.Text.TextUnit,  # unit
                                   _type.INT32,  # count
                                   _Pointer[_type.INT32]],  # result
                                  _type.HRESULT]
    MoveEndpointByRange: _Callable[[_enum.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint,  # endpoint
                                    ITextRangeProvider,  # textRangeProvider
                                    _enum.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint],  # targetEndpoint
                                   _type.HRESULT]
    Select: _Callable[[],
                      _type.HRESULT]
    AddToSelection: _Callable[[],
                              _type.HRESULT]
    RemoveFromSelection: _Callable[[],
                                   _type.HRESULT]
    ScrollIntoView: _Callable[[_type.boolean],  # alignToTop
                              _type.HRESULT]
    GetChildren: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                            _Pointer[_Pointer[IIRawElementProviderSimple]]],  # result
                           _type.HRESULT]


class ITextRangeProvider2(_inspectable.IInspectable):
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]


class IToggleProvider(_inspectable.IInspectable):
    get_ToggleState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.ToggleState]],  # value
                               _type.HRESULT]
    Toggle: _Callable[[],
                      _type.HRESULT]


class ITransformProvider(_inspectable.IInspectable):
    get_CanMove: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CanResize: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanRotate: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    Move: _Callable[[_type.DOUBLE,  # x
                     _type.DOUBLE],  # y
                    _type.HRESULT]
    Resize: _Callable[[_type.DOUBLE,  # width
                       _type.DOUBLE],  # height
                      _type.HRESULT]
    Rotate: _Callable[[_type.DOUBLE],  # degrees
                      _type.HRESULT]


class ITransformProvider2(_inspectable.IInspectable):
    get_CanZoom: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_ZoomLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_MaxZoom: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_MinZoom: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    Zoom: _Callable[[_type.DOUBLE],  # zoom
                    _type.HRESULT]
    ZoomByUnit: _Callable[[_enum.Microsoft.UI.Xaml.Automation.ZoomUnit],  # zoomUnit
                          _type.HRESULT]


class IValueProvider(_inspectable.IInspectable):
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    SetValue: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IVirtualizedItemProvider(_inspectable.IInspectable):
    Realize: _Callable[[],
                       _type.HRESULT]


class IWindowProvider(_inspectable.IInspectable):
    get_IsModal: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsTopmost: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Maximizable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Minimizable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_InteractionState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.WindowInteractionState]],  # value
                                    _type.HRESULT]
    get_VisualState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Automation.WindowVisualState]],  # value
                               _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    SetVisualState: _Callable[[_enum.Microsoft.UI.Xaml.Automation.WindowVisualState],  # state
                              _type.HRESULT]
    WaitForInputIdle: _Callable[[_type.INT32,  # milliseconds
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
