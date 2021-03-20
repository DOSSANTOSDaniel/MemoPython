# Devine un numéro tiré au hasard
### Entête
Algorithme jeu de hasard
* Rôle : jeux servant à tenter de deviner des chiffres sélectionnés au hasard
* Entrée : nombre au hasard, nombre choisi par l’utilisateur
* Sortie : nombre d’essais avant de trouver, si un des deux chiffres et bon, affiche (gagné si trouvé)
### Langage naturelle

```
Variable :i, nb_hasard, nb_choisi, essai,  bonnes_rep
Début
   nb_hasard= nombre entier au hasard entre 10 et 20
   afficher « saisir un nombre à 2 chiffres »
   saisir nb_choisi
   essai=1
   tant que nb_choisi est différent de nb_hasard faire :
      bonnes_rep=0
      pour i de 0 à 2 faire :
         si nb_hasard[i]==nb_choisi[i] alors
            bonnes_rep=bonnes_rep+1
         fin si
      fin pour
   afficher « il y a bonnes_rep chiffre(s) correct(s) recommencer ! : »
   saisir nb_choisi
   essai=essai+1
   fin de tant que
   
   afficher Bravo le nb_choisi est le nombre hasard !, trouvé en essai, !
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

nb_hasard = str(random.randrange(10,21))
nb_choisi = input("saisir un nombre de 10 à 20 :")
essai = 1

while (nb_choisi != nb_hasard):
    
    bonnes_rep = 0
    
    for i in range(2):
        if ( nb_choisi[i] == nb_hasard[i] ):
            bonnes_rep = bonnes_rep+1
            
    #On n’a pas le droit de donner plus de de 1 argument a input, ici on a concaténé avec les + pour que ça fasse 1 seul argument
    nb_choisi = input("il y a "+str(bonnes_rep)+" chiffre(s) correct(s) recommencer! : ")
    essai = essai+1
    
print("Brovo le ",nb_choisi,"est le nombre hasard!, trouvé en",essai,"essai(s) !")               


```
