# -*- coding: utf-8 -*-
"""Génération de données synthétiques pour les options."""
import numpy as np
import pandas as pd

def generer_prix_sous_jacent(S0=100, mu=0.05, sigma=0.2, T=1, n_jours=252):
    """
    Génère une trajectoire de prix par mouvement brownien géométrique.
    Retourne un DataFrame avec les prix quotidiens.
    """
    dt = T / n_jours
    prix = [S0]
    for _ in range(n_jours):
        prix.append(prix[-1] * np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*np.random.normal()))
    dates = pd.date_range(start='2023-01-01', periods=n_jours+1, freq='D')
    return pd.Series(prix, index=dates, name='Prix')
