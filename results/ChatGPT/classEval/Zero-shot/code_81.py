import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        data = sorted(data)
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    @staticmethod
    def mode(data):
        count = Counter(data)
        max_count = max(count.values())
        return [key for key, value in count.items() if value == max_count]

    @staticmethod
    def correlation(x, y):
        n = len(x)
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)) * sum((y[i] - mean_y) ** 2 for i in range(n)))
        return numerator / denominator if denominator != 0 else 0

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        n = len(data)
        return [[Statistics3.correlation(data[i], data[j]) for j in range(n)] for i in range(n)]

    @staticmethod
    def standard_deviation(data):
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]