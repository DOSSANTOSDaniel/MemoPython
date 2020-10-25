# Les fonctions
- Objectifs :
	1. 	Structurer le code d'un programme en plusieurs petits bouts de code pour rendre le code plus clair et facilement maintenable.
	2. 	Chaque fonction effectue qu'une seule tâche.

- Quand utiliser :
	1. Pour réaliser plusieurs fois la même action au sein d'un programme.

## Syntaxe de base
```Python
def ma_fonction(liste des parametres):
      bloc de code
```
## Fonction sans paramètres
```Python
def ma_fonction():		# Declaration de la fonction
	print("Salut !")

ma_fonction()		# Appel de la fonction
```
Résultat : Salut !
## Fonction avec paramètres
```Python
def ma_fonction(texte):
	print(texte)

ma_fonction("Salut !")
```
Résultat : Salut !

## Autres détails
### L'instruction return dans une fonction
```Python
def ma_fonction():
    calcul = 5 + 5
    return calcul		# La fonction retourne la valeur 10


resultat = ma_fonction() + 10

print(resultat)

```
#### Quand utiliser print ou return dans une fonction ?
Print est une fonction alors que return est une instruction.

Il faut utiliser print pour affiicher une information à l'écran pour un humain.

Il faut utiliser return pour envoyer une valeur dans un point de votre code, envoyer une valeur vers une autre fonction ou vers une variable.
