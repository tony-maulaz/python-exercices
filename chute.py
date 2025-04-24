import numpy as np
import matplotlib.pyplot as plt
import random
import csv

MASSE_BALLE = 0.025
K_BALLE = 0.05  # coefficient de frottement

def generer_donnees_chute_csv(fichier, v0_init, dt=0.001):
    """
    Simule la chute d'une balle avec frottements, enregistre dans un CSV,
    et ajoute un bruit gaussien facultatif sur le temps.
    """
    
    hauteurs = np.arange(0, 3.1, 0.25)

    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['hauteur (m)', 'temps (s)'])

        for h in hauteurs:
            g = 9.81
            y = h
            v = v0_init
            t = 0
            bruit_std = 0.01

            while y > 0:
                a = -g - (K_BALLE / MASSE_BALLE) * v
                v += a * dt
                y += v * dt
                t += dt

            t_bruite = t + random.gauss(0, bruit_std)
            writer.writerow([max(0, round(h, 5)), round(t_bruite, 5)])



def lire_donnees_csv(fichier):
    donnees = []
    with open(fichier, 'r') as f:
        next(f)
        for ligne in f:
            h_str, t_str = ligne.strip().split(',')
            donnees.append((float(h_str), float(t_str)))
    return donnees

def simulate_chute(h, k=K_BALLE, g=9.81, dt=0.001):
    """
    Simule la chute d'une balle d'une hauteur h avec frottement de l'air.
    Retourne le temps de chute en secondes.
    """
    v = 0  # vitesse initiale
    y = h  # position initiale
    t = 0  # temps

    while y > 0:
        a = -g - (k / MASSE_BALLE) * v  # accélération avec frottement
        v += a * dt  # mise à jour de la vitesse
        y += v * dt  # mise à jour de la position
        t += dt      # incrément du temps

    return t

generer_donnees_chute_csv("chute_3m.csv", v0_init=0.0)


hauteurs = np.linspace(0, 3, 100)
print("Hauteurs (m):", hauteurs)

temps_simules = [simulate_chute(h) for h in hauteurs]

donnees = lire_donnees_csv('chute_3m.csv')

hauteurs_exp, temps_exp = zip(*donnees)

# Graphe comparaison
plt.plot(hauteurs, temps_simules, label="Simulation")
plt.scatter(hauteurs_exp, temps_exp, color='red', label="Données expérimentales")
plt.xlabel("Hauteur (m)")
plt.ylabel("Temps de chute (s)")
plt.title("Simulation vs Données expérimentales")
plt.grid(True)
plt.legend()
plt.show()