from .. import MoebooruSource


class MyImoutoSource(MoebooruSource, source=False):
    NAME = 'MyImouto'


from . import (
    lolibooru)  # NOQA: E402
