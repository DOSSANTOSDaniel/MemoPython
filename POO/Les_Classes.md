# Les classes
## C'est quoi une classe ?
Une classe c'est comme un plan de construction, elle permet à partir de ces plans de créer des objets, la classe va donc décrire ce que sera l'objet.
C'est dans la classe qu'on défini les propriétés et les fonctions des objets.

* Dans une classe les propriétés se nomment attributs.
* Dans une classe les fonctions se nomment méthodes.

Pour créer une classe on a besoin :
1. Nom de la classe.
2. De ses attributs (décrit les propriétés de la classe).
3. De ses comportements (décrit les fonctions de la classe).

Quand on crée un objet à partir d'une classe (instanciation).
Il est préférable de mettre chaque classe dans un fichier à part.
Les nom des classes doivent toujours être en CamalCase.

### Déclaration de la classe :
```Python
class Chien
    def __init__(self):
	self.nom = "Licos"
	self.race = "Berger Allemand"
	self.age = "8 ans"
```
Pour définir les attributs d'un objet, il faut définir un constructeur dans la classe.
Un constructeur se défini par la méthode "__init__", cette méthode est appelé à chaque création d'objets.

### Instanciation de la classe (création de l'objet Chien1) :
```
Chien1 = Chien()
```
### Affichage d l'attribut 'nom' de l'objet Chien1
```python
>>>  Chien1.nom
>>>  'Licos'
``` 
### Changer l'attribut 'nom' de l'objet Chien1
```
>>>  Chien1.nom = "Toto"
``` 
