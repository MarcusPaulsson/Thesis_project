import math
from collections import Counter

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        data.sort()
        n = len(data)
        if n % 2 == 0:
            return (data[n // 2 - 1] + data[n // 2]) / 2.0
        else:
            return data[n // 2]

    @staticmethod
    def mode(data):
        frequency = Counter(data)
        max_freq = max(frequency.values())
        return [key for key, value in frequency.items() if value == max_freq]

    @staticmethod
    def correlation(x, y):
        n = len(x)
        if n != len(y):
            raise ValueError("Lists x and y must have the same length.")
        
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)) * 
                                sum((y[i] - mean_y) ** 2 for i in range(n)))
        
        if denominator == 0:
            return 0  # Avoid division by zero
        return numerator / denominator

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        n = len(data)
        corr_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                corr_matrix[i][j] = Statistics3.correlation(data[i], data[j])
        return corr_matrix

    @staticmethod
    def standard_deviation(data):
        mean_val = Statistics3.mean(data)
        variance = sum((x - mean_val) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        mean_val = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_val) / std_dev for x in data]