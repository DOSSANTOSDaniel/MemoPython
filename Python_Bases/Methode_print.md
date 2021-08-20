# La fonction print

Elle permet d'afficher une valeur à l'écran.

Exemple d'affichage pour une chaîne de caractère :

```python
>>> print("Bonjour")
Bonjour
 
```

Une chaîne de caractères est toujours entouré de doubles cotes(" ") ou de simples cotes(' ').

En python il n'y a pas de différence entre les doubles quottes et les simples quottes ("" = '').

Paramètres de la fonction print :

| Paramètre | Description |
|:--|:--|
| sep=' ' | Spécification d'un séparateur |
| end=' ' | Permet de définir l'affichage après l'affichage |

Affichage d'une chaîne de caractère avec séparateur :

```python
>>> print("Bonjour", "Hello", sep=' ----> ')
Bonjour ----> Hello

```

Afficher la valeur d'une variable :

```python
>>> toto = 'Bonjour toto'
>>> print(toto)

Bonjour toto

```

Affichage avec un retour à la ligne :

```python
>>> print('Bonjour \n')

Bonjour
 
```

Affichage avec une tabulation :

```python
>>> print('\t Bonjour')
	 Bonjour
```

Affichage sur plusieurs lignes :

```Python
print("""
Bonjour,
tout le monde!
""") 
```

Affichage des variables

Méthode 1 :

```Python
# Code
var = 5

print(var)

# Résultat
5
>>>
```

Méthode 2 :

```Python
# Code
mon_nom = "Mon nom est {nom} !"

print(mon_nom.format(nom = "Jean"))

# Résultat
Mon nom est Jean !
```

autre exemple :

```Python
# Code
nom = 'Ana'
age = 21

print("{} a {} ans".format(nom,age))

# Résultat
Ana a 21 ans
```

Méthode 3 :

```Python
# Code
nom = 'Ana'
age = 21

print(f"{nom} a {age} ans")

# Résultat
Ana a 21 ans
```