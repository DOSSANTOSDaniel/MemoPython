# Affichage des utilisateurs du système possédant un shell

```python
import pwd  # affiche les entrées du fichier /etc/passwd
import re   # permet d'utiliser les regex

pfile = pwd.getpwall()

for i in pfile:
    match = re.search(r'sh\Z', i.pw_shell)       # vérification regex 
    if match:
      print(f"Utilisateur : {i.pw_name} --- Shell : {i.pw_shell}")

``` 
