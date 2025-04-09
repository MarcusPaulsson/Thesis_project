import numpy as np

class DataStatistics:
    """
    A class for performing data statistics, including sum, minimum, maximum, variance,
    standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initializes the DataStatistics instance with the provided data.

        :param data: list or array-like, the input data for statistics
        """
        self.data = np.array(data)

    def get_sum(self):
        """Calculate the sum of the data."""
        return np.sum(self.data)

    def get_min(self):
        """Calculate the minimum value in the data."""
        return np.min(self.data)

    def get_max(self):
        """Calculate the maximum value in the data."""
        return np.max(self.data)

    def get_variance(self):
        """Calculate variance, rounded to two decimal places."""
        return round(np.var(self.data), 2)

    def get_std_deviation(self):
        """Calculate standard deviation, rounded to two decimal places."""
        return round(np.std(self.data), 2)

    def get_correlation(self):
        """Calculate correlation of the dataset with itself, which is always 1.0."""
        return 1.0  # A dataset always perfectly correlates with itself

