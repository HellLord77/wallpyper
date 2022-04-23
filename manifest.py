import argparse
import os
import re
import shutil
import tempfile
from xml.etree import ElementTree

# noinspection PyPackageRequirements
from PyInstaller.utils.win32 import winmanifest


def _merge_xml(self: ElementTree.Element, other: ElementTree.Element):
    elements = {element.tag: element for element in self}
    for element in other:
        if len(element) == 0:
            try:
                elements[element.tag].text = element.text
            except KeyError:
                elements[element.tag] = element
                self.append(element)
        else:
            try:
                _merge_xml(elements[element.tag], element)
            except KeyError:
                elements[element.tag] = element
                self.append(element)


def merge_xml(self: str, other: str, ns: bool = True) -> str:
    root = ElementTree.fromstring(self)
    _merge_xml(root, ElementTree.fromstring(other))
    ElementTree.indent(root)
    xml = ElementTree.tostring(root, 'unicode')
    if not ns:
        xml = re.sub(r':ns\d=', '=', re.sub(r'<(/?)ns\d+:', '<\\1', xml))
    return xml


def main(path: str, manifest: str, merge: bool = True):
    if merge:
        manifest = merge_xml(winmanifest.GetManifestResources(path)[winmanifest.RT_MANIFEST][1][0].decode(), manifest)
    with tempfile.TemporaryFile() as temp:
        with open(path, 'rb') as file:
            shutil.copyfileobj(file, temp)
        winmanifest.UpdateManifestResourcesFromXML(path, manifest.encode())
        temp.seek(os.path.getsize(path), os.SEEK_SET)
        with open(path, 'ab') as file:
            shutil.copyfileobj(temp, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Adds manifest to executable')
    parser.add_argument('path', help='Executable path')
    manifest_group = parser.add_mutually_exclusive_group(required=True)
    manifest_group.add_argument('-manifest', help='Raw manifest data')
    manifest_group.add_argument('-manifest_path', help='Manifest path')
    parser.add_argument('-merge', action=argparse.BooleanOptionalAction, default=False, help='Merge existing manifest')
    args = parser.parse_args()
    if args.manifest_path:
        with open(args.manifest_path, 'r') as manifest_file:
            args.manifest = manifest_file.read()
    main(args.path, args.manifest, args.merge)
