import math

class DataStatistics4:
    """
    This class performs advanced mathematical calculations and statistics, including:
        - Correlation coefficient
        - Skewness
        - Kurtosis
        - Probability Density Function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the Pearson correlation coefficient between two datasets.

        Args:
            data1 (list): The first list of numerical data.
            data2 (list): The second list of numerical data.

        Returns:
            float: The Pearson correlation coefficient. Returns 0.0 if the denominator is zero or if data sets are empty or of unequal length.

        Raises:
            ValueError: If the input data lists have different lengths.

        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998
        >>> DataStatistics4.correlation_coefficient([1, 1, 1], [2, 2, 2])
        0.0
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 3])
        0.9999999999999998
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 4])
        0.9819805060619659
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [1, 5, 3])
        0.4999999999999999
        """
        if not data1 or not data2:
            return 0.0

        n = len(data1)
        if n != len(data2):
            raise ValueError("Data sets must have the same length")

        sum_x = sum(data1)
        sum_y = sum(data2)
        sum_x_squared = sum(x**2 for x in data1)
        sum_y_squared = sum(y**2 for y in data2)
        sum_xy = sum(x * y for x, y in zip(data1, data2))

        numerator = n * sum_xy - sum_x * sum_y
        denominator_x = n * sum_x_squared - sum_x**2
        denominator_y = n * sum_y_squared - sum_y**2

        if denominator_x <= 0 or denominator_y <= 0:
            return 0.0

        denominator = math.sqrt(denominator_x * denominator_y)

        if denominator == 0:
            return 0.0

        return numerator / denominator

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a dataset.

        Args:
            data (list): The list of numerical data.

        Returns:
            float: The skewness of the data. Returns 0.0 if the standard deviation is zero or if the data has fewer than 3 elements.

        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463
        >>> DataStatistics4.skewness([1, 1, 1])
        0.0
        >>> DataStatistics4.skewness([1, 2, 3])
        0.0
        >>> DataStatistics4.skewness([1, 2, 4])
        1.7181079837227264
        >>> DataStatistics4.skewness([1, 5, 3])
        0.0
        """
        n = len(data)
        if n < 3:
            return 0.0

        mean = sum(data) / n
        variance = sum((x - mean)**2 for x in data) / (n - 1)
        std_dev = math.sqrt(variance)

        if std_dev == 0:
            return 0.0

        skewness = sum((x - mean)**3 for x in data) / ((n - 1) * std_dev**3)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a dataset (using the Fisher definition, where kurtosis of the normal distribution is 0).

        Args:
            data (list): The list of numerical data.

        Returns:
            float: The kurtosis of the data.  Returns NaN if the standard deviation is zero or if the data has fewer than 4 elements.

        >>> DataStatistics4.kurtosis([1, 2, 5])
        -1.5000000000000002
        >>> DataStatistics4.kurtosis([1, 20,100])
        -1.5000000000000007
        >>> DataStatistics4.kurtosis([1, 1, 1])
        nan
        >>> DataStatistics4.kurtosis([1, 2, 3])
        -1.5000000000000002
        >>> DataStatistics4.kurtosis([1, 2, 4])
        -1.4999999999999996
        >>> DataStatistics4.kurtosis([1, 5, 3])
        -1.5000000000000002
        """
        n = len(data)
        if n < 4:
            return float('NaN')

        mean = sum(data) / n
        variance = sum((x - mean)**2 for x in data) / (n - 1)
        std_dev = math.sqrt(variance)

        if std_dev == 0:
            return float('NaN')

        kurtosis = sum((x - mean)**4 for x in data) / ((n - 1) * std_dev**4) - 3
        return kurtosis

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a dataset, assuming a normal distribution.

        Args:
            data (list): The list of numerical data for which to calculate the PDF.
            mu (float): The mean of the normal distribution.
            sigma (float): The standard deviation of the normal distribution.

        Returns:
            list: A list of PDF values corresponding to each data point.

        >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
        [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]
        >>> DataStatistics4.pdf([1, 1, 1], 1, 1)
        [0.3989422804014327, 0.3989422804014327, 0.3989422804014327]
        >>> DataStatistics4.pdf([1, 2, 3], 2, 1)
        [0.24197072451914337, 0.3989422804014327, 0.24197072451914337]
        >>> DataStatistics4.pdf([1, 2, 3], 1, 2)
        [0.19947114020071635, 0.17603266338214976, 0.12098536225957168]
        >>> DataStatistics4.pdf([1, 2, 3], 2, 2)
        [0.17603266338214976, 0.19947114020071635, 0.17603266338214976]
        """
        pdf_values = []
        for x in data:
            exponent = -((x - mu)**2) / (2 * sigma**2)
            coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
            pdf = coefficient * math.exp(exponent)
            pdf_values.append(pdf)
        return pdf_values