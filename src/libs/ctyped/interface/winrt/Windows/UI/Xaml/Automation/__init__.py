from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Xaml as _Windows_UI_Xaml
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IAnnotationPatternIdentifiers(_inspectable.IInspectable):
    pass


class IAnnotationPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_AnnotationTypeIdProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_AnnotationTypeNameProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                              _type.HRESULT]
    get_AuthorProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                  _type.HRESULT]
    get_DateTimeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                    _type.HRESULT]
    get_TargetProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                  _type.HRESULT]


class IAutomationAnnotation(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.AnnotationType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType],  # value
                        _type.HRESULT]
    get_Element: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                           _type.HRESULT]
    put_Element: _Callable[[_Windows_UI_Xaml.IUIElement],  # value
                           _type.HRESULT]


class IAutomationAnnotationFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType,  # type
                               _Pointer[IAutomationAnnotation]],  # value
                              _type.HRESULT]
    CreateWithElementParameter: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType,  # type
                                           _Windows_UI_Xaml.IUIElement,  # element
                                           _Pointer[IAutomationAnnotation]],  # value
                                          _type.HRESULT]


class IAutomationAnnotationStatics(_inspectable.IInspectable, factory=True):
    get_TypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_ElementProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class IAutomationElementIdentifiers(_inspectable.IInspectable):
    pass


class IAutomationElementIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_AcceleratorKeyProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                          _type.HRESULT]
    get_AccessKeyProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_AutomationIdProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]
    get_BoundingRectangleProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]
    get_ClassNameProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_ClickablePointProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                          _type.HRESULT]
    get_ControlTypeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_HasKeyboardFocusProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_HelpTextProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                    _type.HRESULT]
    get_IsContentElementProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_IsControlElementProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_IsEnabledProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_IsKeyboardFocusableProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                               _type.HRESULT]
    get_IsOffscreenProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_IsPasswordProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_IsRequiredForFormProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]
    get_ItemStatusProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_ItemTypeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                    _type.HRESULT]
    get_LabeledByProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_LocalizedControlTypeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                _type.HRESULT]
    get_NameProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                _type.HRESULT]
    get_OrientationProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_LiveSettingProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]


class IAutomationElementIdentifiersStatics2(_inspectable.IInspectable, factory=True):
    get_ControlledPeersProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                           _type.HRESULT]


class IAutomationElementIdentifiersStatics3(_inspectable.IInspectable, factory=True):
    get_PositionInSetProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                         _type.HRESULT]
    get_SizeOfSetProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_LevelProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                 _type.HRESULT]
    get_AnnotationsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]


class IAutomationElementIdentifiersStatics4(_inspectable.IInspectable, factory=True):
    get_LandmarkTypeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]
    get_LocalizedLandmarkTypeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                 _type.HRESULT]


class IAutomationElementIdentifiersStatics5(_inspectable.IInspectable, factory=True):
    get_IsPeripheralProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]
    get_IsDataValidForFormProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                              _type.HRESULT]
    get_FullDescriptionProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                           _type.HRESULT]
    get_DescribedByProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_FlowsToProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_FlowsFromProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]


class IAutomationElementIdentifiersStatics6(_inspectable.IInspectable, factory=True):
    get_CultureProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]


class IAutomationElementIdentifiersStatics7(_inspectable.IInspectable, factory=True):
    get_HeadingLevelProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]


class IAutomationElementIdentifiersStatics8(_inspectable.IInspectable, factory=True):
    get_IsDialogProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                    _type.HRESULT]


class IAutomationProperties(_inspectable.IInspectable):
    pass


class IAutomationPropertiesStatics(_inspectable.IInspectable, factory=True):
    get_AcceleratorKeyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetAcceleratorKey: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    SetAcceleratorKey: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                  _type.HSTRING],  # value
                                 _type.HRESULT]
    get_AccessKeyProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    GetAccessKey: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    SetAccessKey: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _type.HSTRING],  # value
                            _type.HRESULT]
    get_AutomationIdProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetAutomationId: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    SetAutomationId: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _type.HSTRING],  # value
                               _type.HRESULT]
    get_HelpTextProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetHelpText: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    SetHelpText: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _type.HSTRING],  # value
                           _type.HRESULT]
    get_IsRequiredForFormProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetIsRequiredForForm: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    SetIsRequiredForForm: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                     _type.boolean],  # value
                                    _type.HRESULT]
    get_ItemStatusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    GetItemStatus: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                              _Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    SetItemStatus: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                              _type.HSTRING],  # value
                             _type.HRESULT]
    get_ItemTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetItemType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    SetItemType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _type.HSTRING],  # value
                           _type.HRESULT]
    get_LabeledByProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    GetLabeledBy: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Pointer[_Windows_UI_Xaml.IUIElement]],  # result
                            _type.HRESULT]
    SetLabeledBy: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Windows_UI_Xaml.IUIElement],  # value
                            _type.HRESULT]
    get_NameProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    GetName: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                        _Pointer[_type.HSTRING]],  # result
                       _type.HRESULT]
    SetName: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                        _type.HSTRING],  # value
                       _type.HRESULT]
    get_LiveSettingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    GetLiveSetting: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                               _Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting]],  # result
                              _type.HRESULT]
    SetLiveSetting: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                               _enum.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting],  # value
                              _type.HRESULT]


