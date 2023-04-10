import dataclasses
import enum
import json
import os
import random
import urllib.request
from typing import Optional

_PATH = 'browsers.json'
_BROWSERS: Optional[dict[str, dict]] = None


class Device(enum.StrEnum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'


class DesktopPlatform(enum.StrEnum):
    LINUX = 'linux'
    WINDOWS = 'windows'
    DARWIN = 'darwin'


class MobilePlatform(enum.StrEnum):
    ANDROID = 'android'
    IOS = 'ios'


class Browser(enum.StrEnum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'


@dataclasses.dataclass
class UserAgent:
    device: Optional[str | Device] = None
    platform: Optional[str | DesktopPlatform | MobilePlatform] = None
    browser: Optional[str | Browser] = None
    allow_brotli: bool = False

    def __post_init__(self):
        if self.device is None:
            self.device = random.choice(tuple(Device))
        if self.platform is None:
            self.platform = random.choice(tuple(
                DesktopPlatform if self.device == Device.DESKTOP else MobilePlatform))
        if self.browser is None:
            self.browser = (Browser.CHROME if self.platform == MobilePlatform.IOS
                            else random.choice(tuple(Browser)))

    def encode(self, request: Optional[urllib.request.Request] = None) -> tuple[dict[str, str], tuple[str, ...]]:
        global _BROWSERS
        if _BROWSERS is None:
            with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
                _BROWSERS = json.load(file)
        headers = _BROWSERS['headers'][self.browser].copy()
        cipher_suite = tuple(_BROWSERS['cipherSuite'][self.browser])
        headers['User-Agent'] = random.choice(_BROWSERS['user_agents'][self.device][
                                                  self.platform][self.browser])
        if not self.allow_brotli:
            encodings = urllib.request.parse_http_list(headers['Accept-Encoding'])
            try:
                encodings.remove('br')
            except ValueError:
                pass
            else:
                headers['Accept-Encoding'] = ', '.join(encodings)
        if request is not None:
            for header in headers:
                request.add_header(*header)
            if (verify := getattr(request, '_verify', None)) is not None:
                verify.set_ciphers(':'.join(cipher_suite))
        return headers, cipher_suite


if __debug__:
    def _download():
        import urllib.parse
        import urllib.request
        path = os.path.join(os.path.dirname(__file__), _PATH)
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/VeNoMouS/cloudscraper/master/cloudscraper/user_agent/', _PATH), path)
        with open(path, encoding='utf-8') as file:
            json.load(file)
