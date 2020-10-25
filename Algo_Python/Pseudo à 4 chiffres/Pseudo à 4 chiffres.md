# Pseudo à 4 chiffres
### Entête
Algoritme pseudo
* Rôle : obtenir un pseudo correct puis afficher bonjour {pseudo}
* Entrée : pseudo de l’utilisateur
* Sortie : message (bonjour {pseudo})

### Langage naturel
<pre><code>
Variables: pseudo (chaîne)
Début
   afficher « saisir un pseudo à 4 chiffres »
   saisir pseudo
   tant que la longueur de pseudo est inférieur à 4 faire :
      afficher « Erreur ressaisir un pseudo à 4 chiffres »
      saisir pseudo
   fin de tant que
   afficher « bonjour {pseudo} »
Fin
</code></pre>
