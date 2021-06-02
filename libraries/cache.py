import functools


def one_cache(callback):  # TODO: pass last return somehow
    cached = [False, (), {}, None]

    @functools.wraps(callback)
    def wrapper(*args, **kwargs):
        if not cached[0] or cached[1] != args or cached[2] != kwargs:
            cached[:] = True, args, kwargs, callback(*args, **kwargs)
        return cached[3]

    return wrapper
