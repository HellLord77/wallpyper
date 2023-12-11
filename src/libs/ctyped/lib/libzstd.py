from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..enum import zstd as _enum_zstd

# zstd
ZSTD_versionNumber: _Callable[[],
                              _type.c_uint]
"""
ZSTD_versionNumber() : Return runtime library version, the value is
(MAJOR*100*100 + MINOR*100 + RELEASE).
"""
ZSTD_versionString: _Callable[[],
                              _type.c_char_p]
"""
ZSTD_versionString() : Return runtime library version, like "1.4.5". Requires
v1.3.0+.
"""
ZSTD_compress: _Callable[[_type.c_void_p,  # dst
                          _type.c_size_t,  # dstCapacity
                          _type.c_void_p,  # src
                          _type.c_size_t,  # srcSize
                          _type.c_int],  # compressionLevel
                         _type.c_size_t]
"""
************************************* Simple API
*************************************
"""
ZSTD_decompress: _Callable[[_type.c_void_p,  # dst
                            _type.c_size_t,  # dstCapacity
                            _type.c_void_p,  # src
                            _type.c_size_t],  # compressedSize
                           _type.c_size_t]
"""
ZSTD_decompress() : `compressedSize` : must be the _exact_ size of some number
of compressed and/or skippable frames. `dstCapacity` is an upper bound of
originalSize to regenerate. If user cannot imply a maximum upper bound, it's
better to use streaming mode to decompress data.
"""
ZSTD_getFrameContentSize: _Callable[[_type.c_void_p,  # src
                                     _type.c_size_t],  # srcSize
                                    _type.c_ulonglong]
ZSTD_getDecompressedSize: _Callable[[_type.c_void_p,  # src
                                     _type.c_size_t],  # srcSize
                                    _type.c_ulonglong]
"""
ZSTD_getDecompressedSize() : NOTE: This function is now obsolete, in favor of
ZSTD_getFrameContentSize(). Both functions work the same way, but
ZSTD_getDecompressedSize() blends "empty", "unknown" and "error" results to the
same return value (0), while ZSTD_getFrameContentSize() gives them separate
return values.
"""
ZSTD_findFrameCompressedSize: _Callable[[_type.c_void_p,  # src
                                         _type.c_size_t],  # srcSize
                                        _type.c_size_t]
"""
ZSTD_findFrameCompressedSize() : Requires v1.4.0+ `src` should point to the
start of a ZSTD frame or skippable frame. `srcSize` must be >= first frame size
"""
ZSTD_compressBound: _Callable[[_type.c_size_t],  # srcSize
                              _type.c_size_t]
ZSTD_isError: _Callable[[_type.c_size_t],  # code
                        _type.c_uint]
"""
ZSTD_isError() : Most ZSTD_* functions returning a size_t value can be tested
for error, using ZSTD_isError().
"""
ZSTD_getErrorName: _Callable[[_type.c_size_t],  # code
                             _type.c_char_p]
ZSTD_minCLevel: _Callable[[],
                          _type.c_int]
ZSTD_maxCLevel: _Callable[[],
                          _type.c_int]
ZSTD_defaultCLevel: _Callable[[],
                              _type.c_int]
ZSTD_createCCtx: _Callable[[],
                           _Pointer[_struct.ZSTD_CCtx]]
ZSTD_freeCCtx: _Callable[[_Pointer[_struct.ZSTD_CCtx]],  # cctx
                         _type.c_size_t]
ZSTD_compressCCtx: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                              _type.c_void_p,  # dst
                              _type.c_size_t,  # dstCapacity
                              _type.c_void_p,  # src
                              _type.c_size_t,  # srcSize
                              _type.c_int],  # compressionLevel
                             _type.c_size_t]
"""
ZSTD_compressCCtx() : Same as ZSTD_compress(), using an explicit ZSTD_CCtx.
Important : in order to behave similarly to `ZSTD_compress()`, this function
compresses at requested compression level, __ignoring any other parameter__ . If
any advanced parameter was set using the advanced API, they will all be reset.
Only `compressionLevel` remains.
"""
ZSTD_createDCtx: _Callable[[],
                           _Pointer[_struct.ZSTD_DCtx]]
ZSTD_freeDCtx: _Callable[[_Pointer[_struct.ZSTD_DCtx]],  # dctx
                         _type.c_size_t]
ZSTD_decompressDCtx: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                _type.c_void_p,  # dst
                                _type.c_size_t,  # dstCapacity
                                _type.c_void_p,  # src
                                _type.c_size_t],  # srcSize
                               _type.c_size_t]
"""
ZSTD_decompressDCtx() : Same as ZSTD_decompress(), requires an allocated
ZSTD_DCtx. Compatible with sticky parameters.
"""
ZSTD_cParam_getBounds: _Callable[[_enum_zstd.ZSTD_cParameter],  # cParam
                                 _struct.ZSTD_bounds]
"""
ZSTD_cParam_getBounds() : All parameters must belong to an interval with lower
and upper bounds, otherwise they will either trigger an error or be
automatically clamped.
"""
ZSTD_CCtx_setParameter: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                   _enum_zstd.ZSTD_cParameter,  # param
                                   _type.c_int],  # value
                                  _type.c_size_t]
"""
ZSTD_CCtx_setParameter() : Set one compression parameter, selected by enum
ZSTD_cParameter. All parameters have valid bounds. Bounds can be queried using
ZSTD_cParam_getBounds(). Providing a value beyond bound will either clamp it, or
trigger an error (depending on parameter). Setting a parameter is generally only
possible during frame initialization (before starting compression). Exception :
when using multi-threading mode (nbWorkers >= 1), the following parameters can
be updated _during_ compression (within same frame): => compressionLevel,
hashLog, chainLog, searchLog, minMatch, targetLength and strategy. new
parameters will be active for next job only (after a flush()).
"""
ZSTD_CCtx_setPledgedSrcSize: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                        _type.c_ulonglong],  # pledgedSrcSize
                                       _type.c_size_t]
"""
ZSTD_CCtx_setPledgedSrcSize() : Total input data size to be compressed as a
single frame. Value will be written in frame header, unless if explicitly
forbidden using ZSTD_c_contentSizeFlag. This value will also be controlled at
end of frame, and trigger an error if not respected.
"""
ZSTD_CCtx_reset: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                            _enum_zstd.ZSTD_ResetDirective],  # reset
                           _type.c_size_t]
"""
ZSTD_CCtx_reset() : There are 2 different things that can be reset,
independently or jointly : - The session : will stop compressing current frame,
and make CCtx ready to start a new one. Useful after an error, or to interrupt
any ongoing compression. Any internal data not yet flushed is cancelled.
Compression parameters and dictionary remain unchanged. They will be used to
compress next frame. Resetting session never fails. - The parameters : changes
all parameters back to "default". This also removes any reference to any
dictionary or external sequence producer. Parameters can only be changed between
2 sessions (i.e. no compression is currently ongoing) otherwise the reset fails,
and function returns an error value (which can be tested using ZSTD_isError()) -
Both : similar to resetting the session, followed by resetting parameters.
"""
ZSTD_compress2: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                           _type.c_void_p,  # dst
                           _type.c_size_t,  # dstCapacity
                           _type.c_void_p,  # src
                           _type.c_size_t],  # srcSize
                          _type.c_size_t]
