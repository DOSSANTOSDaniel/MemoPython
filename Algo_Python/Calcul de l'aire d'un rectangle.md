# Calcul de l’aire d’un rectangle

### Entête
Algorithme aire d’un rectangle
* Rôle : calculer l’aire d’un rectangle
* Entrée : la largeur, la longueur
* Sortie : affiche l’aire du rectangle

### Langage naturelle

```
Variable : long (entier),larg (entier), aire (entier)
Début
   afficher « Quelle est la longueur du rectangle »
   saisir long
   afficher « Quelle est la largeur du rectangle »
   saisir larg
   air=longxlarg
   afficher « L’aire du rectangle est de (aire) »
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

long=int(input("quelle est la longueur ? : "))
larg=int(input("quelle est la largeur ? : "))
aire=long*larg
print("l'aire du rectangle est de",aire)
```