# Vérifie si un utilisateur est pèsent sur le système

```python
import pwd
# Compatible seulement sur des systèmes de type UNIX (pwd)

def if_user_exist(user):
    try:
        pwd.getpwnam(user)
    except ValueError:
        print(user, "ne fait pas partie des utilisateurs du système !")
    else:
        print(user, "fait partie des utilisateurs du système !")


if_user_exist('toto')
```