"""
ZSTD_compress2() : Behave the same as ZSTD_compressCCtx(), but compression
parameters are set using the advanced API. ZSTD_compress2() always starts a new
frame. Should cctx hold data from a previously unfinished frame, everything
about it is forgotten. - Compression parameters are pushed into CCtx before
starting compression, using ZSTD_CCtx_set*() - The function is always blocking,
returns when compression is completed. NOTE: Providing `dstCapacity >=
ZSTD_compressBound(srcSize)` guarantees that zstd will have enough space to
successfully compress the data, though it is possible it fails for other
reasons.
"""
ZSTD_dParam_getBounds: _Callable[[_enum_zstd.ZSTD_dParameter],  # dParam
                                 _struct.ZSTD_bounds]
"""
ZSTD_dParam_getBounds() : All parameters must belong to an interval with lower
and upper bounds, otherwise they will either trigger an error or be
automatically clamped.
"""
ZSTD_DCtx_setParameter: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                   _enum_zstd.ZSTD_dParameter,  # param
                                   _type.c_int],  # value
                                  _type.c_size_t]
"""
ZSTD_DCtx_setParameter() : Set one compression parameter, selected by enum
ZSTD_dParameter. All parameters have valid bounds. Bounds can be queried using
ZSTD_dParam_getBounds(). Providing a value beyond bound will either clamp it, or
trigger an error (depending on parameter). Setting a parameter is only possible
during frame initialization (before starting decompression).
"""
ZSTD_DCtx_reset: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                            _enum_zstd.ZSTD_ResetDirective],  # reset
                           _type.c_size_t]
"""
ZSTD_DCtx_reset() : Return a DCtx to clean state. Session and parameters can be
reset jointly or separately. Parameters can only be reset when no active frame
is being decompressed.
"""
ZSTD_createCStream: _Callable[[],
                              _Pointer[_struct.ZSTD_CStream]]
"""
===== ZSTD_CStream management functions =====
"""
ZSTD_freeCStream: _Callable[[_Pointer[_struct.ZSTD_CStream]],  # zcs
                            _type.c_size_t]
ZSTD_compressStream2: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                 _Pointer[_struct.ZSTD_outBuffer],  # output
                                 _Pointer[_struct.ZSTD_inBuffer],  # input
                                 _enum_zstd.ZSTD_EndDirective],  # endOp
                                _type.c_size_t]
"""
ZSTD_compressStream2() : Requires v1.4.0+ Behaves about the same as
ZSTD_compressStream, with additional control on end directive. - Compression
parameters are pushed into CCtx before starting compression, using
ZSTD_CCtx_set*() - Compression parameters cannot be changed once compression is
started (save a list of exceptions in multi-threading mode) - output->pos must
be <= dstCapacity, input->pos must be <= srcSize - output->pos and input->pos
will be updated. They are guaranteed to remain below their respective limit. -
endOp must be a valid directive - When nbWorkers==0 (default), function is
blocking : it completes its job before returning to caller. - When nbWorkers>=1,
function is non-blocking : it copies a portion of input, distributes jobs to
internal worker threads, flush to output whatever is available, and then
immediately returns, just indicating that there is some data remaining to be
flushed. The function nonetheless guarantees forward progress : it will return
only after it reads or write at least 1+ byte. - Exception : if the first call
requests a ZSTD_e_end directive and provides enough dstCapacity, the function
delegates to ZSTD_compress2() which is always blocking. -
"""
ZSTD_CStreamInSize: _Callable[[],
                              _type.c_size_t]
"""
These buffer sizes are softly recommended. They are not required :
ZSTD_compressStream*() happily accepts any buffer size, for both input and
output. Respecting the recommended size just makes it a bit easier for
ZSTD_compressStream*(), reducing the amount of memory shuffling and buffering,
resulting in minor performance savings.
"""
ZSTD_CStreamOutSize: _Callable[[],
                               _type.c_size_t]
ZSTD_initCStream: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                             _type.c_int],  # compressionLevel
                            _type.c_size_t]
"""
Equivalent to:
"""
ZSTD_compressStream: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                _Pointer[_struct.ZSTD_outBuffer],  # output
                                _Pointer[_struct.ZSTD_inBuffer]],  # input
                               _type.c_size_t]
"""
Alternative for ZSTD_compressStream2(zcs, output, input, ZSTD_e_continue). NOTE:
The return value is different. ZSTD_compressStream() returns a hint for the next
read size (if non-zero and not an error). ZSTD_compressStream2() returns the
minimum nb of bytes left to flush (if non-zero and not an error).
"""
ZSTD_flushStream: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                             _Pointer[_struct.ZSTD_outBuffer]],  # output
                            _type.c_size_t]
"""
Equivalent to ZSTD_compressStream2(zcs, output, &emptyInput, ZSTD_e_flush).
"""
ZSTD_endStream: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                           _Pointer[_struct.ZSTD_outBuffer]],  # output
                          _type.c_size_t]
"""
Equivalent to ZSTD_compressStream2(zcs, output, &emptyInput, ZSTD_e_end).
"""
ZSTD_createDStream: _Callable[[],
                              _Pointer[_struct.ZSTD_DStream]]
"""
===== ZSTD_DStream management functions =====
"""
ZSTD_freeDStream: _Callable[[_Pointer[_struct.ZSTD_DStream]],  # zds
                            _type.c_size_t]
ZSTD_initDStream: _Callable[[_Pointer[_struct.ZSTD_DStream]],  # zds
                            _type.c_size_t]
"""
ZSTD_initDStream() : Initialize/reset DStream state for new decompression
operation. Call before new decompression operation using same DStream.
"""
ZSTD_decompressStream: _Callable[[_Pointer[_struct.ZSTD_DStream],  # zds
                                  _Pointer[_struct.ZSTD_outBuffer],  # output
                                  _Pointer[_struct.ZSTD_inBuffer]],  # input
                                 _type.c_size_t]
"""
ZSTD_decompressStream() : Streaming decompression function. Call repetitively to
consume full input updating it as necessary. Function will update both input and
output `pos` fields exposing current state via these fields: - `input.pos <
input.size`, some input remaining and caller should provide remaining input on
the next call. - `output.pos < output.size`, decoder finished and flushed all
remaining buffers. - `output.pos == output.size`, potentially uncflushed data
present in the internal buffers, call ZSTD_decompressStream() again to flush
remaining data to output. Note : with no additional input, amount of data
flushed <= ZSTD_BLOCKSIZE_MAX.
"""
ZSTD_DStreamInSize: _Callable[[],
                              _type.c_size_t]
ZSTD_DStreamOutSize: _Callable[[],
                               _type.c_size_t]
ZSTD_compress_usingDict: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # ctx
                                    _type.c_void_p,  # dst
                                    _type.c_size_t,  # dstCapacity
                                    _type.c_void_p,  # src
                                    _type.c_size_t,  # srcSize
                                    _type.c_void_p,  # dict
                                    _type.c_size_t,  # dictSize
                                    _type.c_int],  # compressionLevel
                                   _type.c_size_t]
"""
************************ Simple dictionary API *************************
"""
ZSTD_decompress_usingDict: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                      _type.c_void_p,  # dst
                                      _type.c_size_t,  # dstCapacity
                                      _type.c_void_p,  # src
                                      _type.c_size_t,  # srcSize
                                      _type.c_void_p,  # dict
                                      _type.c_size_t],  # dictSize
                                     _type.c_size_t]
"""
ZSTD_decompress_usingDict() : Decompression using a known Dictionary. Dictionary
must be identical to the one used during compression. Note : This function loads
the dictionary, resulting in significant startup delay. It's intended for a
dictionary used only once. Note : When `dict == NULL || dictSize < 8` no
dictionary is used.
"""
ZSTD_createCDict: _Callable[[_type.c_void_p,  # dictBuffer
                             _type.c_size_t,  # dictSize
                             _type.c_int],  # compressionLevel
                            _Pointer[_struct.ZSTD_CDict]]
