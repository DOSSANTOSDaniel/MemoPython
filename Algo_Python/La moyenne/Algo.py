#!/usr/bin/python
# -*- coding: utf-8 -*-

notes=int(input("Combien il y a de notes ? : "))
nom=input("nom de l’élève : ")
liste=[]
somme=0
for k in range(notes):
    ele_note=int(input("note : "))
    liste.append(ele_note)
for z in range(notes):
    somme=somme+liste[z]
total=somme/notes
print("l'élève",nom,"a",total,"de moyenne générale")
