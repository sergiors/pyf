Pyf
---

**Pyf** is a functional library. It's built on the shoulders of [Pipe](https://github.com/JulienPalard/Pipe) project. 
If you don't find some functions here, we recommend you take a look on the [Pipe](https://github.com/JulienPalard/Pipe) project.

Below It's all functions that have been implemented.


```python
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

>>> ['b', 'c'] | reduce(lambda x, y: x+y, 'a')
'abc'

>>> {'black': '#000', 'gray': '#808080'} | pick(['gray'])
{'gray': '#808080'}

>>> {'indigo': '#4b0082', 'navy': '#000080'} | omit(['indigo'])
{'navy': '#000080'}

```

Contributions
-------------

Everyone's welcome to contribute it. You might open a pull request at anytime.

License
-------

MIT