"""
ZSTD_createCDict() : When compressing multiple messages or blocks using the same
dictionary, it's recommended to digest the dictionary only once, since it's a
costly operation. ZSTD_createCDict() will create a state from digesting a
dictionary. The resulting state can be used for future compression operations
with very limited startup cost. ZSTD_CDict can be created once and shared by
multiple threads concurrently, since its usage is read-only. can be released
after ZSTD_CDict creation, because its content is copied within CDict. Note 1 :
Consider experimental function `ZSTD_createCDict_byReference()` if you prefer to
not duplicate content. Note 2 : A ZSTD_CDict can be created from an empty , in
which case the only thing that it transports is the . This can be useful in a
pipeline featuring ZSTD_compress_usingCDict() exclusively, expecting a
ZSTD_CDict parameter with any data, including those without a known dictionary.
"""
ZSTD_freeCDict: _Callable[[_Pointer[_struct.ZSTD_CDict]],  # CDict
                          _type.c_size_t]
"""
ZSTD_freeCDict() : Function frees memory allocated by ZSTD_createCDict(). If a
NULL pointer is passed, no operation is performed.
"""
ZSTD_compress_usingCDict: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                     _type.c_void_p,  # dst
                                     _type.c_size_t,  # dstCapacity
                                     _type.c_void_p,  # src
                                     _type.c_size_t,  # srcSize
                                     _Pointer[_struct.ZSTD_CDict]],  # cdict
                                    _type.c_size_t]
"""
ZSTD_compress_usingCDict() : Compression using a digested Dictionary.
Recommended when same dictionary is used multiple times. Note : compression
level is _decided at dictionary creation time_, and frame parameters are
hardcoded (dictID=yes, contentSize=yes, checksum=no)
"""
ZSTD_createDDict: _Callable[[_type.c_void_p,  # dictBuffer
                             _type.c_size_t],  # dictSize
                            _Pointer[_struct.ZSTD_DDict]]
"""
ZSTD_createDDict() : Create a digested dictionary, ready to start decompression
operation without startup delay. dictBuffer can be released after DDict
creation, as its content is copied inside DDict.
"""
ZSTD_freeDDict: _Callable[[_Pointer[_struct.ZSTD_DDict]],  # ddict
                          _type.c_size_t]
"""
ZSTD_freeDDict() : Function frees memory allocated with ZSTD_createDDict() If a
NULL pointer is passed, no operation is performed.
"""
ZSTD_decompress_usingDDict: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                       _type.c_void_p,  # dst
                                       _type.c_size_t,  # dstCapacity
                                       _type.c_void_p,  # src
                                       _type.c_size_t,  # srcSize
                                       _Pointer[_struct.ZSTD_DDict]],  # ddict
                                      _type.c_size_t]
"""
ZSTD_decompress_usingDDict() : Decompression using a digested Dictionary.
Recommended when same dictionary is used multiple times.
"""
ZSTD_getDictID_fromDict: _Callable[[_type.c_void_p,  # dict
                                    _type.c_size_t],  # dictSize
                                   _type.c_uint]
"""
ZSTD_getDictID_fromDict() : Requires v1.4.0+ Provides the dictID stored within
dictionary. if
"""
ZSTD_getDictID_fromCDict: _Callable[[_Pointer[_struct.ZSTD_CDict]],  # cdict
                                    _type.c_uint]
"""
ZSTD_getDictID_fromCDict() : Requires v1.5.0+ Provides the dictID of the
dictionary loaded into `cdict`. If
"""
ZSTD_getDictID_fromDDict: _Callable[[_Pointer[_struct.ZSTD_DDict]],  # ddict
                                    _type.c_uint]
"""
ZSTD_getDictID_fromDDict() : Requires v1.4.0+ Provides the dictID of the
dictionary loaded into `ddict`. If
"""
ZSTD_getDictID_fromFrame: _Callable[[_type.c_void_p,  # src
                                     _type.c_size_t],  # srcSize
                                    _type.c_uint]
"""
ZSTD_getDictID_fromFrame() : Requires v1.4.0+ Provides the dictID required to
decompressed the frame stored within `src`. If
"""
ZSTD_CCtx_loadDictionary: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                     _type.c_void_p,  # dict
                                     _type.c_size_t],  # dictSize
                                    _type.c_size_t]
"""
ZSTD_CCtx_loadDictionary() : Requires v1.4.0+ Create an internal CDict from
`dict` buffer. Decompression will have to use same dictionary.
"""
ZSTD_CCtx_refCDict: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                               _Pointer[_struct.ZSTD_CDict]],  # cdict
                              _type.c_size_t]
"""
ZSTD_CCtx_refCDict() : Requires v1.4.0+ Reference a prepared dictionary, to be
used for all future compressed frames. Note that compression parameters are
enforced from within CDict, and supersede any compression parameter previously
set within CCtx. The parameters ignored are labelled as "superseded-by-cdict" in
the ZSTD_cParameter enum docs. The ignored parameters will be used again if the
CCtx is returned to no-dictionary mode. The dictionary will remain valid for
future compressed frames using same CCtx.
"""
ZSTD_CCtx_refPrefix: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                _type.c_void_p,  # prefix
                                _type.c_size_t],  # prefixSize
                               _type.c_size_t]
"""
ZSTD_CCtx_refPrefix() : Requires v1.4.0+ Reference a prefix (single-usage
dictionary) for next compressed frame. A prefix is **only used once**. Tables
are discarded at end of frame (ZSTD_e_end). Decompression will need same prefix
to properly regenerate data. Compressing with a prefix is similar in outcome as
performing a diff and compressing it, but performs much faster, especially
during decompression (compression speed is tunable with compression level). This
method is compatible with LDM (long distance mode).
"""
ZSTD_DCtx_loadDictionary: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                     _type.c_void_p,  # dict
                                     _type.c_size_t],  # dictSize
                                    _type.c_size_t]
"""
ZSTD_DCtx_loadDictionary() : Requires v1.4.0+ Create an internal DDict from dict
buffer, to be used to decompress all future frames. The dictionary remains valid
for all future frames, until explicitly invalidated, or a new dictionary is
loaded.
"""
ZSTD_DCtx_refDDict: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                               _Pointer[_struct.ZSTD_DDict]],  # ddict
                              _type.c_size_t]
"""
ZSTD_DCtx_refDDict() : Requires v1.4.0+ Reference a prepared dictionary, to be
used to decompress next frames. The dictionary remains active for decompression
of future frames using same DCtx.
"""
ZSTD_DCtx_refPrefix: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                _type.c_void_p,  # prefix
                                _type.c_size_t],  # prefixSize
                               _type.c_size_t]
"""
ZSTD_DCtx_refPrefix() : Requires v1.4.0+ Reference a prefix (single-usage
dictionary) to decompress next frame. This is the reverse operation of
ZSTD_CCtx_refPrefix(), and must use the same prefix as the one used during
compression. Prefix is **only used once**. Reference is discarded at end of
frame. End of frame is reached when ZSTD_decompressStream() returns 0.
"""
ZSTD_sizeof_CCtx: _Callable[[_Pointer[_struct.ZSTD_CCtx]],  # cctx
                            _type.c_size_t]
"""
ZSTD_sizeof_*() : Requires v1.4.0+ These functions give the _current_ memory
usage of selected object. Note that object memory usage can evolve (increase or
decrease) over time.
"""
ZSTD_sizeof_DCtx: _Callable[[_Pointer[_struct.ZSTD_DCtx]],  # dctx
                            _type.c_size_t]
ZSTD_sizeof_CStream: _Callable[[_Pointer[_struct.ZSTD_CStream]],  # zcs
                               _type.c_size_t]
