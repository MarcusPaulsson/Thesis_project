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
        # Convert input to numpy array
        testData = np.array(testData)

        # Calculate observed agreement
        total = np.sum(testData)
        observed_agreement = np.sum(np.diag(testData)) / total

        # Calculate expected agreement
        row_sums = np.sum(testData, axis=1)
        col_sums = np.sum(testData, axis=0)
        expected_agreement = np.sum((row_sums * col_sums) / (total ** 2))

        # Calculate Cohen's kappa
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss kappa value of an N * k matrix
        :param testData: Input data matrix, N * k
        :param N: int, Number of samples
        :param k: int, Number of categories
        :param n: int, Number of raters
        :return: float, Fleiss kappa value
        """
        # Convert input to numpy array
        testData = np.array(testData)

        # Calculate the proportion of each category
        pi = np.sum(testData, axis=0) / (N * n)

        # Calculate the overall agreement
        P = np.sum((np.sum(testData**2, axis=1) - n) / (n * (n - 1))) / N

        # Calculate the expected agreement
        Pe = np.sum(pi**2)

        # Calculate Fleiss' kappa
        fleiss_kappa_value = (P - Pe) / (1 - Pe)
        return fleiss_kappa_value