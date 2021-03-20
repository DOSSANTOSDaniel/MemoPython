# Les listes

## La différence entre tuples et listes

* Quand utiliser des tuples
	- Pour des donnée de différents types.
	
* Quand utiliser des listes
	- Pour des données de même type.

* Le tuple est immuable mais l'itération à travers lui est plus rapide qu'avec une liste.

* Les listes sont modifiables contrairement aux tuples.


Syntaxe, création d'une liste :

```python
ma_liste = []
``` 

Ajout d'éléments :

```python
ma_liste.append("toto")

``` 

Afficher un élément de la liste en particulier :

```python
print("Le deuxième élément est : ", ma_liste[1])

``` 

Supprimer une entrée à l'aide de son index :

```python
del ma_liste[1]

```  

Supprimer une entrée à l'aide de sa valeur :

```python
ma_liste.remove("toto")

``` 

Inverser les valeurs d'une liste :

```python
ma_liste.reverse()

``` 

Compter le nombre d'items dans notre liste :

```python
print(len(ma_liste))

``` 

Compter le nombre d’occurrences concernant une valeur en particulier :

```python
print(ma_liste.count("toto"))

``` 

Afficher l'index correspondant à une certaine valeur :

```python
print(ma_liste.index("toto"))

``` 

Afficher la dernière occurrence de la liste :

```python
print(ma_liste[-1])

# On peut aussi déterminer des plages [2:5]

``` 

Vérifier si la liste contient une occurrence donnée :

```python
print("toto" in ma_liste)

# Résultat : True/False

``` 

Affichage des occurrences de la liste à l'aide de for :

```python
for i in enumerate(ma_liste):
    print(i)

``` 

Il est aussi possible d'avoir des listes à l'intérieur d'autres listes.