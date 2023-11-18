import configparser
import glob
import os
import re

PATH = r'C:\ProgramData\Corsair\CUE5\GameSdkEffects'

_GAMES: dict[str, dict[str, int]] = {}
_RE_NAME = re.compile('[^_0-9a-zA-Z]+')


def get_priority(path: str) -> dict[str, int]:
    parser = configparser.ConfigParser(strict=False)
    parser.optionxform = str
    with open(path) as file:
        parser.read_string('[DEFAULT]\n' + file.read())
    return {key: int(value) for key, value in parser.defaults().items()}


def str_game(game: str, data: dict[str, int]) -> str:
    name = _RE_NAME.sub('', game)
    string = f'class {name}(_Game):\n'
    if game != name:
        string += f'    _name = {game!r}\n'
    string += '    # noinspection PyPep8Naming\n'
    string += '    class profile(_Profile):\n'
    for key, value in sorted(data.items()):
        string += f'        {key} = {value}\n'
    return string


def main():
    for path in glob.glob(os.path.join(PATH, '*', 'priorities.cfg')):
        name = os.path.basename(os.path.dirname(path))
        _GAMES[name] = get_priority(path)
    string = ''
    for game in _GAMES.items():
        string += str_game(*game)
    print(string)


if __name__ == '__main__':
    main()
