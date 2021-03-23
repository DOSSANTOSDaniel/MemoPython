# Les expression régulières

Permet de valider ou pas une correspondance entre deux valeurs.

Exemple :
 
```python

import re

var = "Bonjour"

if re.search("^B*", var):
    print("Valide")
else:
    print("non valide")

```