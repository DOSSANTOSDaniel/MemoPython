# Les tuples

## La différence entre tuples et listes

* Quand utiliser des tuples
	- Pour des donnée de différents types.
	
* Quand utiliser des listes
	- Pour des données de même type.

* Le tuple est immuable mais l'itération à travers lui est plus rapide qu'avec une liste.
* Les listes sont modifiables contrairement aux tuples.

Attention, une fois un tuple déclaré on ne peut plus le modifier !

Déclaration d'un tuple :

```python
mon_tuple = ("toto", 5, 456)
``` 

Un tuple existe s'il contient au moins une valeur et une virgule, s'il contient juste une valeur ce n'est pas considéré comme un tuple.

Exemple :

```python
>>> toto = ("bonjour")
>>> type(toto)
<class 'str'>

>>> toto = (5)
>>> type(toto)
<class 'int'>

>>> toto = (5,)
>>> type(toto)
<class 'tuple'>

>>> toto = ("toto", 5)
>>> type(toto)
<class 'tuple'>

``` 

Afficher un élément du tuple :

```python
print(mon_tuple[1])
``` 

On peut afficher les tuples comme les listes c'est un peut près les mêmes propriétés.

