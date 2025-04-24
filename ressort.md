# Exercice : Estimation de la force en fonction de l'allongement (loi de Hooke expérimentale)
## Objectif
Modéliser expérimentalement la relation entre la force appliquée sur un ressort et son allongement, à l’aide d’une interpolation polynomiale basée sur moyenne de mesures répétées.

## Contexte
Lors d’une expérience en laboratoire, un ressort a été soumis à différentes forces, et son allongement a été mesuré **5 fois** pour chaque valeur. ue série a été enregistrée dans un fichier distinct.
Les fichiers sont nommés `ressort_allongement_x.csv`.

## Étapes
1. Charger les données des 5 fichiers CSV (sans utiliser pandas).
2. Afficher sur un même graphique toutes les courbes de mesure (force vs allongement) pour visualiser la variabilité.
3. Calculer la moyenne des allongements pour chaque valeur de force.
4. Afficher la courbe moyenne sur le même graphique.
5. Appliquer une **interpolation polynomiale** à partir de la courbe moyenne uniquement.
6. Tracer la courbe interpolée sur un second graphique.
7. Écrire une fonction `force_estimee(allongement)` qui retourne la force estimée exercée pour un allongement donné.
8. Tester la fonction pour différentes valeurs d’allongement.

## Contraintes
- Ne pas utiliser pandas.
- Utiliser `Polynomial` de `numpy.polynomial`.
- La fonction `force_estimee` doit lever une erreur si l’allongement est hors du domaine des données.
- Afficher un avertissement si l’allongement est hors de l’intervalle mesuré.

## Bonus (facultatif)
- Ajouter une légende pour chaque courbe de mesure.
- Sauvegarder les graphiques.
