
# Des attributs inscrits directement dans une classe

Définir des attributs directement dans la classe permet de simplifier nos objets quand il, doivent tous avoir certaines données identiques.

Exemple d'une classe qui permet de compter le nombre d'objets créés :
```python
class compteur:  
    objets = 0  
  def __init__(self):  
        compteur.objets += 1
```   
  Instanciation :
```python
object_un = compteur()
```
Affichage du nombre d'objets :
```python
print(object_un.objets)
```
Résultats :
```python
>>> 1
```
Instanciation 2 :
```python
object_deux = compteur()
```
Affichage du nombre d'objets :
```python
print(object_deux.objets)
```
Résultats :
```python
>>> 2
```
