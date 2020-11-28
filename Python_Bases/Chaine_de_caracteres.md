## Les chaînes de caractères

Il est possible de récupérer seulement certains caractères d'une chaîne de caractères

Exemple :

```python
>>> toto = "Daniel"
>>> print(toto[0])
D
>>> print(toto[5])
l

```

Avoir le dernier caractère sans savoir le nombre de caractères :

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

Extraire une partie de la chaîne de caractère

L'index commence toujours à 0.

Extraire à partir du caractère à l'index 2 jusqu’à la fin

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

```python

```

```python

```
