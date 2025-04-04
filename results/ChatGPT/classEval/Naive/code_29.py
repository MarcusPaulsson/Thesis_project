from collections import Counter

class DataStatistics:
    """
    This class performs statistical calculations: mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the decimal separator.
        
        :param data: list, data list
        :return: float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        if not data:
            return 0.0
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the decimal separator.
        
        :param data: list, data list
        :return: float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        if not data:
            return 0.0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
        else:
            return round(sorted_data[mid], 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data.
        
        :param data: list, data list
        :return: list, the mode(s)
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        if not data:
            return []
        frequency = Counter(data)
        max_count = max(frequency.values())
        modes = [value for value, count in frequency.items() if count == max_count]
        return modes