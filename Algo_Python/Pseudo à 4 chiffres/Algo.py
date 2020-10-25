#!/usr/bin/python
# -*- coding: utf-8 -*-

pseudo=input("Saisir un pseudo de 4 chiffres : ")
while (len(pseudo)<4):
    pseudo=input("#Erreur resaisir un pseudo à 4 chiffres# : ")
print("Bonjour [",pseudo,"]")
