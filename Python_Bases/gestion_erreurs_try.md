# try pour la gestion des erreurs

Cette commande est à utiliser quand nous savons qu'une commande peut renvoyer une erreur.

Cette commande permet de prendre en charge certaines exceptions, et de mener des action selon les exceptions obtenues.

Nous pouvons avoir deux types d'erreurs :
* Les erreurs de syntaxe.
* Les erreurs d’exception, même si la syntaxe du code est bonne.

Exemple de procédure :

1. On va exécuter notre code sans try pour voir quel est le type d'exception :

```python
poids = int(input("Votre poids : "))

# Résultat :

Votre poids : bonjour
Traceback (most recent call last):
  File "/home/daniel/PycharmProjects/p_0/main2.py", line 1, in <module>
    poids = int(input("Votre poids : "))
ValueError: invalid literal for int() with base 10: 'bonjour'

Process finished with exit code 1

``` 

On peut voir que l’exception est de type "ValueError" car on a essayé de transformer une string en entier, pour pouvoir gérer cette exception dans notre code on va utiliser try :

```python

poids = ''

try:
    poids = int(input("Votre poids : "))   # On essaye cette commande
except ValueError:
    print(f"Erreur d'assignation, la valeur à saisir doit être un entier !")   # Si erreur: ValueError alors on fait cette action
else:
    print(f"La variable poids à été correctement assignée avec la valeur {poids} !")   # Si non on fait cette action


``` 

Autre exemple :

```python

nb = int(input('Saisir un nombre : '))
res = 5 / nb

print(f"Le résultat : {res}")


# Résultat :

Saisir un numbre : 0
Traceback (most recent call last):
  File "/home/daniel/PycharmProjects/p_0/main2.py", line 2, in <module>
    res = 5 / nb
ZeroDivisionError: division by zero

Process finished with exit code 1

``` 

Ici on peut voir que l'exception est de type ZeroDivisionError, car on ne peut pas diviser un nombre par 0 :

```python

res = ''

try:
    nb = int(input('Saisir un nombre : '))
except ValueError:
    print(f"Erreur d'assignation, la valeur à saisir doit être un entier !")
else:
    print(f"La variable nb à été correctement assignée avec la valeur {nb} !")
    try:
        res = 5 / nb
    except ZeroDivisionError:
        print("On ne peut pas diviser un nombre par 0 !")
    else:
        print(f"Le résultat est : {res}")

``` 

A noter qu'on peut trouver plusieurs fois except dans une instruction try, mais on peut aussi avoir plusieurs exceptions dans la clause except.