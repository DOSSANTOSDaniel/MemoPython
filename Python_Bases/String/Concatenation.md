# Concaténation de chaînes de caractères

On peut combiner deux chaînes de caractères en une seule avec l'opérateur "+".

Exemple :

```python
>>> toto = "Daniel" + "Ana"

>>> print(toto)

DanielAna

```

On peut directement faire la concaténation dans la fonction print.

```python
>>> print("Daniel" + "Ana")

DanielAna

```

Afficher une chaîne de caractère et la valeur d'une variable.

```python
>>> prenom = "daniel"

>>> print("Ton prénom est :", prenom)

Ton prénom est : daniel

```

Afficher une chaîne de caractère et le résultat d'un calcul.

```python
>>> print("Ton age : ", 2020 - 1988)

Ton age :  32

```

Utilisation de print avec la méthode format.

```python
>>> print("{0} a eu {1} ans.".format("Daniel", 32))

Daniel a eu 32 ans.

```
* 0 correspond à Daniel
* 1 correspond à 32

Autres manière d'utiliser format.

```python
>>> prenom = "Daniel"
>>> age = 32

>>> print(f"{prenom} a eu {age} ans.")

Daniel a eu 32 ans.

```

