import math
from collections import Counter

class Statistics3:
    """
    This class implements methods for calculating statistical indicators 
    such as median, mode, correlation matrix, mean, standard deviation, and Z-score.
    """

    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.
        :param data: List of numbers.
        :return: Median value as float or None if data is empty.
        """
        if not data:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2 if n % 2 == 0 else sorted_data[mid]

    @staticmethod
    def mode(data):
        """
        Calculates the mode of the given list.
        :param data: List of numbers.
        :return: List of modes.
        """
        if not data:
            return []
        frequency = Counter(data)
        max_freq = max(frequency.values())
        return [value for value, count in frequency.items() if count == max_freq]

    @staticmethod
    def mean(data):
        """
        Calculates the mean of the given list.
        :param data: List of numbers.
        :return: Mean value as float or None if data is empty.
        """
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.
        :param data: List of numbers.
        :return: Standard deviation as float or None if data is empty.
        """
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        Calculates the Z-score of the given list.
        :param data: List of numbers.
        :return: List of Z-scores or None if data is empty or has one element.
        """
        if not data or len(data) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]

    @staticmethod
    def correlation(x, y):
        """
        Calculates the correlation coefficient between two lists.
        :param x: First list of numbers.
        :param y: Second list of numbers.
        :return: Correlation coefficient as float or None if lists have different lengths or are empty.
        """
        if len(x) != len(y) or len(x) == 0:
            return None
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y))
        
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix for a 2D list.
        :param data: List of lists of numbers.
        :return: 2D list representing the correlation matrix.
        """
        if not data or not data[0]:
            return [[None] * len(data[0])] * len(data[0])
        
        n = len(data[0])
        corr_matrix = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                corr_matrix[i][j] = Statistics3.correlation([row[i] for row in data], [row[j] for row in data])
        return corr_matrix