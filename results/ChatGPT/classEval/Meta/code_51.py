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
        """
        # Convert to numpy array for easier calculations
        matrix = np.array(testData)
        n = np.sum(matrix)
        total_agreement = np.sum(np.diag(matrix))
        total_raters = matrix.sum(axis=1)

        # Calculate the observed agreement
        p_o = total_agreement / n
        
        # Calculate the expected agreement
        p_e = np.sum((total_raters / n) ** 2)
        
        # Calculate Cohen's kappa
        kappa_value = (p_o - p_e) / (1 - p_e) if (1 - p_e) != 0 else 0
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
        matrix = np.array(testData)
        
        # Calculate the proportion of raters who selected each category
        p = np.sum(matrix, axis=0) / (N * n)
        
        # Calculate the observed agreement
        P = np.sum((np.sum(matrix, axis=1) / n) ** 2) / N
        
        # Calculate the expected agreement
        P_e = np.sum(p ** 2)
        
        # Calculate Fleiss' kappa
        kappa_value = (P - P_e) / (1 - P_e) if (1 - P_e) != 0 else 0
        return kappa_value