ZSTD_sizeof_DStream: _Callable[[_Pointer[_struct.ZSTD_DStream]],  # zds
                               _type.c_size_t]
ZSTD_sizeof_CDict: _Callable[[_Pointer[_struct.ZSTD_CDict]],  # cdict
                             _type.c_size_t]
ZSTD_sizeof_DDict: _Callable[[_Pointer[_struct.ZSTD_DDict]],  # ddict
                             _type.c_size_t]
ZSTD_findDecompressedSize: _Callable[[_type.c_void_p,  # src
                                      _type.c_size_t],  # srcSize
                                     _type.c_ulonglong]
"""
ZSTD_findDecompressedSize() : `src` should point to the start of a series of
ZSTD encoded and/or skippable frames `srcSize` must be the _exact_ size of this
series (i.e. there should be a frame boundary at `src + srcSize`)
"""
ZSTD_decompressBound: _Callable[[_type.c_void_p,  # src
                                 _type.c_size_t],  # srcSize
                                _type.c_ulonglong]
"""
ZSTD_decompressBound() : `src` should point to the start of a series of ZSTD
encoded and/or skippable frames `srcSize` must be the _exact_ size of this
series (i.e. there should be a frame boundary at `src + srcSize`)
"""
ZSTD_frameHeaderSize: _Callable[[_type.c_void_p,  # src
                                 _type.c_size_t],  # srcSize
                                _type.c_size_t]
"""
ZSTD_frameHeaderSize() : srcSize must be >= ZSTD_FRAMEHEADERSIZE_PREFIX.
"""
ZSTD_getFrameHeader: _Callable[[_Pointer[_struct.ZSTD_frameHeader],  # zfhPtr
                                _type.c_void_p,  # src
                                _type.c_size_t],  # srcSize
                               _type.c_size_t]
"""
ZSTD_getFrameHeader() : decode Frame Header, or requires larger `srcSize`.
"""
ZSTD_getFrameHeader_advanced: _Callable[[_Pointer[_struct.ZSTD_frameHeader],  # zfhPtr
                                         _type.c_void_p,  # src
                                         _type.c_size_t,  # srcSize
                                         _enum_zstd.ZSTD_format_e],  # format
                                        _type.c_size_t]
"""
ZSTD_getFrameHeader_advanced() : same as ZSTD_getFrameHeader(), with added
capability to select a format (like ZSTD_f_zstd1_magicless)
"""
ZSTD_decompressionMargin: _Callable[[_type.c_void_p,  # src
                                     _type.c_size_t],  # srcSize
                                    _type.c_size_t]
"""
ZSTD_decompressionMargin() : Zstd supports in-place decompression, where the
input and output buffers overlap. In this case, the output buffer must be at
least (Margin + Output_Size) bytes large, and the input buffer must be at the
end of the output buffer.
"""
ZSTD_sequenceBound: _Callable[[_type.c_size_t],  # srcSize
                              _type.c_size_t]
"""
ZSTD_sequenceBound() : `srcSize` : size of the input buffer
"""
ZSTD_generateSequences: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # zc
                                   _Pointer[_struct.ZSTD_Sequence],  # outSeqs
                                   _type.c_size_t,  # outSeqsSize
                                   _type.c_void_p,  # src
                                   _type.c_size_t],  # srcSize
                                  _type.c_size_t]
"""
ZSTD_generateSequences() : Generate sequences using ZSTD_compress2(), given a
source buffer.
"""
ZSTD_mergeBlockDelimiters: _Callable[[_Pointer[_struct.ZSTD_Sequence],  # sequences
                                      _type.c_size_t],  # seqsSize
                                     _type.c_size_t]
"""
ZSTD_mergeBlockDelimiters() : Given an array of ZSTD_Sequence, remove all
sequences that represent block delimiters/last literals by merging them into the
literals of the next sequence.
"""
ZSTD_compressSequences: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                   _type.c_void_p,  # dst
                                   _type.c_size_t,  # dstSize
                                   _Pointer[_struct.ZSTD_Sequence],  # inSeqs
                                   _type.c_size_t,  # inSeqsSize
                                   _type.c_void_p,  # src
                                   _type.c_size_t],  # srcSize
                                  _type.c_size_t]
"""
ZSTD_compressSequences() : Compress an array of ZSTD_Sequence, associated with
buffer, into dst. contains the entire input (not just the literals). If >
sum(sequence.length), the remaining bytes are considered all literals If a
dictionary is included, then the cctx should reference the dict. (see:
ZSTD_CCtx_refCDict(), ZSTD_CCtx_loadDictionary(), etc.) The entire source is
compressed into a single frame.
"""
ZSTD_writeSkippableFrame: _Callable[[_type.c_void_p,  # dst
                                     _type.c_size_t,  # dstCapacity
                                     _type.c_void_p,  # src
                                     _type.c_size_t,  # srcSize
                                     _type.c_uint],  # magicVariant
                                    _type.c_size_t]
"""
ZSTD_writeSkippableFrame() : Generates a zstd skippable frame containing data
given by src, and writes it to dst buffer.
"""
ZSTD_readSkippableFrame: _Callable[[_type.c_void_p,  # dst
                                    _type.c_size_t,  # dstCapacity
                                    _Pointer[_type.c_uint],  # magicVariant
                                    _type.c_void_p,  # src
                                    _type.c_size_t],  # srcSize
                                   _type.c_size_t]
"""
ZSTD_readSkippableFrame() : Retrieves a zstd skippable frame containing data
given by src, and writes it to dst buffer.
"""
ZSTD_isSkippableFrame: _Callable[[_type.c_void_p,  # buffer
                                  _type.c_size_t],  # size
                                 _type.c_uint]
"""
ZSTD_isSkippableFrame() : Tells if the content of `buffer` starts with a valid
Frame Identifier for a skippable frame.
"""
ZSTD_estimateCCtxSize: _Callable[[_type.c_int],  # compressionLevel
                                 _type.c_size_t]
"""
ZSTD_estimate*() : These functions make it possible to estimate memory usage of
a future {D,C}Ctx, before its creation.
"""
ZSTD_estimateCCtxSize_usingCParams: _Callable[[_struct.ZSTD_compressionParameters],  # cParams
                                              _type.c_size_t]
ZSTD_estimateCCtxSize_usingCCtxParams: _Callable[[_Pointer[_struct.ZSTD_CCtx_params]],  # params
                                                 _type.c_size_t]
ZSTD_estimateDCtxSize: _Callable[[],
                                 _type.c_size_t]
ZSTD_estimateCStreamSize: _Callable[[_type.c_int],  # compressionLevel
                                    _type.c_size_t]
"""
ZSTD_estimateCStreamSize() : ZSTD_estimateCStreamSize() will provide a budget
large enough for any compression level up to selected one. It will also consider
src size to be arbitrarily "large", which is worst case. If srcSize is known to
always be small, ZSTD_estimateCStreamSize_usingCParams() can provide a tighter
estimation. ZSTD_estimateCStreamSize_usingCParams() can be used in tandem with
ZSTD_getCParams() to create cParams from compressionLevel.
ZSTD_estimateCStreamSize_usingCCtxParams() can be used in tandem with
ZSTD_CCtxParams_setParameter(). Only single-threaded compression is supported.
This function will return an error code if ZSTD_c_nbWorkers is >= 1. Note :
CStream size estimation is only correct for single-threaded compression.
ZSTD_DStream memory budget depends on window Size. This information can be
passed manually, using ZSTD_estimateDStreamSize, or deducted from a valid frame
Header, using ZSTD_estimateDStreamSize_fromFrame(); Note : if streaming is init
with function ZSTD_init?Stream_usingDict(), an internal ?Dict will be created,
which additional size is not estimated here. In this case, get total size by
adding ZSTD_estimate?DictSize Note 2 : only single-threaded compression is
supported. ZSTD_estimateCStreamSize_usingCCtxParams() will return an error code
if ZSTD_c_nbWorkers is >= 1. Note 3 : ZSTD_estimateCStreamSize* functions are
not compatible with the Block-Level Sequence Producer API at this time. Size
estimates assume that no external sequence producer is registered.
"""
ZSTD_estimateCStreamSize_usingCParams: _Callable[[_struct.ZSTD_compressionParameters],  # cParams
                                                 _type.c_size_t]
