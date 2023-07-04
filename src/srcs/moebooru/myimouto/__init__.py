from .. import MoebooruSource


class MyImoutoSource(MoebooruSource, source=False):
    pass


from . import (
    lolibooru)  # NOQA: E402
