# Pseudo à 4 chiffres
### Entête
Algorithme pseudo
* Rôle : obtenir un pseudo correct puis afficher bonjour {pseudo}
* Entrée : pseudo de l’utilisateur
* Sortie : message (bonjour {pseudo})

### Langage naturel

```
Variables: pseudo (chaîne)
Début
   afficher « saisir un pseudo à 4 chiffres »
   saisir pseudo
   tant que la longueur de pseudo est inférieur à 4 faire :
      afficher « Erreur ressaisir un pseudo à 4 chiffres »
      saisir pseudo
   fin de tant que
   afficher « bonjour {pseudo} »
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

pseudo = input("Saisir un pseudo de 4 caractères : ")

while (len(pseudo)<4 or len(pseudo)>4):
    pseudo = input("#Erreur resaisir un pseudo à 4 caractères : ")
    
print("Bonjour ",pseudo)
```
