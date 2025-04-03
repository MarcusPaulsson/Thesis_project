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
        # Convert list to numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the agreement
        n = np.sum(testData)
        p0 = np.sum(np.diag(testData)) / n  # observed agreement
        pe = np.sum(np.sum(testData, axis=0)**2) / (n**2)  # expected agreement
        
        # Cohen's kappa calculation
        kappa_value = (p0 - pe) / (1 - pe)
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
        # Convert list to numpy array for easier manipulation
        testData = np.array(testData)
        
        # Calculate the proportion of each category
        p = np.sum(testData, axis=0) / (n * N)
        
        # Calculate the expected agreement
        P_e = np.sum(p**2)
        
        # Calculate the observed agreement
        P_o = 0
        for i in range(N):
            pi = np.sum(testData[i, :]**2) / (n**2)
            P_o += pi
        P_o /= N
        
        # Fleiss' kappa calculation
        kappa_value = (P_o - P_e) / (1 - P_e)
        return kappa_value