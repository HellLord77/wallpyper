from __future__ import annotations as _

from typing import Callable as _Callable

from ... import AppNotifications as _Microsoft_Windows_AppNotifications
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAppNotificationBuilder(_inspectable.IInspectable):
    AddArgument: _Callable[[_type.HSTRING,  # key
                            _type.HSTRING,  # value
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    SetTimeStamp: _Callable[[_struct.Windows.Foundation.DateTime,  # value
                             _Pointer[IAppNotificationBuilder]],  # result
                            _type.HRESULT]
    SetDuration: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationDuration,  # duration
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    SetScenario: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationScenario,  # value
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    AddText: _Callable[[_type.HSTRING,  # text
                        _Pointer[IAppNotificationBuilder]],  # result
                       _type.HRESULT]
    AddText2: _Callable[[_type.HSTRING,  # text
                         IAppNotificationTextProperties,  # properties
                         _Pointer[IAppNotificationBuilder]],  # result
                        _type.HRESULT]
    SetAttributionText: _Callable[[_type.HSTRING,  # text
                                   _Pointer[IAppNotificationBuilder]],  # result
                                  _type.HRESULT]
    SetAttributionText2: _Callable[[_type.HSTRING,  # text
                                    _type.HSTRING,  # language
                                    _Pointer[IAppNotificationBuilder]],  # result
                                   _type.HRESULT]
    SetInlineImage: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                               _Pointer[IAppNotificationBuilder]],  # result
                              _type.HRESULT]
    SetInlineImage2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                                _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationImageCrop,  # imageCrop
                                _Pointer[IAppNotificationBuilder]],  # result
                               _type.HRESULT]
    SetInlineImage3: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                                _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationImageCrop,  # imagecrop
                                _type.HSTRING,  # alternateText
                                _Pointer[IAppNotificationBuilder]],  # result
                               _type.HRESULT]
    SetAppLogoOverride: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                                   _Pointer[IAppNotificationBuilder]],  # result
                                  _type.HRESULT]
    SetAppLogoOverride2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                                    _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationImageCrop,  # imageCrop
                                    _Pointer[IAppNotificationBuilder]],  # result
                                   _type.HRESULT]
    SetAppLogoOverride3: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                                    _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationImageCrop,  # imageCrop
                                    _type.HSTRING,  # alternateText
                                    _Pointer[IAppNotificationBuilder]],  # result
                                   _type.HRESULT]
    SetHeroImage: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                             _Pointer[IAppNotificationBuilder]],  # result
                            _type.HRESULT]
    SetHeroImage2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # imageUri
                              _type.HSTRING,  # alternateText
                              _Pointer[IAppNotificationBuilder]],  # result
                             _type.HRESULT]
    SetAudioUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # audioUri
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    SetAudioUri2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # audioUri
                             _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationAudioLooping,  # loop
                             _Pointer[IAppNotificationBuilder]],  # result
                            _type.HRESULT]
    SetAudioEvent: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationSoundEvent,  # appNotificationSoundEvent
                              _Pointer[IAppNotificationBuilder]],  # result
                             _type.HRESULT]
    SetAudioEvent2: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationSoundEvent,  # appNotificationSoundEvent
                               _enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationAudioLooping,  # loop
                               _Pointer[IAppNotificationBuilder]],  # result
                              _type.HRESULT]
    MuteAudio: _Callable[[_Pointer[IAppNotificationBuilder]],  # result
                         _type.HRESULT]
    AddTextBox: _Callable[[_type.HSTRING,  # id
                           _Pointer[IAppNotificationBuilder]],  # result
                          _type.HRESULT]
    AddTextBox2: _Callable[[_type.HSTRING,  # id
                            _type.HSTRING,  # placeHolderText
                            _type.HSTRING,  # title
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    AddButton: _Callable[[IAppNotificationButton,  # value
                          _Pointer[IAppNotificationBuilder]],  # result
                         _type.HRESULT]
    AddComboBox: _Callable[[IAppNotificationComboBox,  # value
                            _Pointer[IAppNotificationBuilder]],  # result
                           _type.HRESULT]
    AddProgressBar: _Callable[[IAppNotificationProgressBar,  # value
                               _Pointer[IAppNotificationBuilder]],  # result
                              _type.HRESULT]
    BuildNotification: _Callable[[_Pointer[_Microsoft_Windows_AppNotifications.IAppNotification]],  # result
                                 _type.HRESULT]
    SetTag: _Callable[[_type.HSTRING,  # value
                       _Pointer[IAppNotificationBuilder]],  # result
                      _type.HRESULT]
    SetGroup: _Callable[[_type.HSTRING,  # group
                         _Pointer[IAppNotificationBuilder]],  # result
                        _type.HRESULT]


class IAppNotificationBuilderStatics(_inspectable.IInspectable, factory=True):
    IsUrgentScenarioSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                         _type.HRESULT]


class IAppNotificationButton(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                             _type.HRESULT]
    put_Arguments: _Callable[[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]],  # value
                             _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                        _type.HRESULT]
    get_ToolTip: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_ToolTip: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_ContextMenuPlacement: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_ContextMenuPlacement: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_ButtonStyle: _Callable[[_Pointer[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationButtonStyle]],  # value
                               _type.HRESULT]
    put_ButtonStyle: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationButtonStyle],  # value
                               _type.HRESULT]
    get_InputId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_InputId: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_InvokeUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_InvokeUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]
    get_TargetAppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_TargetAppId: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    AddArgument: _Callable[[_type.HSTRING,  # key
                            _type.HSTRING,  # value
                            _Pointer[IAppNotificationButton]],  # result
                           _type.HRESULT]
    SetIcon: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # value
                        _Pointer[IAppNotificationButton]],  # result
                       _type.HRESULT]
    SetToolTip: _Callable[[_type.HSTRING,  # value
                           _Pointer[IAppNotificationButton]],  # result
                          _type.HRESULT]
    SetContextMenuPlacement: _Callable[[_Pointer[IAppNotificationButton]],  # result
                                       _type.HRESULT]
    SetButtonStyle: _Callable[[_enum.Microsoft.Windows.AppNotifications.Builder.AppNotificationButtonStyle,  # value
                               _Pointer[IAppNotificationButton]],  # result
                              _type.HRESULT]
    SetInputId: _Callable[[_type.HSTRING,  # value
                           _Pointer[IAppNotificationButton]],  # result
                          _type.HRESULT]
    SetInvokeUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # protocolUri
                             _Pointer[IAppNotificationButton]],  # result
                            _type.HRESULT]
    SetInvokeUri2: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # protocolUri
                              _type.HSTRING,  # targetAppId
                              _Pointer[IAppNotificationButton]],  # result
                             _type.HRESULT]


class IAppNotificationButtonFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # content
                               _Pointer[IAppNotificationButton]],  # value
                              _type.HRESULT]


class IAppNotificationButtonStatics(_inspectable.IInspectable, factory=True):
    IsToolTipSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    IsButtonStyleSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                      _type.HRESULT]


class IAppNotificationComboBox(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                         _type.HRESULT]
    put_Items: _Callable[[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]],  # value
                         _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    AddItem: _Callable[[_type.HSTRING,  # id
                        _type.HSTRING,  # content
                        _Pointer[IAppNotificationComboBox]],  # result
                       _type.HRESULT]
    SetTitle: _Callable[[_type.HSTRING,  # value
                         _Pointer[IAppNotificationComboBox]],  # result
                        _type.HRESULT]
    SetSelectedItem: _Callable[[_type.HSTRING,  # id
                                _Pointer[IAppNotificationComboBox]],  # result
                               _type.HRESULT]


class IAppNotificationComboBoxFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # id
                               _Pointer[IAppNotificationComboBox]],  # value
                              _type.HRESULT]


class IAppNotificationProgressBar(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_ValueStringOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_ValueStringOverride: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    SetTitle: _Callable[[_type.HSTRING,  # value
                         _Pointer[IAppNotificationProgressBar]],  # result
                        _type.HRESULT]
    BindTitle: _Callable[[_Pointer[IAppNotificationProgressBar]],  # result
                         _type.HRESULT]
    SetStatus: _Callable[[_type.HSTRING,  # value
                          _Pointer[IAppNotificationProgressBar]],  # result
                         _type.HRESULT]
    BindStatus: _Callable[[_Pointer[IAppNotificationProgressBar]],  # result
                          _type.HRESULT]
    SetValue: _Callable[[_type.DOUBLE,  # value
                         _Pointer[IAppNotificationProgressBar]],  # result
                        _type.HRESULT]
    BindValue: _Callable[[_Pointer[IAppNotificationProgressBar]],  # result
                         _type.HRESULT]
    SetValueStringOverride: _Callable[[_type.HSTRING,  # value
                                       _Pointer[IAppNotificationProgressBar]],  # result
                                      _type.HRESULT]
    BindValueStringOverride: _Callable[[_Pointer[IAppNotificationProgressBar]],  # result
                                       _type.HRESULT]


class IAppNotificationTextProperties(_inspectable.IInspectable):
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IncomingCallAlignment: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IncomingCallAlignment: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_MaxLines: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_MaxLines: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    SetLanguage: _Callable[[_type.HSTRING,  # value
                            _Pointer[IAppNotificationTextProperties]],  # result
                           _type.HRESULT]
    SetIncomingCallAlignment: _Callable[[_Pointer[IAppNotificationTextProperties]],  # result
                                        _type.HRESULT]
    SetMaxLines: _Callable[[_type.INT32,  # value
                            _Pointer[IAppNotificationTextProperties]],  # result
                           _type.HRESULT]
