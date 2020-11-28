## Le type des variables

| Type | Description |
|:--|:--|
| int | Entier exemple : (5) |
| float | Nombre flottant exemple : (5.6) |
| str | Chaîne de caractère exemple : ("Bonjour") |
| bool | Booléen exemple (True ou False) |

### Vérifier le type d'une variable

Pour vérifier le type d'une variable on utilise la fonction type.

```python
>>> type(variable_a)
<class 'int'>

```
Ici la variable variable_a est de type "int", c'est donc un entier.

### Convertir une variable dans un autre type

Pour convertir la valeur 255 qui est un entier en une chaîne de caractère :

```python
>>> str(255)
'255'

```

Quelques exemples de conversions

```python
>>> toto = 255
>>> float(toto)
255.0
>>> str(toto)
'255'
>>> oct(toto)
'0o377'
>>> bin(toto)
'0b11111111'
>>> hex(toto)
'0xff'

```

Tableau des conversions

| Type | Description |
|:--|:--|
| int(X) | Conversion de X en entier |
| float(X) | Conversion de X en chiffres à virgule (flottants) |
| str(X) | Conversion de X en une chaîne de caractère |
| oct(X) | Conversion de X en base octale |
| bin(X) | Conversion de X en base binaire |
| hex(X) | Conversion de X en base hexadécimale |

