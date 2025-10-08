# DataTrail - Analyses de Courses Trail

Ce dépôt contient les analyses de données pour différentes courses de trail.

## Projets

### 🏔️ Swiss Canyon Trail 2024
- **Dossier:** `swiss_canyon_trail_2024/`
- **Description:** Analyse des résultats du Swiss Canyon Trail 2024
- **Distances:** 16k, 31k, 51k, 81k, 111k

### 🏔️ Trail des Glières 2025
- **Dossier:** `trail_glieres_2025/`
- **Description:** Analyse des résultats du Trail des Glières 2025
- **Distances:** 21km Solo et 21km Duo

## Structure

Chaque projet contient :
- Un notebook Jupyter avec l'analyse complète
- Les fichiers de données sources (CSV, PDF)
- La configuration Poetry pour les dépendances
- Les tests associés

## Installation

Chaque projet utilise Poetry pour la gestion des dépendances :

```bash
cd [nom_du_projet]
poetry install
poetry shell
jupyter lab
```