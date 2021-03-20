# Affichage du nombre de fichiers et de dossiers par rapport à un chemin donné

```python
import os

name_dir = []
name_file = []
rep = "/etc/apt/"

for ocu in os.listdir(rep):
    if os.path.isdir(rep + ocu):
        name_dir.append(rep + ocu)
    elif os.path.isfile(rep + ocu):
        name_file.append(rep + ocu)
    else:
        print("Fichier non reconnu :", rep + ocu)

nb_dir = len(name_dir)
nb_file = len(name_file)

print("Il y a", nb_dir, "dossiers")
print("Les dossiers : \n", name_dir)
print("\n")
print("Il y a", nb_file, "fichiers")
print("Les fichiers : \n", name_file)
```

Résultat :
```python
Il y a 5 dossiers
Les dossiers : 
 ['/etc/apt/auth.conf.d', '/etc/apt/apt.conf.d', '/etc/apt/sources.list.d', '/etc/apt/preferences.d', '/etc/apt/trusted.gpg.d']


Il y a 4 fichiers
Les fichiers : 
 ['/etc/apt/trusted.gpg~', '/etc/apt/sources.list', '/etc/apt/sources.list.save', '/etc/apt/trusted.gpg']
>>> 
```