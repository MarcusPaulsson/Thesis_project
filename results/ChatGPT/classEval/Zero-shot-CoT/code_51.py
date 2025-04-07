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
        """
        n = np.sum(testData)
        p = np.sum(testData, axis=0) / n  # Probability of each category
        p0 = np.sum(np.diagonal(testData)) / n  # Observed agreement
        pe = np.sum(p ** 2)  # Expected agreement
        kappa_value = (p0 - pe) / (1 - pe) if (1 - pe) != 0 else 0
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
        """
        # Calculate the proportion of each category
        p = np.sum(testData, axis=0) / (n * N)
        
        # Calculate P_i for each item
        P_i = np.sum((testData ** 2 - n * testData) / (n * (n - 1)), axis=1) / N
        
        # Calculate P_e
        P_e = np.sum(p ** 2)

        # Calculate Fleiss' kappa
        P_bar = np.mean(P_i)
        fleiss_kappa_value = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else 0
        return fleiss_kappa_value