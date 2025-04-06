import numpy as np

class DataStatistics:
    """
    A class for performing statistical analysis on a dataset, including methods to calculate
    sum, minimum, maximum, variance, standard deviation, and correlation.
    """

    def __init__(self, data):
        """
        Initialize the DataStatistics class with a dataset.
        
        :param data: list or array-like
        :raises ValueError: if data is empty or not numeric
        """
        if not data or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Data must be a non-empty list of numeric values.")
        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of the dataset.
        
        :return: float
        """
        return np.sum(self.data)

    def get_min(self):
        """
        Calculate the minimum value in the dataset.
        
        :return: float
        """
        return np.min(self.data)

    def get_max(self):
        """
        Calculate the maximum value in the dataset.
        
        :return: float
        """
        return np.max(self.data)

    def get_variance(self):
        """
        Calculate the sample variance of the dataset, rounded to two decimal places.
        
        :return: float
        """
        return round(np.var(self.data, ddof=1), 2)

    def get_std_deviation(self):
        """
        Calculate the sample standard deviation of the dataset, rounded to two decimal places.
        
        :return: float
        """
        return round(np.std(self.data, ddof=1), 2)

    def get_correlation(self, other_data):
        """
        Calculate the correlation coefficient with another dataset.
        
        :param other_data: list or array-like
        :return: float
        :raises ValueError: if other_data is empty or not of the same length as the data
        """
        if not other_data or len(other_data) != len(self.data):
            raise ValueError("Other data must be a non-empty list of the same length as the dataset.")
        
        other_data = np.array(other_data)
        return np.corrcoef(self.data, other_data)[0, 1]