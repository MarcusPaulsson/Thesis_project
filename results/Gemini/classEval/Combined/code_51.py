import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(testData):
        """
        Calculate Cohen's kappa coefficient.

        Args:
            testData: A square matrix representing the ratings.

        Returns:
            The Cohen's kappa coefficient.

        Raises:
            ValueError: If the input data is not a square matrix.
            ZeroDivisionError: If there is division by zero.
        """
        matrix = np.asarray(testData, dtype=float)
        if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Input must be a square matrix.")

        n = matrix.shape[0]  # Dimension of the matrix

        observed_agreement = np.trace(matrix) / np.sum(matrix)

        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        total_sum = np.sum(matrix)

        expected_agreement = np.sum(row_sums * col_sums) / (total_sum ** 2)

        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)

        return kappa


    @staticmethod
    def fleiss_kappa(testData):
        """
        Calculate Fleiss' kappa coefficient for inter-rater reliability.

        Args:
            testData: A matrix of shape (N, k) where N is the number of subjects and k is the number of categories.  Each cell contains the number of raters who assigned that category to that subject.

        Returns:
            The Fleiss' kappa coefficient.

        Raises:
            ValueError: If the input data is not a matrix.
            ZeroDivisionError: If there is division by zero.
        """

        matrix = np.asarray(testData, dtype=float)
        if len(matrix.shape) != 2:
            raise ValueError("Input must be a matrix.")

        N = matrix.shape[0]  # Number of subjects
        k = matrix.shape[1]  # Number of categories
        n = np.sum(matrix[0, :]) # Number of raters.  Assume constant number of raters

        p_j = np.sum(matrix, axis=0) / (N * n)
        P_i = (np.sum(matrix ** 2, axis=1) - n) / (n * (n - 1))
        P_bar = np.mean(P_i)
        P_e = np.sum(p_j ** 2)

        kappa = (P_bar - P_e) / (1 - P_e)

        return kappa