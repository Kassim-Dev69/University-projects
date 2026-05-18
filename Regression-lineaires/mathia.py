import pandas as pd

try:
  df = pd.read.csv('')
except FileNotFoundError:
  print("Erreur : Le fichier 'anime_dataset.csv' n'existe pas !")
  exit()
