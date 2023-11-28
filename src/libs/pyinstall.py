__version__ = '0.0.2'

import __main__
import copy
import glob
import io
import logging
import os
import shutil
import sys
import tempfile
from xml.etree import ElementTree

logger = logging.getLogger(__name__)

FROZEN = hasattr(sys, 'frozen')
TEMP_DIR = getattr(sys, '_MEIPASS', '')


def get_launch_args() -> tuple[str, ...]:
    args = sys.executable,
    if not FROZEN:
        args += __main__.__file__,
    return args


def clean_temp() -> bool:
    cleaned = True
    base = os.path.dirname(TEMP_DIR) or tempfile.gettempdir()
    logger.debug('Cleaning temporary directory: %s', base)
    for dir_ in glob.iglob(os.path.join(base, f'_MEI{"[0-9]" * 6}')):
        path = os.path.join(base, dir_)
        if os.path.isdir(path) and path != TEMP_DIR:
            pydll = glob.glob(os.path.join(path, f'python[0-9]*.dll'))  # TODO platforms
            if pydll and os.path.isfile(pydll[0]):
                try:
                    os.remove(pydll[0])
                except PermissionError:
                    continue
            logger.warning('Removing temporary directory: %s', path)
            shutil.rmtree(path, True)
            cleaned = cleaned and not os.path.exists(path)
    if not any(os.scandir(base)):
        os.remove(base)
        cleaned = cleaned and not os.path.exists(base)
    return cleaned


def _calc_winpe_size(stream: io.BytesIO) -> int:
    stream.seek(0)
    buff = stream.read(4096)
    header_offset = int.from_bytes(buff[60:64], 'little')
    machine = int.from_bytes(buff[header_offset + 4:header_offset + 6], 'little')
    if machine == 0x014c:
        header_sz = 248
    elif machine == 0x8664:
        header_sz = 264
    else:
        return 0
    max_ptr = 0
    size = 0
    for index in range(int.from_bytes(buff[header_offset + 6:header_offset + 8], 'little')):
        section_offset = header_offset + header_sz + index * 40
        data_ptr = int.from_bytes(buff[section_offset + 20:section_offset + 24], 'little')
        if data_ptr > max_ptr:
            max_ptr = data_ptr
            size = max_ptr + int.from_bytes(buff[section_offset + 16:section_offset + 20], 'little')
    return size


def _element_merge(self: ElementTree.Element, other: ElementTree.Element):
    elements = {element.tag: element for element in self}
    for element in other:
        try:
            if len(element):
                _element_merge(elements[element.tag], element)
            else:
                elements[element.tag].text = element.text
        except KeyError:
            elements[element.tag] = copy.copy(element)
            self.append(element)


def add_manifest(path: str, manifest: str, merge: bool = True):
    winmanifest = __import__('PyInstaller.utils.win32.winmanifest', fromlist=['PyInstaller.utils.win32'])
    if merge:
        root = ElementTree.XML(winmanifest.GetManifestResources(
            path)[winmanifest.RT_MANIFEST][1][0].decode())
        _element_merge(root, ElementTree.XML(manifest))
        ElementTree.indent(root)
        manifest = ElementTree.tostring(root, 'unicode')
    with tempfile.TemporaryFile() as temp:
        with open(path, 'rb') as file:
            shutil.copyfileobj(file, temp)
        winmanifest.UpdateManifestResourcesFromXML(path, manifest.encode())
        temp.seek(_calc_winpe_size(temp))
        with open(path, 'ab') as file:
            shutil.copyfileobj(temp, file)
