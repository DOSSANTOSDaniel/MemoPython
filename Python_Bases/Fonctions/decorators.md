# Les décorators

Il permet d’étendre une fonction sans pour autant changer son code.

On ajoute des fonctionnalités à la fonction sans la modifiée.

Exemple :

```Python
# le decorator
def deco(ma_fonction):
    print("Information : ")
    return ma_fonction
    
# la fonction décorée
@deco
def ma_fonction():
    return "Il pleut"
    
print(ma_fonction())

# résultat
Information : 
Il pleut
>>> 
```

La fonction ma_fonction à été décorée dans le but de lui ajouter "information : ".