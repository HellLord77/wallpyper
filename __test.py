import importlib
import os

import utils

MODULES = []
tuple(module[:-3] for module in os.listdir('modules') if module.endswith('.py') and module != '__init__.py')
for module in os.listdir('modules'):
    if module.endswith('.py'):
        MODULES.append(importlib.import_module(f'modules.{module[:-3]}'))

if __name__ == '__main__':
    print(MODULES)
    print(utils.join_url(MODULES[1].BASE_URL))
    utils.MAIN = 69
    print(utils.MAIN)
