# Une classe avec une méthode  
Les méthodes sont des actions attribuées à un objet.

Voici la création de la méthode texte qui permet d'écrire un texte.
```python
class banniere:
  def __init__(self):
      self.feuille = ""
  def texte(self, message):
      if self.feuille != "":
          self.feuille += "\n"
      self.feuille += message
```
Instanciation de la classe :
```python
ban1 = banniere()
```
Utilisation de la méthode texte pour écrire "Bonjour" :
```python
ban1.texte("Bonjour")
```
Affichage du message :
```python
print(ban1.feuille)
>>> Bonjour
```
