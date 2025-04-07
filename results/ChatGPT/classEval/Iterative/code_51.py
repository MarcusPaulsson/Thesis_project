import numpy as np

class KappaCalculator:
    """
    A class to calculate Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate Cohen's kappa value of a k-dimensional matrix.
        
        :param testData: The k-dimensional matrix for which to calculate Cohen's kappa value.
        :param k: int, Matrix dimension.
        :return: float, the Cohen's kappa value of the matrix.
        
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        testData = np.array(testData)
        n = np.sum(testData)
        total_agreement = np.sum(np.diag(testData))
        expected_agreement = np.sum(np.sum(testData, axis=0) ** 2) / (n ** 2)
        observed_agreement = total_agreement / n
        
        # Avoid division by zero
        if expected_agreement == 1:
            return 1.0 if observed_agreement == expected_agreement else 0.0
        
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
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
        >>>                                  [0, 2, 6, 4, 2],
        >>>                                  [0, 0, 3, 5, 6],
        >>>                                  [0, 3, 9, 2, 0],
        >>>                                  [2, 2, 8, 1, 1],
        >>>                                  [7, 7, 0, 0, 0],
        >>>                                  [3, 2, 6, 3, 0],
        >>>                                  [2, 5, 3, 2, 2],
        >>>                                  [6, 5, 2, 1, 0],
        >>>                                  [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        testData = np.array(testData)
        p = np.sum(testData, axis=0) / (N * n)
        P_e = np.sum(p ** 2)
        P = np.sum(np.diag(np.dot(testData, testData.T))) / (n * (n - 1))
        
        # Avoid division by zero
        if P_e == 1:
            return 1.0 if P == P_e else 0.0
        
        fleiss_kappa_value = (P - P_e) / (1 - P_e)
        return fleiss_kappa_value