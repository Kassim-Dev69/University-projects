import pandas as pd

try:
  df = pd.read.csv('housing.csv')
except:
  print("Erreur : Le fichier 'housing.csv' n'existe pas !")
  exit()

print("--- Aperçu des données ---")
print(df.head(10))
