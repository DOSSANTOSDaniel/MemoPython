# Liste des diviseurs d’un nombre
### Entête
Algorithme liste de diviseurs
* Rôle : affiche la liste des diviseurs d’un nombre 
* Entrée : nombre à tester
* Sortie : affiche les diviseur d’un nombre

### Langage naturelle

```
Variable : liste (liste), nb (entier), i (entier)
Début
   déclarer une liste vide
   afficher saisir un nombre : 
   saisir nb
   pour i de 1 à nb+1 faire :
      si nb%i = 0 alors :
         ajouter i à la liste
      fin si
   fin pour
   afficher la liste
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

liste = []

nb = int(input("saisir un nombre : "))

for i in range(1,nb+1):
    if (nb%i == 0):
        liste.append(i)
        
print(liste)

```
