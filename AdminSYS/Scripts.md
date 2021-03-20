# Scripts en Python

Entête désignant l’interpréteur sur Linux :

```python
#!/usr/bin/env python3
```

Récupération d'arguments :
```python
#!/usr/bin/env python3
import sys
print("Le script :", sys.argv[0])
print("Le premier argument :", sys.argv[1])

```

Résultat :
```bash
[daniel🐧iS3810](~)$ ./script.py Bonjour

Le script : ./script.py
L'argument : Bonjour
```

Gestion des arguments passés :
```python
#!/usr/bin/env python3
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument( '--dir', '-d', help='Saisir le chemin complet du dossier', default='/etc/')
args = parser.parse_args()
d = args.dir

for f in os.listdir(d):
    if os.path.isfile(d + f):
        print(f)
```

Ce code permet de prendre en argument le chemin d'un répertoire avec --d ou -d, puis il va lister seulement les fichiers contenue dans ce répertoire.

Exemple :
```bash
┌──[daniel🐧iS3810]-(~/mu_code)
│
└─$ python3 test.py --dir /home/daniel/

.face
.profile
.bashrc.bak
.xboardrc
.cardpeek.log
.Xauthority
.python_history
scriptapp.txt
.bash_logout
.bash_history
toto.txt
.xsession-errors
.gtk-bookmarks
.bashrc
.sudo_as_admin_successful
.gitconfig
.mtoolsrc
config3.ini
.viminfo
.vimrc
.gtkrc-2.0
.multisystem-theme
.fonts.conf
.psql_history
```
