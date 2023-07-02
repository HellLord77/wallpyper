import __feature__

if __feature__.BROTLI:
    from libs import request
    from plat import brotli


    class BrotliDecoder(request.Decoder):
        _encoding_ = 'br'

        def __init__(self):
            self._decoder = brotli.Decompressor()

        def flush(self) -> bytes:
            return self._decoder.unused_data

        def decode(self, data: bytes) -> bytes:
            return self._decoder.decompress(data)
