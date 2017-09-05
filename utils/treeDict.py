>>> class Tree(dict):
...     def __missing__(self, key):
...         value = self[key] = type(self)()
...         return value

>>> # common names by class, order, genus, and type-species
>>> common_names = Tree()
>>> common_names['Mammalia']['Primates']['Homo']['H. sapiens'] = 'human being'
>>> common_names
{'Mammalia': {'Primates': {'Homo': {'H. sapiens': 'human being'}}}}

>>> # Famous quotes by play, act, scene, and page
>>> quotes = Tree()
>>> quotes['Hamlet'][1][3][3] = 'This above all: to thine own self be true.'
>>> quotes
{'Hamlet': {1: {3: {3: 'This above all: to thine own self be true.'}}}}
