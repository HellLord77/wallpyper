__version__ = '0.0.2'

import enum
import urllib.parse

_URL_TEMPLATE = (
    'https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:{}',
    'https://www.google.com/searchbyimage?image_url={}',
    'https://iqdb.org?url={}',
    'https://www.repostsleuth.com/search?url={}',
    'https://saucenao.com/search.php?url={}',
    'https://pic.sogou.com/ris?query={}',
    'https://tineye.com/search?url={}',
    'https://trace.moe?url={}',
    'https://yandex.com/images/search?rpt=imageview&url={}')


class Engine(enum.Enum):
    BING = 0
    GOOGLE = 1
    IQDB = 2
    REPOSTSLEUTH = 3
    SAUCENAO = 4
    SOGOU = 5
    TINEYE = 6
    TRACE = 7
    YANDEX = 8


def get(engine: int | str | Engine, url: str) -> str:
    if isinstance(engine, str):
        engine = getattr(Engine, engine.upper())
    if isinstance(engine, Engine):
        engine = engine.value
    return _URL_TEMPLATE[engine].format(urllib.parse.quote_plus(url))
