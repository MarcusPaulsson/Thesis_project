import math
from collections import Counter

class Statistics3:
    """
    A class to calculate various statistical measures including median, mode, correlation, mean,
    standard deviation, and z-score.
    """

    @staticmethod
    def median(data):
        """
        Calculate the median of the given list.
        :param data: List of numerical values.
        :return: Median value as float or None if the list is empty.
        """
        if not data:
            return None
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0 if len(sorted_data) % 2 == 0 else sorted_data[mid]

    @staticmethod
    def mode(data):
        """
        Calculate the mode of the given list.
        :param data: List of numerical values.
        :return: List of mode(s) or empty list if no mode exists.
        """
        if not data:
            return []
        frequency = Counter(data)
        max_freq = max(frequency.values())
        return [num for num, freq in frequency.items() if freq == max_freq]

    @staticmethod
    def correlation(x, y):
        """
        Calculate the correlation coefficient between two lists.
        :param x: First list of numerical values.
        :param y: Second list of numerical values.
        :return: Correlation coefficient as float or None if lists are empty or of unequal length.
        """
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        mean_x, mean_y = sum(x) / n, sum(y) / n
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = (math.sqrt(sum((xi - mean_x) ** 2 for xi in x)) *
                       math.sqrt(sum((yi - mean_y) ** 2 for yi in y)))
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def mean(data):
        """
        Calculate the mean of the given list.
        :param data: List of numerical values.
        :return: Mean value as float or None if the list is empty.
        """
        return sum(data) / len(data) if data else None

    @staticmethod
    def correlation_matrix(data):
        """
        Calculate the correlation matrix for a list of lists.
        :param data: List of lists containing numerical values.
        :return: 2D list representing the correlation matrix.
        """
        if not data or not all(len(row) == len(data[0]) for row in data):
            return [[None] * len(data) for _ in range(len(data[0]))]
        
        n = len(data)
        return [[Statistics3.correlation(data[i], data[j]) for j in range(n)] for i in range(n)]

    @staticmethod
    def standard_deviation(data):
        """
        Calculate the standard deviation of the given list.
        :param data: List of numerical values.
        :return: Standard deviation as float or None if the list is empty.
        """
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        Calculate the z-scores of the given list.
        :param data: List of numerical values.
        :return: List of z-scores or None if the list has one or fewer elements.
        """
        if len(data) <= 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]