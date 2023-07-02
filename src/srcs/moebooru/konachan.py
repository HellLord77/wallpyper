from . import MoebooruSource


class Konachan(MoebooruSource):  # https://konachan.com/help/api
    NAME = 'Konachan.com'
    VERSION = '0.0.1'
    URL = 'https://konachan.com'

    @classmethod
    def _format_name(cls, name: str) -> str:
        return super()._format_name(name).removeprefix(' -')
