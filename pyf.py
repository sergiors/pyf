# -*- coding: utf-8 -*-

from pipe import Pipe


@Pipe
def prepend(lst: list, elm) -> list:
    return [elm] + lst

@Pipe
def merge(l_dct: dict, r_dct: dict) -> dict:
    return {**l_dct, **r_dct}


if __name__ == '__main__':
    import doctest
    doctest.testfile('README.md')