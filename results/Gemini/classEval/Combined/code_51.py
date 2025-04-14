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
            testData: A square matrix representing the confusion matrix.  Rows and columns
                      represent the categories being rated.

        Returns:
            float: Cohen's kappa value.

        Raises:
            ValueError: if the input matrix is not square.
        """
        matrix = np.array(testData)
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Input matrix must be square.")

        n = len(matrix)
        total_sum = np.sum(matrix)
        observed_agreement = np.trace(matrix) / total_sum

        row_sums = np.sum(matrix, axis=1)
        col_sums = np.sum(matrix, axis=0)

        expected_agreement = np.sum(row_sums * col_sums) / (total_sum ** 2)

        kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
        return kappa

    @staticmethod
    def fleiss_kappa(testData):
        """
        Calculate Fleiss' kappa coefficient for inter-rater reliability.

        Args:
            testData: A matrix where rows represent subjects and columns represent categories.
                      Each cell contains the number of raters who assigned that category to that subject.

        Returns:
            float: Fleiss' kappa value.
        """
        data = np.array(testData)
        N, k = data.shape
        n = np.sum(data[0, :])  # Assuming all subjects have the same number of ratings

        total_ratings = N * n

        # Calculate the proportion of all assignments which were to the ith category
        p_i = np.sum(data, axis=0) / total_ratings

        # Calculate the extent to which raters agree for the jth subject
        P_j = (np.sum(data**2, axis=1) - n) / (n * (n - 1))

        # Calculate the mean extent to which raters agree
        P_mean = np.mean(P_j)

        # Calculate the extent to which agreement is expected by chance
        P_e = np.sum(p_i**2)

        # Calculate Fleiss' Kappa
        kappa = (P_mean - P_e) / (1 - P_e)

        return kappa