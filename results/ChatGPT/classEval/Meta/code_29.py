from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        data = sorted(data)
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            median_value = (data[mid - 1] + data[mid]) / 2
        else:
            median_value = data[mid]
        return round(median_value, 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:list, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        frequency = Counter(data)
        max_freq = max(frequency.values())
        modes = [key for key, count in frequency.items() if count == max_freq]
        return modes if len(modes) > 1 else modes[0]