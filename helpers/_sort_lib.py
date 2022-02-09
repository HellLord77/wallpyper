import os
import re

SYS32 = os.path.join(os.environ['windir'], 'System32')


def main():
    names = {}
    with open('..\\src\\libs\\ctyped\\_func.py') as file:
        for match in re.finditer(r'class ([^_].*)\(metaclass=_WinDLL\):', file.read()):
            name = match.groups()[0]
            with open(os.path.join(SYS32, f'{name}.dll')) as dll:
                names[name] = os.path.splitext(os.path.basename(dll.name))[0]
    for name in sorted(names, key=lambda k: names.__getitem__(k).lower()):
        print(name.ljust(10), os.path.splitext(names[name])[0])


if __name__ == '__main__':
    main()
