from typing import Iterator, Optional, TypedDict

from libs import request
from . import File, Source

URL_BASE = request.join_url('https://api.shutterstock.com', 'v2')
URL_IMAGES = request.join_url(URL_BASE, 'images')
URL_IMAGES_SEARCH = request.join_url(URL_IMAGES, 'search')
URL_USER = request.join_url(URL_BASE, 'user')

CONFIG_KEY = 'key'
CONFIG_SECRET = 'secret'
CONFIG_TYPE = 'image_type'
CONFIG_ORIENTATION = 'orientation'
CONFIG_COLOR = 'color'
CONFIG_PEOPLE = 'people_model_released'
CONFIG_AGE = 'people_age'
CONFIG_GENDER = 'people_gender'
CONFIG_NUMBER = 'people_number'
CONFIG_LICENSE = 'license'
CONFIG_SAFE = 'safe'
CONFIG_SORT = 'sort'

TYPES = 'photo', 'illustration', 'vector'
ORIENTATIONS = '', 'horizontal', 'vertical'
COLORS = (
    '', 'bw', 'E72525', 'F48700', 'ECA71D', 'F1F129', 'A9E418', '06D506',
    '0ECB9B', '1AE0E0', '0BBBF5', '1F55F8', '0000FF', '7F00FF', 'BF00FF', 'EA06B1')
PEOPLE = '', 'true', 'false'
AGES = '', 'infants', 'children', 'teenagers', '20s', '30s', '40s', '50s', '60s', 'older'
GENDERS = 'male', 'female', 'both'
NUMBERS = '', '1', '2', '3', '4'
LICENCES = 'commercial', 'editorial', 'enhanced'
SAVES = 'true', 'false'
SORTS = 'popular', 'newest', 'relevance', 'random'


def _authenticate(key: str, secret: str) -> bool:
    return bool(request.get(URL_IMAGES_SEARCH, {'per_page': '1'}, auth=(key, secret)))


class ShutterStock(Source):  # https://api-reference.shutterstock.com
    NAME = '# shutterstock'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_KEY: str,
        CONFIG_SECRET: str,
        'query': str,
        CONFIG_TYPE: tuple[str, str, str],
        CONFIG_ORIENTATION: str,
        CONFIG_COLOR: str,
        CONFIG_PEOPLE: str,
        CONFIG_AGE: str,
        CONFIG_NUMBER: str,
        CONFIG_LICENSE: tuple[str, str, str],
        CONFIG_SAFE: str,
        CONFIG_SORT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_KEY: '',
        CONFIG_SECRET: '',
        'query': '',
        CONFIG_TYPE: TYPES,
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_COLOR: COLORS[0],
        CONFIG_PEOPLE: PEOPLE[0],
        CONFIG_AGE: AGES[0],
        CONFIG_NUMBER: NUMBERS[0],
        CONFIG_LICENSE: LICENCES,
        CONFIG_SAFE: SAVES[0],
        CONFIG_SORT: SORTS[0]}

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        datas: Optional[list] = None
        auth = params.pop(CONFIG_KEY), params.pop(CONFIG_SECRET)
        params['spellcheck_query'] = 'false'
        params['page'] = '1'
        params['per_page'] = '500'
        while True:
            if not datas:
                response = request.get(URL_IMAGES_SEARCH, params, auth=auth)
                if response:
                    datas = response.json()['data']
            yield
