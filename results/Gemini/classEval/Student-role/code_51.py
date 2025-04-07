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
        po = np.trace(matrix) / np.sum(matrix)
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        pe = np.sum(row_sums * col_sums) / (np.sum(matrix) ** 2)
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
        matrix = np.array(testData)
        total_ratings = N * n
        
        # Calculate p_j
        p_j = np.sum(matrix, axis=0) / total_ratings
        
        # Calculate P_i
        P_i = (np.sum(matrix**2, axis=1) - n) / (n * (n - 1))
        
        # Calculate P_bar
        P_bar = np.sum(P_i) / N
        
        # Calculate P_e_bar
        P_e_bar = np.sum(p_j**2)
        
        # Calculate Kappa
        kappa = (P_bar - P_e_bar) / (1 - P_e_bar)
        
        return kappa