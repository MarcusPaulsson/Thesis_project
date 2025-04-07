import math
from collections import Counter

class Statistics3:
    @staticmethod
    def median(data):
        if not data:
            return None
        data.sort()
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    @staticmethod
    def mode(data):
        if not data:
            return []
        count = Counter(data)
        max_count = max(count.values())
        return [num for num, cnt in count.items() if cnt == max_count]

    @staticmethod
    def correlation(x, y):
        if len(x) != len(y) or len(x) < 2:
            return None
        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)
        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y))
        return numerator / denominator if denominator != 0 else None

    @staticmethod
    def mean(data):
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        if not data or not data[0]:
            return [[None] * len(data[0])] * len(data) if data else []
        n = len(data[0])
        return [[Statistics3.correlation([row[i] for row in data], [row[j] for row in data]) for j in range(n)] for i in range(n)]

    @staticmethod
    def standard_deviation(data):
        if not data:
            return None
        mean_value = Statistics3.mean(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        if not data or len(set(data)) == 1:
            return None
        mean_value = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)
        return [(x - mean_value) / std_dev for x in data]