import importlib
import os
from xml.etree import ElementTree


def main():
    path = os.path.join('../.idea', 'dictionaries', f'{os.getlogin()}.xml')
    xml = ElementTree.parse(path)
    dic = xml.getroot()[0]
    try:
        append = dic[0].append
    except IndexError:
        words = ElementTree.Element('words')
        dic.append(words)
        append = words.append
    for const in dir(importlib.import_module('win32con')):
        if not const.startswith('__') and not const.endswith('__'):
            word = ElementTree.Element('w')
            word.text = const
            append(word)
    ElementTree.indent(xml)
    xml.write(path)


if __name__ == '__main__':
    main()
