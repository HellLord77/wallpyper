from __future__ import annotations

from typing import Callable as _Callable

from .. import Provider as _Windows_UI_Xaml_Automation_Provider
from ... import Automation as _Windows_UI_Xaml_Automation
from ... import Controls as _Windows_UI_Xaml_Controls
from ...Controls import Primitives as _Windows_UI_Xaml_Controls_Primitives
from .... import Xaml as _Windows_UI_Xaml
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IAppBarAutomationPeer(_inspectable.IInspectable):
    pass


class IAppBarAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IAppBar,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IAppBarAutomationPeer]],  # value
                                       _type.HRESULT]


class IAppBarButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IAppBarButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IAppBarButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IAppBarButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IAppBarToggleButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IAppBarToggleButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IAppBarToggleButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IAppBarToggleButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IAutoSuggestBoxAutomationPeer(_inspectable.IInspectable):
    pass


class IAutoSuggestBoxAutomationPeerFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IAutoSuggestBox,  # owner
                                        _Pointer[IAutoSuggestBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IAutomationPeer(_inspectable.IInspectable):
    get_EventsSource: _Callable[[_Pointer[IAutomationPeer]],  # value
                                _type.HRESULT]
    put_EventsSource: _Callable[[IAutomationPeer],  # value
                                _type.HRESULT]
    GetPattern: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.PatternInterface,  # patternInterface
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]
    RaiseAutomationEvent: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationEvents],  # eventId
                                    _type.HRESULT]
    RaisePropertyChangedEvent: _Callable[[_Windows_UI_Xaml_Automation.IAutomationProperty,  # automationProperty
                                          _inspectable.IInspectable,  # oldValue
                                          _inspectable.IInspectable],  # newValue
                                         _type.HRESULT]
    GetAcceleratorKey: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetAccessKey: _Callable[[_Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    GetAutomationControlType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationControlType]],  # result
                                        _type.HRESULT]
    GetAutomationId: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    GetBoundingRectangle: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # result
                                    _type.HRESULT]
    GetChildren: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAutomationPeer]]],  # result
                           _type.HRESULT]
    GetClassName: _Callable[[_Pointer[_type.HSTRING]],  # result
                            _type.HRESULT]
    GetClickablePoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # result
                                 _type.HRESULT]
    GetHelpText: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    GetItemStatus: _Callable[[_Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    GetItemType: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    GetLabeledBy: _Callable[[_Pointer[IAutomationPeer]],  # result
                            _type.HRESULT]
    GetLocalizedControlType: _Callable[[_Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    GetName: _Callable[[_Pointer[_type.HSTRING]],  # result
                       _type.HRESULT]
    GetOrientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationOrientation]],  # result
                              _type.HRESULT]
    HasKeyboardFocus: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    IsContentElement: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    IsControlElement: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    IsEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    IsKeyboardFocusable: _Callable[[_Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    IsOffscreen: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    IsPassword: _Callable[[_Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    IsRequiredForForm: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetFocus: _Callable[[],
                        _type.HRESULT]
    GetParent: _Callable[[_Pointer[IAutomationPeer]],  # result
                         _type.HRESULT]
    InvalidatePeer: _Callable[[],
                              _type.HRESULT]
    GetPeerFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                                 _Pointer[IAutomationPeer]],  # result
                                _type.HRESULT]
    GetLiveSetting: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting]],  # result
                              _type.HRESULT]


class IAutomationPeer2(_inspectable.IInspectable):
    pass


