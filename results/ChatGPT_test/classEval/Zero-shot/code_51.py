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
        # Convert to numpy array for easier calculations
        data = np.array(testData)
        n = np.sum(data)  # Total number of observations
        p0 = np.sum(np.diag(data)) / n  # Proportion of agreement
        pe = np.sum(np.sum(data, axis=0) ** 2) / (n ** 2)  # Expected agreement
        kappa_value = (p0 - pe) / (1 - pe) if (1 - pe) != 0 else 0
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
        """
        # Convert to numpy array for easier calculations
        data = np.array(testData)
        # Calculate the proportion of ratings for each category
        p = np.sum(data, axis=0) / (N * n)
        P = np.sum((data / n) ** 2, axis=0)  # Proportion of agreement
        P_bar = np.sum(P) / N  # Mean of P
        P_e = np.sum(p ** 2)  # Expected agreement
        fleiss_kappa_value = (P_bar - P_e) / (1 - P_e) if (1 - P_e) != 0 else 0
        return fleiss_kappa_value