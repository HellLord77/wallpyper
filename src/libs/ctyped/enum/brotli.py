from . import _Enum


# decode
class BrotliDecoderResult(_Enum):
    """
    Result type for ::BrotliDecoderDecompress and ::BrotliDecoderDecompressStream
    functions.
    """
    ERROR = 0
    """
    Decoding error, e.g. corrupted input or memory allocation problem.
    """
    SUCCESS = 1
    """
    Decoding successfully completed.
    """
    NEEDS_MORE_INPUT = 2
    """
    Partially done; should be called again with more input.
    """
    NEEDS_MORE_OUTPUT = 3
    """
    Partially done; should be called again with more output.
    """


class BrotliDecoderErrorCode(_Enum):
    """
    Error code for detailed logging / production debugging.
    """
    NO_ERROR = 0
    SUCCESS = 1
    NEEDS_MORE_INPUT = 2
    NEEDS_MORE_OUTPUT = 3
    ERROR_FORMAT_EXUBERANT_NIBBLE = -1
    ERROR_FORMAT_RESERVED = -2
    ERROR_FORMAT_EXUBERANT_META_NIBBLE = -3
    ERROR_FORMAT_SIMPLE_HUFFMAN_ALPHABET = -4
    ERROR_FORMAT_SIMPLE_HUFFMAN_SAME = -5
    ERROR_FORMAT_CL_SPACE = -6
    ERROR_FORMAT_HUFFMAN_SPACE = -7
    ERROR_FORMAT_CONTEXT_MAP_REPEAT = -8
    ERROR_FORMAT_BLOCK_LENGTH_1 = -9
    ERROR_FORMAT_BLOCK_LENGTH_2 = -10
    ERROR_FORMAT_TRANSFORM = -11
    ERROR_FORMAT_DICTIONARY = -12
    ERROR_FORMAT_WINDOW_BITS = -13
    ERROR_FORMAT_PADDING_1 = -14
    ERROR_FORMAT_PADDING_2 = -15
    ERROR_FORMAT_DISTANCE = -16
    ERROR_DICTIONARY_NOT_SET = -19
    ERROR_INVALID_ARGUMENTS = -20
    ERROR_ALLOC_CONTEXT_MODES = -21
    ERROR_ALLOC_TREE_GROUPS = -22
    ERROR_ALLOC_CONTEXT_MAP = -25
    ERROR_ALLOC_RING_BUFFER_1 = -26
    ERROR_ALLOC_RING_BUFFER_2 = -27
    ERROR_ALLOC_BLOCK_TYPE_TREES = -30
    ERROR_UNREACHABLE = -31


class BrotliDecoderParameter(_Enum):
    """
    Options to be used with ::BrotliDecoderSetParameter.
    """
    DISABLE_RING_BUFFER_REALLOCATION = 0
    """
    Disable "canny" ring buffer allocation strategy.
    """
    LARGE_WINDOW = 1
    """
    Flag that determines if "Large Window Brotli" is used.
    """


# encode
class BrotliEncoderMode(_Enum):
    """
    Options for ::MODE parameter.
    """
    GENERIC = 0
    """
    Default compression mode.
    """
    TEXT = 1
    """
    Compression mode for UTF-8 formatted text input.
    """
    FONT = 2
    """
    Compression mode used in WOFF 2.0.
    """


class BrotliEncoderOperation(_Enum):
    """
    Operations that can be performed by streaming encoder.
    """
    PROCESS = 0
    """
    Process input.
    """
    FLUSH = 1
    """
    Produce output for all processed input.
    """
    FINISH = 2
    """
    Finalize the stream.
    """
    EMIT_METADATA = 3
    """
    Emit metadata block to stream.
    """


class BrotliEncoderParameter(_Enum):
    """
    Options to be used with ::BrotliEncoderSetParameter.
    """
    MODE = 0
    """
    Tune encoder for specific input.
    """
    QUALITY = 1
    """
    The main compression speed-density lever.
    """
    LGWIN = 2
    """
    Recommended sliding LZ77 window size.
    """
    LGBLOCK = 3
    """
    Recommended input block size.
    """
    DISABLE_LITERAL_CONTEXT_MODELING = 4
    """
    Flag that affects usage of "literal context modeling" format feature.
    """
    SIZE_HINT = 5
    """
    Estimated total input size for all ::BrotliEncoderCompressStream calls.
    """
    LARGE_WINDOW = 6
    """
    Flag that determines if "Large Window Brotli" is used.
    """
    NPOSTFIX = 7
    """
    Recommended number of postfix bits (NPOSTFIX).
    """
    NDIRECT = 8
    """
    Recommended number of direct distance codes (NDIRECT).
    """
    STREAM_OFFSET = 9
    """
    Number of bytes of input stream already processed by a different instance.
    """


# shared_dictionary
class BrotliSharedDictionaryType(_Enum):
    """
    Input data type for ::BrotliSharedDictionaryAttach.
    """
    RAW = 0
    """
    Raw LZ77 prefix dictionary.
    """
    SERIALIZED = 1
    """
    Serialized shared dictionary.
    """
