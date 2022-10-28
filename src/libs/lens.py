__version__ = '0.0.1'

import enum
import urllib.parse


class Engine(enum.Enum):
    BING = 'https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:{}'
    GOOGLE = 'https://www.google.com/searchbyimage?image_url={}'
    IQDB = 'https://iqdb.org?url={}'
    REPOSTSLEUTH = 'https://www.repostsleuth.com/search?url={}'
    SAUCENAO = 'https://saucenao.com/search.php?url={}'
    SOGOU = 'https://pic.sogou.com/ris?query={}'
    TINEYE = 'https://tineye.com/search?url={}'
    TRACE = 'https://trace.moe?url={}'
    YANDEX = 'https://yandex.com/images/search?rpt=imageview&url={}'


def get(engine: str | Engine, url: str) -> str:
    if isinstance(engine, str):
        engine = getattr(Engine, engine)
    return engine.value.format(urllib.parse.quote_plus(url))
