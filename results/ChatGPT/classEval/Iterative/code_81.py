import math
from collections import Counter

class Statistics3:
    """
    A class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.
        :param data: The given list, list.
        :return: The median of the given list, float.
        """
        if not data:
            raise ValueError("The data list cannot be empty.")
        data = sorted(data)
        n = len(data)
        mid = n // 2
        return (data[mid - 1] + data[mid]) / 2 if n % 2 == 0 else data[mid]

    @staticmethod
    def mode(data):
        """
        Calculates the mode of the given list.
        :param data: The given list, list.
        :return: The mode of the given list, list.
        """
        if not data:
            raise ValueError("The data list cannot be empty.")
        count = Counter(data)
        max_count = max(count.values())
        modes = [key for key, value in count.items() if value == max_count]
        return modes if len(modes) < len(data) else []

    @staticmethod
    def mean(data):
        """
        Calculates the mean of the given list.
        :param data: The given list, list.
        :return: The mean of the given list, float.
        """
        if not data:
            raise ValueError("The data list cannot be empty.")
        return sum(data) / len(data)

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.
        :param data: The given list, list.
        :return: The standard deviation of the given list, float.
        """
        if not data:
            raise ValueError("The data list cannot be empty.")
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        Calculates the z-score of the given list.
        :param data: The given list, list.
        :return: The z-score of the given list, list.
        """
        if not data:
            raise ValueError("The data list cannot be empty.")
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]

    @staticmethod
    def correlation(x, y):
        """
        Calculates the correlation of the given lists.
        :param x: The first list, list.
        :param y: The second list, list.
        :return: The correlation of the given lists, float.
        """
        if len(x) != len(y):
            raise ValueError("The two lists must have the same length.")
        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
        denominator_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
        return numerator / (denominator_x * denominator_y) if denominator_x and denominator_y else 0

    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix of the given list of lists.
        :param data: The given list of lists, list.
        :return: The correlation matrix, list of lists.
        """
        if not data or any(len(row) != len(data[0]) for row in data):
            raise ValueError("All rows must have the same length and data must not be empty.")
        n = len(data)
        return [[Statistics3.correlation(data[i], data[j]) for j in range(n)] for i in range(n)]