import numpy as np


class KappaCalculator:
    """
    A class to calculate Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa value from a confusion matrix.
        
        :param testData: A square confusion matrix (2D list or array).
        :return: Cohen's kappa value (float).
        """
        testData = np.array(testData)
        observed_agreement = np.trace(testData) / np.sum(testData)
        total_ratings = np.sum(testData)
        expected_agreement = np.sum(np.square(np.sum(testData, axis=0))) / (total_ratings ** 2)
        
        # Avoid division by zero
        if expected_agreement == 1:
            return 0.0  # If expected agreement is 1, kappa is 0
        
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, n):
        """
        Calculate Fleiss' kappa value from a ratings matrix.
        
        :param testData: A 2D array of ratings (N samples x k categories).
        :param N: Number of samples (rows in testData).
        :param n: Number of raters (assumed to be the same for all samples).
        :return: Fleiss' kappa value (float).
        """
        testData = np.array(testData)
        p = np.sum(testData, axis=0) / (N * n)
        P = np.sum((np.sum(testData, axis=1) / n) ** 2) / N
        P_e = np.sum(p ** 2)

        # Avoid division by zero
        if P_e == 1:
            return 0.0  # If expected agreement is 1, kappa is 0
        
        fleiss_kappa_value = (P - P_e) / (1 - P_e)
        return fleiss_kappa_value


class KappaCalculatorTestKappa(unittest.TestCase):
    def test_kappa(self):
        test_cases = [
            ([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 0.25),
            ([[2, 2, 1], [1, 2, 1], [1, 1, 2]], 0.19469026548672572),
            ([[2, 1, 2], [1, 2, 1], [1, 1, 2]], 0.19469026548672572),
            ([[2, 1, 1], [2, 2, 1], [1, 1, 2]], 0.19469026548672572),
            ([[2, 1, 1], [1, 2, 2], [1, 1, 2]], 0.19469026548672572)
        ]
        for data, expected in test_cases:
            self.assertAlmostEqual(KappaCalculator.kappa(data), expected)


class KappaCalculatorTestFleissKappa(unittest.TestCase):
    def test_fleiss_kappa(self):
        test_cases = [
            ([[0, 0, 0, 0, 14],
              [0, 2, 6, 4, 2],
              [0, 0, 3, 5, 6],
              [0, 3, 9, 2, 0],
              [2, 2, 8, 1, 1],
              [7, 7, 0, 0, 0],
              [3, 2, 6, 3, 0],
              [2, 5, 3, 2, 2],
              [6, 5, 2, 1, 0],
              [0, 2, 2, 3, 7]], 10, 14, 0.20993070442195522),
            ([[1, 0, 0, 0, 14],
              [0, 2, 6, 4, 2],
              [0, 0, 3, 5, 6],
              [0, 3, 9, 2, 0],
              [2, 2, 8, 1, 1],
              [7, 7, 0, 0, 0],
              [3, 2, 6, 3, 0],
              [2, 5, 3, 2, 2],
              [6, 5, 2, 1, 0],
              [0, 2, 2, 3, 7]], 10, 14, 0.2115748928799344),
            ([[0, 1, 0, 0, 14],
              [0, 2, 6, 4, 2],
              [0, 0, 3, 5, 6],
              [0, 3, 9, 2, 0],
              [2, 2, 8, 1, 1],
              [7, 7, 0, 0, 0],
              [3, 2, 6, 3, 0],
              [2, 5, 3, 2, 2],
              [6, 5, 2, 1, 0],
              [0, 2, 2, 3, 7]], 10, 14, 0.21076904123090398),
            ([[0, 0, 1, 0, 14],
              [0, 2, 6, 4, 2],
              [0, 0, 3, 5, 6],
              [0, 3, 9, 2, 0],
              [2, 2, 8, 1, 1],
              [7, 7, 0, 0, 0],
              [3, 2, 6, 3, 0],
              [2, 5, 3, 2, 2],
              [6, 5, 2, 1, 0],
              [0, 2, 2, 3, 7]], 10, 14, 0.2096583016522883),
            ([[0, 0, 0, 1, 14],
              [0, 2, 6, 4, 2],
              [0, 0, 3, 5, 6],
              [0, 3, 9, 2, 0],
              [2, 2, 8, 1, 1],
              [7, 7, 0, 0, 0],
              [3, 2, 6, 3, 0],
              [2, 5, 3, 2, 2],
              [6, 5, 2, 1, 0],
              [0, 2, 2, 3, 7]], 10, 14, 0.21147425143148907)
        ]
        for data, N, n, expected in test_cases:
            self.assertAlmostEqual(KappaCalculator.fleiss_kappa(data, N, n), expected)

