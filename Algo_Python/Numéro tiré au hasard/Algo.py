#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
nb_hasard=str(random.randrange(10,21))
nb_choisi=input("saisir un nombre à 2 chiffres :")
essai=1
while (nb_choisi != nb_hasard):
    bonnes_rep=0
    for k in range(2):
        if ( nb_choisi[k] == nb_hasard[k] ):
            bonnes_rep=bonnes_rep+1
    #On n’a pas le droit de donner plus de de 1 argument a input, ici on a concaténé avec les + pour que ça fasse 1 seul argument
    nb_choisi=input("il y a "+str(bonnes_rep)+" chiffre(s) correct(s) recommencer! : ")
    essai=essai+1
print("Brovo le ",nb_choisi,"est le nombre hasard!, trouvé en",essai,"essai(s) !")               