class IAutomationPropertiesStatics2(_inspectable.IInspectable, factory=True):
    get_AccessibilityViewProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetAccessibilityView: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AccessibilityView]],  # result
                                    _type.HRESULT]
    SetAccessibilityView: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                     _enum.Windows.UI.Xaml.Automation.Peers.AccessibilityView],  # value
                                    _type.HRESULT]
    get_ControlledPeersProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetControlledPeers: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IUIElement]]],  # result
                                  _type.HRESULT]


class IAutomationPropertiesStatics3(_inspectable.IInspectable, factory=True):
    get_PositionInSetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetPositionInSet: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    SetPositionInSet: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                 _type.INT32],  # value
                                _type.HRESULT]
    get_SizeOfSetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    GetSizeOfSet: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Pointer[_type.INT32]],  # result
                            _type.HRESULT]
    SetSizeOfSet: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _type.INT32],  # value
                            _type.HRESULT]
    get_LevelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    GetLevel: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    SetLevel: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                         _type.INT32],  # value
                        _type.HRESULT]
    get_AnnotationsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    GetAnnotations: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                               _Pointer[_Windows_Foundation_Collections.IVector[IAutomationAnnotation]]],  # result
                              _type.HRESULT]


class IAutomationPropertiesStatics4(_inspectable.IInspectable, factory=True):
    get_LandmarkTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetLandmarkType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType]],  # result
                               _type.HRESULT]
    SetLandmarkType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _enum.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType],  # value
                               _type.HRESULT]
    get_LocalizedLandmarkTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetLocalizedLandmarkType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _Pointer[_type.HSTRING]],  # result
                                        _type.HRESULT]
    SetLocalizedLandmarkType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _type.HSTRING],  # value
                                        _type.HRESULT]


class IAutomationPropertiesStatics5(_inspectable.IInspectable, factory=True):
    get_IsPeripheralProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetIsPeripheral: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    SetIsPeripheral: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _type.boolean],  # value
                               _type.HRESULT]
    get_IsDataValidForFormProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    GetIsDataValidForForm: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetIsDataValidForForm: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                      _type.boolean],  # value
                                     _type.HRESULT]
    get_FullDescriptionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetFullDescription: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    SetFullDescription: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                   _type.HSTRING],  # value
                                  _type.HRESULT]
    get_LocalizedControlTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetLocalizedControlType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    SetLocalizedControlType: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                        _type.HSTRING],  # value
                                       _type.HRESULT]
    get_DescribedByProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    GetDescribedBy: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                               _Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IDependencyObject]]],  # result
                              _type.HRESULT]
    get_FlowsToProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetFlowsTo: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                           _Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IDependencyObject]]],  # result
                          _type.HRESULT]
    get_FlowsFromProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    GetFlowsFrom: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IDependencyObject]]],  # result
                            _type.HRESULT]


class IAutomationPropertiesStatics6(_inspectable.IInspectable, factory=True):
    get_CultureProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetCulture: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                           _Pointer[_type.INT32]],  # result
                          _type.HRESULT]
    SetCulture: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                           _type.INT32],  # value
                          _type.HRESULT]


class IAutomationPropertiesStatics7(_inspectable.IInspectable, factory=True):
    get_HeadingLevelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetHeadingLevel: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel]],  # result
                               _type.HRESULT]
    SetHeadingLevel: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                _enum.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel],  # value
                               _type.HRESULT]


class IAutomationPropertiesStatics8(_inspectable.IInspectable, factory=True):
    get_IsDialogProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetIsDialog: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    SetIsDialog: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _type.boolean],  # value
                           _type.HRESULT]


class IAutomationPropertiesStatics9(_inspectable.IInspectable, factory=True):
    get_AutomationControlTypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetAutomationControlType: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                         _Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationControlType]],  # result
                                        _type.HRESULT]
    SetAutomationControlType: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                         _enum.Windows.UI.Xaml.Automation.Peers.AutomationControlType],  # value
                                        _type.HRESULT]


class IAutomationProperty(_inspectable.IInspectable):
    pass


class IDockPatternIdentifiers(_inspectable.IInspectable):
    pass


class IDockPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_DockPositionProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]


class IDragPatternIdentifiers(_inspectable.IInspectable):
    pass


class IDragPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_DropEffectProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_DropEffectsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_GrabbedItemsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                        _type.HRESULT]
    get_IsGrabbedProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]


class IDropTargetPatternIdentifiers(_inspectable.IInspectable):
    pass


class IDropTargetPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_DropTargetEffectProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_DropTargetEffectsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]


class IExpandCollapsePatternIdentifiers(_inspectable.IInspectable):
    pass


class IExpandCollapsePatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ExpandCollapseStateProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                               _type.HRESULT]


class IGridItemPatternIdentifiers(_inspectable.IInspectable):
    pass


class IGridItemPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ColumnProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                  _type.HRESULT]
    get_ColumnSpanProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_ContainingGridProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                          _type.HRESULT]
    get_RowProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                               _type.HRESULT]
    get_RowSpanProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]


class IGridPatternIdentifiers(_inspectable.IInspectable):
    pass


class IGridPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ColumnCountProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_RowCountProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                    _type.HRESULT]


class IMultipleViewPatternIdentifiers(_inspectable.IInspectable):
    pass


class IMultipleViewPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_CurrentViewProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_SupportedViewsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                          _type.HRESULT]


class IRangeValuePatternIdentifiers(_inspectable.IInspectable):
    pass


class IRangeValuePatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_IsReadOnlyProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_LargeChangeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_MaximumProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_MinimumProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_SmallChangeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_ValueProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                 _type.HRESULT]


class IScrollPatternIdentifiers(_inspectable.IInspectable):
    pass


class IScrollPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_HorizontallyScrollableProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                  _type.HRESULT]
    get_HorizontalScrollPercentProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                   _type.HRESULT]
    get_HorizontalViewSizeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                              _type.HRESULT]
    get_NoScroll: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_VerticallyScrollableProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                _type.HRESULT]
    get_VerticalScrollPercentProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                 _type.HRESULT]
    get_VerticalViewSizeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]


class ISelectionItemPatternIdentifiers(_inspectable.IInspectable):
    pass


class ISelectionItemPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_IsSelectedProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_SelectionContainerProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                              _type.HRESULT]


class ISelectionPatternIdentifiers(_inspectable.IInspectable):
    pass


class ISelectionPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_CanSelectMultipleProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]
    get_IsSelectionRequiredProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                               _type.HRESULT]
    get_SelectionProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]


class ISpreadsheetItemPatternIdentifiers(_inspectable.IInspectable):
    pass


class ISpreadsheetItemPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_FormulaProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]


class IStylesPatternIdentifiers(_inspectable.IInspectable):
    pass


class IStylesPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ExtendedPropertiesProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                              _type.HRESULT]
    get_FillColorProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_FillPatternColorProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_FillPatternStyleProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]
    get_ShapeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                 _type.HRESULT]
    get_StyleIdProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_StyleNameProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]


class ITableItemPatternIdentifiers(_inspectable.IInspectable):
    pass


class ITableItemPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ColumnHeaderItemsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]
    get_RowHeaderItemsProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                          _type.HRESULT]


class ITablePatternIdentifiers(_inspectable.IInspectable):
    pass


class ITablePatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ColumnHeadersProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                         _type.HRESULT]
    get_RowHeadersProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_RowOrColumnMajorProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                            _type.HRESULT]


class ITogglePatternIdentifiers(_inspectable.IInspectable):
    pass


class ITogglePatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_ToggleStateProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]


class ITransformPattern2Identifiers(_inspectable.IInspectable):
    pass


class ITransformPattern2IdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_CanZoomProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_ZoomLevelProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_MaxZoomProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_MinZoomProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]


class ITransformPatternIdentifiers(_inspectable.IInspectable):
    pass


class ITransformPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_CanMoveProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_CanResizeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_CanRotateProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]


class IValuePatternIdentifiers(_inspectable.IInspectable):
    pass


class IValuePatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_IsReadOnlyProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                      _type.HRESULT]
    get_ValueProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                 _type.HRESULT]


class IWindowPatternIdentifiers(_inspectable.IInspectable):
    pass


class IWindowPatternIdentifiersStatics(_inspectable.IInspectable, factory=True):
    get_CanMaximizeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_CanMinimizeProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                       _type.HRESULT]
    get_IsModalProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                   _type.HRESULT]
    get_IsTopmostProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                     _type.HRESULT]
    get_WindowInteractionStateProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                                  _type.HRESULT]
    get_WindowVisualStateProperty: _Callable[[_Pointer[IAutomationProperty]],  # value
                                             _type.HRESULT]
