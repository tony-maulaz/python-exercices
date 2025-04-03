# Exercice : Estimation de la taille en fonction de l'âge

## Objectif
L'objectif de cet exercice est de modéliser la taille moyenne d'un enfant en fonction de son âge, en utilisant une interpolation polynomiale.
Vous allez travailler à partir de données mesurées pour des garçons et des filles, puis créer une fonction qui permet d'estimer la taille pour un âge donné.

## Contexte
Des données expérimentales ont été recueillies pour mesurer la taille moyenne d'enfants de 2 à 18 ans, séparément pour les garçons (hommes) et les filles (femmes).
Ces données sont stockées dans un fichier `taille_age.csv`.

## Étapes
1. Charger les données depuis le fichier CSV (sans utiliser pandas).
2. Séparer les données en deux groupes : garçons et filles.
3. Créer une figure avec deux sous-graphes (subplots)
4. Afficher les points mesurés sur un graphique (`matplotlib`) pour chaque groupe (homme - femme).
5. Afficher sur le graphique du bas la différence de taille entre les garçons et les filles pour chaque âge.
6. Appliquer une **interpolation polynomiale** sur chaque série (homme - femme).
7. Tracer les courbes interpolées sur le même graphique.
8. Écrire une fonction `taille_estimee(age, sexe)` qui retourne la taille estimée pour un âge et un sexe donnés.
9. Tester la fonction pour différentes valeurs.

## Visualisation avec `subplot`
Utiliser `matplotlib.pyplot.subplot` pour créer deux graphiques superposés :
- **Graphique 1 (en haut)** : courbes de taille (points + interpolation) pour hommes et femmes.
- **Graphique 2 (en bas)** : courbe représentant la différence de taille estimée entre les hommes et les femmes selon l’âge.

## Contraintes
- Ne pas utiliser pandas.
- Utiliser `Polynomial` de `numpy.polynomial`.
- La fonction `taille_estimee` doit lever une erreur si le sexe n’est ni "homme" ni "femme".
- Si on essaie d’estimer la taille pour un âge hors du domaine [2, 18], afficher un message d’avertissement.

## Données
Les données sont dans le fichier `taille_age.csv` au format suivant :

```csv
sexe,age,taille_cm
homme,2,88
homme,4,102
...
femme,16,165
femme,18,167
```

## Bonus (facultatif)
- Afficher les courbes avec des couleurs et styles personnalisés.
- Sauvegarder les graphiques dans un fichier image.