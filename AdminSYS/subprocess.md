# Le module subprocess permet de passer des commandes directement au système d'exploitation, (windows ou Linux/Unix)

```python

import subprocess

if subprocess.run(["ls", "-la"]):
    print("ok")

```
