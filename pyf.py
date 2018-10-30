import builtins
import functools

from pipe import Pipe


__all__ = [
    'identity', 'always', 'as_str', 'as_int', 'prop', 'prepend', 'merge',
    'path', 'map', 'filter', 'reduce', 'pick', 'omit',
]


def identity(x):
    return x


def always(x):
    return lambda: x


@Pipe
def as_str(x) -> str:
    return str(x)


@Pipe
def as_int(x) -> int:
    return int(x)


@Pipe
def prop(dct: dict, k: str, default=None):
    return dct.get(k, default)


@Pipe
def prepend(lst: list, elm) -> list:
    return [elm] + lst


@Pipe
def merge(l_dct: dict, r_dct: dict) -> dict:
    return {**l_dct, **r_dct}


@Pipe
def path(dct: dict, steps: list):
    k = steps[0]
    v = dct.get(k)

    return v if type(v) is not dict else v | path(steps[1:])


@Pipe
def map(xs: list, f: callable):
    return builtins.map(f, xs)


@Pipe
def filter(xs, f: callable):
    return builtins.filter(f, xs)


@Pipe
def reduce(xs: list, f: callable, init=None):
    if init is None:
        init, *xs = xs

    return functools.reduce(f, xs, init)


@Pipe
def pick(dct: dict, names: list) -> dict:
    return {k: v for k, v in dct.items() if k in names}


@Pipe
def omit(dct: dict, names: list) -> dict:
    return {k: v for k, v in dct.items() if k not in names}


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md', verbose=True)