#!/usr/bin/env python
# -*- coding: utf-8 -*-


import builtins
import functools


from pipe import Pipe
from pipe import as_list


__all__ = [
    'prop', 'prepend', 'merge', 'path', 'map', 'filter', 'reduce',
    'pick', 'omit', 'equal'
]


def equal(x) -> bool:
    return lambda y: x == y


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
def map(xs: list, f: callable) -> list:
    return builtins.map(f, xs) | as_list


@Pipe
def filter(xs, f: callable) -> list:
    return builtins.filter(f, xs) | as_list


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
