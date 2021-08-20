# Les environnements virtuels

Permet de mieux gérer les dépendances de chaque projet en les isolant dans un environnement propre au projet.

Installation

```Python
pip install virtualenv
```

Création d'un nouveau projet

```Python
virtualenv <nom_de_projet>
```

On vient de créer un environnement de développement exclusivement pour notre projet.

Activation de l'environnement

```Python
source <nom_de_projet>/bin/activate
```

Pour sortir de cet environnement 

```Python
source <nom_de_projet>/bin/deactivate
```

Pour modifier la version de python utilisée dans l'environnement 

```Python
virtualenv --python /usr/bin/python3 <nom_de_projet>

source <nom_de_projet>/bin/activate
```

Chaque environnement va contenir ses propres dépendances.

Lister les dépendances dans un environnement  

```Python
pip list
```
