import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """


    @staticmethod
    def kappa(testData, k):
        """
        Calculate the cohens kappa value of a k-dimensional matrix
        :param testData: The k-dimensional matrix that needs to calculate the cohens kappa value
        :param k: int, Matrix dimension
        :return:float, the cohens kappa value of the matrix
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        matrix = np.array(testData)
        n = matrix.shape[0]
        observed_agreement = np.trace(matrix) / np.sum(matrix)
        expected_agreement = 0
        for i in range(k):
            expected_agreement += np.sum(matrix[i, :]) * np.sum(matrix[:, i])
        expected_agreement /= (np.sum(matrix) ** 2)
        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fliss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
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
        data = np.array(testData)
        p_j = np.sum(data, axis=0) / (N * n)
        P_i = (np.sum(data**2, axis=1) - n) / (n * (n - 1))
        P_mean = np.mean(P_i)
        P_e = np.sum(p_j**2)
        kappa = (P_mean - P_e) / (1 - P_e)
        return kappa