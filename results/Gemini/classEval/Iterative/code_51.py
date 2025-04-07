import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """

    @staticmethod
    def kappa(data):
        """
        Calculate Cohen's kappa coefficient.

        Args:
            data (list of lists or numpy.ndarray): A square confusion matrix.

        Returns:
            float: Cohen's kappa coefficient.  Returns NaN if the denominator is zero.

        Raises:
            TypeError: if input is not a list or numpy array
            ValueError: if input is not a square matrix

        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]])
        0.25
        >>> KappaCalculator.kappa([[10, 2], [3, 5]])
        0.38095238095238093
        """
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("Input data must be a list or numpy array.")

        matrix = np.array(data)

        if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Input data must be a square matrix.")

        n = np.sum(matrix)
        if n == 0: # Handle the case where the sum of all values is zero
            return np.nan

        p_o = np.trace(matrix) / n

        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)

        p_e = np.sum(row_sums * col_sums) / (n ** 2)

        kappa = (p_o - p_e) / (1 - p_e) if (1 - p_e) !=0 else np.nan # prevent division by zero
        return kappa

    @staticmethod
    def fleiss_kappa(data):
        """
        Calculate Fleiss' kappa coefficient for inter-rater reliability.

        Args:
            data (list of lists or numpy.ndarray): A matrix where rows represent subjects and columns represent categories.
                                                    Each cell contains the number of raters who assigned that category to that subject.

        Returns:
            float: Fleiss' kappa coefficient. Returns NaN if the denominator is zero or if there are invalid inputs.

        Raises:
            TypeError: if input is not a list or numpy array
            ValueError: if input data is invalid or inconsistent

        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        ...                              [0, 2, 6, 4, 2],
        ...                              [0, 0, 3, 5, 6],
        ...                              [0, 3, 9, 2, 0],
        ...                              [2, 2, 8, 1, 1],
        ...                              [7, 7, 0, 0, 0],
        ...                              [3, 2, 6, 3, 0],
        ...                              [2, 5, 3, 2, 2],
        ...                              [6, 5, 2, 1, 0],
        ...                              [0, 2, 2, 3, 7]])
        0.20993070442195522
        """
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("Input data must be a list or numpy array.")

        matrix = np.array(data)
        N, k = matrix.shape

        n = np.sum(matrix[0, :])
        # Validate all rows have the same number of raters
        for i in range(1, N):
            if np.sum(matrix[i, :]) != n:
                raise ValueError("Number of ratings per subject must be constant.")

        p_i = np.sum(matrix, axis=0) / (N * n)
        P_i = (np.sum(matrix ** 2, axis=1) - n) / (n * (n - 1))
        P = np.sum(P_i) / N
        P_e = np.sum(p_i ** 2)

        kappa = (P - P_e) / (1 - P_e) if (1 - P_e) != 0 else np.nan # prevent division by zero
        return kappa