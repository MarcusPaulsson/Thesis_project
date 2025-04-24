import math

class Statistics3:
    """
    This is a class that implements methods for calculating indicators such as median, mode, correlation matrix, and Z-score in statistics.
    """

    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The median of the data. Returns None if the input list is empty.
        """
        if not data:
            return None

        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    @staticmethod
    def mode(data):
        """
        Calculates the mode(s) of the given list.

        Args:
            data (list): The input list.

        Returns:
            list: A list containing the mode(s) of the data.  Returns an empty list if the input list is empty.
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
        Calculates the Pearson correlation coefficient between two lists.

        Args:
            x (list): The first list of numerical data.
            y (list): The second list of numerical data.

        Returns:
            float: The Pearson correlation coefficient. Returns None if the lists are of different lengths or if either standard deviation is zero.
        """
        if len(x) != len(y) or len(x) <= 1:
            return None

        n = len(x)

        sum_x = sum(x)
        sum_y = sum(y)
        sum_x_squared = sum(xi ** 2 for xi in x)
        sum_y_squared = sum(yi ** 2 for yi in y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))

        numerator = n * sum_xy - sum_x * sum_y
        denominator_x = n * sum_x_squared - sum_x ** 2
        denominator_y = n * sum_y_squared - sum_y ** 2

        if denominator_x <= 0 or denominator_y <= 0:
            return None

        denominator = math.sqrt(denominator_x * denominator_y)

        if denominator == 0:
            return None

        return numerator / denominator

    @staticmethod
    def mean(data):
        """
        Calculates the mean (average) of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The mean of the data. Returns None if the input list is empty.
        """
        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix for a given list of lists (matrix).

        Args:
            data (list of lists): A list of lists, where each inner list represents a variable.

        Returns:
            list of lists: The correlation matrix.  Returns a matrix filled with None if the input contains only one variable.
        """
        num_variables = len(data)
        correlation_matrix = []

        for i in range(num_variables):
            row = []
            for j in range(num_variables):
                if num_variables == 1:
                    row.append(None)
                else:
                    row.append(Statistics3.correlation(data[i], data[j]))
            correlation_matrix.append(row)

        return correlation_matrix

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The standard deviation of the data. Returns None if the input list is empty. Returns 0.0 if the list has only one element.
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
        Calculates the Z-scores for each element in the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            list: A list of Z-scores. Returns None if the input list is empty or if the standard deviation is zero.
        """
        if not data:
            return None

        n = len(data)
        if n <= 1:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores