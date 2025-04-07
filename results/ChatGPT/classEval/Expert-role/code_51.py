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
        # Convert testData to a numpy array for easier calculations
        matrix = np.array(testData)
        n = np.sum(matrix)  # Total number of observations
        
        # Calculate observed agreement
        p_o = np.sum(np.diagonal(matrix)) / n
        
        # Calculate expected agreement
        p_e = 0
        for col in range(k):
            p_e += (np.sum(matrix[:, col]) / n) ** 2
        
        # Calculate Cohen's kappa
        kappa_value = (p_o - p_e) / (1 - p_e) if (1 - p_e) != 0 else 0
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
        # Convert testData to a numpy array for easier calculations
        matrix = np.array(testData)
        
        # Calculate the proportion of ratings for each category
        p = np.sum(matrix, axis=0) / (n * N)
        
        # Calculate the observed agreement
        P = np.sum((np.sum(matrix, axis=1) / n) ** 2)
        P /= N
        
        # Calculate the expected agreement
        P_e = np.sum(p ** 2)
        
        # Calculate Fleiss' kappa
        fleiss_kappa_value = (P - P_e) / (1 - P_e) if (1 - P_e) != 0 else 0
        return fleiss_kappa_value