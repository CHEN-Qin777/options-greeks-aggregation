# -*- coding: utf-8 -*-
"""Backtest simplifié d'une stratégie de couverture (protective put)."""
import numpy as np
import pandas as pd

def backtest_protective_put(prix_actif, dates, K, T_jours, r, sigma, frais=0):
    """
    Stratégie : acheter l'actif et un put ATM, conserver jusqu'à expiration.
    Retourne un DataFrame avec les valeurs du portefeuille couvert et non couvert.
    
    Attention : backtest simplifié sur une seule période.
    Pour un backtest réaliste, il faudrait réévaluer l'option chaque jour.
    """
    # Prix initial
    S0 = prix_actif[0]
    # Prix du put
    from .arbre_binomial import prix_option_europeenne
    prix_put = prix_option_europeenne(S0, K, T_jours/365, r, sigma, 100, 'put')
    
    # Valeur initiale du portefeuille couvert : 1 actif + 1 put
    valeur_couvert = [S0 + prix_put]
    valeur_non_couvert = [S0]
    
    # Simulation jusqu'à maturité (on suppose qu'on garde jusqu'au bout)
    # On calcule la valeur à l'échéance
    ST = prix_actif[-1]
    valeur_put_final = max(K - ST, 0)
    valeur_couvert.append(ST + valeur_put_final)
    valeur_non_couvert.append(ST)
    
    # Création d'un DataFrame avec les dates clés
    dates_bt = [dates[0], dates[-1]]
    df = pd.DataFrame({
        'Date': dates_bt,
        'Portefeuille couvert': valeur_couvert,
        'Portefeuille non couvert': valeur_non_couvert
    })
    return df
