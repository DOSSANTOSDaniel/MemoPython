# Moyenne d’un élève
### Entête
Algorithme de calcul de la moyenne
* Rôle : calculer la moyenne des notes d’un élève
* Entrée : nom de l’élève, les notes de l’élève, 
* Sortie : affiche la moyenne des notes de l’élève, affiche le nom de l’élève
### Langage naturelle

```
Variable : notes (entier), nom (chaîne de caractères), liste (réel), somme (entier), k (entier), ele_notes (entier), total (entier)
Début
   afficher « Combien il y a de notes ? : »
   saisir notes
   afficher « quel est le nom de l’élève ?: »
   saisir nom
   déclarer la liste liste vide
   déclarer la variable somme à 0
   pour k de 0 à notes faire :
      afficher « saisir la note numéro n : »
      saisir ele_note
      ajouter ele_note à la liste liste
   pour z de 0 à notes faire :
      somme=somme+liste[z]
   total=somme/notes
   afficher « l’élève (nom) a (total) de moyenne générale »
Fin
```

### Code python

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

notes = int(input("Combien il y a de notes ? : "))
nom = input("nom de l’élève : ")
liste = []
somme = 0

for k in range(notes):
    ele_note = int(input('Note numéro {} : '.format(k+1)))
    liste.append(ele_note)
    
for z in range(notes):
    somme = somme+liste[z]
    
total = somme/notes
print("l'élève",nom,"a",total,"de moyenne générale")

```

