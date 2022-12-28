from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Lights as _Windows_Devices_Lights
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Graphics import Imaging as _Windows_Graphics_Imaging
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ILampArrayBitmapEffect(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_StartDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    put_StartDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                              _type.HRESULT]
    get_UpdateInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_UpdateInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    get_SuggestedBitmapSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                       _type.HRESULT]
    add_BitmapRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ILampArrayBitmapEffect, ILampArrayBitmapRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_BitmapRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class ILampArrayBitmapEffectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Devices_Lights.ILampArray,  # lampArray
                               _type.UINT32,  # __lampIndexesSize
                               _Pointer[_type.INT32],  # lampIndexes
                               _Pointer[ILampArrayBitmapEffect]],  # value
                              _type.HRESULT]

    _factory = True


class ILampArrayBitmapRequestedEventArgs(_inspectable.IInspectable):
    get_SinceStarted: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    UpdateBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # bitmap
                            _type.HRESULT]


class ILampArrayBlinkEffect(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_AttackDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_AttackDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    get_SustainDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_SustainDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_DecayDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    put_DecayDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                 _type.HRESULT]
    get_RepetitionDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_RepetitionDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_StartDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    put_StartDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                              _type.HRESULT]
    get_Occurrences: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_Occurrences: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_RepetitionMode: _Callable[[_Pointer[_enum.Windows.Devices.Lights.Effects.LampArrayRepetitionMode]],  # value
                                  _type.HRESULT]
    put_RepetitionMode: _Callable[[_enum.Windows.Devices.Lights.Effects.LampArrayRepetitionMode],  # value
                                  _type.HRESULT]


class ILampArrayBlinkEffectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Devices_Lights.ILampArray,  # lampArray
                               _type.UINT32,  # __lampIndexesSize
                               _Pointer[_type.INT32],  # lampIndexes
                               _Pointer[ILampArrayBlinkEffect]],  # value
                              _type.HRESULT]

    _factory = True


class ILampArrayColorRampEffect(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_RampDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    put_RampDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                _type.HRESULT]
    get_StartDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    put_StartDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                              _type.HRESULT]
    get_CompletionBehavior: _Callable[[_Pointer[_enum.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior]],  # value
                                      _type.HRESULT]
    put_CompletionBehavior: _Callable[[_enum.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior],  # value
                                      _type.HRESULT]


class ILampArrayColorRampEffectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Devices_Lights.ILampArray,  # lampArray
                               _type.UINT32,  # __lampIndexesSize
                               _Pointer[_type.INT32],  # lampIndexes
                               _Pointer[ILampArrayColorRampEffect]],  # value
                              _type.HRESULT]

    _factory = True


class ILampArrayCustomEffect(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_UpdateInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_UpdateInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    add_UpdateRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ILampArrayCustomEffect, ILampArrayUpdateRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_UpdateRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class ILampArrayCustomEffectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Devices_Lights.ILampArray,  # lampArray
                               _type.UINT32,  # __lampIndexesSize
                               _Pointer[_type.INT32],  # lampIndexes
                               _Pointer[ILampArrayCustomEffect]],  # value
                              _type.HRESULT]

    _factory = True


class ILampArrayEffect(_inspectable.IInspectable):
    get_ZIndex: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ZIndex: _Callable[[_type.INT32],  # value
                          _type.HRESULT]


class ILampArrayEffectPlaylist(_inspectable.IInspectable):
    Append: _Callable[[ILampArrayEffect],  # effect
                      _type.HRESULT]
    OverrideZIndex: _Callable[[_type.INT32],  # zIndex
                              _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    get_EffectStartMode: _Callable[[_Pointer[_enum.Windows.Devices.Lights.Effects.LampArrayEffectStartMode]],  # value
                                   _type.HRESULT]
    put_EffectStartMode: _Callable[[_enum.Windows.Devices.Lights.Effects.LampArrayEffectStartMode],  # value
                                   _type.HRESULT]
    get_Occurrences: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_Occurrences: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_RepetitionMode: _Callable[[_Pointer[_enum.Windows.Devices.Lights.Effects.LampArrayRepetitionMode]],  # value
                                  _type.HRESULT]
    put_RepetitionMode: _Callable[[_enum.Windows.Devices.Lights.Effects.LampArrayRepetitionMode],  # value
                                  _type.HRESULT]


class ILampArrayEffectPlaylistStatics(_inspectable.IInspectable):
    StartAll: _Callable[[_Windows_Foundation_Collections.IIterable[ILampArrayEffectPlaylist]],  # value
                        _type.HRESULT]
    StopAll: _Callable[[_Windows_Foundation_Collections.IIterable[ILampArrayEffectPlaylist]],  # value
                       _type.HRESULT]
    PauseAll: _Callable[[_Windows_Foundation_Collections.IIterable[ILampArrayEffectPlaylist]],  # value
                        _type.HRESULT]

    _factory = True


class ILampArraySolidEffect(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_StartDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    put_StartDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                              _type.HRESULT]
    get_CompletionBehavior: _Callable[[_Pointer[_enum.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior]],  # value
                                      _type.HRESULT]
    put_CompletionBehavior: _Callable[[_enum.Windows.Devices.Lights.Effects.LampArrayEffectCompletionBehavior],  # value
                                      _type.HRESULT]


class ILampArraySolidEffectFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Devices_Lights.ILampArray,  # lampArray
                               _type.UINT32,  # __lampIndexesSize
                               _Pointer[_type.INT32],  # lampIndexes
                               _Pointer[ILampArraySolidEffect]],  # value
                              _type.HRESULT]

    _factory = True


class ILampArrayUpdateRequestedEventArgs(_inspectable.IInspectable):
    get_SinceStarted: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    SetColor: _Callable[[_struct.Windows.UI.Color],  # desiredColor
                        _type.HRESULT]
    SetColorForIndex: _Callable[[_type.INT32,  # lampIndex
                                 _struct.Windows.UI.Color],  # desiredColor
                                _type.HRESULT]
    SetSingleColorForIndices: _Callable[[_struct.Windows.UI.Color,  # desiredColor
                                         _type.UINT32,  # __lampIndexesSize
                                         _Pointer[_type.INT32]],  # lampIndexes
                                        _type.HRESULT]
    SetColorsForIndices: _Callable[[_type.UINT32,  # __desiredColorsSize
                                    _Pointer[_struct.Windows.UI.Color],  # desiredColors
                                    _type.UINT32,  # __lampIndexesSize
                                    _Pointer[_type.INT32]],  # lampIndexes
                                   _type.HRESULT]
