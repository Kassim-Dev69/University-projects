# Analyse Statistique des Animes 📊

[![Tests](https://github.com/University-projects/S3/stats-inferentielles/workflows/Test%20Anime%20Analysis%20Script/badge.svg)](https://github.com/University-projects/S3/stats-inferentielles/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️ for Statistics](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F%20for-Statistics-red)](https://github.com)

Projet d'analyse de données et statistiques inférentielles sur un dataset d'animes.

## 📊 Status du Projet

| Critère            | Status                                                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Tests**          | ![Build Status](https://img.shields.io/github/actions/workflow/status/University-projects/S3/stats-inferentielles/test.yml?branch=main) |
| **Version Python** | 3.9, 3.10, 3.11                                                                                                                         |
| **Dépendances**    | pandas, matplotlib, seaborn, numpy, scipy                                                                                               |
| **État**           | ✅ Production                                                                                                                           |

## Objectif

Analyser la relation entre les notes MyAnimeList (MAL) et un score philosophique attribué aux animes, en utilisant des méthodes de statistiques descriptives et inférentielles.

## Étapes du Pipeline

### 1️⃣ Visualisation des données brutes

- Chargement du fichier `anime_dataset.csv`
- Aperçu des données et des types

### 2️⃣ Nettoyage des données

- Suppression des doublons
- Conversion des types (numérique, etc.)
- Gestion des valeurs manquantes
- Sauvegarde dans `anime_cleaned.csv`

### 3️⃣ Analyse descriptive

- Statistiques globales (moyenne, médiane, écart-type)
- Calcul spécifique sur la note MAL et le score philosophique

### 4️⃣ Visualisation des données nettoyées

- Histogramme de distribution des notes
- Nuage de points (Note MAL vs Score Philosophique)
- Coefficient de corrélation de Pearson

### 5️⃣ Statistiques inférentielles

- Tirage d'un échantillon aléatoire (n=150)
- Calcul d'intervalles de confiance (90%, 95%, 99%) avec la loi de Student

## Fichiers

- `anime_analysis.py` : Script principal d'analyse
- `anime_dataset.csv` : Dataset brut initial
- `anime_cleaned.csv` : Dataset nettoyé (généré après exécution)

## Prérequis

```bash
pip install pandas matplotlib seaborn numpy scipy
```

## Utilisation

```bash
python anime_analysis.py
```

Le script affichera un rapport complet à la console et générera des visualisations avec Matplotlib.

## Auteur

Projet réalisé pour le cours de Statistiques Inférentielles du S3.

---

_Inspiré de l'exercice 1 du contrôle continu n°01 de Statistiques Inférentielles._