class IAutomationPeer3(_inspectable.IInspectable):
    Navigate: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection,  # direction
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]
    GetElementFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # pointInWindowCoordinates
                                    _Pointer[_inspectable.IInspectable]],  # result
                                   _type.HRESULT]
    GetFocusedElement: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                 _type.HRESULT]
    ShowContextMenu: _Callable[[],
                               _type.HRESULT]
    GetControlledPeers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAutomationPeer]]],  # result
                                  _type.HRESULT]
    GetAnnotations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAutomationPeerAnnotation]]],  # result
                              _type.HRESULT]
    SetParent: _Callable[[IAutomationPeer],  # peer
                         _type.HRESULT]
    RaiseTextEditTextChangedEvent: _Callable[[_enum.Windows.UI.Xaml.Automation.AutomationTextEditChangeType,  # automationTextEditChangeType
                                              _Windows_Foundation_Collections.IVectorView[_type.HSTRING]],  # changedData
                                             _type.HRESULT]
    GetPositionInSet: _Callable[[_Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    GetSizeOfSet: _Callable[[_Pointer[_type.INT32]],  # result
                            _type.HRESULT]
    GetLevel: _Callable[[_Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    RaiseStructureChangedEvent: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationStructureChangeType,  # structureChangeType
                                           IAutomationPeer],  # child
                                          _type.HRESULT]


class IAutomationPeer4(_inspectable.IInspectable):
    GetLandmarkType: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType]],  # result
                               _type.HRESULT]
    GetLocalizedLandmarkType: _Callable[[_Pointer[_type.HSTRING]],  # result
                                        _type.HRESULT]


class IAutomationPeer5(_inspectable.IInspectable):
    IsPeripheral: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    IsDataValidForForm: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    GetFullDescription: _Callable[[_Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]


class IAutomationPeer6(_inspectable.IInspectable):
    GetCulture: _Callable[[_Pointer[_type.INT32]],  # result
                          _type.HRESULT]


class IAutomationPeer7(_inspectable.IInspectable):
    RaiseNotificationEvent: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationNotificationKind,  # notificationKind
                                       _enum.Windows.UI.Xaml.Automation.Peers.AutomationNotificationProcessing,  # notificationProcessing
                                       _type.HSTRING,  # displayString
                                       _type.HSTRING],  # activityId
                                      _type.HRESULT]


class IAutomationPeer8(_inspectable.IInspectable):
    GetHeadingLevel: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel]],  # result
                               _type.HRESULT]


class IAutomationPeer9(_inspectable.IInspectable):
    IsDialog: _Callable[[_Pointer[_type.boolean]],  # result
                        _type.HRESULT]


class IAutomationPeerAnnotation(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.AnnotationType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType],  # value
                        _type.HRESULT]
    get_Peer: _Callable[[_Pointer[IAutomationPeer]],  # value
                        _type.HRESULT]
    put_Peer: _Callable[[IAutomationPeer],  # value
                        _type.HRESULT]


class IAutomationPeerAnnotationFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType,  # type
                               _Pointer[IAutomationPeerAnnotation]],  # value
                              _type.HRESULT]
    CreateWithPeerParameter: _Callable[[_enum.Windows.UI.Xaml.Automation.AnnotationType,  # type
                                        IAutomationPeer,  # peer
                                        _Pointer[IAutomationPeerAnnotation]],  # value
                                       _type.HRESULT]


class IAutomationPeerAnnotationStatics(_inspectable.IInspectable, factory=True):
    get_TypeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_PeerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]


class IAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IAutomationPeer]],  # value
                              _type.HRESULT]


