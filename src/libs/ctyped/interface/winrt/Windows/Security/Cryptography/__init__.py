from __future__ import annotations

from typing import Callable as _Callable

from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ICryptographicBufferStatics(_inspectable.IInspectable):
    Compare: _Callable[[_Windows_Storage_Streams.IBuffer,  # object1
                        _Windows_Storage_Streams.IBuffer,  # object2
                        _Pointer[_type.boolean]],  # isEqual
                       _type.HRESULT]
    GenerateRandom: _Callable[[_type.UINT32,  # length
                               _Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                              _type.HRESULT]
    GenerateRandomNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    CreateFromByteArray: _Callable[[_type.UINT32,  # __valueSize
                                    _Pointer[_type.BYTE],  # value
                                    _Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                   _type.HRESULT]
    CopyToByteArray: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                _Pointer[_type.UINT32],  # __valueSize
                                _Pointer[_Pointer[_type.BYTE]]],  # value
                               _type.HRESULT]
    DecodeFromHexString: _Callable[[_type.HSTRING,  # value
                                    _Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                   _type.HRESULT]
    EncodeToHexString: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    DecodeFromBase64String: _Callable[[_type.HSTRING,  # value
                                       _Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                      _type.HRESULT]
    EncodeToBase64String: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                     _Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    ConvertStringToBinary: _Callable[[_type.HSTRING,  # value
                                      _enum.Windows.Security.Cryptography.BinaryStringEncoding,  # encoding
                                      _Pointer[_Windows_Storage_Streams.IBuffer]],  # buffer
                                     _type.HRESULT]
    ConvertBinaryToString: _Callable[[_enum.Windows.Security.Cryptography.BinaryStringEncoding,  # encoding
                                      _Windows_Storage_Streams.IBuffer,  # buffer
                                      _Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]

    _factory = True
