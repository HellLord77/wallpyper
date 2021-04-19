import atexit
import os
import tempfile


# noinspection PyUnusedLocal
def _handler(*args, **kwargs):
    pass


def _uid():
    import hashlib
    import sys
    with open(sys.argv[0], 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


# noinspection PyDefaultArgument
def init(uid=_uid(),
         crash_handler=_handler, crash_handler_args=(), crash_handler_kwargs={},
         exit_handler=_handler, exit_handler_args=(), exit_handler_kwargs={}):
    temp_dir = tempfile.gettempdir()
    os.makedirs(temp_dir, exist_ok=True)
    path = os.path.join(temp_dir, uid)
    flags = os.O_CREAT | os.O_EXCL
    try:
        _descriptor = os.open(path, flags)
    except FileExistsError:
        try:
            os.remove(path)
        except PermissionError:
            exit_handler(*exit_handler_args, **exit_handler_kwargs)
            raise SystemExit
        else:
            crash_handler(*crash_handler_args, **crash_handler_kwargs)
            _descriptor = os.open(path, flags)
    else:
        atexit.register(os.remove, path)
        atexit.register(os.close, _descriptor)
