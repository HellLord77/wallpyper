import sys

FROZEN = hasattr(sys, 'frozen')


def redirect_print(path: str,
                   write_once: bool,
                   *streams):
    streams = streams or (sys.stdout, sys.stderr)


def clean_temp():
    path = getattr(sys, '_MEIPASS', '')
    if path:
        print(path)
