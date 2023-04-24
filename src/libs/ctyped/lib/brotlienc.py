from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..enum import brotli as _enum_brotli

# encode
BrotliEncoderSetParameter: _Callable[[_Pointer[_struct.BrotliEncoderState],  # state
                                      _enum_brotli.BrotliEncoderParameter,  # param
                                      _type.uint32_t],  # value
                                     _type.c_int]
"""
Sets the specified parameter to the given encoder instance.
"""
BrotliEncoderCreateInstance: _Callable[[_type.brotli_alloc_func,  # alloc_func
                                        _type.brotli_free_func,  # free_func
                                        _type.c_void_p],  # opaque
                                       _Pointer[_struct.BrotliEncoderState]]
"""
Creates an instance of ::BrotliEncoderState and initializes it.
"""
BrotliEncoderDestroyInstance: _Callable[[_Pointer[_struct.BrotliEncoderState]],  # state
                                        _type.c_void]
"""
Deinitializes and frees ::BrotliEncoderState instance.
"""
BrotliEncoderMaxCompressedSize: _Callable[[_type.c_size_t],  # input_size
                                          _type.c_size_t]
"""
Calculates the output size bound for the given input_size.
"""
BrotliEncoderCompress: _Callable[[_type.c_int,  # quality
                                  _type.c_int,  # lgwin
                                  _enum_brotli.BrotliEncoderMode,  # mode
                                  _type.c_size_t,  # input_size
                                  _Pointer[_type.uint8_t],  # input_buffer
                                  _Pointer[_type.c_size_t],  # encoded_size
                                  _Pointer[_type.uint8_t]],  # encoded_buffer
                                 _type.c_int]
"""
Performs one-shot memory-to-memory compression.
"""
BrotliEncoderCompressStream: _Callable[[_Pointer[_struct.BrotliEncoderState],  # state
                                        _enum_brotli.BrotliEncoderOperation,  # op
                                        _Pointer[_type.c_size_t],  # available_in
                                        _Pointer[_Pointer[_type.uint8_t]],  # next_in
                                        _Pointer[_type.c_size_t],  # available_out
                                        _Pointer[_Pointer[_type.uint8_t]],  # next_out
                                        _Pointer[_type.c_size_t]],  # total_out
                                       _type.c_int]
"""
Compresses input stream to output stream.
"""
BrotliEncoderIsFinished: _Callable[[_Pointer[_struct.BrotliEncoderState]],  # state
                                   _type.c_int]
"""
Checks if encoder instance reached the final state.
"""
BrotliEncoderHasMoreOutput: _Callable[[_Pointer[_struct.BrotliEncoderState]],  # state
                                      _type.c_int]
"""
Checks if encoder has more output.
"""
BrotliEncoderTakeOutput: _Callable[[_Pointer[_struct.BrotliEncoderState],  # state
                                    _Pointer[_type.c_size_t]],  # size
                                   _Pointer[_type.uint8_t]]
"""
Acquires pointer to internal output buffer.
"""
BrotliEncoderVersion: _Callable[[],
                                _type.uint32_t]
"""
Gets an encoder library version.
"""

_WinLib(__name__)
