import numpy as np
import pandas as pd


df = pd.read_csv("anime_dataset.csv")
df["themes_profonds"] = df["themes_profonds"].map({"True": True, "False": False})