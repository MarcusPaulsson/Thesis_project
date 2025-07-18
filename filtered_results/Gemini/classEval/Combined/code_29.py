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
        if not data:
            return 0.00
        
        mean_value = sum(data) / len(data)
        return round(mean_value, 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        if not data:
            return 0.00

        sorted_data = sorted(data)
        n = len(sorted_data)

        if n % 2 == 0:
            # Even number of elements
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            median_value = (mid1 + mid2) / 2
        else:
            # Odd number of elements
            median_value = sorted_data[n // 2]
        
        return round(float(median_value), 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        if not data:
            return []

        counts = Counter(data)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
        modes.sort()
        return modes