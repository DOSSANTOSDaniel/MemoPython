#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nom du projet : FindExt
Auteur(s) : DOS SANTOS Daniel
Version : 0
Notes : Ce programme va permettre de rechercher
des fichiers par extention.
"""

# Programme principal
######################

# Imports de modules
# --------------------
import os

# Variables globales
# --------------------
listeFiles = []
listeFilesFilter = []
continuer = '1'

# Modules / Fonctions
# --------------------

# Programme
# --------------------
while continuer == '1':
    continuer = '1'
    print("\n\n************************************")
    print("Programme FindExt")
    print("Saissir le chemin absolu d'un dossier")
    print("Saissir l'extention des fichiers que vous cherchez")
    print("Exemple : ")
    print("Saisir le chemin : /home/daniel")
    print("Quelle extention : docx")
    print("*************************************\n")

    chemin = input("Saisir le chemin : ")
    extent = input("Quelle extention : ")

    extent = '.'+extent

    for root, dirs, files in os.walk(chemin):
        for fichier in files:
            listeFiles.append(os.path.join(root, fichier))

    for file in listeFiles:
        extentFile = os.path.splitext(file)[1]
        if extentFile == extent:
            print("\n\n Voici les résultats : \n")
            print("\n", file, "\n")

    while True:
        print()
        choix = input("Voulez vous quitter[0] ou continuer[1] : ")
        if choix == '0':
            continuer = 0
        else:
            break
        break

print("\n Fin du Programme FindExt \n")
