# Système d'exploitation et autres tâches
## Utilisant le module os
Affiche l'utilisateur courent :
```Python
import os

user = os.getlogin()

print(user)
```

Création d'un répertoire :
```Python
os.mkdir("/home/daniel/dossier_1")
```

Affiche le répertoire courant :
```Python
current_dir = os.getcwd()

print(current_dir)
```

Vérifier si un répertoire existe :
```Python
if os.path.exists("/home/daniel/dossier"):
    print("Le dossier existe déjà !")
else:
    print("Le dossier n'existe pas !")
```

Tester si c'est un répertoire ou un fichier :
```Python
test_directory = "/home/daniel/dossier_toto"

if os.path.isdir(test_directory):
    print("C'est un dossier")
elif os.path.isfile(test_directory):
    print("C'est un fichier")
else:
    print("Type de fichier non pris en charge")
```

Affiche le chemin absolu courant :
```Python
abs_dir = os.path.abspath(".")

print(abs_dir)
```

Afficher le dossier parent :
```Python
dir_1 = "/home/daniel/file/video.mp4"
p_dir = os.path.dirname(dir_1)
print(p_dir)
```

Afficher la partie fichier du chemin :
```Python
dir_1 = "/home/daniel/file/video.mp4"
p_dir = os.path.basename(dir_1)

print(p_dir)
```

Lister le contenu d'un dossier :
```Python
dir_1 = "/home/daniel"
list_dir = os.listdir(dir_1)

print(list_dir)
```

Lister le contenu d'un dossier (autre manière) :
```Python
dir_1 = "/home/daniel"
for i in os.scandir(dir_1):
    print(i)
```

## Utilisant le module glob
Lister un certain type de fichiers :
```Python
dir_1 = "/home/daniel"
list_dir = glob.glob("/home/daniel/*.png")

print(list_dir)
```

