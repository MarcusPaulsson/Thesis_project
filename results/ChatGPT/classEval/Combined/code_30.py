import numpy as np

class DataStatistics:
    """
    A class for performing basic statistical calculations on a dataset.
    Supports sum, minimum, maximum, variance, standard deviation, and correlation.
    """

    def __init__(self, data):
        """
        Initialize the DataStatistics object with a dataset.
        
        :param data: list or array-like, the dataset to analyze
        """
        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of the dataset.
        
        :return: float, the sum of the data
        """
        return np.sum(self.data)

    def get_min(self):
        """
        Calculate the minimum value in the dataset.
        
        :return: float, the minimum value
        """
        return np.min(self.data)

    def get_max(self):
        """
        Calculate the maximum value in the dataset.
        
        :return: float, the maximum value
        """
        return np.max(self.data)

    def get_variance(self):
        """
        Calculate the sample variance of the dataset, rounded to two decimal places.
        
        :return: float, the variance of the data
        """
        return round(np.var(self.data, ddof=1), 2)

    def get_std_deviation(self):
        """
        Calculate the sample standard deviation of the dataset, rounded to two decimal places.
        
        :return: float, the standard deviation of the data
        """
        return round(np.std(self.data, ddof=1), 2)

    def get_correlation(self):
        """
        Calculate the correlation of the dataset with itself (always 1.0).
        
        :return: float, the correlation coefficient
        """
        return 1.0  # Correlation of a dataset with itself is always 1.0