ZSTD_estimateCStreamSize_usingCCtxParams: _Callable[[_Pointer[_struct.ZSTD_CCtx_params]],  # params
                                                    _type.c_size_t]
ZSTD_estimateDStreamSize: _Callable[[_type.c_size_t],  # windowSize
                                    _type.c_size_t]
ZSTD_estimateDStreamSize_fromFrame: _Callable[[_type.c_void_p,  # src
                                               _type.c_size_t],  # srcSize
                                              _type.c_size_t]
ZSTD_estimateCDictSize: _Callable[[_type.c_size_t,  # dictSize
                                   _type.c_int],  # compressionLevel
                                  _type.c_size_t]
"""
ZSTD_estimate?DictSize() : ZSTD_estimateCDictSize() will bet that src size is
relatively "small", and content is copied, like ZSTD_createCDict().
ZSTD_estimateCDictSize_advanced() makes it possible to control compression
parameters precisely, like ZSTD_createCDict_advanced(). Note : dictionaries
created by reference (`ZSTD_dlm_byRef`) are logically smaller.
"""
ZSTD_estimateCDictSize_advanced: _Callable[[_type.c_size_t,  # dictSize
                                            _struct.ZSTD_compressionParameters,  # cParams
                                            _enum_zstd.ZSTD_dictLoadMethod_e],  # dictLoadMethod
                                           _type.c_size_t]
ZSTD_estimateDDictSize: _Callable[[_type.c_size_t,  # dictSize
                                   _enum_zstd.ZSTD_dictLoadMethod_e],  # dictLoadMethod
                                  _type.c_size_t]
ZSTD_initStaticCCtx: _Callable[[_type.c_void_p,  # workspace
                                _type.c_size_t],  # workspaceSize
                               _Pointer[_struct.ZSTD_CCtx]]
"""
ZSTD_initStatic*() : Initialize an object using a pre-allocated fixed-size
buffer. workspace: The memory area to emplace the object into. Provided pointer
*must be 8-bytes aligned*. Buffer must outlive object. workspaceSize: Use
ZSTD_estimate*Size() to determine how large workspace must be to support target
scenario.
"""
ZSTD_initStaticCStream: _Callable[[_type.c_void_p,  # workspace
                                   _type.c_size_t],  # workspaceSize
                                  _Pointer[_struct.ZSTD_CStream]]
ZSTD_initStaticDCtx: _Callable[[_type.c_void_p,  # workspace
                                _type.c_size_t],  # workspaceSize
                               _Pointer[_struct.ZSTD_DCtx]]
ZSTD_initStaticDStream: _Callable[[_type.c_void_p,  # workspace
                                   _type.c_size_t],  # workspaceSize
                                  _Pointer[_struct.ZSTD_DStream]]
ZSTD_initStaticCDict: _Callable[[_type.c_void_p,  # workspace
                                 _type.c_size_t,  # workspaceSize
                                 _type.c_void_p,  # dict
                                 _type.c_size_t,  # dictSize
                                 _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                 _enum_zstd.ZSTD_dictContentType_e,  # dictContentType
                                 _struct.ZSTD_compressionParameters],  # cParams
                                _Pointer[_struct.ZSTD_CDict]]
ZSTD_initStaticDDict: _Callable[[_type.c_void_p,  # workspace
                                 _type.c_size_t,  # workspaceSize
                                 _type.c_void_p,  # dict
                                 _type.c_size_t,  # dictSize
                                 _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                 _enum_zstd.ZSTD_dictContentType_e],  # dictContentType
                                _Pointer[_struct.ZSTD_DDict]]
ZSTD_createCCtx_advanced: _Callable[[_struct.ZSTD_customMem],  # customMem
                                    _Pointer[_struct.ZSTD_CCtx]]
ZSTD_createCStream_advanced: _Callable[[_struct.ZSTD_customMem],  # customMem
                                       _Pointer[_struct.ZSTD_CStream]]
ZSTD_createDCtx_advanced: _Callable[[_struct.ZSTD_customMem],  # customMem
                                    _Pointer[_struct.ZSTD_DCtx]]
ZSTD_createDStream_advanced: _Callable[[_struct.ZSTD_customMem],  # customMem
                                       _Pointer[_struct.ZSTD_DStream]]
ZSTD_createCDict_advanced: _Callable[[_type.c_void_p,  # dict
                                      _type.c_size_t,  # dictSize
                                      _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                      _enum_zstd.ZSTD_dictContentType_e,  # dictContentType
                                      _struct.ZSTD_compressionParameters,  # cParams
                                      _struct.ZSTD_customMem],  # customMem
                                     _Pointer[_struct.ZSTD_CDict]]
ZSTD_createThreadPool: _Callable[[_type.c_size_t],  # numThreads
                                 _Pointer[_struct.ZSTD_threadPool]]
ZSTD_freeThreadPool: _Callable[[_Pointer[_struct.ZSTD_threadPool]],  # pool
                               _type.c_void]
ZSTD_CCtx_refThreadPool: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                    _Pointer[_struct.ZSTD_threadPool]],  # pool
                                   _type.c_size_t]
ZSTD_createCDict_advanced2: _Callable[[_type.c_void_p,  # dict
                                       _type.c_size_t,  # dictSize
                                       _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                       _enum_zstd.ZSTD_dictContentType_e,  # dictContentType
                                       _Pointer[_struct.ZSTD_CCtx_params],  # cctxParams
                                       _struct.ZSTD_customMem],  # customMem
                                      _Pointer[_struct.ZSTD_CDict]]
"""
This API is temporary and is expected to change or disappear in the future!
"""
ZSTD_createDDict_advanced: _Callable[[_type.c_void_p,  # dict
                                      _type.c_size_t,  # dictSize
                                      _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                      _enum_zstd.ZSTD_dictContentType_e,  # dictContentType
                                      _struct.ZSTD_customMem],  # customMem
                                     _Pointer[_struct.ZSTD_DDict]]
ZSTD_createCDict_byReference: _Callable[[_type.c_void_p,  # dictBuffer
                                         _type.c_size_t,  # dictSize
                                         _type.c_int],  # compressionLevel
                                        _Pointer[_struct.ZSTD_CDict]]
"""
ZSTD_createCDict_byReference() : Create a digested dictionary for compression
Dictionary content is just referenced, not duplicated. As a consequence,
`dictBuffer` **must** outlive CDict, and its content must remain unmodified
throughout the lifetime of CDict. note: equivalent to
ZSTD_createCDict_advanced(), with dictLoadMethod==ZSTD_dlm_byRef
"""
ZSTD_getCParams: _Callable[[_type.c_int,  # compressionLevel
                            _type.c_ulonglong,  # estimatedSrcSize
                            _type.c_size_t],  # dictSize
                           _struct.ZSTD_compressionParameters]
"""
ZSTD_getCParams() :
"""
ZSTD_getParams: _Callable[[_type.c_int,  # compressionLevel
                           _type.c_ulonglong,  # estimatedSrcSize
                           _type.c_size_t],  # dictSize
                          _struct.ZSTD_parameters]
