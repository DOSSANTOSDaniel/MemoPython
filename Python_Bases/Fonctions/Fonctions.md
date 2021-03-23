# Les fonctions

- Objectifs :
	1. 	Structurer le code d'un programme en plusieurs petits bouts de code pour rendre le code plus clair et facilement maintenable.
	2. 	Chaque fonction effectue qu'une seule tâche.

- Quand utiliser :
	1. Pour réaliser plusieurs fois la même action au sein d'un programme.

## Syntaxe de base

Pour la création d'une fonction on utilise le mot clé "def" puis on donne un nom à notre fonction.

```Python
def ma_fonction(liste des paramètres):
      bloc de code

```

## Fonction sans paramètres

```Python
def ma_fonction():		# Déclaration de la fonction
	print("Salut !")

ma_fonction()		# Appel de la fonction

#Résultat : Salut !
```

## Fonction avec paramètres

```Python
def ma_fonction(texte):
	print(texte)

ma_fonction("Salut !")

#Résultat : Salut !
```

On peut aussi faire l'appel d'une fonction dans une fonction.

Il est conseillé de ne pas faire plus de 4 imbrications.

## Fonctions avec retour de paramètres

L'instruction return dans une fonction

Attention on ne peut pas avoir plusieurs return dans une fonction !

Exemple :

```Python
def ma_fonction():
    calcul = 5 + 5
    return calcul		# La fonction retourne la valeur 10

print(ma_fonction() + 10) # réutilisation de la valeur de retour de la fonction ma_fonction

#Résultat : 20
```

Quand utiliser print ou return dans une fonction ? :

Print est une fonction alors que return est une instruction.

* Il faut utiliser print pour afficher une information à l'écran destinée à un humain.

* Il faut utiliser return pour envoyer une valeur dans un point de votre code, envoyer une valeur vers une autre fonction ou vers une variable.

## Variables globale et locale dans une fonction

Une fonction peut accueillir des variables à portée globale ou des variables à portée locale.
* Les variables à portée globales sont accessibles sur l'ensemble du code.
* Les variables à portée locales sont propres à chaque fonction et ne sont accessibles que au sein de la fonction.

On peut afficher les variables globales avec la fonction `globals()` et les variables locales avec la fonction `locals()`. 

Exemple de lecture d'une variable globale dans une fonction :

```python
var = 'Salut!'           # Variable globale

def ma_fonction():       # Déclaration
    print(var)

ma_fonction()            # Appel de la fonction
```

Résultat :

```python
Salut!
>>> 
```

Exemple de lecture d'une variable locale et globale :

```python
var = 'Salut !'           # Variable globale

def ma_fonction():

    var = 'Hello !'      # Variable locale
           
    print(var)

ma_fonction()            # Appel de la fonction

print(var)               # Affiche la variable var accessible

```

Résultat :

```python
Hello !
Salut ! # Ici la variable locale est inaccessible alors elle n'écrase pas la variable globale var
>>> 
```

Plus en détail :

```python
var = 'Salut !'           # Variable globale

def ma_fonction():

    var = 'Hello !'       # Variable locale
                        
    print("Variable locale : ", locals())
    print("Variables globales : ", globals())
           
    print(var)

ma_fonction()            # Appel de la fonction

print(var)               # Affiche la variable var accessible

```

Résultat :

```python
Variable locale :  {'var': 'Hello !'}

Variables globales :  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fd06450c220>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/daniel/mu_code/test300.py', '__cached__': None, 'var': 'Salut !', 'ma_fonction': <function ma_fonction at 0x7fd0644f61f0>}

Hello !

Salut !

>>> 

```

On peut transformer une variable locale en variable globale, exemple :

```python
def ma_fonction():
    global var
    var = 'toto'
    print(var)

ma_fonction()

print(var)
```

Résultat :

```python
toto
toto
>>> 
```