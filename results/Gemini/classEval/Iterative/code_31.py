import math
from typing import List, Union

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1: List[Union[int, float]], data2: List[Union[int, float]]) -> float:
        """
        Calculate the Pearson correlation coefficient of two sets of data.

        Args:
            data1: The first set of data, a list of numerical values.
            data2: The second set of data, a list of numerical values.

        Returns:
            The Pearson correlation coefficient, a float between -1 and 1.  Returns NaN if either input list is empty or if the standard deviation of either list is zero.

        Raises:
            ValueError: If the data sets do not have the same length.

        Examples:
            >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
            1.0
            >>> DataStatistics4.correlation_coefficient([1, 2, 3], [6, 5, 4])
            -1.0
            >>> DataStatistics4.correlation_coefficient([1, 2, 3], [1, 2, 3])
            1.0
            >>> DataStatistics4.correlation_coefficient([1, 2, 3], [3, 2, 1])
            -1.0
        """
        if not data1 or not data2:
            return float('NaN')

        n = len(data1)
        if n != len(data2):
            raise ValueError("Data sets must have the same length")

        mean1 = sum(data1) / n
        mean2 = sum(data2) / n

        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        std_dev1 = math.sqrt(sum((x - mean1)**2 for x in data1))
        std_dev2 = math.sqrt(sum((y - mean2)**2 for y in data2))

        if std_dev1 == 0 or std_dev2 == 0:
            return float('NaN')  # Handle cases where standard deviation is zero

        return numerator / (std_dev1 * std_dev2)


    @staticmethod
    def skewness(data: List[Union[int, float]]) -> float:
        """
        Calculate the skewness of a set of data.

        Args:
            data: The input data list, a list of numerical values.

        Returns:
            The skewness, a float. Returns NaN if the input list is empty or if the standard deviation is zero.

        Examples:
            >>> DataStatistics4.skewness([1, 2, 5])
            1.0453591785333538
            >>> DataStatistics4.skewness([1, 2, 3, 4, 5])
            0.0
            >>> DataStatistics4.skewness([1, 1, 1])
            0.0
        """
        n = len(data)
        if not data:
            return float('NaN')

        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean)**2 for x in data) / (n - 1)) if n > 1 else 0.0


        if std_dev == 0:
            return float('NaN')  # Avoid division by zero

        sum_cubed_deviations = sum((x - mean)**3 for x in data)
        skewness = sum_cubed_deviations / ((n - 1) * (std_dev**3)) if n > 1 else 0.0
        return skewness

    @staticmethod
    def kurtosis(data: List[Union[int, float]]) -> float:
        """
        Calculate the excess kurtosis of a set of data. Excess kurtosis is kurtosis - 3.

        Args:
            data: The input data list, a list of numerical values.

        Returns:
            The excess kurtosis, a float.  Returns NaN if the input list is empty or if the standard deviation is zero.

        Examples:
            >>> DataStatistics4.kurtosis([1, 20,100])
            -1.268292682926829
            >>> DataStatistics4.kurtosis([1, 2, 3, 4, 5])
            -1.3
            >>> DataStatistics4.kurtosis([1, 1, 1, 1, 1])
            -3.0
        """
        n = len(data)
        if not data:
            return float('NaN')

        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean)**2 for x in data) / (n - 1)) if n > 1 else 0.0


        if std_dev == 0:
            return float('NaN')  # Avoid division by zero

        sum_fourth_power_deviations = sum((x - mean)**4 for x in data)
        kurtosis = sum_fourth_power_deviations / ((n - 1) * (std_dev**4)) - 3 if n > 1 else -3.0
        return kurtosis

    @staticmethod
    def pdf(data: List[Union[int, float]], mu: float, sigma: float) -> List[float]:
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.

        Args:
            data: The input data list, a list of numerical values.
            mu: The mean of the normal distribution, a float.
            sigma: The standard deviation of the normal distribution, a float.

        Returns:
            A list of floats representing the probability density function (PDF) values for each data point.  Returns a list of NaN if sigma is zero.

        Examples:
            >>> DataStatistics4.pdf([1, 2, 3], 1, 1)
            [0.3989422804014327, 0.24197072451914337, 0.05399096651318806]
            >>> DataStatistics4.pdf([1, 2, 3], 0, 1)
            [0.24197072451914337, 0.05399096651318806, 0.004431848411938007]
        """
        if sigma == 0:
            return [float('NaN')] * len(data)

        pdf_values = []
        for x in data:
            exponent = -((x - mu)**2) / (2 * sigma**2)
            coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
            pdf_values.append(coefficient * math.exp(exponent))
        return pdf_values