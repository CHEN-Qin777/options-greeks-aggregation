# -*- coding: utf-8 -*-
"""Modèle binomial pour le pricing d'options européennes."""
import numpy as np

def prix_option_europeenne(S, K, T, r, sigma, n, type_='call'):
    """
    Calcule le prix d'une option européenne par arbre binomial.
    
    Paramètres
    ----------
    S : float
        Prix du sous-jacent
    K : float
        Prix d'exercice
    T : float
        Temps jusqu'à maturité (en années)
    r : float
        Taux sans risque
    sigma : float
        Volatilité
    n : int
        Nombre de pas de l'arbre
    type_ : str
        'call' ou 'put'
    
    Retour
    ------
    float : prix de l'option
    """
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Valeurs du sous-jacent à l'échéance
    prix_actif = np.zeros(n+1)
    for i in range(n+1):
        prix_actif[i] = S * (u ** (n-i)) * (d ** i)

    # Valeur de l'option à l'échéance
    if type_ == 'call':
        valeur = np.maximum(prix_actif - K, 0)
    else:
        valeur = np.maximum(K - prix_actif, 0)

    # Récurrence inverse
    for j in range(n-1, -1, -1):
        for i in range(j+1):
            valeur[i] = np.exp(-r * dt) * (p * valeur[i] + (1-p) * valeur[i+1])
    return valeur[0]
