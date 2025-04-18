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
        """
        if not data:
            return 0.00
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        if not data:
            return 0.00
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            # Even number of elements
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
        else:
            # Odd number of elements
            return sorted_data[n // 2]

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        """
        if not data:
            return []

        count = Counter(data)
        max_count = max(count.values())
        modes = [key for key, value in count.items() if value == max_count]
        modes.sort()
        return modes