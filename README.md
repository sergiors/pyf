
    >>> from pyf import *

    >>> [1, 2, 3] | prepend(1)
    [1, 1, 2, 3]

    >>> {'foo': 'bar'} | merge({'bar': 'foo'})
    {'foo': 'bar', 'bar': 'foo'}

    >>> {'name': 'Joe'} | prop('name')
    'Joe'

    >>> {'addr': {'country': 'Brazil'}} | path(['addr', 'country'])
    'Brazil'

    >>> [1, 2, 3] | map(lambda x: x + 2)
    [3, 4, 5]

    >>> [-1, 1, 2, -2, 3] | filter(lambda x: x > 0)
    [1, 2, 3]

    >>> [1, 2, 3, 4, 5] | reduce(lambda x, y: x+y)
    15