# Affichage et édition de fichiers texte

Lire un fichier texte :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture seule
in_file = file_1.read() # lecture du contenu du fichier

print(in_file) # affichage du contenu

file_1.close() # fermeture du fichier
```

Autre méthode pour lire un fichier :
```python
with open('/home/daniel/toto.txt') as of:
    lines = of.readlines()

for ln in lines:
    print(ln)

```

Rechercher une occurrence dans un texte :
```python
ocu = 'Bonjour'

with open('/home/daniel/toto.txt') as of:
    lines = of.readlines()

for ln in lines:
    if ocu in ln:
        print("Occurrence :", ocu)
        print("Ligne :", ln)
    else:
        print("Non trouvé !")
```

Lire une partie des caractères d'un fichier texte :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture
in_file = file_1.read(10) # lecture de 10 caractères

print(in_file) # affichage du contenu

file_1.close() # fermeture du fichier
```

Lire ligne par ligne :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture
count = ""
while True:
    line = file_1.readline()
    if line == "":
        break
    
    count = count + line

print(count)

file_1.close() # fermeture du fichier
```

Lire ligne par ligne (autre méthode) :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture seule

line = file_1.readlines() # Attention il y a un S "readlines"

print(line[0])
print(line[1])

file_1.close() # fermeture du fichier
```

Compter le nombre de lignes dans un fichier texte :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture seule

line = file_1.readlines() 

print(len(line))

file_1.close() # fermeture du fichier
```

Lecture avec plus de précision :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture seule

line = file_1.readlines()[1] # Récupération de la deuxième ligne

char_target = line[16:23] # récupération du caractère 16 au 23

print(char_target)

file_1.close() # fermeture du fichier
```

Lecture à partir d'une certaine position :
```Python
file_1 = open("/home/daniel/toto.txt", "r") # ouverture du fichier en lecture seule

file_1.seek(8) # Lire à partir du caractère 8

print(file_1.read())

file_1.close() # fermeture du fichier
```

Lecture et écriture à partir d'une certaine position :
```Python
file_1 = open("/home/daniel/toto.txt", "r+") # ouverture et écriture du fichier sans écraser l'existant

file_1.seek(16) # Lire à partir du caractère 16

file_1.write("Salut") # rajouter Salut à partir de la position 16
file_1.seek(0)
print(file_1.read())

file_1.close() # fermeture du fichier
```

Traitement du texte :

| Options | Description |
|:--:|:--:|
| a | "append" ajouter à la fin du fichier et crée le fichier s'il n'existe pas |
| w | "write" écrase le contenue existant et crée le fichier s'il n'existe pas |
| r+ | "read" lecture et écriture sans écraser le contenu existant |
| x | "create" crée un fichier, si le fichier existe déjà alors une erreur sera renvoyée |


Ajouter du texte et afficher :
```Python
file_1 = open("/home/daniel/toto.txt", "a") # ouverture et écriture du fichier sans écraser l'existant
file_1.write("Fin du paragraphe !") # rajouter du texte
file_1.close() # fermeture du fichier
#lecture
file_1 = open("/home/daniel/toto.txt", "r") # ouverture et écriture du fichier sans écraser l'existant
print(file_1.read())
file_1.close() # fermeture du fichier
```

Simple exemple de création de fichier :
```python
file_2 = open("Bonjour.txt", "x")
```