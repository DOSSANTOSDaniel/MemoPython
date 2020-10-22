#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nom du projet : WRfile
Auteur(s) :
Version :
Notes : Programme permettant la création, suppression,
modification et affichage d'un fichier texte.
"""

# Programme principal
######################

# Imports de modules
# --------------------
import os

# Variables globales
# --------------------

# Modules / Fonctions
# --------------------
def writeFile(myFile):
    f = open(myFile, "a")
    while True:
        ligne = input("Ecrivez ici, laisser une ligne vide pour quitter")
        if ligne == '':
            break
        f.write(ligne + "\n")
    f.close()

def readFile():
    f = open(myFile, "r")
    texte = f.read()
    print(texte)
    f.close()

def createFile(myFile):
    f = open(myFile, "w")
    f.close()
    print("\n Fichier créé : \n", myFile)

def removeFile(myFile):
    os.remove(myFile)
    print("\n Fichier supprimé ! \n")

# def modifyFile():

# Programme
# --------------------
while True:
    print()
    print("\t\t\t\t __ Menu __")
    print("+--------------------------------------------+")
    print("| Saisir [1] pour créer un fichier texte     |")
    print("| Saisir [2] pour écrire sur un fichier texte|")
    print("| Saisir [3] pour modifier un fichier texte  |")
    print("| Saisir [4] pour lire un fichier texte      |")
    print("| Saisir [5] pour supprimer un fichier texte |")
    print("+--------------------------------------------+ \n")

    chMenu = input("Votre choix : ")
    print()

    FileDoc = input("Sur quel fichier voulez-vous travailler ? : ")
    print()

    while chMenu not in ['1', '2', '3', '4', '5']:
        print("\n Erreur de saissie \n")
        chMenu = input("Votre choix : ")
        print()

    if chMenu == '1':
        print("Création d'un fichier")
        createFile(FileDoc)
    else:
        pass

print("FIN")
