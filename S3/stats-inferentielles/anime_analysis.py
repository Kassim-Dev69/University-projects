import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

'''
-------------------------------------------------------------------------------
------------- ÉTAPE 1 - VISUALISATION DES DONNÉES - ANIME DATASET -------------
-------------------------------------------------------------------------------
'''
print("-----------------------------------------------------------------------------------------")
print("------------------ ÉTAPE 1 - VISUALISATION DES DONNÉES - ANIME DATASET ------------------")
print("-----------------------------------------------------------------------------------------")
# 1. Charger le dataset
try:
    df = pd.read_csv('anime_dataset.csv')
except FileNotFoundError:
    print("Erreur : Le fichier 'anime_dataset.csv' n'existe pas !")
    exit()

# 2. Afficher les 10 premières lignes pour vérifier que tout est bien chargé
print("--- Aperçu des données ---")
print(df.head(10))

# 3. Afficher des informations sur les colonnes
print("\n--- Informations sur le dataset ---")
print(df.info())

'''
-------------------------------------------------------------------------------------
--------------- ÉTAPE 2 - NETTOYAGE DES DONNÉES - ANIME DATASET ---------------------
--- (Processus que j'ai appris dans le cours de Power BI, faire du Data cleaning) ---
-------------------------------------------------------------------------------------
'''
print("-----------------------------------------------------------------------------------------")
print("-------------------- ÉTAPE 2 - NETTOYAGE DES DONNÉES - ANIME DATASET --------------------")
print("-----------------------------------------------------------------------------------------")

# 4. Vérifier et supprimer les doublons
print("\n--- Vérification des doublons ---")
# On compte le nombre de doublons
num_duplicates = df.duplicated().sum()

if num_duplicates > 0:
    print(f"Il y a {num_duplicates} doublons dans le dataset.")
    df = df.drop_duplicates()
    print(f"Dimensions après suppression des doublons : {df.shape}")
else:
    print("Il n'y a pas de doublons dans le dataset.")

# 5. Vérifier les types de données et les convertir si nécessaire
print("\n--- Types de données avant conversion ---")
print(df.dtypes)

# Convertir les colonnes 'score_philo' et 'episodes' en numérique, en gérant les valeurs manquantes
df['score_philo'] = pd.to_numeric(df['score_philo'], errors='coerce')
df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
df['note_mal'] = pd.to_numeric(df['note_mal'], errors='coerce')
print("\n--- Types de données après conversion ---")
print(df.dtypes)

# 6. Vérifier les valeurs manquantes après conversion
print("\n--- Valeurs manquantes ---")
print(df.isnull().sum())

if df.isnull().sum().any():
    print("\nAttention : Il y a des valeurs manquantes dans le dataset. Elles seront supprimées pour l'analyse.")
    # 7. Supprimer les lignes où il manque les données que l'on veut analyser (score_philo et note_mal)
    df_cleaned = df.dropna().copy()
    print(f"\nDimensions après suppression des lignes sans données clés : {df_cleaned.shape}")
else:
    df_cleaned = df.copy()
    print("\nAucune valeur manquante dans les colonnes clés. Aucune ligne supprimée.")
    # Sauvegarder le fichier nettoyé
    
# 8. Vérifier si on a supprimé trop de lignes
if len(df_cleaned) < (len(df) * 0.5):
    print("Alerte : Plus de 50% des données ont été supprimées !")                
else:
    # Sauvegarder le fichier nettoyé                
    df_cleaned.to_csv('anime_cleaned.csv', index=False)                
    print("Fichier sauvegardé.")
    
'''
-------------------------------------------------------------------------------------
---------------- ÉTAPE 3 - ANALYSE STATISTIQUES - ANIME CLEANED ---------------------
-------------------------------------------------------------------------------------
'''

print("------------------------------------------------------------------------------------------")
print("--------------------- ÉTAPE 3 - ANALYSE STATISTIQUES - ANIME CLEANED ---------------------")
print("-------------------------------- STATISTIQUES DESCRIPTIVES -------------------------------")
print("------------------------------------------------------------------------------------------")

# 1. Charger le dataset nettoyé
try:
    df = pd.read_csv('anime_cleaned.csv')
    print("Le fichier anime_cleaned.csv est existant et a été chargé avec succès !")
except FileNotFoundError:
    print("Erreur : Le fichier anime_cleaned.csv n'existe pas !")
    exit()

# 2. Statistiques descriptives
print("--- Statistiques descriptives globales ---")
print(df.describe())

