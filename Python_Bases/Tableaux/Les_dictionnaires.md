# Les dictionnaires

Syntaxe pour déclarer un dictionnaire :

```python
mon_dict = {}
``` 

Déclarer un dictionnaire avec des valeurs :

```python
mon_dict = {}

mon_dict["nom"] = ("daniel", "hamza")
#         ^           ^         ^
#         |           |         |
# [Clés]--+           +---+-----+
#                         |
# [Occurrences]-----------+
``` 

Afficher le dictionnaire :

```python
print(mon_dict)

{'nom': ('daniel', 'hamza')}

``` 

Afficher seulement les occurrences correspondantes à la clé "nom" :

```python
print(mon_dict["nom"])
``` 

Afficher les clés :

```python
print(mon_dict.keys())
```  

Afficher les valeurs :

```python
print(mon_dict.values())
```  

Autre manière de déclarer un dictionnaire

```Python
mon_dict = { "Fruit": "pomme", "voiture": "roues" }
                ^        ^          ^        ^  
                |        |          |        |
clés -----------+--------|----------+        |
                         |                   |
Valeurs -----------------+-------------------+
```

Supprimer un couple clés valeurs

```Python
del mon_dict["voiture"]
```

Afficher les différents éléments

```Python
print(mon_dict.items())
```