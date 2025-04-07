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
        # Convert to numpy array for easier manipulation
        data = np.array(testData)
        
        # Calculate the total number of observations
        total = np.sum(data)
        
        # Calculate the observed agreement
        observed_agreement = np.sum(np.diag(data)) / total
        
        # Calculate the expected agreement
        row_sums = np.sum(data, axis=1)
        col_sums = np.sum(data, axis=0)
        expected_agreement = np.sum((row_sums * col_sums) / (total ** 2))
        
        # Cohen's Kappa calculation
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
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
        # Convert to numpy array for easier manipulation
        data = np.array(testData)
        
        # Calculate the total number of raters
        p = np.sum(data, axis=1) / n
        
        # Calculate the overall agreement
        P_bar = np.sum(p ** 2) / N
        
        # Calculate the expected agreement
        P_e = np.sum((np.sum(data, axis=0) / (N * n)) ** 2)
        
        # Fleiss' Kappa calculation
        fleiss_kappa_value = (P_bar - P_e) / (1 - P_e)
        return fleiss_kappa_value