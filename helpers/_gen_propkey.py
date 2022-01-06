import os
import re

VERSION = '10.0.22000.0'


def main():
    path = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits', '10', 'Include', VERSION, 'um', 'propkey.h')
    with open(path, 'r') as file:
        for match in re.compile(r'//\s\sName:.*(PKEY_[a-zA-Z_]*)+\n'
                                r'//\s\sType:.*\n'
                                r'//\s\sFormatID:.*({[0-9A-Z-]+}),\s([0-9]+)').finditer(file.read()):
            group = match.groups()
            print(f"{group[0]} = '{group[1]}', {group[2]}")


if __name__ == '__main__':
    main()
