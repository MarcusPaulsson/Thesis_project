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
        try:
            mean_value = sum(data) / len(data)
            return round(mean_value, 2)
        except TypeError:
            raise TypeError("Data must be a list of numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

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

        try:
            sorted_data = sorted(data)
            n = len(sorted_data)

            if n % 2 == 0:
                # Even number of elements
                mid1 = sorted_data[n // 2 - 1]
                mid2 = sorted_data[n // 2]
                median = (mid1 + mid2) / 2
            else:
                # Odd number of elements
                median = sorted_data[n // 2]

            if isinstance(median, float):
                return round(median, 2)
            else:
                return median
        except TypeError:
            raise TypeError("Data must be a list of numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

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

        try:
            count = Counter(data)
            max_count = max(count.values())
            modes = [key for key, value in count.items() if value == max_count]
            modes.sort()
            return modes
        except TypeError:
            raise TypeError("Data must be a list of numbers or strings.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None