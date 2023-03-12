__version__ = '0.0.3'

import enum
import urllib.parse
import webbrowser


class Engine(enum.StrEnum):
    ALAMY = 'https://www.alamy.com/search.html?imageurl={}'
    BING = 'https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:{}'
    GOOGLE = 'https://www.google.com/searchbyimage?sbisrc=1&image_url={}'
    GOOGLELENS = 'https://lens.google.com/uploadbyurl?url={}'
    IQDB = 'https://iqdb.org?url={}'
    REPOSTSLEUTH = 'https://www.repostsleuth.com/search?url={}'
    SAUCENAO = 'https://saucenao.com/search.php?url={}'
    SOGOU = 'https://pic.sogou.com/ris?query={}'
    TINEYE = 'https://tineye.com/search?url={}'
    TRACE = 'https://trace.moe?url={}'
    YANDEX = 'https://yandex.com/images/search?rpt=imageview&url={}'

    def format(self, url: str) -> str:
        return self.value.format(urllib.parse.quote_plus(url))

    def open(self, url: str) -> bool:
        return webbrowser.open(self.format(url))
