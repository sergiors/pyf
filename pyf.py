import builtins
import functools

from pipe import Pipe

__all__ = [
    'identity', 'always', 'as_str', 'as_int', 'prop', 'values', 'prepend',
    'merge', 'path', 'map', 'filter', 'reduce', 'pick', 'omit', 'equal', 'find',
    'find_index'
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


def equal(x) -> bool:
    return lambda y: x == y


@Pipe
def prop(dct: dict, k: str, default=None):
    return dct.get(k, default)


@Pipe
def values(dct: dict) -> list:
    return list(dct.values())


@Pipe
def prepend(lst: list, elm) -> list:
    return [elm] + lst


@Pipe
def merge(l_dct: dict, r_dct: dict) -> dict:
    return {**l_dct, **r_dct}


@Pipe
def path(dct: dict, steps: list, default=None):
    k = steps[0]
    v = dct.get(k, default)
    t = steps[1:]

    return v if not t else v | path(t, default)


@Pipe
def map(lst: list, f: callable):
    return builtins.map(f, lst)


@Pipe
def filter(lst, f: callable):
    return builtins.filter(f, lst)


@Pipe
def reduce(lst: list, f: callable, init=None):
    if not init:
        init, *lst = lst

    return functools.reduce(f, lst, init)


@Pipe
def pick(dct: dict, names: list) -> dict:
    return {k: v for k, v in dct.items() if k in names}


@Pipe
def omit(dct: dict, names: list) -> dict:
    return {k: v for k, v in dct.items() if k not in names}


@Pipe
def find(lst: list, f: callable):
    v = next(iter(lst), None)

    if not v:
        return None

    if f(v):
        return v

    return lst[1:] | find(f)

@Pipe
def find_index(lst: list, f: callable):
    for k, v in enumerate(lst):
        if f(v):
            return k

    return None


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md', verbose=True)
