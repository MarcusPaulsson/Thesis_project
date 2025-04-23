import numpy as np

class KappaCalculator:
    """
    This is a class as KappaCalculator, supporting to calculate Cohen's and Fleiss' kappa coefficient.
    """


    @staticmethod
    def kappa(testData, k):
        """
        Calculate the Cohen's kappa value of a k-dimensional matrix.

        Args:
            testData (list of lists or numpy.ndarray): The k-dimensional matrix.
            k (int): Matrix dimension.

        Returns:
            float: The Cohen's kappa value of the matrix.

        Raises:
            TypeError: If testData is not a list or numpy array.
            ValueError: If the input matrix is not square.

        >>> KappaCalculator.kappa([[2, 1, 1], [1, 2, 1], [1, 1, 2]], 3)
        0.25
        """
        try:
            matrix = np.array(testData, dtype=float)
        except:
            raise TypeError("Input data must be convertible to a numpy array.")

        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Input matrix must be square.")

        n = matrix.shape[0]
        if n != k:
            print("Warning: Provided dimension k does not match the actual dimension of the matrix.")


        po = np.trace(matrix) / np.sum(matrix)
        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)
        pe = np.sum(row_sums * col_sums) / (np.sum(matrix) ** 2)
        kappa = (po - pe) / (1 - pe)
        return kappa

    @staticmethod
    def fleiss_kappa(testData, N, k, n):
        """
        Calculate the Fleiss' kappa value of an N * k matrix.

        Args:
            testData (list of lists or numpy.ndarray): Input data matrix, N * k.
            N (int): Number of subjects.
            k (int): Number of categories.
            n (int): Number of raters.

        Returns:
            float: Fleiss' kappa value.

        Raises:
            TypeError: If testData is not a list or numpy array.
            ValueError: If the dimensions of the input data are inconsistent with N and k.

        >>> KappaCalculator.fleiss_kappa([[0, 0, 0, 0, 14],
        ...                              [0, 2, 6, 4, 2],
        ...                              [0, 0, 3, 5, 6],
        ...                              [0, 3, 9, 2, 0],
        ...                              [2, 2, 8, 1, 1],
        ...                              [7, 7, 0, 0, 0],
        ...                              [3, 2, 6, 3, 0],
        ...                              [2, 5, 3, 2, 2],
        ...                              [6, 5, 2, 1, 0],
        ...                              [0, 2, 2, 3, 7]], 10, 5, 14)
        0.20993070442195522
        """
        try:
            data = np.array(testData, dtype=float)
        except:
            raise TypeError("Input data must be convertible to a numpy array.")

        if data.shape != (N, k):
            raise ValueError("Input data dimensions are inconsistent with N and k.")

        total_ratings = N * n

        # Calculate the proportion of all assignments which were to the j-th category
        p_j = np.sum(data, axis=0) / total_ratings

        # Calculate the extent to which raters agree for the i-th subject
        P_i = (np.sum(data**2, axis=1) - n) / (n * (n - 1))

        # Calculate the mean extent to which raters agree
        P_mean = np.sum(P_i) / N

        # Calculate the expected extent of chance agreement
        P_e = np.sum(p_j**2)

        # Calculate Fleiss' Kappa
        kappa = (P_mean - P_e) / (1 - P_e)

        return kappa