class IAutomationPeerOverrides(_inspectable.IInspectable):
    GetPatternCore: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.PatternInterface,  # patternInterface
                               _Pointer[_inspectable.IInspectable]],  # result
                              _type.HRESULT]
    GetAcceleratorKeyCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                     _type.HRESULT]
    GetAccessKeyCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                _type.HRESULT]
    GetAutomationControlTypeCore: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationControlType]],  # result
                                            _type.HRESULT]
    GetAutomationIdCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                   _type.HRESULT]
    GetBoundingRectangleCore: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # result
                                        _type.HRESULT]
    GetChildrenCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAutomationPeer]]],  # result
                               _type.HRESULT]
    GetClassNameCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                _type.HRESULT]
    GetClickablePointCore: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # result
                                     _type.HRESULT]
    GetHelpTextCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    GetItemStatusCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetItemTypeCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    GetLabeledByCore: _Callable[[_Pointer[IAutomationPeer]],  # result
                                _type.HRESULT]
    GetLocalizedControlTypeCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                           _type.HRESULT]
    GetNameCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    GetOrientationCore: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationOrientation]],  # result
                                  _type.HRESULT]
    HasKeyboardFocusCore: _Callable[[_Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    IsContentElementCore: _Callable[[_Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    IsControlElementCore: _Callable[[_Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    IsEnabledCore: _Callable[[_Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    IsKeyboardFocusableCore: _Callable[[_Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    IsOffscreenCore: _Callable[[_Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    IsPasswordCore: _Callable[[_Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    IsRequiredForFormCore: _Callable[[_Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetFocusCore: _Callable[[],
                            _type.HRESULT]
    GetPeerFromPointCore: _Callable[[_struct.Windows.Foundation.Point,  # point
                                     _Pointer[IAutomationPeer]],  # result
                                    _type.HRESULT]
    GetLiveSettingCore: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting]],  # result
                                  _type.HRESULT]


class IAutomationPeerOverrides2(_inspectable.IInspectable):
    ShowContextMenuCore: _Callable[[],
                                   _type.HRESULT]
    GetControlledPeersCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAutomationPeer]]],  # result
                                      _type.HRESULT]


class IAutomationPeerOverrides3(_inspectable.IInspectable):
    NavigateCore: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection,  # direction
                             _Pointer[_inspectable.IInspectable]],  # result
                            _type.HRESULT]
    GetElementFromPointCore: _Callable[[_struct.Windows.Foundation.Point,  # pointInWindowCoordinates
                                        _Pointer[_inspectable.IInspectable]],  # result
                                       _type.HRESULT]
    GetFocusedElementCore: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                     _type.HRESULT]
    GetAnnotationsCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAutomationPeerAnnotation]]],  # result
                                  _type.HRESULT]
    GetPositionInSetCore: _Callable[[_Pointer[_type.INT32]],  # result
                                    _type.HRESULT]
    GetSizeOfSetCore: _Callable[[_Pointer[_type.INT32]],  # result
                                _type.HRESULT]
    GetLevelCore: _Callable[[_Pointer[_type.INT32]],  # result
                            _type.HRESULT]


class IAutomationPeerOverrides4(_inspectable.IInspectable):
    GetLandmarkTypeCore: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType]],  # result
                                   _type.HRESULT]
    GetLocalizedLandmarkTypeCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                            _type.HRESULT]


class IAutomationPeerOverrides5(_inspectable.IInspectable):
    IsPeripheralCore: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    IsDataValidForFormCore: _Callable[[_Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    GetFullDescriptionCore: _Callable[[_Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    GetDescribedByCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[IAutomationPeer]]],  # result
                                  _type.HRESULT]
    GetFlowsToCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[IAutomationPeer]]],  # result
                              _type.HRESULT]
    GetFlowsFromCore: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[IAutomationPeer]]],  # result
                                _type.HRESULT]


class IAutomationPeerOverrides6(_inspectable.IInspectable):
    GetCultureCore: _Callable[[_Pointer[_type.INT32]],  # result
                              _type.HRESULT]


class IAutomationPeerOverrides8(_inspectable.IInspectable):
    GetHeadingLevelCore: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel]],  # result
                                   _type.HRESULT]


class IAutomationPeerOverrides9(_inspectable.IInspectable):
    IsDialogCore: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]


class IAutomationPeerProtected(_inspectable.IInspectable):
    PeerFromProvider: _Callable[[_Windows_UI_Xaml_Automation_Provider.IIRawElementProviderSimple,  # provider
                                 _Pointer[IAutomationPeer]],  # result
                                _type.HRESULT]
    ProviderFromPeer: _Callable[[IAutomationPeer,  # peer
                                 _Pointer[_Windows_UI_Xaml_Automation_Provider.IIRawElementProviderSimple]],  # result
                                _type.HRESULT]