# 3. Statistiques sur la note MAL (score)
print("\n--- Statistiques sur la note MAL (score) ---")
print(f"Moyenne : {df['note_mal'].mean():.2f}")
print(f"Médiane : {df['note_mal'].median():.2f}")
print(f"Écart-type : {df['note_mal'].std():.2f}")

# 4. Statistiques sur le score philosophique
print("\n--- Statistiques sur le score philosophique ---")
print(f"Moyenne : {df['score_philo'].mean():.2f}")
print(f"Médiane : {df['score_philo'].median():.2f}")
print(f"Écart-type : {df['score_philo'].std():.2f}")

'''
------------------------------------------------------------------------------------------
---------------- ÉTAPE 4 - VISUALISATION DES DONNÉES - ANIME CLEANED ---------------------
------------------------------------------------------------------------------------------
'''

print("-----------------------------------------------------------------------------------------------")
print("--------------------- ÉTAPE 4 - VISUALISATION DES DONNÉES - ANIME CLEANED ---------------------")
print("-----------------------------------------------------------------------------------------------")


# 1. Configurer le style des graphiques
sns.set_theme(style="whitegrid")

# 2. Créer une figure avec deux sous-graphiques (subplots)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# A. Histogramme de la note MAL (Distribution)
sns.histplot(df['note_mal'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution des notes MAL')
axes[0].set_xlabel('Note')
axes[0].set_ylabel('Fréquence')

# B. Nuage de points
sns.scatterplot(x='note_mal', y='score_philo', data=df, ax=axes[1], alpha=0.5)
axes[1].set_title('Note MAL vs Score Philosophique')
axes[1].set_xlabel('Note MAL')
axes[1].set_ylabel('Score Philosophique')

# 3. Calculer la corrélation
correlation = df['note_mal'].corr(df['score_philo'])
print("\n--- Analyse de la corrélation ---")
print(f"Coefficient de corrélation de Pearson : {correlation:.2f}")

if correlation > 0.7:
    print("Interprétation : Corrélation forte. Les animes avec un score philosophique élevé sont généralement très bien notés.")
elif correlation > 0.3:
    print("Interprétation : Corrélation modérée. Le score philosophique influence positivement la note MAL.")
else:
    print("Interprétation : Corrélation faible. La note MAL ne dépend pas fortement du score philosophique.")

axes[1].text(0.05, 0.95, f'Corrélation: {correlation:.2f}', 
             transform=axes[1].transAxes, fontsize=12, fontweight='bold',
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
# -------------------------------------------------------------------------

# 4. Afficher les graphiques
plt.tight_layout()
plt.show()


'''
----------------------------------------------------------------------------------------------
---------------- ÉTAPE 5 - STATISTIQUES INFÉRENTIELLES - ANIME CLEANED -----------------------
-- (Inspiré de l'exo 1 de notre contrôle continue n°01 du S3 en Statistiques Inférentielles)--
----------------------------------------------------------------------------------------------
'''

print("-------------------------------------------------------------------------------------------------")
print("--------------------- ÉTAPE 5 - STATISTIQUES INFÉRENTIELLES - ANIME CLEANED ---------------------")
print("-------------------------------------------------------------------------------------------------")

# 1. Prenons un échantillon aléatoire de 150 animes
df_sample = df.sample(n=150, random_state=42)
notes = df_sample['note_mal']

# 2. Calculons l'écart-type et la moyenne empiriques de l'échantillon
moyenne_empirique = notes.mean()
ecart_type = notes.std()
print(f"--- Paramètres de l'échantillon (n=150) ---")
print(f"Moyenne empirique (x̄) : {moyenne_empirique:.4f}")
print(f"Écart-type (s) : {ecart_type:.4f}")

# 3. Créons d'abord une fonction pour calculer l'intervalle de confiance
def calculer_intervalle(data, confiance=0.95):
    n = len(data)
    moyenne = np.mean(data)
    # Calcul de l'erreur standard (écart-type / racine de n)
    erreur_standard = stats.sem(data)
    # Calcul de la marge d'erreur avec la loi t de Student
    # n-1 degrés de liberté
    intervalle = stats.t.interval(confiance, n-1, loc=moyenne, scale=erreur_standard)
    return intervalle

# 4. Calculer et afficher les intervalles de confiance
pourcentage = [0.90, 0.95, 0.99]
print(f"\n--- Intervalles de confiance pour la note moyenne ---")

for pourcentage in pourcentage:
    ic = calculer_intervalle(notes, confiance=pourcentage)
    print(f"IC {int(pourcentage*100)}% : [{ic[0]:.4f} ; {ic[1]:.4f}]")
    