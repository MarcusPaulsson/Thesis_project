import math
from collections import Counter

class Statistics3:
    """
    This class implements methods for calculating statistical indicators
    such as median, mode, correlation, mean, correlation matrix,
    standard deviation, and Z-score.
    """

    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.
        :param data: The given list (list of numbers).
        :return: The median of the given list (float).
        """
        n = len(data)
        if n == 0:
            raise ValueError("Data list is empty")
        sorted_data = sorted(data)
        mid = n // 2
        return (sorted_data[mid] + sorted_data[mid - 1]) / 2 if n % 2 == 0 else sorted_data[mid]

    @staticmethod
    def mode(data):
        """
        Calculates the mode of the given list.
        :param data: The given list (list of numbers).
        :return: The mode of the given list (list).
        """
        if not data:
            raise ValueError("Data list is empty")
        frequency = Counter(data)
        max_count = max(frequency.values())
        return [num for num, count in frequency.items() if count == max_count]

    @staticmethod
    def correlation(x, y):
        """
        Calculates the correlation of the given lists.
        :param x: The first list (list of numbers).
        :param y: The second list (list of numbers).
        :return: The correlation of the given lists (float).
        """
        if len(x) != len(y):
            raise ValueError("Lists must be of the same length")
        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / n
        std_x = Statistics3.standard_deviation(x)
        std_y = Statistics3.standard_deviation(y)
        return covariance / (std_x * std_y)

    @staticmethod
    def mean(data):
        """
        Calculates the mean of the given list.
        :param data: The given list (list of numbers).
        :return: The mean of the given list (float).
        """
        if not data:
            raise ValueError("Data list is empty")
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix of the given list of lists.
        :param data: The given list of lists (2D list).
        :return: The correlation matrix of the given list (list of lists).
        """
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Input must be a 2D list")
        num_vars = len(data)
        return [[Statistics3.correlation(data[i], data[j]) for j in range(num_vars)] for i in range(num_vars)]

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.
        :param data: The given list (list of numbers).
        :return: The standard deviation of the given list (float).
        """
        if not data:
            raise ValueError("Data list is empty")
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        Calculates the z-score of the given list.
        :param data: The given list (list of numbers).
        :return: The z-score of the given list (list).
        """
        if not data:
            raise ValueError("Data list is empty")
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]