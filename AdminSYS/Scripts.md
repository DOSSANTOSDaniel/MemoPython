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
print("L'argument :", sys.argv[1])

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
parser.add_argument( '--dir', '-d', help='Enter directory name', default='/etc/')
args = parser.parse_args()
d = args.dir

for f in os.listdir(d):
    if os.path.isfile(d + f):
        print(f)
```

