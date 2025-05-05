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

## Code d'aide
```python
fig, ax1 = plt.subplots(figsize=(10, 5))

# Axe Y principal : sin(t)
ax1.plot(t, sin_t, label="sin(t)", color="blue")
ax1.set_ylabel("sin(t)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")
ax1.set_xlabel("Temps (rad)")

ax2 = ax1.twinx()
ax2.plot(t, cos_t, label="cos(t)", color="red")
ax2.set_ylabel("cos(t)", color="red")
ax2.tick_params(axis='y', labelcolor="red")

plt.title("sin(t) et cos(t) sur deux axes Y")

plt.tight_layout()
```

```python
xp = np.array([0, 1, 2, 3])
fp = np.array([0, 1, 0, -1])

x_interp = np.linspace(0, 3, 100)
y_interp = np.interp(x_interp, xp, fp)
```
