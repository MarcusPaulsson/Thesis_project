import numpy as np

class KappaCalculator:
    """
    This class calculates Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate Cohen's kappa value of a k-dimensional matrix.
        
        :param testData: The k-dimensional matrix to calculate Cohen's kappa value.
        :param k: int, Matrix dimension.
        :return: float, the Cohen's kappa value of the matrix.
        
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        observed_agreement = np.sum(np.diag(testData))
        total = np.sum(testData)
        expected_agreement = np.sum(np.sum(testData, axis=0) ** 2) / (total ** 2)

        if total == 0:
            return 0.0

        kappa_value = (observed_agreement / total - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate Fleiss' kappa value of an N * k matrix.
        
        :param testData: Input data matrix, N * k.
        :param N: int, Number of samples.
        :param k: int, Number of categories.
        :param n: int, Number of raters.
        :return: float, Fleiss' kappa value.
        
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                               [0, 2, 6, 4, 2],
        >>>                               [0, 0, 3, 5, 6],
        >>>                               [0, 3, 9, 2, 0],
        >>>                               [2, 2, 8, 1, 1],
        >>>                               [7, 7, 0, 0, 0],
        >>>                               [3, 2, 6, 3, 0],
        >>>                               [2, 5, 3, 2, 2],
        >>>                               [6, 5, 2, 1, 0],
        >>>                               [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        p = np.sum(testData, axis=0) / (N * n)
        P_e = np.sum(p ** 2)
        P_o = np.mean(np.sum(testData ** 2, axis=1) / (n ** 2))

        if P_e == 1:
            return 0.0

        fleiss_kappa_value = (P_o - P_e) / (1 - P_e)
        return fleiss_kappa_value