# Exercice : Analyse d’un signal électrique

## Objectif
Analyser des signaux électriques mesurés : tension et courant en fonction du temps, et en déduire l'impédance du système.

## Contexte
Deux fichiers de mesures ont été fournis :
- `mesure_tension.csv` : tension mesurée en volts (V) en fonction du temps (s)
- `mesure_courant.csv` : courant mesuré en ampères (A) en fonction du temps (s)

Les mesures de tension et de courant n’ont **pas été prises aux mêmes instants**.

## Étapes
1. Charger les deux fichiers CSV **sans utiliser pandas**.
2. Afficher la tension et le courant sur **un même graphique** :
   - Axe Y gauche : tension (en volts)
   - Axe Y droite : courant (en ampères)
   - Axe X : temps (en secondes)

3. Interpoler les données pour calculer l'impédance :
   - Utiliser une interpolation linéaire pour approximer les valeurs de courant aux temps de la tension.
   - Calculer l’impédance instantanée : `Z(t) = V(t) / I(t)` (attention à éviter la division par zéro).

4. Afficher la courbe de l’impédance en fonction du temps sur un **second graphique** (sous le premier) grâce à `matplotlib.pyplot.subplot`.

## Contraintes
- Ne pas utiliser pandas.
- Utiliser `numpy` et `matplotlib`.
- Vérifier que le courant n’est pas nul avant de diviser.

## Bonus
- Ajouter une couleur différente pour chaque courbe.
- Ajouter un titre, des labels, et une légende.
- Sauvegarder les figures en image.
