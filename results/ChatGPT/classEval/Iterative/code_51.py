import numpy as np

class KappaCalculator:
    """
    This class calculates Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa value of a square matrix.
        :param testData: 2D list or numpy array, the confusion matrix
        :return: float, Cohen's kappa value
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
        0.25
        """
        testData = np.array(testData)
        n = np.sum(testData)
        p0 = np.trace(testData) / n  # observed agreement
        pe = np.sum(np.square(np.sum(testData, axis=0))) / (n**2)  # expected agreement
        return (p0 - pe) / (1 - pe) if (1 - pe) != 0 else 0.0

    @staticmethod
    def fleiss_kappa(testData):
        """
        Calculate Fleiss' kappa value of an N x k matrix.
        :param testData: 2D list or numpy array, N x k matrix of ratings
        :return: float, Fleiss' kappa value
        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                                 [0, 2, 6, 4, 2],
        >>>                                 [0, 0, 3, 5, 6],
        >>>                                 [0, 3, 9, 2, 0],
        >>>                                 [2, 2, 8, 1, 1],
        >>>                                 [7, 7, 0, 0, 0],
        >>>                                 [3, 2, 6, 3, 0],
        >>>                                 [2, 5, 3, 2, 2],
        >>>                                 [6, 5, 2, 1, 0],
        >>>                                 [0, 2, 2, 3, 7]], 10)
        0.20993070442195522
        """
        testData = np.array(testData)
        N, k = testData.shape
        n = np.sum(testData, axis=1)  # total ratings for each sample
        p = np.sum(testData, axis=0) / np.sum(testData)  # proportion of ratings for each category
        P = np.sum((n / np.sum(testData))**2)  # observed agreement
        Pe = np.sum(p**2)  # expected agreement
        return (P - Pe) / (1 - Pe) if (1 - Pe) != 0 else 0.0