class IAutomationPeerStatics(_inspectable.IInspectable, factory=True):
    ListenerExists: _Callable[[_enum.Windows.UI.Xaml.Automation.Peers.AutomationEvents,  # eventId
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]


class IAutomationPeerStatics3(_inspectable.IInspectable, factory=True):
    GenerateRawElementProviderRuntimeId: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId]],  # result
                                                   _type.HRESULT]


class IButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IButtonBaseAutomationPeer(_inspectable.IInspectable):
    pass


class IButtonBaseAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IButtonBase,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IButtonBaseAutomationPeer]],  # value
                                       _type.HRESULT]


class ICalendarDatePickerAutomationPeer(_inspectable.IInspectable):
    pass


class ICalendarDatePickerAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ICalendarDatePicker,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ICalendarDatePickerAutomationPeer]],  # value
                                       _type.HRESULT]


class ICaptureElementAutomationPeer(_inspectable.IInspectable):
    pass


class ICaptureElementAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ICaptureElement,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ICaptureElementAutomationPeer]],  # value
                                       _type.HRESULT]


class ICheckBoxAutomationPeer(_inspectable.IInspectable):
    pass


class ICheckBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ICheckBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ICheckBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IColorPickerSliderAutomationPeer(_inspectable.IInspectable):
    pass


class IColorPickerSliderAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IColorPickerSlider,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IColorPickerSliderAutomationPeer]],  # value
                                       _type.HRESULT]


class IColorSpectrumAutomationPeer(_inspectable.IInspectable):
    pass


class IColorSpectrumAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IColorSpectrum,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IColorSpectrumAutomationPeer]],  # value
                                       _type.HRESULT]


class IComboBoxAutomationPeer(_inspectable.IInspectable):
    pass


class IComboBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IComboBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IComboBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IComboBoxItemAutomationPeer(_inspectable.IInspectable):
    pass


class IComboBoxItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IComboBoxItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IComboBoxItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IComboBoxItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IComboBoxItemDataAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IComboBoxAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IComboBoxItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class IDatePickerAutomationPeer(_inspectable.IInspectable):
    pass


class IDatePickerAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IDatePicker,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IDatePickerAutomationPeer]],  # value
                                       _type.HRESULT]


class IDatePickerFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IFlipViewAutomationPeer(_inspectable.IInspectable):
    pass


class IFlipViewAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IFlipView,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IFlipViewAutomationPeer]],  # value
                                       _type.HRESULT]


class IFlipViewItemAutomationPeer(_inspectable.IInspectable):
    pass


class IFlipViewItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IFlipViewItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IFlipViewItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IFlipViewItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IFlipViewItemDataAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IFlipViewAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IFlipViewItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class IFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IFlyoutPresenterAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IFlyoutPresenter,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IFlyoutPresenterAutomationPeer]],  # value
                                       _type.HRESULT]


class IFrameworkElementAutomationPeer(_inspectable.IInspectable):
    get_Owner: _Callable[[_Pointer[_Windows_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]


class IFrameworkElementAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml.IFrameworkElement,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IFrameworkElementAutomationPeer]],  # value
                                       _type.HRESULT]


class IFrameworkElementAutomationPeerStatics(_inspectable.IInspectable, factory=True):
    FromElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                            _Pointer[IAutomationPeer]],  # result
                           _type.HRESULT]
    CreatePeerForElement: _Callable[[_Windows_UI_Xaml.IUIElement,  # element
                                     _Pointer[IAutomationPeer]],  # result
                                    _type.HRESULT]


class IGridViewAutomationPeer(_inspectable.IInspectable):
    pass


class IGridViewAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IGridView,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IGridViewAutomationPeer]],  # value
                                       _type.HRESULT]


class IGridViewHeaderItemAutomationPeer(_inspectable.IInspectable):
    pass


class IGridViewHeaderItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IGridViewHeaderItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IGridViewHeaderItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IGridViewItemAutomationPeer(_inspectable.IInspectable):
    pass


class IGridViewItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IGridViewItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IGridViewItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IGridViewItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IGridViewItemDataAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IGridViewAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IGridViewItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class IGroupItemAutomationPeer(_inspectable.IInspectable):
    pass


class IGroupItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IGroupItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IGroupItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IHubAutomationPeer(_inspectable.IInspectable):
    pass


class IHubAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IHub,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IHubAutomationPeer]],  # value
                                       _type.HRESULT]


class IHubSectionAutomationPeer(_inspectable.IInspectable):
    pass


class IHubSectionAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IHubSection,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IHubSectionAutomationPeer]],  # value
                                       _type.HRESULT]


class IHyperlinkButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IHyperlinkButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IHyperlinkButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IHyperlinkButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IImageAutomationPeer(_inspectable.IInspectable):
    pass


class IImageAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IImage,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IImageAutomationPeer]],  # value
                                       _type.HRESULT]


class IInkToolbarAutomationPeer(_inspectable.IInspectable):
    pass


class IItemAutomationPeer(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]
    get_ItemsControlAutomationPeer: _Callable[[_Pointer[IItemsControlAutomationPeer]],  # value
                                              _type.HRESULT]


class IItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IItemsControlAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IItemAutomationPeer]],  # value
                                               _type.HRESULT]


class IItemsControlAutomationPeer(_inspectable.IInspectable):
    pass


class IItemsControlAutomationPeer2(_inspectable.IInspectable):
    CreateItemAutomationPeer: _Callable[[_inspectable.IInspectable,  # item
                                         _Pointer[IItemAutomationPeer]],  # result
                                        _type.HRESULT]


class IItemsControlAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IItemsControl,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IItemsControlAutomationPeer]],  # value
                                       _type.HRESULT]


class IItemsControlAutomationPeerOverrides2(_inspectable.IInspectable):
    OnCreateItemAutomationPeer: _Callable[[_inspectable.IInspectable,  # item
                                           _Pointer[IItemAutomationPeer]],  # result
                                          _type.HRESULT]


class IListBoxAutomationPeer(_inspectable.IInspectable):
    pass


class IListBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IListBoxItemAutomationPeer(_inspectable.IInspectable):
    pass


class IListBoxItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListBoxItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListBoxItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IListBoxItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IListBoxItemDataAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IListBoxAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IListBoxItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class IListPickerFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListView,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListViewAutomationPeer]],  # value
                                       _type.HRESULT]


class IListViewBaseAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewBaseAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListViewBase,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListViewBaseAutomationPeer]],  # value
                                       _type.HRESULT]


class IListViewBaseHeaderItemAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewBaseHeaderItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListViewBaseHeaderItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListViewBaseHeaderItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IListViewHeaderItemAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewHeaderItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListViewHeaderItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListViewHeaderItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IListViewItemAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IListViewItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IListViewItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IListViewItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IListViewItemDataAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IListViewBaseAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[IListViewItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class ILoopingSelectorAutomationPeer(_inspectable.IInspectable):
    pass


class ILoopingSelectorItemAutomationPeer(_inspectable.IInspectable):
    pass


class ILoopingSelectorItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IMapControlAutomationPeer(_inspectable.IInspectable):
    pass


class IMediaElementAutomationPeer(_inspectable.IInspectable):
    pass


class IMediaElementAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IMediaElement,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IMediaElementAutomationPeer]],  # value
                                       _type.HRESULT]


class IMediaPlayerElementAutomationPeer(_inspectable.IInspectable):
    pass


class IMediaPlayerElementAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IMediaPlayerElement,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IMediaPlayerElementAutomationPeer]],  # value
                                       _type.HRESULT]


class IMediaTransportControlsAutomationPeer(_inspectable.IInspectable):
    pass


class IMediaTransportControlsAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IMediaTransportControls,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IMediaTransportControlsAutomationPeer]],  # value
                                       _type.HRESULT]


