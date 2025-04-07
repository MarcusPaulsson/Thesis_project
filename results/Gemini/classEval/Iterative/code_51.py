import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(testData, k):
        """
        Calculate the Cohen's kappa value of a k-dimensional matrix.
        :param testData: The k-dimensional matrix that needs to calculate the Cohen's kappa value.
        :param k: int, Matrix dimension (number of raters or categories).  Unused in calculation, but kept for consistency.
        :return: float, the Cohen's kappa value of the matrix.
        :raises ValueError: if input matrix is not square.
        :raises ValueError: if input matrix contains negative values.
        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        matrix = np.array(testData, dtype=float)

        if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Input matrix must be square.")

        if np.any(matrix < 0):
            raise ValueError("Input matrix must not contain negative values.")

        n = np.sum(matrix)  # Total number of ratings
        po = np.trace(matrix) / n  # Observed agreement
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        pe = np.sum(row_sums * col_sums) / (n ** 2)  # Expected agreement
        kappa = (po - pe) / (1 - pe)

        return kappa


    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss' kappa value of an N * k matrix.
        :param testData: Input data matrix, N * k, where N is the number of subjects and k is the number of categories.
        :param N: int, Number of subjects.
        :param k: int, Number of categories.
        :param n: int, Number of raters.
        :return: float, Fleiss' kappa value.
        :raises ValueError: if the shape of the input data does not match the declared N and k.
        :raises ValueError: if the number of raters is not consistent across subjects.

        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        >>>                              [0, 2, 6, 4, 2],
        >>>                              [0, 0, 3, 5, 6],
        >>>                              [0, 3, 9, 2, 0],
        >>>                              [2, 2, 8, 1, 1],
        >>>                              [7, 7, 0, 0, 0],
        >>>                              [3, 2, 6, 3, 0],
        >>>                              [2, 5, 3, 2, 2],
        >>>                              [6, 5, 2, 1, 0],
        >>>                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        matrix = np.array(testData, dtype=float)

        if matrix.shape != (N, k):
            raise ValueError("Shape of input data matrix must be (N, k).")

        # Check for consistent number of ratings per subject
        ratings_per_subject = np.sum(matrix, axis=1)
        if not np.all(ratings_per_subject == n):
            raise ValueError("Number of ratings per subject must be consistent.")

        p = np.sum(matrix, axis=0) / (N * n)  # Proportion of all assignments which were to i-th category
        P = (np.sum(matrix ** 2, axis=1) - n) / (n * (n - 1)) # Agreement among raters for i-th subject
        P_mean = np.mean(P) # Average agreement among raters
        Pe = np.sum(p ** 2) # The extent to which the amount of agreement that could be expected by chance
        kappa = (P_mean - Pe) / (1 - Pe)

        return kappa