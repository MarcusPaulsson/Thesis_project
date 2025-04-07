import math
import statistics

class DataStatistics4:
    """
    This is a class that performs advanced mathematical calculations and statistics, including correlation coefficient, skewness, kurtosis, and probability density function (PDF) for a normal distribution.
    """

    @staticmethod
    def correlation_coefficient(data1, data2):
        """
        Calculate the correlation coefficient of two sets of data.
        :param data1: The first set of data, list.
        :param data2: The second set of data, list.
        :return: The correlation coefficient, float.
        """
        return statistics.correlation(data1, data2)

    @staticmethod
    def skewness(data):
        """
        Calculate the skewness of a set of data.
        :param data: The input data list, list.
        :return: The skewness, float.
        """
        n = len(data)
        mean = statistics.mean(data)
        variance = statistics.variance(data)
        if variance == 0:
            return float('nan')
        skewness = (n * sum((x - mean) ** 3 for x in data)) / ((n - 1) * (n - 2) * variance ** (3/2))
        return skewness

    @staticmethod
    def kurtosis(data):
        """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        """
        n = len(data)
        mean = statistics.mean(data)
        variance = statistics.variance(data)
        if variance == 0:
            return float('nan')
        kurtosis = (n * (n + 1) * sum((x - mean) ** 4 for x in data) / ((n - 1) * (n - 2) * (n - 3) * variance ** 2)) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
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
        pdf_values = []
        for x in data:
            pdf_value = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
            pdf_values.append(pdf_value)
        return pdf_values