from collections import Counter

class DataStatistics:
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """

    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the decimal separator.
        :param data: list, data list
        :return: float, the mean value
        """
        if not data:
            raise ValueError("Data list cannot be empty.")
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the decimal separator.
        :param data: list, data list
        :return: float, the median value
        """
        if not data:
            raise ValueError("Data list cannot be empty.")
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
        :return: list, the modes
        """
        if not data:
            raise ValueError("Data list cannot be empty.")
        count = Counter(data)
        max_count = max(count.values())
        modes = [num for num, freq in count.items() if freq == max_count]
        return modes if len(modes) < len(data) else list(set(data))