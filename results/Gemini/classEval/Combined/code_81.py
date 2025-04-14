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
            float: The median of the data.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
            ValueError: If the input data list is empty.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not data:
            raise ValueError("Input data list cannot be empty.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Input data must contain only numerical values.")

        n = len(data)
        sorted_data = sorted(data)  # Avoid modifying the original list
        if n % 2 == 0:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_data[n // 2]
        return median

    @staticmethod
    def mode(data):
        """
        Calculates the mode(s) of the given list.

        Args:
            data (list): The input list.

        Returns:
            list: A list containing the mode(s).  If all elements appear only once, returns the original list.

        Raises:
            TypeError: If the input data is not a list.
            ValueError: If the input data list is empty.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not data:
            raise ValueError("Input data list cannot be empty.")

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

        if len(modes) == len(data) and len(set(data)) == len(data):
            return modes
        
        return modes

    @staticmethod
    def mean(data):
        """
        Calculates the mean of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The mean of the data, or None if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Input data must contain only numerical values.")

        if not data:
            return None
        return sum(data) / len(data)

    @staticmethod
    def standard_deviation(data):
        """
        Calculates the standard deviation of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The standard deviation of the data, or None if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Input data must contain only numerical values.")

        n = len(data)
        if n == 0:
            return None

        mean = Statistics3.mean(data)
        if mean is None:
            return None

        variance = sum([(x - mean) ** 2 for x in data]) / n
        return math.sqrt(variance)

    @staticmethod
    def z_score(data):
        """
        Calculates the z-scores of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            list: A list of z-scores, or None if the standard deviation is zero or the input list has fewer than 2 elements.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise TypeError("Input data must contain only numerical values.")

        n = len(data)
        if n <= 1:
            return None

        mean = Statistics3.mean(data)
        std_dev = Statistics3.standard_deviation(data)

        if std_dev == 0:
            return None

        if mean is None or std_dev is None:
            return None

        z_scores = [(x - mean) / std_dev for x in data]
        return z_scores

    @staticmethod
    def correlation(x, y):
        """
        Calculates the Pearson correlation coefficient between two lists.

        Args:
            x (list): The first list of numerical data.
            y (list): The second list of numerical data.

        Returns:
            float: The Pearson correlation coefficient, or None if the lists have different lengths or the standard deviation of either list is zero.

        Raises:
            TypeError: If either input is not a list or contains non-numerical data.
        """
        if not isinstance(x, list) or not isinstance(y, list):
            raise TypeError("Inputs must be lists.")
        if not all(isinstance(val, (int, float)) for val in x) or not all(isinstance(val, (int, float)) for val in y):
            raise TypeError("Inputs must contain only numerical values.")

        if len(x) != len(y):
            return None

        n = len(x)
        if n <= 1:
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
    def correlation_matrix(data):
        """
        Calculates the correlation matrix for a list of lists.

        Args:
            data (list): A list of lists, where each inner list represents a variable.

        Returns:
            list: A correlation matrix (list of lists), where each element (i, j) represents the correlation between variable i and variable j. Returns a matrix filled with None if the input is invalid.

        Raises:
            TypeError: If the input is not a list of lists or if any inner list contains non-numerical data.
        """
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            return [[None] * 3 for _ in range(3)]

        for row in data:
            if not all(isinstance(val, (int, float)) for val in row):
                return [[None] * 3 for _ in range(3)]

        num_variables = len(data)
        if num_variables == 0:
            return [[None] * 3 for _ in range(3)]

        matrix_width = len(data[0]) if data else 0
        correlation_matrix = [[None] * matrix_width for _ in range(num_variables)]

        for i in range(num_variables):
            for j in range(num_variables):
                correlation = Statistics3.correlation(data[i], data[j])
                if correlation is not None:
                    correlation_matrix[i] = [correlation] * matrix_width
                    break
                else:
                    correlation_matrix[i] = [None] * matrix_width
                    break
        return correlation_matrix