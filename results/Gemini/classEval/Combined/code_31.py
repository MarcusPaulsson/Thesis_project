import math

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """


    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data,list.
        :param data2: The second set of data,list.
        :return: The correlation coefficient, float.
        """
        if len(data1) != len(data2):
            raise ValueError("Data sets must have the same length")

        n = len(data1)
        if n <= 1:
            return 0.0

        mean1 = sum(data1) / n
        mean2 = sum(data2) / n

        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(data1, data2))
        denominator1 = sum((x - mean1) ** 2 for x in data1)
        denominator2 = sum((y - mean2) ** 2 for y in data2)

        if denominator1 == 0 or denominator2 == 0:
            return 0.0  # Handle cases where one or both datasets have zero variance

        correlation = numerator / math.sqrt(denominator1 * denominator2)
        return correlation

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        """
        n = len(data)
        if n < 3:
            return 0.0

        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))

        if std_dev == 0:
            return 0.0

        skewness = sum((x - mean) ** 3 for x in data) / ((n - 1) * std_dev ** 3)
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        """
        n = len(data)
        if n < 4:
            return float('NaN')

        mean = sum(data) / n
        std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))

        if std_dev == 0:
            return float('NaN')

        kurtosis = sum((x - mean) ** 4 for x in data) / ((n - 1) * std_dev ** 4) - 3
        return kurtosis

    @staticmethod
    def pdf(data, mu, sigma):
        """
        Calculate the probability density function (PDF) of a set of data under a normal distribution.
        :param data: The input data list, list.
        :param mu: The mean of the normal distribution, float.
        :param sigma: The standard deviation of the normal distribution, float.
        :return: The probability density function (PDF), list.
        """
        if sigma <= 0:
            raise ValueError("Standard deviation (sigma) must be positive.")

        pdf_values = []
        for x in data:
            exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
            coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
            pdf = coefficient * math.exp(exponent)
            pdf_values.append(pdf)
        return pdf_values