# Exercice : Temps de chute d'une balle avec frottements de l'air

## Contexte
Dans un projet, il est nécessaire de pouvoir estimer le temps de chute d'une balle en fonction de sa hauteur et de sa vitesse initiale afin de prédire le moment où elle touchera le sol.

Une série de mesure a été effectuée pour estimer le temps de chute d'une balle en fonction de sa hauteur. Ces mesures ont été prises dans un environnement où la résistance de l'air est significative.

Lors des mesures, la balle a été lâchée (vitesse initiale nulle) d'une certaine hauteur et le temps qu'elle a mis à toucher le sol a été enregistré. Ces données sont disponibles dans un fichier CSV.

## Objectif
Le but de cet exercice est de calculer de manière **itérative** le temps que met une balle à tomber d'une certaine hauteur, en prenant en compte les frottements de l'air.
Vous devrez également **interpoler les données mesurées** pour pouvoir estimer le temps de chute pour d'autres hauteurs.
À la fin, vous devrez construire une **fonction** qui retourne le temps de chute d'une balle en fonction de la hauteur (en m) et de la vitesse initiale.

## Contraintes
- Vous ne devez **pas utiliser pandas**
- La chute est **verticale**
- La vitesse initiale dans les mesures est **nulle**

## Approche de la simulation (avec frottements)
1. On simule la chute de la balle **étape par étape (itérativement)**, en petits intervalles de temps $\Delta t$
2. À chaque étape, on met à jour la **vitesse** et la **position**
3. La **force** est :
    $F = m * a$
4. Vous arrêtez la boucle quand la position atteint 0 (la balle touche le sol)

5. On ajoute une **force de frottement** proportionnelle à la vitesse :

    $F_{frottement} = -k * v$

   avec $k$ une constante de frottement à définir (ex : 0.1)


## Partie 1 : Simulation itérative
- Écrire une fonction `simulate_chute(h)` qui retourne le temps de chute total.
- Créer un vecteur `hauteurs` contenant les hauteurs de 0 à 1 m
- Pour chaque hauteur, simuler la chute et stocker le temps de chute dans une liste
- Créer un graphe avec matplotlib pour afficher le temps de chute en fonction de la hauteur

## Partie 2 : Données expérimentales
- Un fichier `chute.csv` vous est fourni avec deux colonnes : hauteur (en m), temps mesuré (en s)
- Charger les données dans une liste de tuples (hauteur, temps)
- Afficher les données sur un graphe
- Comparer la forme de la courbe avec celle obtenue par simulation

### Valeurs physiques
- Masse de la balle : 25 g
- Accélération de la gravité : 9.81 m/s²

## Partie 3 : Calcul du temps de chute
- Écrire une fonction `temps_de_chute(h, v0)` qui retourne le temps de chute pour une hauteur donnée et une vitesse initiale.
