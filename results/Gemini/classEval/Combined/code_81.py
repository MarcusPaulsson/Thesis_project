import math

class Statistics3:
    """
    This class implements methods for calculating statistical indicators such as
    median, mode, correlation, correlation matrix, standard deviation, mean, and Z-score.
    """

    @staticmethod
    def median(data):
        """
        Calculates the median of the given list.

        Args:
            data (list): A list of numerical data.

        Returns:
            float: The median of the data. Returns None if the input list is empty.

        Raises:
            TypeError: If the input is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        if not data:
            return None
        try:
            sorted_data = sorted(data)
            n = len(sorted_data)
            if n % 2 == 0:
                mid1 = sorted_data[n // 2 - 1]
                mid2 = sorted_data[n // 2]
                median = (mid1 + mid2) / 2
            else:
                median = sorted_data[n // 2]
            return median
        except TypeError:
            raise TypeError("List must contain numerical data.")

    @staticmethod
    def mode(data):
        """
        Calculates the mode(s) of the given list.

        Args:
            data (list): A list of data.

        Returns:
            list: A sorted list of the mode(s). Returns an empty list if the input list is empty.

        Raises:
            TypeError: If the input is not a list.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")

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

        return sorted(modes)

    @staticmethod
    def correlation(x, y):
        """
        Calculates the Pearson correlation coefficient between two lists.

        Args:
            x (list): A list of numerical data.
            y (list): A list of numerical data.

        Returns:
            float: The Pearson correlation coefficient. Returns None if the lists are of different lengths
                   or if either list has a standard deviation of zero.

        Raises:
            TypeError: If either input is not a list or contains non-numerical data.
            ValueError: If either list contains fewer than two elements.
        """
        if not isinstance(x, list) or not isinstance(y, list):
            raise TypeError("Inputs must be lists.")
        if len(x) != len(y):
            return None
        if len(x) < 2:
            return None

        try:
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

            return numerator / denominator
        except TypeError:
            raise TypeError("Lists must contain numerical data.")

    @staticmethod
    def mean(data):
        """
        Calculates the mean of the given list.

        Args:
            data (list): A list of numerical data.

        Returns:
            float: The mean of the data. Returns None if the input list is empty.

        Raises:
            TypeError: If the input is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")
        if not data:
            return None
        try:
            return sum(data) / len(data)
        except TypeError:
            raise TypeError("List must contain numerical data.")

    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix of the given list of lists.

        Args:
            data (list): A list of lists, where each inner list represents a variable.

        Returns:
            list: A correlation matrix (list of lists).  Returns a matrix filled with None if
            the input contains only one variable.

        Raises:
            TypeError: If the input is not a list of lists.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")

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
        Calculates the sample standard deviation of the given list.

        Args:
            data (list): A list of numerical data.

        Returns:
            float: The sample standard deviation of the data. Returns None if the input list is empty.
                   Returns 0.0 if the list contains only one element.

        Raises:
            TypeError: If the input is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")

        if not data:
            return None

        n = len(data)
        if n <= 1:
            return 0.0

        try:
            mean = Statistics3.mean(data)
            variance = sum((x - mean) ** 2 for x in data) / (n - 1)
            return math.sqrt(variance)
        except TypeError:
            raise TypeError("List must contain numerical data.")

    @staticmethod
    def z_score(data):
        """
        Calculates the Z-scores of the given list.

        Args:
            data (list): A list of numerical data.

        Returns:
            list: A list of Z-scores. Returns None if the input list is empty or contains only one element,
                  or if the standard deviation is zero.

        Raises:
            TypeError: If the input is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input must be a list.")

        if not data or len(data) <= 1:
            return None

        try:
            mean = Statistics3.mean(data)
            std_dev = Statistics3.standard_deviation(data)

            if std_dev == 0:
                return None

            z_scores = [(x - mean) / std_dev for x in data]
            return z_scores
        except TypeError:
            raise TypeError("List must contain numerical data.")