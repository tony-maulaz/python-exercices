import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# --- Chargement CSV sans pandas ---
def lire_csv(fichier, colonne_temps, colonne_valeur):
    temps = []
    valeurs = []
    with open(fichier, "r") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            temps.append(float(ligne[colonne_temps]))
            valeurs.append(float(ligne[colonne_valeur]))
    return np.array(temps), np.array(valeurs)

# Chargement des données
temps_V, tension = lire_csv("mesure_tension.csv", "temps_s", "tension_V")
temps_I, courant = lire_csv("mesure_courant.csv", "temps_s", "courant_A")

# --- Ajustement d'un polynôme sur le courant ---
poly_courant = Polynomial.fit(temps_I, courant, deg=5)
courant_poly = poly_courant(temps_V)  # courant évalué aux temps de la tension

# --- Calcul de l’impédance ---
courant_safe = np.where(courant_poly == 0, np.nan, courant_poly)
impedance = tension / courant_safe

# --- Tracé avec subplot ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Graphique 1 : Tension et courant (modélisé)
ax1.plot(temps_V, tension, label="Tension (V)", color="blue")
ax1.set_ylabel("Tension (V)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")

# Deuxième axe Y pour courant modélisé
ax1b = ax1.twinx()
ax1b.plot(temps_V, courant_poly, label="Courant (modèle)", color="orange")
ax1b.set_ylabel("Courant (A)", color="orange")
ax1b.tick_params(axis='y', labelcolor="orange")

ax1.set_title("Tension et Courant modélisé")

# Graphique 2 : Impédance
ax2.plot(temps_V, impedance, label="Impédance (Ω)", color="green")
ax2.set_xlabel("Temps (s)")
ax2.set_ylabel("Impédance (Ohms)")
ax2.set_title("Impédance calculée à partir du modèle")
ax2.grid(True)

plt.tight_layout()
plt.show()
