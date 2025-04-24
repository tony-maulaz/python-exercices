import pandas as pd
import numpy as np


# Génération de 5 séries de mesure avec un peu de bruit
true_allongements = np.array([0, 1.2, 2.3, 3.5, 4.7, 5.9, 7.2, 8.5, 9.9, 11.3, 12.8])
forces = np.arange(0, 11, 1)  # 0 à 10 N
num_series = 5

# Création de 5 séries avec bruit
for s in range(1, num_series + 1):
    data = {'force_N': [], 'allongement_cm': []}
    noise = np.random.normal(0, 0.2, size=true_allongements.shape)
    for f, a_noisy in zip(forces, true_allongements + noise):
        data['force_N'].append(f)
        data['allongement_cm'].append(round(a_noisy, 2))

    df = pd.DataFrame(data)

    # Calcul de la moyenne des allongements par force
    df_mean = df.groupby('force_N')['allongement_cm'].mean().reset_index()

    # Sauvegarde du fichier CSV
    file_path = f"ressort_allongement_{s}.csv"
    df_mean.to_csv(file_path, index=False)
