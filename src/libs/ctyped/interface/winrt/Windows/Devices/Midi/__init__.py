from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Enumeration as _Windows_Devices_Enumeration
from ... import Foundation as _Windows_Foundation
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IMidiChannelPressureMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]


class IMidiChannelPressureMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiChannelPressureMessage: _Callable[[_type.BYTE,  # channel
                                                 _type.BYTE,  # pressure
                                                 _Pointer[IMidiChannelPressureMessage]],  # value
                                                _type.HRESULT]


class IMidiControlChangeMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Controller: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    get_ControlValue: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]


class IMidiControlChangeMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiControlChangeMessage: _Callable[[_type.BYTE,  # channel
                                               _type.BYTE,  # controller
                                               _type.BYTE,  # controlValue
                                               _Pointer[IMidiControlChangeMessage]],  # value
                                              _type.HRESULT]


class IMidiInPort(_inspectable.IInspectable):
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMidiInPort, IMidiMessageReceivedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IMidiInPortStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMidiInPort]]],  # value
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IMidiMessage(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_RawData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                           _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Devices.Midi.MidiMessageType]],  # value
                        _type.HRESULT]


class IMidiMessageReceivedEventArgs(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[IMidiMessage]],  # value
                           _type.HRESULT]


class IMidiNoteOffMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Note: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    get_Velocity: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]


class IMidiNoteOffMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiNoteOffMessage: _Callable[[_type.BYTE,  # channel
                                         _type.BYTE,  # note
                                         _type.BYTE,  # velocity
                                         _Pointer[IMidiNoteOffMessage]],  # value
                                        _type.HRESULT]


class IMidiNoteOnMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Note: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    get_Velocity: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]


class IMidiNoteOnMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiNoteOnMessage: _Callable[[_type.BYTE,  # channel
                                        _type.BYTE,  # note
                                        _type.BYTE,  # velocity
                                        _Pointer[IMidiNoteOnMessage]],  # value
                                       _type.HRESULT]


class IMidiOutPort(_inspectable.IInspectable):
    SendMessage: _Callable[[IMidiMessage],  # midiMessage
                           _type.HRESULT]
    SendBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # midiData
                          _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IMidiOutPortStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMidiOutPort]]],  # value
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IMidiPitchBendChangeMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Bend: _Callable[[_Pointer[_type.UINT16]],  # value
                        _type.HRESULT]


class IMidiPitchBendChangeMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiPitchBendChangeMessage: _Callable[[_type.BYTE,  # channel
                                                 _type.UINT16,  # bend
                                                 _Pointer[IMidiPitchBendChangeMessage]],  # value
                                                _type.HRESULT]


class IMidiPolyphonicKeyPressureMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Note: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.BYTE]],  # value
                            _type.HRESULT]


class IMidiPolyphonicKeyPressureMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiPolyphonicKeyPressureMessage: _Callable[[_type.BYTE,  # channel
                                                       _type.BYTE,  # note
                                                       _type.BYTE,  # pressure
                                                       _Pointer[IMidiPolyphonicKeyPressureMessage]],  # value
                                                      _type.HRESULT]


class IMidiProgramChangeMessage(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]
    get_Program: _Callable[[_Pointer[_type.BYTE]],  # value
                           _type.HRESULT]


class IMidiProgramChangeMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiProgramChangeMessage: _Callable[[_type.BYTE,  # channel
                                               _type.BYTE,  # program
                                               _Pointer[IMidiProgramChangeMessage]],  # value
                                              _type.HRESULT]


class IMidiSongPositionPointerMessage(_inspectable.IInspectable):
    get_Beats: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]


class IMidiSongPositionPointerMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiSongPositionPointerMessage: _Callable[[_type.UINT16,  # beats
                                                     _Pointer[IMidiSongPositionPointerMessage]],  # value
                                                    _type.HRESULT]


class IMidiSongSelectMessage(_inspectable.IInspectable):
    get_Song: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]


class IMidiSongSelectMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiSongSelectMessage: _Callable[[_type.BYTE,  # song
                                            _Pointer[IMidiSongSelectMessage]],  # value
                                           _type.HRESULT]


class IMidiSynthesizer(_inspectable.IInspectable):
    get_AudioDevice: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                               _type.HRESULT]
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]


class IMidiSynthesizerStatics(_inspectable.IInspectable, factory=True):
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMidiSynthesizer]]],  # value
                           _type.HRESULT]
    CreateFromAudioDeviceAsync: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # audioDevice
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IMidiSynthesizer]]],  # value
                                          _type.HRESULT]
    IsSynthesizer: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation,  # midiDevice
                              _Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IMidiSystemExclusiveMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiSystemExclusiveMessage: _Callable[[_Windows_Storage_Streams.IBuffer,  # rawData
                                                 _Pointer[IMidiMessage]],  # value
                                                _type.HRESULT]


class IMidiTimeCodeMessage(_inspectable.IInspectable):
    get_FrameType: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    get_Values: _Callable[[_Pointer[_type.BYTE]],  # value
                          _type.HRESULT]


class IMidiTimeCodeMessageFactory(_inspectable.IInspectable, factory=True):
    CreateMidiTimeCodeMessage: _Callable[[_type.BYTE,  # frameType
                                          _type.BYTE,  # values
                                          _Pointer[IMidiTimeCodeMessage]],  # value
                                         _type.HRESULT]
