# -*- coding: utf-8 -*-
"""Calcul des Grecques par différences finies."""
from .arbre_binomial import prix_option_europeenne

def calculer_grecques(S, K, T, r, sigma, n=100, type_='call', epsilon=0.01):
    """
    Calcule les Grecques d'une option européenne.
    
    Retourne un dictionnaire avec les clés : delta, gamma, vega, theta, rho.
    """
    prix = prix_option_europeenne(S, K, T, r, sigma, n, type_)

    # Delta
    prix_up = prix_option_europeenne(S+epsilon, K, T, r, sigma, n, type_)
    prix_down = prix_option_europeenne(S-epsilon, K, T, r, sigma, n, type_)
    delta = (prix_up - prix_down) / (2 * epsilon)

    # Gamma
    gamma = (prix_up - 2*prix + prix_down) / (epsilon**2)

    # Vega (dérivée par rapport à sigma)
    prix_vol_up = prix_option_europeenne(S, K, T, r, sigma+0.01, n, type_)
    vega = (prix_vol_up - prix) / 0.01

    # Theta (dérivée par rapport au temps, en réduisant T d'un jour)
    dt_jour = 1/365
    if T > dt_jour:
        prix_t_down = prix_option_europeenne(S, K, T-dt_jour, r, sigma, n, type_)
        theta = (prix_t_down - prix) / dt_jour  # attention signe : perte de temps = diminution prix
    else:
        theta = 0

    # Rho (dérivée par rapport à r)
    prix_r_up = prix_option_europeenne(S, K, T, r+0.01, sigma, n, type_)
    rho = (prix_r_up - prix) / 0.01

    return {'delta': delta, 'gamma': gamma, 'vega': vega, 'theta': theta, 'rho': rho}
