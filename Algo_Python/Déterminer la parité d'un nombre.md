# Déterminer la parité d’un nombre
### Entête
Algorithme pair ou impair
* Rôle : affiche si un nombre est pair ou impair
* Entrée : nombre à tester
* Sortie : affiche si le nombre est pair ou impair

### Langage naturelle

```python
Variable :nb (entier)
Début
   afficher saisir un nombre
   saisir nb
   si nb%2 == 0 alors :
      afficher c’est pair
   si non afficher c’est impair
   fin si
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

nb=int(input("saisir un nombre : "))
if (nb%2==0):
    print("c'est pair")
else:
    print("c'est impair")
```