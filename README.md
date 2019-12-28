Pyf
---

**Pyf** is a functional library. It's built on the shoulders of [Pipe](https://github.com/JulienPalard/Pipe) project.
If you don't find some functions here, we recommend you take a look on the [Pipe](https://github.com/JulienPalard/Pipe) project.

Below It's all functions that have been implemented.


```python
>>> from pipe import as_list
>>> from pyf import *

>>> [1, 2, 3] | prepend(1)
[1, 1, 2, 3]

>>> {'foo': 'bar'} | merge({'bar': 'foo'})
{'foo': 'bar', 'bar': 'foo'}

>>> {'name': 'Joe'} | prop('name')
'Joe'

>>> {'name': 'Joe'} | prop('addr', {})
{}

>>> {'name': 'Jimi', 'surname': 'Hendrix'} | values
['Jimi', 'Hendrix']

>>> {'addr': {'country': 'Brazil'}} | path(['addr', 'country'])
'Brazil'

>>> {'user': {'addr': {'country': 'Brazil'}}} | path(['user', 'addr'])
{'country': 'Brazil'}

>>> {'addr': {'country': 'Brazil'}} | path(['addr', 'street_number'], 0)
0

>>> {} | path(['addr', 'street_number'], 0)
0

>>> @partial
... def plus(x):
...     return x + 2
>>> [1, 2, 3] | map(plus) | as_list
[3, 4, 5]

>>> [-1, 1, 2, -2, 3] | filter(lambda x: x > 0) | as_list
[1, 2, 3]

>>> @partial
... def sum(x, y):
...     return x + y
>>> [1, 2, 3, 4, 5] | reduce(sum)
15

>>> ['b', 'c'] | reduce(lambda x, y: x+y, 'a')
'abc'

>>> {'black': '#000', 'gray': '#808080'} | pick(['gray'])
{'gray': '#808080'}

>>> {'indigo': '#4b0082', 'navy': '#000080'} | omit(['indigo'])
{'navy': '#000080'}

>>> [5, 4, 5, 6, 7] | filter(equals(5)) | as_list
[5, 5]

>>> [2, 3, 4, 5, 6, 7, 8] | find(lambda x: x % 2 is 1)
3

>>> [{'name': 'Jimi'}, {'name': 'James'}] | find_index(prop_eq('name', 'James'))
1

>>> [0, 3, 5] | find_index(equals(1))
-1

>>> equals(1, 1)
True

```

Contributions
-------------

Everyone's welcome to contribute it. You might open a pull request at anytime.

License
-------

MIT
