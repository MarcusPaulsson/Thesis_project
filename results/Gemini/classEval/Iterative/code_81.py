import math

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        calculates the median of the given list.
        :param data: the given list, list.
        :return: the median of the given list, float.
        """
        if not data:
            return None
        data_sorted = sorted(data)
        n = len(data_sorted)
        if n % 2 == 0:
            mid1 = data_sorted[n // 2 - 1]
            mid2 = data_sorted[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = data_sorted[n // 2]
        return median

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        """
        if not data:
            return []

        counts = {}
        for item in data:
            counts[item] = counts.get(item, 0) + 1

        max_count = 0
        modes = []
        for item, count in counts.items():
            if count > max_count:
                modes = [item]
                max_count = count
            elif count == max_count:
                modes.append(item)

        return modes

    @staticmethod
    def correlation(x, y):
        """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        """
        n = len(x)
        if n != len(y):
            raise ValueError("The two lists must have the same length")

        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)

        if mean_x is None or mean_y is None:
            return None

        numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
        denominator_x = sum((xi - mean_x)**2 for xi in x)
        denominator_y = sum((yi - mean_y)**2 for yi in y)

        if denominator_x == 0 or denominator_y == 0:
            return None

        denominator = math.sqrt(denominator_x * denominator_y)

        return numerator / denominator

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        """
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        calculates the correlation matrix of the given list.
        :param data: the given list, list.
        :return: the correlation matrix of the given list, list.
        """
        num_variables = len(data)
        correlation_matrix = [[None] * num_variables for _ in range(num_variables)]

        for i in range(num_variables):
            for j in range(num_variables):
                correlation_matrix[i][j] = Statistics3.correlation(data[i], data[j])

        return correlation_matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        """
        if not data:
            return 0.0

        mean = Statistics3.mean(data)

        if mean is None:
            return 0.0

        variance = sum((x - mean)**2 for x in data) / len(data)
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        """
        if not data:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores