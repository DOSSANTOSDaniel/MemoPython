# Sets (liste sans ordre)
1. Les éléments n'ont pas d'ordre.
2. Les doublons sont impossibles.

Syntaxe de base

```Python
set = {}
```

Afficher les ressemblances avec une autre liste

```Python
>>> set = { "A", "Z", 1, 45, "X", 3 }
>>> 
>>> set2 = { "A", "F", 3, 45, "W", 6 }
>>> 
>>> print(set.intersection(set2))
{3, 45, 'A'}
```

Afficher les différences avec une autre liste

```Python
>>> print(set.difference(set2))
{'Z', 1, 'X'}
>>> 
```

Fusion de deux listes

```Python
>>> print(set.union(set2))
{1, 3, 'A', 6, 'Z', 'W', 45, 'F', 'X'}
```

Comme il n'y a pas d'ordre alors on ne peut pas avoir d'index.`