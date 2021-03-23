# La fonction lambda
Cette fonction permet d'écrire des fonctions en une seule ligne.

Exemple :

```python
speed_fonction = lambda nb : nb+5  # Déclaration de la fonction

print(speed_fonction(6))           # Affichage et appel de la fonction

```

Résultat :

```python
11
>>> 
```

En détail :

```python
speed_fonction = lambda nb : nb+5  # Déclaration de la fonction
#       ^          ^     ^     ^
#       |          |     |     |
#[Nom]--+          |     |     | 
#                  |     |     |
#[type]------------+     |     |
#                        |     |
#[Paramètre d'entrée]----+     |
#                              |
#[Paramètre de retour]---------+
```

Même fonction sans lambda :

```python
def speed_fonction(nb):          # Déclaration de la fonction
    return nb+5
    
print(speed_fonction(5))         # Affichage et appel de la fonction

```

Résultat :

```python
10
>>> 
```

Il n’y a aucune différence entre les fonctions lambda et les autres fonctions, c'est juste la syntaxe qui change. 
