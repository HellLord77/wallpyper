import enum
import re
import urllib.parse
from typing import Optional

from . import _TParams
from . import get as _get
from . import get_params as _get_params
from . import join_url as _join_url
from . import post as _post

_URL_BASE = _join_url('https://www.google.com', 'recaptcha')
_RE_TOKEN = re.compile(r'"recaptcha-token" value="(.*?)"')
_RE_RESPONSE = re.compile(r'"rresp","(.*?)"')


class Endpoint(enum.StrEnum):
    API2 = 'api2'
    ENTERPRISE = 'enterprise'


def default_data() -> dict[str, str]:
    return {
        'v':      '',
        'reason': 'q',
        'c':      '',
        'k':      '',
        'co':     '',
        'hl':     'en',
        'size':   'invisible',
        'chr':    '[89,64,27]',
        'vh':     '13599012192',
        'bg':     '!q62grYxHRvVxjUIjSFNd0mlvrZ-iCgIHAAAB6FcAAAANnAkBySdqTJGFRK7SirleWAwPVhv9-XwP8ugGSTJJgQ46-0IMBKN8HUnfPqm'
                  '4sCefwxOOEURND35prc9DJYG0pbmg_jD18qC0c-lQzuPsOtUhHTtfv3--SVCcRvJWZ0V3cia65HGfUys0e1K-IZoArlxM9qZfUMXJKAF'
                  'uWqZiBn-Qi8VnDqI2rRnAQcIB8Wra6xWzmFbRR2NZqF7lDPKZ0_SZBEc99_49j07ISW4X65sMHL139EARIOipdsj5js5JyM19a2TCZJt'
                  'Au4XL1h0ZLfomM8KDHkcl_b0L-jW9cvAe2K2uQXKRPzruAvtjdhMdODzVWU5VawKhpmi2NCKAiCRUlJW5lToYkR_X-07AqFLY6qi4ZbJ'
                  '_sSrD7fCNNYFKmLfAaxPwPmp5Dgei7KKvEQmeUEZwTQAS1p2gaBmt6SCOgId3QBfF_robIkJMcXFzj7R0G-s8rwGUSc8EQzT_DCe9SZs'
                  'Jyobu3Ps0-YK-W3MPWk6a69o618zPSIIQtSCor9w_oUYTLiptaBAEY03NWINhc1mmiYu2Yz5apkW_KbAp3HD3G0bhzcCIYZOGZxyJ44H'
                  'dGsCJ-7ZFTcEAUST-aLbS-YN1AyuC7ClFO86CMICVDg6aIDyCJyIcaJXiN-bN5xQD_NixaXatJy9Mx1XEnU4Q7E_KISDJfKUhDktK5LM'
                  'qBJa-x1EIOcY99E-eyry7crf3-Hax3Uj-e-euzRwLxn2VB1Uki8nqJQVYUgcjlVXQhj1X7tx4jzUb0yB1TPU9uMBtZLRvMCRKvFdnn77'
                  'HgYs5bwOo2mRECiFButgigKXaaJup6NM4KRUevhaDtnD6aJ8ZWQZTXz_OJ74a_OvPK9eD1_5pTG2tUyYNSyz-alhvHdMt5_MAdI3op4Z'
                  'mcvBQBV9VC2JLjphDuTW8eW_nuK9hN17zin6vjEL8YIm_MekB_dIUK3T1Nbyqmyzigy-Lg8tRL6jSinzdwOTc9hS5SCsPjMeiblc65aJ'
                  'C8AKmA5i80f-6Eg4BT305UeXKI3QwhI3ZJyyQAJTata41FoOXl3EF9Pyy8diYFK2G-CS8lxEpV7jcRYduz4tEPeCpBxU4O_KtM2iv4ST'
                  'kwO4Z_-c-fMLlYu9H7jiFnk6Yh8XlPE__3q0FHIBFf15zVSZ3qroshYiHBMxM5BVQBOExbjoEdYKx4-m9c23K3suA2sCkxHytptG-6yh'
                  'HJR3EyWwSRTY7OpX_yvhbFri0vgchw7U6ujyoXeCXS9N4oOoGYpS5OyFyRPLxJH7yjXOG2Play5HJ91LL6J6qg1iY8MIq9XQtiVZHadV'
                  'pZVlz3iKcX4vXcQ3rv_qQwhntObGXPAGJWEel5OiJ1App7mWy961q3mPg9aDEp9VLKU5yDDw1xf6tOFMwg2Q-PNDaKXAyP_FOkxOjnu8'
                  'dPhuKGut6cJr449BKDwbnA9BOomcVSztEzHGU6HPXXyNdZbfA6D12f5lWxX2B_pobw3a1gFLnO6mWaNRuK1zfzZcfGTYMATf6d7sj9Rc'
                  'KNS230XPHWGaMlLmNxsgXkEN7a9PwsSVwcKdHg_HU4vYdRX6vkEauOIwVPs4dS7yZXmtvbDaX1zOU4ZYWg0T42sT3nIIl9M2EeFS5Rqm'
                  's_YzNp8J-YtRz1h5RhtTTNcA5jX4N-xDEVx-vD36bZVzfoMSL2k85PKv7pQGLH-0a3DsR0pePCTBWNORK0g_RZCU_H898-nT1syGzNKW'
                  'GoPCstWPRvpL9cnHRPM1ZKemRn0nPVm9Bgo0ksuUijgXc5yyrf5K49UU2J5JgFYpSp7aMGOUb1ibrj2sr-D63d61DtzFJ2mwrLm_KHBi'
                  'N_ECpVhDsRvHe5iOx_APHtImevOUxghtkj-8RJruPgkTVaML2MEDOdL_UYaldeo-5ckZo3VHss7IpLArGOMTEd0bSH8tA8CL8RLQQeSo'
                  'kOMZ79Haxj8yE0EAVZ-k9-O72mmu5I0wH5IPgapNvExeX6O1l3mC4MqLhKPdOZOnTiEBlSrV4ZDH_9fhLUahe5ocZXvXqrud9QGNeTpZ'
                  'sSPeIYubeOC0sOsuqk10sWB7NP-lhifWeDob-IK1JWcgFTytVc99RkZTjUcdG9t8prPlKAagZIsDr1TiX3dy8sXKZ7d9EXQF5P_rHJ8x'
                  'vmUtCWqbc3V5jL-qe8ANypwHsuva75Q6dtqoBR8vCE5xWgfwB0GzR3Xi_l7KDTsYAQIrDZVyY1UxdzWBwJCrvDrtrNsnt0S7BhBJ4ATC'
                  'rW5VFPqXyXRiLxHCIv9zgo-NdBZQ4hEXXxMtbem3KgYUB1Rals1bbi8X8MsmselnHfY5LdOseyXWIR2QcrANSAypQUAhwVpsModw7HMd'
                  'XgV9Uc-HwCMWafOChhBr88tOowqVHttPtwYorYrzriXNRt9LkigESMy1bEDx79CJguitwjQ9IyIEu8quEQb_-7AEXrfDzl_FKgASnnZL'
                  'rAfZMtgyyddIhBpgAvgR_c8a8Nuro-RGV0aNuunVg8NjL8binz9kgmZvOS38QaP5anf2vgzJ9wC0ZKDg2Ad77dPjBCiCRtVe_dqm7FDA'
                  '_cS97DkAwVfFawgce1wfWqsrjZvu4k6x3PAUH1UNzQUxVgOGUbqJsaFs3GZIMiI8O6-tZktz8i8oqpr0RjkfUhw_I2szHF3LM20_bFwh'
                  'tINwg0rZxRTrg4il-_q7jDnVOTqQ7fdgHgiJHZw_OOB7JWoRW6ZlJmx3La8oV93fl1wMGNrpojSR0b6pc8SThsKCUgoY6zajWWa3CesX'
                  '1ZLUtE7Pfk9eDey3stIWf2acKolZ9fU-gspeACUCN20EhGT-HvBtNBGr_xWk1zVJBgNG29olXCpF26eXNKNCCovsILNDgH06vulDUG_v'
                  'R5RrGe5LsXksIoTMYsCUitLz4HEehUOd9mWCmLCl00eGRCkwr9EB557lyr7mBK2KPgJkXhNmmPSbDy6hPaQ057zfAd5s_43UBCMtI-aA'
                  's5NN4TXHd6IlLwynwc1zsYOQ6z_HARlcMpCV9ac-8eOKsaepgjOAX4YHfg3NekrxA2ynrvwk9U-gCtpxMJ4f1cVx3jExNlIX5LxE46FYIhQ'}


def get_endpoint(url: str) -> Endpoint:
    return Endpoint(urllib.parse.urlsplit(url).path.split('/')[-2])


def get_token(endpoint: str | Endpoint, params: _TParams) -> Optional[str]:
    response = _get(_join_url(_URL_BASE, endpoint, 'anchor'), params)
    if response:
        for match in _RE_TOKEN.finditer(response.text):
            return match[1]


def get_response(endpoint: str | Endpoint,
                 params: _TParams, token: str) -> Optional[str]:
    params = _get_params(params)
    data = default_data()
    data['v'] = params['v'][0]
    data['c'] = token
    data['k'] = params['k'][0]
    data['co'] = params['co'][0]
    response = _post(_join_url(
        _URL_BASE, endpoint, 'reload'), data, params={'k': data['k']})
    if response:
        for match in _RE_RESPONSE.finditer(response.text):
            return match[1]


def bypass(url: str) -> Optional[str]:  # TODO
    endpoint = get_endpoint(url)
    if token := get_token(endpoint, _get_params(url)):
        return get_response(endpoint, _get_params(url), token)
