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
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
        data.sort()
        n = len(data)
        if n % 2 == 0:
            mid1 = data[n // 2 - 1]
            mid2 = data[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = data[n // 2]
        return median

    @staticmethod
    def mode(data):
        """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
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
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """
        n = len(x)
        if n != len(y):
            return None

        mean_x = Statistics3.mean(x)
        mean_y = Statistics3.mean(y)

        if mean_x is None or mean_y is None:
            return None

        numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)])
        denominator_x = sum([(x[i] - mean_x) ** 2 for i in range(n)])
        denominator_y = sum([(y[i] - mean_y) ** 2 for i in range(n)])

        if denominator_x == 0 or denominator_y == 0:
            return None

        correlation = numerator / (math.sqrt(denominator_x) * math.sqrt(denominator_y))
        return correlation

    @staticmethod
    def mean(data):
        """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

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
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

        """
        num_variables = len(data)
        correlation_matrix = [[None] * num_variables for _ in range(num_variables)]

        for i in range(num_variables):
            for j in range(num_variables):
                correlation = Statistics3.correlation(data[i], data[j])
                if correlation is not None:
                    correlation_matrix[i][j] = correlation
                else:
                    
                    mean_i = Statistics3.mean(data[i])
                    mean_j = Statistics3.mean(data[j])
                    if mean_i is not None and mean_j is not None:
                        correlation_matrix[i][j] = 1.0
                    else:
                        correlation_matrix[i][j] = None
        return correlation_matrix

    @staticmethod
    def standard_deviation(data):
        """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
        n = len(data)
        if n == 0:
            return 0.0

        mean = Statistics3.mean(data)
        if mean is None:
            return 0.0

        variance = sum([(x - mean) ** 2 for x in data]) / n
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        calculates the z-score of the given list.
        :param data: the given list, list.
        :return: the z-score of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
        n = len(data)
        if n <= 1:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores