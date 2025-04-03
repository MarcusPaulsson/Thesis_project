import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the Cohen's kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the Cohen's kappa value
        :param k: int, Matrix dimension
        :return: float, the Cohen's kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        observed_agreement = np.sum(np.diag(testData)) / np.sum(testData)
        total = np.sum(testData)
        expected_agreement = np.sum((np.sum(testData, axis=0) * np.sum(testData, axis=1))**2) / (total**2)
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss' kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        # Calculate the proportions for each category
        p = np.sum(testData, axis=0) / (N * n)
        P_bar = np.sum(p**2)
        P_e_bar = np.sum(np.sum(testData, axis=1)**2) / (N * n)**2
        fleiss_kappa_value = (P_bar - P_e_bar) / (1 - P_e_bar)
        return fleiss_kappa_value