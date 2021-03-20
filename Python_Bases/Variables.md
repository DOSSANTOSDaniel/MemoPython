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

