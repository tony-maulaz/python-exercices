import csv
import numpy as np
import matplotlib.pyplot as plt

# --- Chargement des fichiers CSV sans pandas ---
def lire_csv(fichier, colonne_temps, colonne_valeur):
    temps = []
    valeurs = []
    with open(fichier, "r") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            temps.append(float(ligne[colonne_temps]))
            valeurs.append(float(ligne[colonne_valeur]))
    return np.array(temps), np.array(valeurs)

# Fichiers
fichier_tension = "mesure_tension.csv"
fichier_courant = "mesure_courant.csv"

# Lecture des données
temps_V, tension = lire_csv(fichier_tension, "temps_s", "tension_V")
temps_I, courant = lire_csv(fichier_courant, "temps_s", "courant_A")

# --- Interpolation du courant sur les temps de la tension ---
courant_interp = np.interp(temps_V, temps_I, courant)

# --- Calcul de l’impédance (éviter la division par zéro) ---
courant_safe = np.where(courant_interp == 0, np.nan, courant_interp)
impedance = tension / courant_safe

# --- Tracé avec subplot ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Graphique 1 : Tension et courant
ax1.plot(temps_V, tension, label="Tension (V)", color="blue")
ax1.set_ylabel("Tension (V)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")

# Deuxième axe Y pour le courant
ax1b = ax1.twinx()
ax1b.plot(temps_V, courant_interp, label="Courant (A)", color="red")
ax1b.set_ylabel("Courant (A)", color="red")
ax1b.tick_params(axis='y', labelcolor="red")

ax1.set_title("Tension et Courant en fonction du temps")

# Graphique 2 : Impédance
ax2.plot(temps_V, impedance, label="Impédance (Ω)", color="green")
ax2.set_xlabel("Temps (s)")
ax2.set_ylabel("Impédance (Ohms)")
ax2.set_title("Impédance instantanée")
ax2.grid(True)

plt.tight_layout()
plt.show()
