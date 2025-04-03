import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Chargement des données depuis un fichier CSV (sans pandas)
def lire_donnees(fichier):
    hommes = []
    femmes = []
    with open(fichier, "r") as f:
        reader = csv.reader(f)
        next(reader)  # sauter l'en-tête
        for row in reader:
            sexe, age, taille = row[0], int(row[1]), float(row[2])
            if sexe == "homme":
                hommes.append((age, taille))
            elif sexe == "femme":
                femmes.append((age, taille))
    return hommes, femmes

# Fichier de données
fichier = "taille_age_50.csv"

# Lecture
hommes, femmes = lire_donnees(fichier)
ages_h, tailles_h = zip(*hommes)
ages_f, tailles_f = zip(*femmes)

# Moyenne des tailles par âge pour interpolation (utile si plusieurs par âge)
def moyenne_par_age(ages, tailles):
    d = {}
    for a, t in zip(ages, tailles):
        d.setdefault(a, []).append(t)
    ages_uniques = sorted(d.keys())
    tailles_moyennes = [np.mean(d[a]) for a in ages_uniques]
    return np.array(ages_uniques), np.array(tailles_moyennes)

ages_h_uni, tailles_h_moy = moyenne_par_age(ages_h, tailles_h)
ages_f_uni, tailles_f_moy = moyenne_par_age(ages_f, tailles_f)

# Interpolation polynomiale degré 3
poly_h = Polynomial.fit(ages_h_uni, tailles_h_moy, deg=3)
poly_f = Polynomial.fit(ages_f_uni, tailles_f_moy, deg=3)

# Fonction d’estimation
def taille_estimee(age, sexe):
    if not 2 <= age <= 18:
        print("⚠️  Âge hors plage de mesure (2 à 18 ans)")
    if sexe == "homme":
        return poly_h(age)
    elif sexe == "femme":
        return poly_f(age)
    else:
        raise ValueError("Sexe inconnu : utiliser 'homme' ou 'femme'")

# Affichage avec subplots
ages_interp = np.linspace(2, 18, 200)
taille_h_interp = poly_h(ages_interp)
taille_f_interp = poly_f(ages_interp)
diff_interp = taille_h_interp - taille_f_interp

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Graphique 1 : tailles
ax1.scatter(ages_h, tailles_h, label="Hommes (mesures)", color="blue", alpha=0.6)
ax1.scatter(ages_f, tailles_f, label="Femmes (mesures)", color="red", alpha=0.6)
ax1.plot(ages_interp, taille_h_interp, label="Hommes (interp.)", color="blue")
ax1.plot(ages_interp, taille_f_interp, label="Femmes (interp.)", color="red")
ax1.set_ylabel("Taille (cm)")
ax1.set_title("Taille en fonction de l'âge")
ax1.legend()
ax1.grid(True)

# Graphique 2 : différence
ax2.plot(ages_interp, diff_interp, label="Différence Homme - Femme", color="purple")
ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
ax2.set_xlabel("Âge (ans)")
ax2.set_ylabel("Différence (cm)")
ax2.set_title("Différence de taille estimée")
ax2.grid(True)

plt.tight_layout()
plt.show()

# Exemple d'estimation
print("Taille estimée à 15 ans :")
print(" - Homme :", round(taille_estimee(15, "homme"), 1), "cm")
print(" - Femme :", round(taille_estimee(15, "femme"), 1), "cm")
