import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        if not data:
            return None
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        if not data:
            return []
        frequency = Counter(data)
        max_count = max(frequency.values())
        return [num for num, count in frequency.items() if count == max_count]

    @staticmethod
    def correlation(x, y):
        if len(x) != len(y) or len(x) == 0:
            return None
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = (math.sqrt(sum((xi - mean_x) ** 2 for xi in x)) *
                       math.sqrt(sum((yi - mean_y) ** 2 for yi in y)))
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def mean(data):
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        if not data or not all(data):
            return [[None] * len(data[0])] * len(data[0])
        return [[Statistics3.correlation(row_i, row_j) for row_j in zip(*data)] for row_i in zip(*data)]

    @staticmethod
    def standard_deviation(data):
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((xi - mean_value) ** 2 for xi in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        if not data or len(set(data)) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(xi - mean_value) / std_dev for xi in data]