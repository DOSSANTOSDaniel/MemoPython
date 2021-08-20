# Les chaînes de caractères

Il est possible de récupérer seulement certains caractères d'une chaîne de caractères

Exemple :

```python
>>> toto = "Daniel"
>>> print(toto[0])
D
>>> print(toto[5])
l

```

Avoir le dernier caractère sans savoir le nombre de caractères 

```python
>>> toto = "Daniel"
>>> print(toto[-1])
l

```

Afficher à partir des dernières lettres vers les premières

```python
>>> toto = "Daniel"
>>> print(toto[-2])
e

```

Extraire une partie de la chaîne de caractère :

L'index commence toujours à 0.

Extraire à partir du caractère à l'index 2 jusqu’à la fin.

```python
>>> toto = "Daniel"
>>> print(toto[2:])
niel

```

Extraire à partir du caractère à l'index 2 jusqu’au début

```python
>>> print(toto[:2])
Da 

```

Extraire à partir du caractère à l'index 2 jusqu'à l'index 5 exclut 

```python
>>> toto = "Daniel"
>>> print(toto[2:5])
nie

```

On a aussi la possibilité de répéter une chaîne de caractère

```python
>>> toto = "Daniel"
>>> fois_4 = toto*4
>>> print(fois_4)
DanielDanielDanielDaniel
>>> 

```

Pour voir les méthodes possibles avec les chaînes de caractères

```Python
>>> var = "Massy"
>>> print(dir(var))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

Afficher l'aide

```Python
>>> var = "Massy"
>>> print(help(var.upper))

# Résultat
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
(END)
``` 

On peut aussi appliquer des fonctions , exemple avec "len"(longueur d'une chaîne)

```Python
>>> var = "Massy"
>>> print(len(var))

# Résultat
5
```
