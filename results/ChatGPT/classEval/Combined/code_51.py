import numpy as np


class KappaCalculator:
    """
    A class to calculate Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa value of a k-dimensional matrix.
        
        :param testData: The k-dimensional matrix (list of lists) to calculate the kappa value
        :return: float, the Cohen's kappa value of the matrix
        """
        flat_data = np.array(testData).flatten()
        total = len(flat_data)
        
        observed_agreements = np.sum(flat_data * (flat_data - 1)) / (total * (total - 1))
        proportions = np.sum(testData, axis=0) / total
        expected_agreements = np.sum(proportions * (proportions - 1))
        
        if expected_agreements == 0:
            return 0.0
        return (observed_agreements - expected_agreements) / (1 - expected_agreements)

    @staticmethod
    def fleiss_kappa(testData, N, n):
        """
        Calculate Fleiss' kappa value of an N * k matrix.
        
        :param testData: Input data matrix (list of lists), N * k
        :param N: int, Number of samples
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        """
        p = np.sum(testData, axis=0) / (N * n)
        P = np.sum((np.sum(testData**2, axis=1) - n) / (n * (n - 1))) / N
        Pe = np.sum(p**2)
        
        if Pe == 1:
            return 0.0
        return (P - Pe) / (1 - Pe)

