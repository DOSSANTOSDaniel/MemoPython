# La structure conditionnelle IF

IF permet de tester plusieurs conditions en les comparent à un état désiré puis permet d'entreprendre des actions selon l'état vérifié.

```python
personne_autorisee = "Daniel"
prenom = input("Votre prénom : ")

if prenom == personne_autorisee:
    print("Vous pouvez passer !")
else:
    print("Vous n'êtes pas autorisé à entrer !")

```

La ligne qui commence par "if" compare si la valeur de la variable "prenom" est identique à la valeur de la variable "personne_autorisee", si c'est le cas alors on indique les actions à faire dans ce cas là.

Si les valeurs des deux variable ne sont pas identiques alors on passe à la ligne qui commence par "else" puis on indique les actions à effectuer dans ce cas là. 

Autre exemple plus complet :

```python
eleve = 'Ana'

if eleve == 'Ana':
    print(eleve, "est présente")
elif eleve == 'Clair':
    print(eleve, "est présente")
elif eleve == 'Sophie':
    print(eleve, "est présente")
else:
    print(eleve, "ne fait pas partie des éleves de cette classe !")
```

| Condition | Description |
|:--|:--|
| if | Si la condition est ... |
| elif | Si non si la condition est ... |
| else | Si non alors c'est ... |

Tableau des différents comparateurs

| Comparateur | Description |
|:--|:--|
| ==  ou is | égal |
| != ou is not | différent |
| < | plus petit |
| > | plus grand |
| <= | plus petit ou égal |
| >= | plus grand ou égal |

Les opérateurs logiques

| Opérateur | Description |
|:--|:--|
| and | et |
| or | ou |

Les opérateurs logiques permettent de combiner plusieurs conditions en une seule ligne.

Exemple :

```python
age = 32

if age >= 18 and age < 60:
    print("Vous êtes un adulte")
elif age > 5 and age <= 17:
    print("Vous êtes enfant")
elif age < 5:
    print("Vous êtes un bébé")
else:
    print("Vous êtes un vieux")

```

Ce code peut être encore plus simplifié :

On peut transformer :

```python
if age >= 18 and age < 60:
```

En :

```python
if 18 <= age < 60:
```

Exemple :

```python

age = 32

if 18 <= age < 60:
    print("Vous êtes un adulte")
elif 5 < age <= 17:
    print("Vous êtes enfant")
elif age < 5:
    print("Vous êtes un bébé")
else:
    print("Vous êtes vieux")
```



