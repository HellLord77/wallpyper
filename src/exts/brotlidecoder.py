import features

if features.BROTLI_DECODE:
    from libs import request
    from win32 import brotli


    class BrotliDecoder(request.Decoder):
        _encoding_ = 'br'

        def __init__(self):
            self._decoder = brotli.Decompressor()

        def flush(self) -> bytes:
            return self._decoder.unused_data

        def decompress(self, data: bytes) -> bytes:
            return self._decoder.decompress(data)
