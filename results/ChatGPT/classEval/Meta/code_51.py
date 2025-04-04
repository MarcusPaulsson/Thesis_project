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
        # Flatten the test data to calculate the confusion matrix
        testData = np.array(testData)
        total = np.sum(testData)
        p0 = np.trace(testData) / total  # Proportion of observed agreement

        # Calculate the expected agreement
        p_e = 0
        for i in range(k):
            p_e += (np.sum(testData[:, i]) / total) ** 2

        # Cohen's kappa calculation
        kappa_value = (p0 - p_e) / (1 - p_e)
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
        # Convert testData to a numpy array
        testData = np.array(testData)

        # Calculate the proportion of ratings for each category
        p = np.sum(testData, axis=0) / (N * n)

        # Calculate the overall agreement
        P_bar = np.sum(np.sum(testData**2, axis=1) - n) / (N * n * (n - 1))

        # Calculate the expected agreement
        P_e = np.sum(p**2)

        # Fleiss' kappa calculation
        fleiss_kappa_value = (P_bar - P_e) / (1 - P_e)
        return fleiss_kappa_value