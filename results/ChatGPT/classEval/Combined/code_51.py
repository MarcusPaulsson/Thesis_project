import numpy as np
import unittest

class KappaCalculator:
    """
    A class to calculate Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa value of a k-dimensional matrix.
        
        :param testData: The k-dimensional matrix (list of lists) to calculate the kappa value
        :return: float, the Cohen's kappa value of the matrix
        """
        flat_data = np.array(testData).flatten()
        total = len(flat_data)
        
        observed_agreements = np.sum(flat_data * (flat_data - 1)) / (total * (total - 1))
        proportions = np.sum(testData, axis=0) / total
        expected_agreements = np.sum(proportions * (proportions - 1))
        
        if expected_agreements == 0:
            return 0.0
        return (observed_agreements - expected_agreements) / (1 - expected_agreements)

    @staticmethod
    def fleiss_kappa(testData, N, n):
        """
        Calculate Fleiss' kappa value of an N * k matrix.
        
        :param testData: Input data matrix (list of lists), N * k
        :param N: int, Number of samples
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        """
        p = np.sum(testData, axis=0) / (N * n)
        P = np.sum((np.sum(testData**2, axis=1) - n) / (n * (n - 1))) / N
        Pe = np.sum(p**2)
        
        if Pe == 1:
            return 0.0
        return (P - Pe) / (1 - Pe)


class KappaCalculatorTestKappa(unittest.TestCase):
    def test_kappa_1(self):
        self.assertEqual(KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]]), 0.25)

    def test_kappa_2(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 2, 1], [1, 2, 1], [1, 1, 2]]), 0.19469026548672572)

    def test_kappa_3(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 1, 2], [1, 2, 1], [1, 1, 2]]), 0.19469026548672572)

    def test_kappa_4(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 1, 1], [2, 2, 1], [1, 1, 2]]), 0.19469026548672572)

    def test_kappa_5(self):
        self.assertAlmostEqual(KappaCalculator.kappa([[2, 1, 1], [1, 2, 2], [1, 1, 2]]), 0.19469026548672572)


class KappaCalculatorTestFleissKappa(unittest.TestCase):
    def test_fleiss_kappa_1(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.20993070442195522)

    def test_fleiss_kappa_2(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[1, 0, 0, 0, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.2115748928799344)

    def test_fleiss_kappa_3(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 1, 0, 0, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.21076904123090398)

    def test_fleiss_kappa_4(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 0, 1, 0, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.2096583016522883)

    def test_fleiss_kappa_5(self):
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 0, 0, 1, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.21147425143148907)


class KappaCalculatorTest(unittest.TestCase):
    def test_kappa_calculator(self):
        self.assertEqual(KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]]), 0.25)
        self.assertAlmostEqual(KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
                                                             [0, 2, 6, 4, 2],
                                                             [0, 0, 3, 5, 6],
                                                             [0, 3, 9, 2, 0],
                                                             [2, 2, 8, 1, 1],
                                                             [7, 7, 0, 0, 0],
                                                             [3, 2, 6, 3, 0],
                                                             [2, 5, 3, 2, 2],
                                                             [6, 5, 2, 1, 0],
                                                             [0, 2, 2, 3, 7]], 10, 14), 0.20993070442195522)


if __name__ == "__main__":
    unittest.main()