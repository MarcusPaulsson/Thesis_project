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
        :return: float, the cohens kappa value of the matrix
        """
        observed_agreement = np.sum(np.diag(testData)) / np.sum(testData)
        expected_agreement = np.sum(np.sum(testData, axis=0) ** 2) / (np.sum(testData) ** 2)
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the fleiss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, fleiss kappa value
        """
        # Calculate the proportion of ratings for each category
        p = np.sum(testData, axis=0) / (N * n)
        P_e = np.sum(p ** 2)

        # Calculate the observed agreement
        P_o = 0.0
        for row in testData:
            p_i = np.sum(row) / (n)
            P_o += p_i ** 2
        P_o /= N

        # Calculate Fleiss' Kappa
        kappa_value = (P_o - P_e) / (1 - P_e)
        return kappa_value