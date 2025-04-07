import math
from collections import Counter

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
            float: The median of the data.  Returns None if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")
        if not data:
            return None  # Handle empty list case
        try:
            data = sorted(data)
            n = len(data)
            if n % 2 == 0:
                mid1 = data[n // 2 - 1]
                mid2 = data[n // 2]
                median = (mid1 + mid2) / 2
            else:
                median = data[n // 2]
            return float(median) # Ensure float return type
        except TypeError:
            raise TypeError("List elements must be numerical.")


    @staticmethod
    def mode(data):
        """
        Calculates the mode(s) of the given list.

        Args:
            data (list): The input list of data.

        Returns:
            list: A list containing the mode(s) of the data.  Returns an empty list if the input list is empty or if all elements appear only once.

        Raises:
            TypeError: If the input data is not a list.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")

        if not data:
            return []  # Handle empty list case

        counts = Counter(data)
        max_count = max(counts.values()) if counts else 0

        if max_count == 1 and len(counts) == len(data):  # Check for all unique values
            return []

        modes = [item for item, count in counts.items() if count == max_count]
        return modes


    @staticmethod
    def correlation(x, y):
        """
        Calculates the Pearson correlation coefficient between two lists.

        Args:
            x (list): The first list of numerical data.
            y (list): The second list of numerical data.

        Returns:
            float: The Pearson correlation coefficient between x and y. Returns 0.0 if the denominator is zero.

        Raises:
            ValueError: If the input lists are not of the same length.
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(x, list) or not isinstance(y, list):
            raise TypeError("Input data must be lists.")

        if len(x) != len(y):
            raise ValueError("Lists must be of the same length.")

        n = len(x)
        if n == 0:
            return 0.0 # Handle empty list case

        try:
            mean_x = sum(x) / n
            mean_y = sum(y) / n

            numerator = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(n)])
            denominator_x = sum([(x[i] - mean_x) ** 2 for i in range(n)])
            denominator_y = sum([(y[i] - mean_y) ** 2 for i in range(n)])
            denominator = math.sqrt(denominator_x * denominator_y)

            if denominator == 0:
                return 0.0

            return numerator / denominator
        except TypeError:
            raise TypeError("List elements must be numerical.")



    @staticmethod
    def mean(data):
        """
        Calculates the mean (average) of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The mean of the data.  Returns None if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")

        if not data:
            return None # Handle empty list case

        try:
            return float(sum(data) / len(data)) # Ensure float return type

        except TypeError:
            raise TypeError("List elements must be numerical.")


    @staticmethod
    def correlation_matrix(data):
        """
        Calculates the correlation matrix of the given list of lists (matrix).

        Args:
            data (list): A list of lists, where each inner list represents a variable.

        Returns:
            list: A correlation matrix (list of lists) representing the pairwise correlations between the variables.  Returns an empty list if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")

        if not data:
            return [] # Handle empty list case

        num_variables = len(data)
        correlation_matrix = []
        for i in range(num_variables):
            row = []
            for j in range(num_variables):
                row.append(Statistics3.correlation(data[i], data[j]))
            correlation_matrix.append(row)
        return correlation_matrix


    @staticmethod
    def standard_deviation(data):
        """
        Calculates the sample standard deviation of the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            float: The sample standard deviation of the data. Returns 0.0 if the list has fewer than 2 elements. Returns None if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")

        if not data:
            return None # Handle empty list case
        
        n = len(data)
        if n < 2:
            return 0.0 # Cannot compute stdev with fewer than 2 data points

        try:
            mean = Statistics3.mean(data) # Use the class's mean method
            variance = sum([(x - mean) ** 2 for x in data]) / (n - 1)  # Sample standard deviation (n-1)
            return math.sqrt(variance)
        except TypeError:
            raise TypeError("List elements must be numerical.")


    @staticmethod
    def z_score(data):
        """
        Calculates the Z-scores for each data point in the given list.

        Args:
            data (list): The input list of numerical data.

        Returns:
            list: A list of Z-scores corresponding to each data point in the input list. Returns a list of 0.0 if the standard deviation is zero. Returns an empty list if the input list is empty.

        Raises:
            TypeError: If the input data is not a list or contains non-numerical data.
        """
        if not isinstance(data, list):
            raise TypeError("Input data must be a list.")

        if not data:
            return []  # Handle empty list case

        try:
            mean = Statistics3.mean(data)
            std_dev = Statistics3.standard_deviation(data)

            if std_dev == 0:
                return [0.0] * len(data) # Return 0 if standard deviation is zero

            return [(x - mean) / std_dev for x in data]
        except TypeError:
            raise TypeError("List elements must be numerical.")