"""
ZSTD_getParams() : same as ZSTD_getCParams(), but
"""
ZSTD_checkCParams: _Callable[[_struct.ZSTD_compressionParameters],  # params
                             _type.c_size_t]
"""
ZSTD_checkCParams() : Ensure param values remain within authorized range.
"""
ZSTD_adjustCParams: _Callable[[_struct.ZSTD_compressionParameters,  # cPar
                               _type.c_ulonglong,  # srcSize
                               _type.c_size_t],  # dictSize
                              _struct.ZSTD_compressionParameters]
"""
ZSTD_adjustCParams() : optimize params for a given `srcSize` and `dictSize`.
`srcSize` can be unknown, in which case use ZSTD_CONTENTSIZE_UNKNOWN. `dictSize`
must be `0` when there is no dictionary. cPar can be invalid : all parameters
will be clamped within valid range in the
"""
ZSTD_CCtx_setCParams: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                 _struct.ZSTD_compressionParameters],  # cparams
                                _type.c_size_t]
"""
ZSTD_CCtx_setCParams() : Set all parameters provided within cparams into the
working cctx. Note : if modifying parameters during compression (MT mode only),
note that changes to the .windowLog parameter will be ignored.
"""
ZSTD_CCtx_setFParams: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                 _struct.ZSTD_frameParameters],  # fparams
                                _type.c_size_t]
"""
ZSTD_CCtx_setFParams() : Set all parameters provided within fparams into the
working cctx.
"""
ZSTD_CCtx_setParams: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                _struct.ZSTD_parameters],  # params
                               _type.c_size_t]
"""
ZSTD_CCtx_setParams() : Set all parameters provided within params into the
working cctx.
"""
ZSTD_compress_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                   _type.c_void_p,  # dst
                                   _type.c_size_t,  # dstCapacity
                                   _type.c_void_p,  # src
                                   _type.c_size_t,  # srcSize
                                   _type.c_void_p,  # dict
                                   _type.c_size_t,  # dictSize
                                   _struct.ZSTD_parameters],  # params
                                  _type.c_size_t]
"""
ZSTD_compress_advanced() : Note : this function is now DEPRECATED. It can be
replaced by ZSTD_compress2(), in combination with ZSTD_CCtx_setParameter() and
other parameter setters. This prototype will generate compilation warnings.
"""
ZSTD_compress_usingCDict_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                              _type.c_void_p,  # dst
                                              _type.c_size_t,  # dstCapacity
                                              _type.c_void_p,  # src
                                              _type.c_size_t,  # srcSize
                                              _Pointer[_struct.ZSTD_CDict],  # cdict
                                              _struct.ZSTD_frameParameters],  # fParams
                                             _type.c_size_t]
"""
ZSTD_compress_usingCDict_advanced() : Note : this function is now DEPRECATED. It
can be replaced by ZSTD_compress2(), in combination with
ZSTD_CCtx_loadDictionary() and other parameter setters. This prototype will
generate compilation warnings.
"""
ZSTD_CCtx_loadDictionary_byReference: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                                 _type.c_void_p,  # dict
                                                 _type.c_size_t],  # dictSize
                                                _type.c_size_t]
"""
ZSTD_CCtx_loadDictionary_byReference() : Same as ZSTD_CCtx_loadDictionary(), but
dictionary content is referenced, instead of being copied into CCtx. It saves
some memory, but also requires that `dict` outlives its usage within `cctx`
"""
ZSTD_CCtx_loadDictionary_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                              _type.c_void_p,  # dict
                                              _type.c_size_t,  # dictSize
                                              _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                              _enum_zstd.ZSTD_dictContentType_e],  # dictContentType
                                             _type.c_size_t]
"""
ZSTD_CCtx_loadDictionary_advanced() : Same as ZSTD_CCtx_loadDictionary(), but
gives finer control over how to load the dictionary (by copy ? by reference ?)
and how to interpret it (automatic ? force raw mode ? full mode only ?)
"""
ZSTD_CCtx_refPrefix_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                         _type.c_void_p,  # prefix
                                         _type.c_size_t,  # prefixSize
                                         _enum_zstd.ZSTD_dictContentType_e],  # dictContentType
                                        _type.c_size_t]
"""
ZSTD_CCtx_refPrefix_advanced() : Same as ZSTD_CCtx_refPrefix(), but gives finer
control over how to interpret prefix content (automatic ? force raw mode
(default) ? full mode only ?)
"""
ZSTD_CCtx_getParameter: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                   _enum_zstd.ZSTD_cParameter,  # param
                                   _Pointer[_type.c_int]],  # value
                                  _type.c_size_t]
"""
ZSTD_CCtx_getParameter() : Get the requested compression parameter value,
selected by enum ZSTD_cParameter, and store it into int* value.
"""
ZSTD_createCCtxParams: _Callable[[],
                                 _Pointer[_struct.ZSTD_CCtx_params]]
"""
ZSTD_CCtx_params : Quick howto : - ZSTD_createCCtxParams() : Create a
ZSTD_CCtx_params structure - ZSTD_CCtxParams_setParameter() : Push parameters
one by one into an existing ZSTD_CCtx_params structure. This is similar to
ZSTD_CCtx_setParameter(). - ZSTD_CCtx_setParametersUsingCCtxParams() : Apply
parameters to an existing CCtx. These parameters will be applied to all
subsequent frames. - ZSTD_compressStream2() : Do compression using the CCtx. -
ZSTD_freeCCtxParams() : Free the memory, accept NULL pointer.
"""
ZSTD_freeCCtxParams: _Callable[[_Pointer[_struct.ZSTD_CCtx_params]],  # params
                               _type.c_size_t]
ZSTD_CCtxParams_reset: _Callable[[_Pointer[_struct.ZSTD_CCtx_params]],  # params
                                 _type.c_size_t]
"""
ZSTD_CCtxParams_reset() : Reset params to default values.
"""
ZSTD_CCtxParams_init: _Callable[[_Pointer[_struct.ZSTD_CCtx_params],  # cctxParams
                                 _type.c_int],  # compressionLevel
                                _type.c_size_t]
"""
ZSTD_CCtxParams_init() : Initializes the compression parameters of cctxParams
according to compression level. All other parameters are reset to their default
values.
"""
ZSTD_CCtxParams_init_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx_params],  # cctxParams
                                          _struct.ZSTD_parameters],  # params
                                         _type.c_size_t]
"""
ZSTD_CCtxParams_init_advanced() : Initializes the compression and frame
parameters of cctxParams according to params. All other parameters are reset to
their default values.
"""
ZSTD_CCtxParams_setParameter: _Callable[[_Pointer[_struct.ZSTD_CCtx_params],  # params
                                         _enum_zstd.ZSTD_cParameter,  # param
                                         _type.c_int],  # value
                                        _type.c_size_t]
"""
ZSTD_CCtxParams_setParameter() : Requires v1.4.0+ Similar to
ZSTD_CCtx_setParameter. Set one compression parameter, selected by enum
ZSTD_cParameter. Parameters must be applied to a ZSTD_CCtx using
ZSTD_CCtx_setParametersUsingCCtxParams().
"""
ZSTD_CCtxParams_getParameter: _Callable[[_Pointer[_struct.ZSTD_CCtx_params],  # params
                                         _enum_zstd.ZSTD_cParameter,  # param
                                         _Pointer[_type.c_int]],  # value
                                        _type.c_size_t]
"""
ZSTD_CCtxParams_getParameter() : Similar to ZSTD_CCtx_getParameter. Get the
requested value of one compression parameter, selected by enum ZSTD_cParameter.
"""
ZSTD_CCtx_setParametersUsingCCtxParams: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                                   _Pointer[_struct.ZSTD_CCtx_params]],  # params
                                                  _type.c_size_t]
