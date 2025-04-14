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
        matrix = np.array(testData)
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        total_sum = np.sum(matrix)

        po = np.trace(matrix) / total_sum

        pe = np.sum(row_sums * col_sums) / (total_sum * total_sum)

        kappa = (po - pe) / (1 - pe)

        return kappa

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
        data = np.array(testData)
        total_ratings = N * n

        # Calculate the proportion of all assignments which were to the ith category
        p = np.sum(data, axis=0) / total_ratings

        # Calculate the extent to which raters agree for the ith subject
        P_i = (np.sum(data**2, axis=1) - n) / (n * (n - 1))

        # Calculate the mean extent to which raters agree
        P_mean = np.sum(P_i) / N

        # Calculate the expected proportion of chance agreement
        P_e = np.sum(p**2)

        # Calculate Fleiss' Kappa
        kappa = (P_mean - P_e) / (1 - P_e)

        return kappa