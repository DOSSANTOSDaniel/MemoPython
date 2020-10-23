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
        ligne = input("Ecrivez ici, laisser une ligne vide pour quitter : ")
        if ligne == '':
            break
        f.write(ligne + "\n")
    f.close()

def readFile(myFile):
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

def modifyFile(myFile):
    nbLines = 0

    f = open(myFile, 'r')
    listeLines = f.readlines()
    f.close()

    for i in listeLines:
        nbLines = int(nbLines) + 1
        print("Ligne :", nbLines, ">", i)

    print()
    changeLine = input("Numéro de ligne à changer : ")
    changeLine = int(changeLine) - 1

    newLine = input("Ecrire dans la nouvelle ligne : ")

    listeLines.remove(listeLines[changeLine])
    listeLines.insert(changeLine, newLine + "\n")

    f = open(myFile, "w")
    f.truncate()
    f.close()

    f = open(myFile, "a")
    f.writelines(listeLines)
    f.close()

    print("\n Sauvegarde effectué \n")


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

    chMenu = '0'
    while chMenu not in ['1', '2', '3', '4', '5']:
        chMenu = input("Votre choix : ")
        print()

    FileDoc = input("Sur quel fichier voulez-vous travailler ? : ")
    print()

    if chMenu == '1':
        print("\n Création d'un fichier \n")
        createFile(FileDoc)
    elif chMenu == '2':
        print("\n Mode écriture \n")
        writeFile(FileDoc)
    elif chMenu == '3':
        print("\n Mode modification \n")
        modifyFile(FileDoc)
    elif chMenu == '4':
        print("\n Mode lecture \n")
        readFile(FileDoc)
    elif chMenu == '5':
        print("\n Suppression d'un fichier \n")
        removeFile(FileDoc)
    else:
        print("\n Erreur de saissie ! \n")