import atexit
import os
import tempfile


# noinspection PyUnusedLocal
def _hook(*args, **kwargs):
    pass


def _uid():
    import hashlib
    import sys
    with open(sys.argv[0], 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()


def init(uid=_uid(),
         crash_hook=_hook, crash_hook_args=(), crash_hook_kwargs=None,
         exit_hook=_hook, exit_hook_args=(), exit_hook_kwargs=None):
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
            exit_hook(*exit_hook_args, **exit_hook_kwargs or {})
            raise SystemExit
        else:
            crash_hook(*crash_hook_args, **crash_hook_kwargs or {})
            _descriptor = os.open(path, flags)
    else:
        atexit.register(os.remove, path)
        atexit.register(os.close, _descriptor)
