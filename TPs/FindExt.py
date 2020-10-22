#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nom du projet : FindExt
Date de dernière mise à jour : 21/10/20
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

# Modules / Fonctions
# --------------------

# Programme
# --------------------
while True:
    print("\n\n************************************")
    print("Programme FindExt")
    print("Saissir le chemin absolu d'un dossier")
    print("Saissir l'extention des fichiers que vous cherchez")
    print("Saissir quit pour quitter le programme")
    print("Exemple : ")
    print("Saisir le chemin : /home/daniel")
    print("Quelle extention : docx")
    print("*************************************\n")

    chemin = input("Saisir le chemin : ")
    extent = input("Quelle extention : ")

    if chemin == 'quit' or extent == 'quit':
        break

    extent = '.'+extent

    for root, dirs, files in os.walk(chemin):
        for fichier in files:
            listeFiles.append(os.path.join(root, fichier))

    for file in listeFiles:
        extentFile = os.path.splitext(file)[1]
        if extentFile == extent:
            print(file)

print("\n Fin du Programme FindExt \n")
