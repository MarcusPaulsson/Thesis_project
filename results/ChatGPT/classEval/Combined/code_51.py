import numpy as np


class KappaCalculator:
    """
    A class to calculate Cohen's and Fleiss' kappa coefficients.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa value from a confusion matrix.
        
        :param testData: A square confusion matrix (2D list or array).
        :return: Cohen's kappa value (float).
        """
        testData = np.array(testData)
        observed_agreement = np.trace(testData) / np.sum(testData)
        total_ratings = np.sum(testData)
        expected_agreement = np.sum(np.square(np.sum(testData, axis=0))) / (total_ratings ** 2)
        
        # Avoid division by zero
        if expected_agreement == 1:
            return 0.0  # If expected agreement is 1, kappa is 0
        
        kappa_value = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa_value

    @staticmethod
    def fleiss_kappa(testData, N, n):
        """
        Calculate Fleiss' kappa value from a ratings matrix.
        
        :param testData: A 2D array of ratings (N samples x k categories).
        :param N: Number of samples (rows in testData).
        :param n: Number of raters (assumed to be the same for all samples).
        :return: Fleiss' kappa value (float).
        """
        testData = np.array(testData)
        p = np.sum(testData, axis=0) / (N * n)
        P = np.sum((np.sum(testData, axis=1) / n) ** 2) / N
        P_e = np.sum(p ** 2)

        # Avoid division by zero
        if P_e == 1:
            return 0.0  # If expected agreement is 1, kappa is 0
        
        fleiss_kappa_value = (P - P_e) / (1 - P_e)
        return fleiss_kappa_value

