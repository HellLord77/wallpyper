from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..enum import brotli as _enum_brotli

# decode
BrotliDecoderSetParameter: _Callable[[_Pointer[_struct.BrotliDecoderState],  # state
                                      _enum_brotli.BrotliDecoderParameter,  # param
                                      _type.uint32_t],  # value
                                     _type.c_int]
"""
Sets the specified parameter to the given decoder instance.
"""
BrotliDecoderAttachDictionary: _Callable[[_Pointer[_struct.BrotliDecoderState],  # state
                                          _enum_brotli.BrotliSharedDictionaryType,  # type
                                          _type.c_size_t,  # data_size
                                          _Pointer[_type.uint8_t]],  # data
                                         _type.c_int]
"""
Adds LZ77 prefix dictionary, adds or replaces built-in static dictionary and
transforms.
"""
BrotliDecoderCreateInstance: _Callable[[_type.brotli_alloc_func,  # alloc_func
                                        _type.brotli_free_func,  # free_func
                                        _type.c_void_p],  # opaque
                                       _Pointer[_struct.BrotliDecoderState]]
"""
Creates an instance of ::BrotliDecoderState and initializes it.
"""
BrotliDecoderDestroyInstance: _Callable[[_Pointer[_struct.BrotliDecoderState]],  # state
                                        _type.c_void]
"""
Deinitializes and frees ::BrotliDecoderState instance.
"""
BrotliDecoderDecompress: _Callable[[_type.c_size_t,  # encoded_size
                                    _Pointer[_type.uint8_t],  # encoded_buffer
                                    _Pointer[_type.c_size_t],  # decoded_size
                                    _Pointer[_type.uint8_t]],  # decoded_buffer
                                   _enum_brotli.BrotliDecoderResult]
"""
Performs one-shot memory-to-memory decompression.
"""
BrotliDecoderDecompressStream: _Callable[[_Pointer[_struct.BrotliDecoderState],  # state
                                          _Pointer[_type.c_size_t],  # available_in
                                          _Pointer[_Pointer[_type.uint8_t]],  # next_in
                                          _Pointer[_type.c_size_t],  # available_out
                                          _Pointer[_Pointer[_type.uint8_t]],  # next_out
                                          _Pointer[_type.c_size_t]],  # total_out
                                         _enum_brotli.BrotliDecoderResult]
"""
Decompresses the input stream to the output stream.
"""
BrotliDecoderHasMoreOutput: _Callable[[_Pointer[_struct.BrotliDecoderState]],  # state
                                      _type.c_int]
"""
Checks if decoder has more output.
"""
BrotliDecoderTakeOutput: _Callable[[_Pointer[_struct.BrotliDecoderState],  # state
                                    _Pointer[_type.c_size_t]],  # size
                                   _Pointer[_type.uint8_t]]
"""
Acquires pointer to internal output buffer.
"""
BrotliDecoderIsUsed: _Callable[[_Pointer[_struct.BrotliDecoderState]],  # state
                               _type.c_int]
"""
Checks if instance has already consumed input.
"""
BrotliDecoderIsFinished: _Callable[[_Pointer[_struct.BrotliDecoderState]],  # state
                                   _type.c_int]
"""
Checks if decoder instance reached the final state.
"""
BrotliDecoderGetErrorCode: _Callable[[_Pointer[_struct.BrotliDecoderState]],  # state
                                     _enum_brotli.BrotliDecoderErrorCode]
"""
Acquires a detailed error code.
"""
BrotliDecoderErrorString: _Callable[[_enum_brotli.BrotliDecoderErrorCode],  # c
                                    _type.c_char_p]
"""
Converts error code to a c-string.
"""
BrotliDecoderVersion: _Callable[[],
                                _type.uint32_t]
"""
Gets a decoder library version.
"""
BrotliDecoderSetMetadataCallbacks: _Callable[[_Pointer[_struct.BrotliDecoderState],  # state
                                              _type.brotli_decoder_metadata_start_func,  # start_func
                                              _type.brotli_decoder_metadata_chunk_func,  # chunk_func
                                              _type.c_void_p],  # opaque
                                             _type.c_void]
"""
Sets callback for receiving metadata blocks.
"""

_WinLib(__name__)
