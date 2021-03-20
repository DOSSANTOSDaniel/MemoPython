# Édition et création de fichiers de configuration au format INI

Création des fichiers de configuration :
```Python
file_1 = open("/home/daniel/config.ini", "a+") # ouverture et écriture du fichier sans écraser l'existant

file_1.writelines("[User] \n")
file_1.writelines("name : 'daniel' \n")
file_1.writelines("password : '1234' \n")
file_1.close() # fermeture du fichier

file_1 = open("/home/daniel/config.ini", "r") # lecture du fichier
print(file_1.read())
file_1.close() # fermeture du fichier
```

Résultat :
```
 [User]
 name : 'daniel'
 password : '1234'
```

## Utilisation du module configparser

Création du fichier de configuration :
```python
import configparser

config = configparser.ConfigParser()
config['Host'] = {'IP': "'192.168.0.21'",
                  'Name': "'Proxmox'",
                  'Size': "'1 To'"}

file_1 = open("/home/daniel/config3.ini", "a+")
config.write(file_1)
file_1.close()
```

Résultat :
```
[Host]
ip = 192.168.0.21
name = Proxmox
size = 1 To
```

Affichage d’éléments de configuration :
```python
config = configparser.ConfigParser()
config.read('/home/daniel/config.ini')
print(config.sections()) # affichage des sections exemple : [Users]
print(config.get('Users', 'name')) # affichage d'une donnée en particulier appartenant à la section User
```

Éditer les paramètres :
```python
config = configparser.ConfigParser()
config.read('/home/daniel/config3.ini')

file_1 = open("/home/daniel/config3.ini", "r+")
config.set('Host', 'IP', "'192.168.0.222'")
config.write(file_1)
file_1.close()
```

Ajouts de nouveaux paramètres :
```python
config = configparser.ConfigParser()
config.read('/home/daniel/config3.ini')

file_1 = open("/home/daniel/config3.ini", "r+")
config.set('Host', 'Type', "'server'")
config.write(file_1)
file_1.close()
```

Ajouter une section avec la méthode add_section() :
```python
config = configparser.ConfigParser()
config.read('/home/daniel/config3.ini')

file_1 = open("/home/daniel/config3.ini", "r+")
config.add_section('Vms')
config.set('Vms', 'name', 'vm1')
config.write(file_1)
file_1.close()
```