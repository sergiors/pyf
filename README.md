
    >>> from pyf import *

    >>> [1, 2, 3] | prepend(1)
    [1, 1, 2, 3]


    >>> {'foo': 'bar'} | merge({'bar': 'foo'})
    {'foo': 'bar', 'bar': 'foo'}