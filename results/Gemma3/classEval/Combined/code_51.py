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
        n = len(testData)
        sum_p = 0
        for i in range(n):
            sum_p += np.trace(testData[i])
        p_o = sum_p / (n * k)
        sum_p_squared = 0
        for i in range(n):
            sum_p_squared += np.sum(testData[i] * testData[i])
        p_e = (sum_p_squared / (n * n * k)) - (1 / k)
        if p_e >= 1:
            return 0.0
        kappa = (p_o - p_e) / (1 - p_e)
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
        P = np.zeros((N, k))
        for i in range(N):
            P[i, :] = np.array(testData[i]) / n
        p_j = np.sum(P, axis=0) / N
        P_bar = np.sum(p_j * p_j)
        Pe = P_bar
        Po = np.sum(np.sum(P * P, axis=1)) / N
        if Pe >= 1:
            return 0.0
        kappa = (Po - Pe) / (1 - Pe)
        return kappa