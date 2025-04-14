import itertools
import math

class ArrangementCalculator:
    """
    The ArrangementCalculator class provides permutation calculations and selection operations for a given set of data elements.
    """

    def __init__(self, data):
        """
        Initializes the ArrangementCalculator object with a list of data.
        :param data: List, the data elements to be used for arrangements.
        """
        self.data = data

    @staticmethod
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        """
        if m is None or n == m:
            return math.factorial(n)
        if m > n:
            return 0
        return math.factorial(n) // math.factorial(n - m)

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        """
        return sum(ArrangementCalculator.count(n, m) for m in range(1, n + 1))

    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal data.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        """
        if m is None:
            m = len(self.data)
        return [list(p) for p in itertools.permutations(self.data, m)]

    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal data.
        :return: List, a list of all arrangements.
        """
        all_arrangements = []
        for m in range(1, len(self.data) + 1):
            all_arrangements.extend(self.select(m))
        return all_arrangements

    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        """
        return math.factorial(n)