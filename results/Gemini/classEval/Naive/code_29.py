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
            return 0.00  # Handle empty list case

        total = sum(data)
        mean_value = total / len(data)
        return float(f"{mean_value:.2f}")

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        if not data:
            return 0.00  # Handle empty list case

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

        return float(f"{median_value:.2f}")

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:list, the mode(s)
        """
        if not data:
            return []  # Handle empty list case

        count = Counter(data)
        max_count = max(count.values())
        modes = [key for key, value in count.items() if value == max_count]
        return modes