class IMenuBarAutomationPeer(_inspectable.IInspectable):
    pass


class IMenuBarAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_UI_Xaml_Controls.IMenuBar,  # owner
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuBarAutomationPeer]],  # value
                              _type.HRESULT]


class IMenuBarItemAutomationPeer(_inspectable.IInspectable):
    pass


class IMenuBarItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_UI_Xaml_Controls.IMenuBarItem,  # owner
                               _inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMenuBarItemAutomationPeer]],  # value
                              _type.HRESULT]


class IMenuFlyoutItemAutomationPeer(_inspectable.IInspectable):
    pass


class IMenuFlyoutItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IMenuFlyoutItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IMenuFlyoutItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IMenuFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IMenuFlyoutPresenterAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IMenuFlyoutPresenter,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IMenuFlyoutPresenterAutomationPeer]],  # value
                                       _type.HRESULT]


class INavigationViewItemAutomationPeer(_inspectable.IInspectable):
    pass


class INavigationViewItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.INavigationViewItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[INavigationViewItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IPasswordBoxAutomationPeer(_inspectable.IInspectable):
    pass


class IPasswordBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IPasswordBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IPasswordBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IPersonPictureAutomationPeer(_inspectable.IInspectable):
    pass


class IPersonPictureAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IPersonPicture,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IPersonPictureAutomationPeer]],  # value
                                       _type.HRESULT]


class IPickerFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IPivotAutomationPeer(_inspectable.IInspectable):
    pass


class IPivotAutomationPeerFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IPivot,  # owner
                                        _Pointer[IPivotAutomationPeer]],  # value
                                       _type.HRESULT]


class IPivotItemAutomationPeer(_inspectable.IInspectable):
    pass


class IPivotItemAutomationPeerFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IPivotItem,  # owner
                                        _Pointer[IPivotItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IPivotItemDataAutomationPeer(_inspectable.IInspectable):
    pass


class IPivotItemDataAutomationPeerFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                IPivotAutomationPeer,  # parent
                                                _Pointer[IPivotItemDataAutomationPeer]],  # value
                                               _type.HRESULT]


class IProgressBarAutomationPeer(_inspectable.IInspectable):
    pass


class IProgressBarAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IProgressBar,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IProgressBarAutomationPeer]],  # value
                                       _type.HRESULT]


class IProgressRingAutomationPeer(_inspectable.IInspectable):
    pass


class IProgressRingAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IProgressRing,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IProgressRingAutomationPeer]],  # value
                                       _type.HRESULT]


class IRadioButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IRadioButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IRadioButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRadioButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IRangeBaseAutomationPeer(_inspectable.IInspectable):
    pass


class IRangeBaseAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IRangeBase,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRangeBaseAutomationPeer]],  # value
                                       _type.HRESULT]


class IRatingControlAutomationPeer(_inspectable.IInspectable):
    pass


class IRatingControlAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IRatingControl,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRatingControlAutomationPeer]],  # value
                                       _type.HRESULT]


class IRepeatButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IRepeatButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IRepeatButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRepeatButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IRichEditBoxAutomationPeer(_inspectable.IInspectable):
    pass


class IRichEditBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IRichEditBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRichEditBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IRichTextBlockAutomationPeer(_inspectable.IInspectable):
    pass


class IRichTextBlockAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IRichTextBlock,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRichTextBlockAutomationPeer]],  # value
                                       _type.HRESULT]


class IRichTextBlockOverflowAutomationPeer(_inspectable.IInspectable):
    pass


class IRichTextBlockOverflowAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IRichTextBlockOverflow,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IRichTextBlockOverflowAutomationPeer]],  # value
                                       _type.HRESULT]


class IScrollBarAutomationPeer(_inspectable.IInspectable):
    pass


class IScrollBarAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IScrollBar,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IScrollBarAutomationPeer]],  # value
                                       _type.HRESULT]


class IScrollViewerAutomationPeer(_inspectable.IInspectable):
    pass


class IScrollViewerAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IScrollViewer,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IScrollViewerAutomationPeer]],  # value
                                       _type.HRESULT]


class ISearchBoxAutomationPeer(_inspectable.IInspectable):
    pass


class ISearchBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ISearchBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ISearchBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class ISelectorAutomationPeer(_inspectable.IInspectable):
    pass


class ISelectorAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.ISelector,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ISelectorAutomationPeer]],  # value
                                       _type.HRESULT]


class ISelectorItemAutomationPeer(_inspectable.IInspectable):
    pass


class ISelectorItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithParentAndItem: _Callable[[_inspectable.IInspectable,  # item
                                                ISelectorAutomationPeer,  # parent
                                                _inspectable.IInspectable,  # baseInterface
                                                _Pointer[_inspectable.IInspectable],  # innerInterface
                                                _Pointer[ISelectorItemAutomationPeer]],  # value
                                               _type.HRESULT]


class ISemanticZoomAutomationPeer(_inspectable.IInspectable):
    pass


class ISemanticZoomAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ISemanticZoom,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ISemanticZoomAutomationPeer]],  # value
                                       _type.HRESULT]


class ISettingsFlyoutAutomationPeer(_inspectable.IInspectable):
    pass


class ISettingsFlyoutAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ISettingsFlyout,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ISettingsFlyoutAutomationPeer]],  # value
                                       _type.HRESULT]


class ISliderAutomationPeer(_inspectable.IInspectable):
    pass


class ISliderAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ISlider,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ISliderAutomationPeer]],  # value
                                       _type.HRESULT]


class ITextBlockAutomationPeer(_inspectable.IInspectable):
    pass


class ITextBlockAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ITextBlock,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ITextBlockAutomationPeer]],  # value
                                       _type.HRESULT]


class ITextBoxAutomationPeer(_inspectable.IInspectable):
    pass


class ITextBoxAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ITextBox,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ITextBoxAutomationPeer]],  # value
                                       _type.HRESULT]


class IThumbAutomationPeer(_inspectable.IInspectable):
    pass


class IThumbAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IThumb,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IThumbAutomationPeer]],  # value
                                       _type.HRESULT]


class ITimePickerAutomationPeer(_inspectable.IInspectable):
    pass


class ITimePickerAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ITimePicker,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ITimePickerAutomationPeer]],  # value
                                       _type.HRESULT]


class ITimePickerFlyoutPresenterAutomationPeer(_inspectable.IInspectable):
    pass


class IToggleButtonAutomationPeer(_inspectable.IInspectable):
    pass


class IToggleButtonAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls_Primitives.IToggleButton,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IToggleButtonAutomationPeer]],  # value
                                       _type.HRESULT]


class IToggleMenuFlyoutItemAutomationPeer(_inspectable.IInspectable):
    pass


class IToggleMenuFlyoutItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IToggleMenuFlyoutItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IToggleMenuFlyoutItemAutomationPeer]],  # value
                                       _type.HRESULT]


class IToggleSwitchAutomationPeer(_inspectable.IInspectable):
    pass


class IToggleSwitchAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.IToggleSwitch,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[IToggleSwitchAutomationPeer]],  # value
                                       _type.HRESULT]


class ITreeViewItemAutomationPeer(_inspectable.IInspectable):
    pass


class ITreeViewItemAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ITreeViewItem,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ITreeViewItemAutomationPeer]],  # value
                                       _type.HRESULT]


class ITreeViewListAutomationPeer(_inspectable.IInspectable):
    pass


class ITreeViewListAutomationPeerFactory(_inspectable.IInspectable):
    CreateInstanceWithOwner: _Callable[[_Windows_UI_Xaml_Controls.ITreeViewList,  # owner
                                        _inspectable.IInspectable,  # baseInterface
                                        _Pointer[_inspectable.IInspectable],  # innerInterface
                                        _Pointer[ITreeViewListAutomationPeer]],  # value
                                       _type.HRESULT]
