import os


def join_path(*paths: str) -> str:
    return '/'.join(paths)


APPDATA_DIR = os.environ['HOME']
PICTURES_DIR = join_path(APPDATA_DIR, 'Pictures')
TEMP_DIR = '/tmp'