"""
ZSTD_CCtx_setParametersUsingCCtxParams() : Apply a set of ZSTD_CCtx_params to
the compression context. This can be done even after compression is started, if
nbWorkers==0, this will have no impact until a new compression is started. if
nbWorkers>=1, new parameters will be picked up at next job, with a few
restrictions (windowLog, pledgedSrcSize, nbWorkers, jobSize, and overlapLog are
not updated).
"""
ZSTD_compressStream2_simpleArgs: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                            _type.c_void_p,  # dst
                                            _type.c_size_t,  # dstCapacity
                                            _Pointer[_type.c_size_t],  # dstPos
                                            _type.c_void_p,  # src
                                            _type.c_size_t,  # srcSize
                                            _Pointer[_type.c_size_t],  # srcPos
                                            _enum_zstd.ZSTD_EndDirective],  # endOp
                                           _type.c_size_t]
"""
ZSTD_compressStream2_simpleArgs() : Same as ZSTD_compressStream2(), but using
only integral types as arguments. This variant might be helpful for binders from
dynamic languages which have troubles handling structures containing memory
pointers.
"""
ZSTD_isFrame: _Callable[[_type.c_void_p,  # buffer
                         _type.c_size_t],  # size
                        _type.c_uint]
"""
ZSTD_isFrame() : Tells if the content of `buffer` starts with a valid Frame
Identifier. Note : Frame Identifier is 4 bytes. If `size < 4`,
"""
ZSTD_createDDict_byReference: _Callable[[_type.c_void_p,  # dictBuffer
                                         _type.c_size_t],  # dictSize
                                        _Pointer[_struct.ZSTD_DDict]]
"""
ZSTD_createDDict_byReference() : Create a digested dictionary, ready to start
decompression operation without startup delay. Dictionary content is referenced,
and therefore stays in dictBuffer. It is important that dictBuffer outlives
DDict, it must remain read accessible throughout the lifetime of DDict
"""
ZSTD_DCtx_loadDictionary_byReference: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                                 _type.c_void_p,  # dict
                                                 _type.c_size_t],  # dictSize
                                                _type.c_size_t]
"""
ZSTD_DCtx_loadDictionary_byReference() : Same as ZSTD_DCtx_loadDictionary(), but
references `dict` content instead of copying it into `dctx`. This saves memory
if `dict` remains around., However, it's imperative that `dict` remains
accessible (and unmodified) while being used, so it must outlive decompression.
"""
ZSTD_DCtx_loadDictionary_advanced: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                              _type.c_void_p,  # dict
                                              _type.c_size_t,  # dictSize
                                              _enum_zstd.ZSTD_dictLoadMethod_e,  # dictLoadMethod
                                              _enum_zstd.ZSTD_dictContentType_e],  # dictContentType
                                             _type.c_size_t]
"""
ZSTD_DCtx_loadDictionary_advanced() : Same as ZSTD_DCtx_loadDictionary(), but
gives direct control over how to load the dictionary (by copy ? by reference ?)
and how to interpret it (automatic ? force raw mode ? full mode only ?).
"""
ZSTD_DCtx_refPrefix_advanced: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                         _type.c_void_p,  # prefix
                                         _type.c_size_t,  # prefixSize
                                         _enum_zstd.ZSTD_dictContentType_e],  # dictContentType
                                        _type.c_size_t]
"""
ZSTD_DCtx_refPrefix_advanced() : Same as ZSTD_DCtx_refPrefix(), but gives finer
control over how to interpret prefix content (automatic ? force raw mode
(default) ? full mode only ?)
"""
ZSTD_DCtx_setMaxWindowSize: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                       _type.c_size_t],  # maxWindowSize
                                      _type.c_size_t]
"""
ZSTD_DCtx_setMaxWindowSize() : Refuses allocating internal buffers for frames
requiring a window size larger than provided limit. This protects a decoder
context from reserving too much memory for itself (potential attack scenario).
This parameter is only useful in streaming mode, since no internal buffer is
allocated in single-pass mode. By default, a decompression context accepts all
window sizes <= (1 << ZSTD_WINDOWLOG_LIMIT_DEFAULT)
"""
ZSTD_DCtx_getParameter: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                   _enum_zstd.ZSTD_dParameter,  # param
                                   _Pointer[_type.c_int]],  # value
                                  _type.c_size_t]
"""
ZSTD_DCtx_getParameter() : Get the requested decompression parameter value,
selected by enum ZSTD_dParameter, and store it into int* value.
"""
ZSTD_DCtx_setFormat: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                _enum_zstd.ZSTD_format_e],  # format
                               _type.c_size_t]
"""
ZSTD_DCtx_setFormat() : This function is REDUNDANT. Prefer
ZSTD_DCtx_setParameter(). Instruct the decoder context about what kind of data
to decode next. This instruction is mandatory to decode data without a fully-
formed header, such ZSTD_f_zstd1_magicless for example.
"""
ZSTD_decompressStream_simpleArgs: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                             _type.c_void_p,  # dst
                                             _type.c_size_t,  # dstCapacity
                                             _Pointer[_type.c_size_t],  # dstPos
                                             _type.c_void_p,  # src
                                             _type.c_size_t,  # srcSize
                                             _Pointer[_type.c_size_t]],  # srcPos
                                            _type.c_size_t]
"""
ZSTD_decompressStream_simpleArgs() : Same as ZSTD_decompressStream(), but using
only integral types as arguments. This can be helpful for binders from dynamic
languages which have troubles handling structures containing memory pointers.
"""
ZSTD_initCStream_srcSize: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                     _type.c_int,  # compressionLevel
                                     _type.c_ulonglong],  # pledgedSrcSize
                                    _type.c_size_t]
"""
ZSTD_initCStream_srcSize() : This function is DEPRECATED, and equivalent to:
ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only); ZSTD_CCtx_refCDict(zcs, NULL); //
clear the dictionary (if any) ZSTD_CCtx_setParameter(zcs,
ZSTD_c_compressionLevel, compressionLevel); ZSTD_CCtx_setPledgedSrcSize(zcs,
pledgedSrcSize);
"""
ZSTD_initCStream_usingDict: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                       _type.c_void_p,  # dict
                                       _type.c_size_t,  # dictSize
                                       _type.c_int],  # compressionLevel
                                      _type.c_size_t]
"""
ZSTD_initCStream_usingDict() : This function is DEPRECATED, and is equivalent
to: ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only); ZSTD_CCtx_setParameter(zcs,
ZSTD_c_compressionLevel, compressionLevel); ZSTD_CCtx_loadDictionary(zcs, dict,
dictSize);
"""
ZSTD_initCStream_advanced: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                      _type.c_void_p,  # dict
                                      _type.c_size_t,  # dictSize
                                      _struct.ZSTD_parameters,  # params
                                      _type.c_ulonglong],  # pledgedSrcSize
                                     _type.c_size_t]
"""
ZSTD_initCStream_advanced() : This function is DEPRECATED, and is equivalent to:
ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only); ZSTD_CCtx_setParams(zcs, params);
ZSTD_CCtx_setPledgedSrcSize(zcs, pledgedSrcSize); ZSTD_CCtx_loadDictionary(zcs,
dict, dictSize);
"""
ZSTD_initCStream_usingCDict: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                        _Pointer[_struct.ZSTD_CDict]],  # cdict
                                       _type.c_size_t]
"""
ZSTD_initCStream_usingCDict() : This function is DEPRECATED, and equivalent to:
ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only); ZSTD_CCtx_refCDict(zcs, cdict);
"""
ZSTD_initCStream_usingCDict_advanced: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                                                 _Pointer[_struct.ZSTD_CDict],  # cdict
                                                 _struct.ZSTD_frameParameters,  # fParams
                                                 _type.c_ulonglong],  # pledgedSrcSize
                                                _type.c_size_t]
