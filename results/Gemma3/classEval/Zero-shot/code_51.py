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
        sum_diag = 0
        sum_all = 0
        for i in range(n):
            sum_diag += testData[i][i]
            sum_all += sum(testData[i])
        po = sum_diag / sum_all
        pe = (sum([sum(row) for row in testData]) / n) ** 2
        kappa = (po - pe) / (1 - pe)
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
        p_j = [sum(testData[i][j] for i in range(N)) / (N * n) for j in range(k)]
        P = sum([x * x for x in p_j])
        P_i = [sum(testData[i][j] for j in range(k)) / n for i in range(N)]
        P_bar = sum(P_i) / N
        Pe = P_bar * P_bar
        P_e = sum([x * x for x in P_i]) / N
        kappa = (P_e - Pe) / (1 - Pe)
        return kappa