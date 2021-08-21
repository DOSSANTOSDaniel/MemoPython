# Le slicing

Cela est applicable seulement aux listes.

Lecture une valeur d'un index précis, du début de la liste vers la fin et vise versa.

Début ---> Fin

```Python
>>> liste = [5, 4, 2, 7, 1]
>>> liste[1]
4
```

Début <--- Fin

```Python
>>> liste = [5, 4, 2, 7, 1]
>>> liste[-1]
1
```

Les séquences de données

Lister les valeurs de l'index 0 à 2

```Python
>>> liste = [5, 4, 2, 7, 1]
>>> liste[0:3]
[5, 4, 2]
```

Lister les valeurs du début de l'index à l'index 3

```Python
>>> liste = [5, 4, 2, 7, 1]
>>> liste[:4]
[5, 4, 2, 7]
```

Lister les valeurs de l'index 2 à la fin de la liste

```Python
>>> liste = [5, 4, 2, 7, 1]
>>> liste[2:]
[2, 7, 1]
```

Lister des valeur de 0 à 5 avec un pas de 2

```Python
>>> liste[0:5:2]
[5, 2, 1]
```

Inverser une liste

```Python
>>> liste[::-1]
[1, 7, 2, 4, 5]
```

Utilisation avec les URL

```Python
>>> url="archlinux.fr"
>>> indexp = url.index('.') # Récupération de l'index correspondant à la valeur '.'

>>> # Le nom
>>> print(url[:indexp])
archlinux

>>> # L'extension
>>> print(url[indexp:])
.fr
```