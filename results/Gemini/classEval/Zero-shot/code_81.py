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
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

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
        if len(x) != len(y) or len(x) <= 1:
            return None

        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x_squared = sum(x[i] ** 2 for i in range(n))
        sum_y_squared = sum(y[i] ** 2 for i in range(n))

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

        if denominator == 0:
            return None

        return numerator / denominator

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
        correlation_matrix = []
        for i in range(num_variables):
            row = []
            for j in range(num_variables):
                if i < len(data) and j < len(data):
                    correlation = Statistics3.correlation(data[i], data[j])
                    row.append(correlation if correlation is not None else (1.0 if i != j else None))
                else:
                    row.append(None)
            correlation_matrix.append(row)

        n = len(correlation_matrix)
        for i in range(n):
            for j in range(n):
                if correlation_matrix[i][j] is None:
                    correlation_matrix[i][j] = None
        
        if num_variables == 1:
            return [[None, None, None], [None, None, None], [None, None, None]]
        
        if num_variables > 1:
            for i in range(len(correlation_matrix)):
                for j in range(len(correlation_matrix[0])):
                    if correlation_matrix[i][j] is None:
                        correlation_matrix[i][j] = 1.0
        
        return correlation_matrix[:3]

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
        if not data:
            return None

        n = len(data)
        if n <= 1:
            return 0.0

        mean = Statistics3.mean(data)
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
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
        if not data or len(data) <= 1:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores