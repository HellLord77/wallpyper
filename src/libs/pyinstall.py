__version__ = '0.0.2'

import glob
import importlib
import io
import os
import shutil
import sys
import tempfile
from xml.etree import ElementTree

FROZEN = hasattr(sys, 'frozen')
TEMP_DIR = getattr(sys, '_MEIPASS', '')


def clean_temp(remove_base: bool = False) -> bool:
    cleaned = True
    base = os.path.dirname(TEMP_DIR) or tempfile.gettempdir()
    for dir_ in glob.iglob(os.path.join(base, f'_MEI{"[0-9]" * 6}')):
        path = os.path.join(base, dir_)
        if os.path.isdir(path) and path != TEMP_DIR:
            pydll = glob.glob(os.path.join(path, f'python{"[0-9]" * 2}.dll'))
            if pydll and os.path.isfile(pydll[0]):
                try:
                    os.remove(pydll[0])
                except PermissionError:
                    continue
            shutil.rmtree(path, True)
            cleaned = cleaned and not os.path.exists(path)
    if remove_base and not any(os.scandir(base)):
        os.remove(base)
        cleaned = cleaned and not os.path.exists(base)
    return cleaned


def _merge_xml_(self: ElementTree.Element, other: ElementTree.Element):
    elements = {element.tag: element for element in self}
    for element in other:
        if not len(element):
            try:
                elements[element.tag].text = element.text
            except KeyError:
                elements[element.tag] = element
                self.append(element)
        else:
            try:
                _merge_xml_(elements[element.tag], element)
            except KeyError:
                elements[element.tag] = element
                self.append(element)


def _merge_xml(self: str, other: str) -> str:
    root = ElementTree.fromstring(self)
    _merge_xml_(root, ElementTree.fromstring(other))
    ElementTree.indent(root)
    return ElementTree.tostring(root, 'unicode')


def _calc_winpe_size(stream: io.BytesIO) -> int:
    stream.seek(0, os.SEEK_SET)
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
    sz = 0
    for index in range(int.from_bytes(buff[header_offset + 6:header_offset + 8], 'little')):
        section_offset = header_offset + header_sz + index * 40
        data_ptr = int.from_bytes(buff[section_offset + 20:section_offset + 24], 'little')
        if data_ptr > max_ptr:
            max_ptr = data_ptr
            sz = max_ptr + int.from_bytes(buff[section_offset + 16:section_offset + 20], 'little')
    return sz


def add_manifest(path: str, manifest: str, merge: bool = True):
    winmanifest = importlib.import_module('PyInstaller.utils.win32.winmanifest')
    if merge:
        manifest = _merge_xml(winmanifest.GetManifestResources(path)[winmanifest.RT_MANIFEST][1][0].decode(), manifest)
    with tempfile.TemporaryFile() as temp:
        with open(path, 'rb') as file:
            shutil.copyfileobj(file, temp)
        winmanifest.UpdateManifestResourcesFromXML(path, manifest.encode())
        temp.seek(_calc_winpe_size(temp), os.SEEK_SET)
        with open(path, 'ab') as file:
            shutil.copyfileobj(temp, file)
