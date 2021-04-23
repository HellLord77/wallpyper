import configparser
import os
import sys

MAIN = sys.modules['__main__']


def exists() -> bool:
    return os.path.isfile(MAIN.CONFIG_PATH)


def load() -> None:
    config = configparser.ConfigParser()
    config.read(MAIN.CONFIG_PATH)
    for module in (MAIN,) + MAIN.MODULES:
        if config.has_section(module.NAME):
            for key, value in module.DEFAULT_CONFIG.items():
                module.CONFIG[key] = config.get(module.NAME, key, fallback=value)
        else:
            module.CONFIG.update(module.DEFAULT_CONFIG)


def save() -> None:
    config = configparser.ConfigParser()
    for module in (MAIN,) + MAIN.MODULES:
        config[module.NAME] = module.CONFIG
    with open(MAIN.CONFIG_PATH, 'w') as file:
        config.write(file)


def remove() -> bool:
    if os.path.isfile(MAIN.CONFIG_PATH):
        os.remove(MAIN.CONFIG_PATH)
    return os.path.isfile(MAIN.CONFIG_PATH)
