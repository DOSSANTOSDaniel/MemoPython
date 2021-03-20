
# Boucle for

Une boucle for permet de répéter une action un nombre de fois déterminé.

Exemple :

```python
for i in range(5):
    print(i)

0
1
2
3
4

```

| Paramètres | Description |
|:--|:--|
| range(5) | C'est une liste de chiffres de 0 à 5 exclut |
| i | Représente chaque chiffre à chaque tour de la boucle, c'est une variable locale |


Paramètres de range

Exemple :

```python
for i in range(10, 20, 2):
    print(i)


10
12
14
16
18

```

```
range(10, 20, 2)
       |   |  |
       |   |  +-----> le pas (de 2 en 2)
       |   +--------> Valeur de fin
       +------------> Valeur de départ
```  

Autre exemple, énumération d’éléments d'une liste :

```python
liste = ["Daniel", "Olivier", "Nicolas"]

for i in liste:
    print(i)

Daniel
Olivier
Nicolas

```

### Utiliser les instructions break et continue

Le break ici permet d'arrêter la boucle quand i est égal à 5 :

```python
for i in range(10):
    if i == 5:
        break
    print(i)

0
1
2
3
4

```

Le continue ici permet de continuer la boucle sans afficher le 5, il affiche les chiffres de 0 à 10 exclut sans afficher le 5.

```python
for i in range(10):
    if i == 5:
        continue
    print(i)

0
1
2
3
4
6
7
8
9

```


