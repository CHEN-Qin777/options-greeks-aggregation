# Évaluation d'options et agrégation des Grecques



## 📌 À propos

**Évaluation d'options et agrégation des Grecques**  
Modèle binomial pour le pricing d'options, calcul des Grecques (Delta, Gamma, Theta, Vega, Rho) et agrégation pour un portefeuille. Implémentation en Python avec visualisations.

## 📋 Description détaillée

Ce projet implémente un modèle binomial pour évaluer des options européennes (call/put). Il calcule les principales sensibilités (Grecques) par différences finies et permet d'agréger ces risques pour un portefeuille multi‑options. Une visualisation de la variation du Delta en fonction du prix du sous‑jacent est également fournie.

Les résultats obtenus (présentés ci‑dessous) correspondent à un call et un put avec les paramètres suivants :
- `S = 100` (prix du sous‑jacent)
- `K = 100` (prix d'exercice)
- `T = 30/365` (30 jours)
- `r = 3%` (taux sans risque)
- `σ = 20%` (volatilité)
- `n = 100` pas dans l'arbre binomial

## ✨ Fonctionnalités

- ✅ Pricing d'options européennes (call/put) par **arbre binomial**
- ✅ Calcul des **Grecques** (Delta, Gamma, Theta, Vega, Rho) par différences finies
- ✅ Agrégation des Grecques pour un **portefeuille** multi‑options
- ✅ Backtest simplifié d'une stratégie de **couverture** (protective put)
- ✅ Visualisation de la sensibilité des Grecques au prix du sous‑jacent
- ✅ Code modulaire, testé et documenté

## 🔧 Installation

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` contient :
```
numpy
scipy
matplotlib
pandas
```

## 🚀 Utilisation

### Version locale
Exécutez le script principal ou importez les modules dans votre propre code Python.

### Version Colab
Ouvrez le notebook [`analyse_grecques_complete.ipynb`](notebooks/analyse_grecques_complete.ipynb) dans Google Colab et exécutez toutes les cellules.

## 📊 Résultats

Les résultats suivants ont été obtenus avec les paramètres par défaut.

### Prix et Grecques d'un call

| Mesure   | Valeur   |
|----------|----------|
| Prix     | 2.4039   |
| Delta    | 0.5285   |
| Gamma    | 7.9385   |
| Vega     | 11.3798  |
| Theta    | -15.4763 |
| Rho      | 4.1679   |

### Agrégation pour un portefeuille (2 calls + 1 put)

| Grecque  | Totale   |
|----------|----------|
| Delta    | 0.5855   |
| Gamma    | 23.8155  |
| Vega     | 34.1393  |

*Les valeurs peuvent légèrement varier selon la graine aléatoire utilisée dans la simulation.*

## 📁 Structure du projet

```
options-greeks-aggregation/
├── README.md
├── requirements.txt
├── data/
│   └── generer_synthetique.py          # Génération de données synthétiques
├── src/
│   ├── arbre_binomial.py                # Modèle binomial
│   ├── grecques.py                       # Calcul des Grecques
│   ├── portefeuille_options.py           # Agrégation pour portefeuille
│   └── backtest.py                        # Backtest simplifié
├── notebooks/
│   └── analyse_grecques_complete.ipynb   # Notebook Colab complet
└── tests/
    └── test_grecques.py                   # Tests unitaires
```

## 📄 Licence

Ce projet est fourni à titre éducatif. Vous êtes libre de l'utiliser et de le modifier.

## 👤 Auteur

Étudiant en Master 2 Mathématiques Financières – Projet de stage.

---

