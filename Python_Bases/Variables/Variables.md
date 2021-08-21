# Les variables

En python on a pas besoin de typer nos variables, le type est automatiquement déduit.

## Syntaxe de base

```python
>>> nombre_1 = 5
>>> nombre_2 = 3
>>> nombre_3 = nombre_1 + nombre_2
>>> nombre_3
8

```

## Affichage des variables

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

Autre exemple :

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

## Permutation des valeurs de deux variables

En plusieurs lignes :

```python
>>> variable_a = 2
>>> variable_b = 5
>>> variable_c = variable_a
>>> variable_a = variable_b
>>> variable_b = variable_c
>>> variable_a
5
>>> variable_b
2

```

En une seule ligne :

```python
>>> variable_a = 2
>>> variable_b = 5
>>> variable_a, variable_b = variable_b, variable_a
>>> variable_a
5
>>> variable_b
2

```
