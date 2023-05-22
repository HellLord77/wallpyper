from __future__ import annotations

from typing import Callable as _Callable

from .. import Streams as _Windows_Storage_Streams
from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class ICompressor(_inspectable.IInspectable):
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]
    DetachStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # stream
                            _type.HRESULT]


class ICompressorFactory(_inspectable.IInspectable, factory=True):
    CreateCompressor: _Callable[[_Windows_Storage_Streams.IOutputStream,  # underlyingStream
                                 _Pointer[ICompressor]],  # createdCompressor
                                _type.HRESULT]
    CreateCompressorEx: _Callable[[_Windows_Storage_Streams.IOutputStream,  # underlyingStream
                                   _enum.Windows.Storage.Compression.CompressAlgorithm,  # algorithm
                                   _type.UINT32,  # blockSize
                                   _Pointer[ICompressor]],  # createdCompressor
                                  _type.HRESULT]


class IDecompressor(_inspectable.IInspectable):
    DetachStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # stream
                            _type.HRESULT]


class IDecompressorFactory(_inspectable.IInspectable, factory=True):
    CreateDecompressor: _Callable[[_Windows_Storage_Streams.IInputStream,  # underlyingStream
                                   _Pointer[IDecompressor]],  # createdDecompressor
                                  _type.HRESULT]
