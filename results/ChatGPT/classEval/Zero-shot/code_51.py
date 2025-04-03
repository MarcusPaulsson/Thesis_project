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
        if isinstance(testData, np.ndarray):
            matrix = testData
        else:
            matrix = np.array(testData)

        n_raters = np.sum(matrix, axis=1)
        total = np.sum(n_raters)
        p_i = np.sum(matrix, axis=0) / total
        p_e = np.sum((np.sum(matrix, axis=0) ** 2)) / (total ** 2)
        p_o = np.sum((n_raters ** 2)) / (total ** 2)
        kappa_value = (p_o - p_e) / (1 - p_e)
        
        return kappa_value

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
        if isinstance(testData, np.ndarray):
            matrix = testData
        else:
            matrix = np.array(testData)
        
        p_i = np.sum(matrix, axis=1) / (n * np.sum(matrix))
        P_bar = np.mean(p_i)
        P_e_bar = np.sum((np.sum(matrix, axis=0) ** 2) / (n ** 2 * N))
        fleiss_kappa_value = (P_bar - P_e_bar) / (1 - P_e_bar)
        
        return fleiss_kappa_value