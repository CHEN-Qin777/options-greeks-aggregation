# -*- coding: utf-8 -*-
"""Agrégation des Grecques pour un portefeuille d'options."""
import numpy as np
from .grecques import calculer_grecques

class PortefeuilleOptions:
    def __init__(self):
        self.positions = []  # chaque élément : (quantité, paramètres, type)

    def ajouter_position(self, quantite, S, K, T, r, sigma, type_='call', n=100):
        """
        Ajoute une position au portefeuille.
        quantité : nombre d'options (positif pour achat, négatif pour vente)
        """
        self.positions.append({
            'quantite': quantite,
            'S': S, 'K': K, 'T': T, 'r': r, 'sigma': sigma,
            'type': type_,
            'n': n
        })

    def calculer_grecques_agregees(self):
        """Calcule la somme pondérée des Grecques de toutes les positions."""
        total = {'delta': 0.0, 'gamma': 0.0, 'vega': 0.0, 'theta': 0.0, 'rho': 0.0}
        for pos in self.positions:
            g = calculer_grecques(
                S=pos['S'], K=pos['K'], T=pos['T'], r=pos['r'],
                sigma=pos['sigma'], n=pos['n'], type_=pos['type']
            )
            q = pos['quantite']
            for key in total:
                total[key] += q * g[key]
        return total

    def afficher_resume(self):
        """Affiche un résumé formaté des Grecques agrégées."""
        total = self.calculer_grecques_agregees()
        print("--- Grecques agrégées du portefeuille ---")
        for key, value in total.items():
            print(f"{key.capitalize()} total : {value:.4f}")
        return total
