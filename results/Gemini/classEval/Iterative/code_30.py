import numpy as np

class DataStatistics2:
    """
    This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initialize Data List
        :param data:list
        Raises:
            TypeError: if data is not a list or numpy array.
            ValueError: if data is empty.
        """
        if not isinstance(data, (list, np.ndarray)):
            raise TypeError("Data must be a list or numpy array.")
        if not data:
            raise ValueError("Data cannot be empty.")

        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of data
        :return: float
        """
        return float(np.sum(self.data))

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return: float
        """
        return float(np.min(self.data))

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return: float
        """
        return float(np.max(self.data))

    def get_variance(self):
        """
        Calculate variance
        :return: float
        """
        return float(np.var(self.data))

    def get_std_deviation(self):
        """
        Calculate standard deviation
        :return: float
        """
        return float(np.std(self.data))

    def get_correlation(self):
        """
        Calculate correlation.  Returns 1.0 if the data has only one element.
        :return: float
        """
        if len(self.data) <= 1:
            return 1.0
        return float(np.corrcoef(self.data, self.data)[0, 1])