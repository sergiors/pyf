# -*- coding: utf-8 -*-

from pipe import Pipe


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
def map(xs: list, f) -> list:
    return [f(x) for x in xs]


@Pipe
def filter(xs: list, f) -> list:
    return [x for x in xs if f(x)]


@Pipe
def reduce(xs: list, f, init=None):
    from functools import reduce

    return reduce(f, xs, init)


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md')