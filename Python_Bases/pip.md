# Le gestionnaire de paquets PIP

## Installation

```Python
sudo apt install python3-pip
```

Afficher l'aide de la commande pip

```Python
pip --help
```

## Migration des dépendances

Quand on transfère notre projet python d'une machine vers une autre, on doit aussi importer les dépendances.

Pour faire un backup des dépendances :

```Python
pip freeeze > dep.txt
```

Pour les importer sur la nouvelle machine il faut les réinstaller :

```Python
pip install -r dep.txt
```

## La mise à jour

Mettre à jour de tous les paquets

```Python
pip list --format=legacy --outdated | cut -d '' -f1 | xargs pip install --upgrade
``` 

xargs permet d’itérer sans avoir besoin de for.
