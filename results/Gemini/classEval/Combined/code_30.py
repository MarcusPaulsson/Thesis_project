import numpy as np

class DataStatistics2:
    """
    This is a class for performing data statistics, supporting to get the sum, minimum, maximum, variance, standard deviation, and correlation of a given dataset.
    """

    def __init__(self, data):
        """
        Initialize Data List
        :param data:list
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not data:  # Check if the list is empty
            raise ValueError("Input data list cannot be empty.")

        self.data = np.array(data)

    def get_sum(self):
        """
        Calculate the sum of data
        :return:float
        """
        return float(np.sum(self.data))

    def get_min(self):
        """
        Calculate the minimum value in the data
        :return:float
        """
        return float(np.min(self.data))

    def get_max(self):
        """
        Calculate the maximum value in the data
        :return:float
        """
        return float(np.max(self.data))

    def get_variance(self):
        """
        Calculate variance, accurate to two digits after the Decimal separator
        :return:float
        """
        variance = np.var(self.data)
        return round(float(variance), 2)

    def get_std_deviation(self):
        """
        Calculate standard deviation, accurate to two digits after the Decimal separator
        :return:float
        """
        std_deviation = np.std(self.data)
        return round(float(std_deviation), 2)

    def get_correlation(self):
        """
        Calculate correlation
        :return:float
        """
        if len(self.data) <= 1:
            return 1.0  # Or raise an exception, depending on desired behavior
        return float(np.corrcoef(self.data, self.data)[0, 1])