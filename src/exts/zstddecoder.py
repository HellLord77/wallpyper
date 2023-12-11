import features

if features.ZSTD_DECODE:
    from libs import request
    from win32 import zstd


    class ZstdDecoder(request.Decoder):
        _encoding_ = 'zstd'

        def __init__(self):
            self._decoder = zstd.Decompressor()

        def flush(self) -> bytes:
            return self._decoder.unused_data

        def decompress(self, data: bytes) -> bytes:
            return self._decoder.decompress(data)
