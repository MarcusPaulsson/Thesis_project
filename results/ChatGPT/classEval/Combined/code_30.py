import numpy as np

class DataStatistics:
    """
    A class for performing data statistics, including sum, minimum, maximum, variance, 
    standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initialize the DataStatistics instance with a list of numeric values.
        
        :param data: list of numeric values
        :raises ValueError: if data is not a list or is empty
        """
        if not isinstance(data, list) or not data:
            raise ValueError("Input data must be a non-empty list.")
        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of the data.
        :return: float
        """
        return np.sum(self.data)

    def get_min(self):
        """
        Calculate the minimum value in the data.
        :return: float
        """
        return np.min(self.data)

    def get_max(self):
        """
        Calculate the maximum value in the data.
        :return: float
        """
        return np.max(self.data)

    def get_variance(self):
        """
        Calculate the variance of the data, accurate to two decimal places.
        :return: float
        """
        return round(np.var(self.data, ddof=0), 2)

    def get_std_deviation(self):
        """
        Calculate the standard deviation of the data, accurate to two decimal places.
        :return: float
        """
        return round(np.std(self.data, ddof=0), 2)

    def get_correlation(self):
        """
        Calculate the correlation of the dataset with itself, which will always return 1.0.
        :return: float
        """
        return 1.0  # Correlation of a dataset with itself is always 1.0