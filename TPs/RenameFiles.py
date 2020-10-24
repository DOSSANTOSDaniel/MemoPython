#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nom du projet : RenameFiles
Auteur(s) :
Version : 0
Notes : Ce programme va permettre de renomer
de multipless fichiers en même temps.
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
countIter = 0

# Modules / Fonctions
# --------------------

def rename(chemin, texte):
    countIter = 0
    for root, dirs, files in os.walk(chemin):
        for fichier in files:
            listeFiles.append(os.path.join(root, fichier))

    for file in listeFiles:
        countIter += 1
        extent = os.path.splitext(file)[1]
        print(extent)
        docPath =  os.path.split(file)[0]
        print(docPath)
        print(file)
        os.rename(file, docPath + '/' + texte + '_' + str(countIter) + extent)

# Programme
# --------------------

while True:

    print("\n\t\t\t __ Menu __")
    print("*************************************")
    print("Saissir le chemin absolu d'un dossier")
    print("Exemple : ")
    print("Saisir le chemin : /home/daniel")
    print("*************************************\n")

    chemin = input("Saisir le chemin : ")

    if os.path.isdir(chemin):
        pass
    else:
        print("Erreur de syntaxe")
        continue

    print("\n Saisir un texte si besoin pour renomer les fichiers")
    print("dans le cas contraire le texte par défaut [file] sera appliqué.")
    print("Modèle de nom : [texte]_[nombre].[extention]")
    texte = input("Saisir Texte : ")

    if len(texte) == 0:
        texte = 'file'

    rename(chemin, texte)

print("\n Fin du Programme RenameFiles \n")