"""
ZSTD_initCStream_usingCDict_advanced() : This function is DEPRECATED, and is
equivalent to: ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only);
ZSTD_CCtx_setFParams(zcs, fParams); ZSTD_CCtx_setPledgedSrcSize(zcs,
pledgedSrcSize); ZSTD_CCtx_refCDict(zcs, cdict);
"""
ZSTD_resetCStream: _Callable[[_Pointer[_struct.ZSTD_CStream],  # zcs
                              _type.c_ulonglong],  # pledgedSrcSize
                             _type.c_size_t]
"""
ZSTD_resetCStream() : This function is DEPRECATED, and is equivalent to:
ZSTD_CCtx_reset(zcs, ZSTD_reset_session_only); ZSTD_CCtx_setPledgedSrcSize(zcs,
pledgedSrcSize); Note: ZSTD_resetCStream() interprets pledgedSrcSize == 0 as
ZSTD_CONTENTSIZE_UNKNOWN, but ZSTD_CCtx_setPledgedSrcSize() does not do the
same, so ZSTD_CONTENTSIZE_UNKNOWN must be explicitly specified.
"""
ZSTD_getFrameProgression: _Callable[[_Pointer[_struct.ZSTD_CCtx]],  # cctx
                                    _struct.ZSTD_frameProgression]
"""
ZSTD_getFrameProgression() : tells how much data has been ingested (read from
input) consumed (input actually compressed) and produced (output) for current
frame. Note : (ingested - consumed) is amount of input data buffered internally,
not yet compressed. Aggregates progression inside active worker threads.
"""
ZSTD_toFlushNow: _Callable[[_Pointer[_struct.ZSTD_CCtx]],  # cctx
                           _type.c_size_t]
"""
ZSTD_toFlushNow() : Tell how many bytes are ready to be flushed immediately.
Useful for multithreading scenarios (nbWorkers >= 1). Probe the oldest active
job, defined as oldest job not yet entirely flushed, and check its output
buffer.
"""
ZSTD_initDStream_usingDict: _Callable[[_Pointer[_struct.ZSTD_DStream],  # zds
                                       _type.c_void_p,  # dict
                                       _type.c_size_t],  # dictSize
                                      _type.c_size_t]
"""
This function is deprecated, and is equivalent to:
"""
ZSTD_initDStream_usingDDict: _Callable[[_Pointer[_struct.ZSTD_DStream],  # zds
                                        _Pointer[_struct.ZSTD_DDict]],  # ddict
                                       _type.c_size_t]
"""
This function is deprecated, and is equivalent to:
"""
ZSTD_resetDStream: _Callable[[_Pointer[_struct.ZSTD_DStream]],  # zds
                             _type.c_size_t]
"""
This function is deprecated, and is equivalent to:
"""
ZSTD_registerSequenceProducer: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                          _type.c_void_p,  # sequenceProducerState
                                          _type.ZSTD_sequenceProducer_F],  # sequenceProducer
                                         _type.c_void]
"""
ZSTD_registerSequenceProducer() : Instruct zstd to use a block-level external
sequence producer function.
"""
ZSTD_compressBegin: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                               _type.c_int],  # compressionLevel
                              _type.c_size_t]
"""
===== Buffer-less streaming compression functions =====
"""
ZSTD_compressBegin_usingDict: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                         _type.c_void_p,  # dict
                                         _type.c_size_t,  # dictSize
                                         _type.c_int],  # compressionLevel
                                        _type.c_size_t]
ZSTD_compressBegin_usingCDict: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                          _Pointer[_struct.ZSTD_CDict]],  # cdict
                                         _type.c_size_t]
ZSTD_copyCCtx: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                          _Pointer[_struct.ZSTD_CCtx],  # preparedCCtx
                          _type.c_ulonglong],  # pledgedSrcSize
                         _type.c_size_t]
ZSTD_compressContinue: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                  _type.c_void_p,  # dst
                                  _type.c_size_t,  # dstCapacity
                                  _type.c_void_p,  # src
                                  _type.c_size_t],  # srcSize
                                 _type.c_size_t]
ZSTD_compressEnd: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                             _type.c_void_p,  # dst
                             _type.c_size_t,  # dstCapacity
                             _type.c_void_p,  # src
                             _type.c_size_t],  # srcSize
                            _type.c_size_t]
ZSTD_compressBegin_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                        _type.c_void_p,  # dict
                                        _type.c_size_t,  # dictSize
                                        _struct.ZSTD_parameters,  # params
                                        _type.c_ulonglong],  # pledgedSrcSize
                                       _type.c_size_t]
"""
The ZSTD_compressBegin_advanced() and ZSTD_compressBegin_usingCDict_advanced()
are now DEPRECATED and will generate a compiler warning
"""
ZSTD_compressBegin_usingCDict_advanced: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                                                   _Pointer[_struct.ZSTD_CDict],  # cdict
                                                   _struct.ZSTD_frameParameters,  # fParams
                                                   _type.c_ulonglong],  # pledgedSrcSize
                                                  _type.c_size_t]
ZSTD_decodingBufferSize_min: _Callable[[_type.c_ulonglong,  # windowSize
                                        _type.c_ulonglong],  # frameContentSize
                                       _type.c_size_t]
"""
===== Buffer-less streaming decompression functions =====
"""
ZSTD_decompressBegin: _Callable[[_Pointer[_struct.ZSTD_DCtx]],  # dctx
                                _type.c_size_t]
ZSTD_decompressBegin_usingDict: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                           _type.c_void_p,  # dict
                                           _type.c_size_t],  # dictSize
                                          _type.c_size_t]
ZSTD_decompressBegin_usingDDict: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                            _Pointer[_struct.ZSTD_DDict]],  # ddict
                                           _type.c_size_t]
ZSTD_nextSrcSizeToDecompress: _Callable[[_Pointer[_struct.ZSTD_DCtx]],  # dctx
                                        _type.c_size_t]
ZSTD_decompressContinue: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                    _type.c_void_p,  # dst
                                    _type.c_size_t,  # dstCapacity
                                    _type.c_void_p,  # src
                                    _type.c_size_t],  # srcSize
                                   _type.c_size_t]
ZSTD_copyDCtx: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                          _Pointer[_struct.ZSTD_DCtx]],  # preparedDCtx
                         _type.c_void]
"""
misc
"""
ZSTD_nextInputType: _Callable[[_Pointer[_struct.ZSTD_DCtx]],  # dctx
                              _enum_zstd.ZSTD_nextInputType_e]
ZSTD_getBlockSize: _Callable[[_Pointer[_struct.ZSTD_CCtx]],  # cctx
                             _type.c_size_t]
"""
===== Raw zstd block functions =====
"""
ZSTD_compressBlock: _Callable[[_Pointer[_struct.ZSTD_CCtx],  # cctx
                               _type.c_void_p,  # dst
                               _type.c_size_t,  # dstCapacity
                               _type.c_void_p,  # src
                               _type.c_size_t],  # srcSize
                              _type.c_size_t]
ZSTD_decompressBlock: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                                 _type.c_void_p,  # dst
                                 _type.c_size_t,  # dstCapacity
                                 _type.c_void_p,  # src
                                 _type.c_size_t],  # srcSize
                                _type.c_size_t]
ZSTD_insertBlock: _Callable[[_Pointer[_struct.ZSTD_DCtx],  # dctx
                             _type.c_void_p,  # blockStart
                             _type.c_size_t],  # blockSize
                            _type.c_size_t]

_WinLib(__name__)
