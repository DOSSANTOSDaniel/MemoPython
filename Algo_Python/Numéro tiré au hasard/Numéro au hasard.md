# Devine un numéro tiré au hasard
### Entête
Algorithme jeu de hasard
* Rôle : jeux servant à tenter de deviner des chiffres sélectionnés au hasard
* Entrée : nombre au hasard, nombre choisi par l’utilisateur
* Sortie : nombre d’essais avant de trouver, si un des deux chiffres et bon, affiche (gagné si trouver)
### Langage naturelle
<pre><code>
Variable :k, nb_hasard, nb_choisi, essai,  bonnes_rep
Début
   nb_hasard= entier au hasard entre 10 et 20
   afficher « saisir un nombre à 2 chiffres »
   saisir nb_choisi
   essai=1
   tant que nb_choisi est différent de nb_hasard faire :
      bonnes_rep=0
      pour k de 0 à 2 faire :
         si nb_hasard[k]==nb_choisi[k] alors
            bonnes_rep=bonnes_rep+1
         fin si
      fin pour
   afficher « il y a bonnes_rep chiffre(s) correct(s) recommencer ! : »
   saisir nb_choisi
   essai=essai+1
   fin de tant que
   afficher Bravo le nb_choisi est le nombre hasard !, trouvé en essai, !
Fin
</code></pre>
