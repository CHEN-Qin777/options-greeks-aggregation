import unittest
import numpy as np
from src.arbre_binomial import prix_option_europeenne
from src.grecques import calculer_grecques

class TestGrecques(unittest.TestCase):
    def test_prix_call(self):
        prix = prix_option_europeenne(100, 100, 30/365, 0.03, 0.2, 100, 'call')
        self.assertAlmostEqual(prix, 2.4039, places=4)

    def test_delta_call(self):
        delta, _, _, _, _ = calculer_grecques(100, 100, 30/365, 0.03, 0.2, 100, 'call')
        self.assertAlmostEqual(delta, 0.5285, places=4)

    def test_gamma_call(self):
        _, gamma, _, _, _ = calculer_grecques(100, 100, 30/365, 0.03, 0.2, 100, 'call')
        self.assertAlmostEqual(gamma, 7.9385, places=4)

if __name__ == '__main__':
    unittest.main()
