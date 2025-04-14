import itertools

class ArrangementCalculator:
    """
    The Arrangement class provides permutation calculations and selection operations for a given set of data elements.
    """

    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

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
            return ArrangementCalculator.factorial(n)
        elif m > n:
            return 0
        else:
            return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        """
        total_arrangements = 0
        for i in range(1, n + 1):
            total_arrangements += ArrangementCalculator.count(n, i)
        return total_arrangements


    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        """
        if m is None:
            m = len(self.datas)

        arrangements = []
        for permutation in itertools.permutations(self.datas, m):
            arrangements.append(list(permutation))
        return arrangements


    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        """
        all_arrangements = []
        for i in range(1, len(self.datas) + 1):
            for permutation in itertools.permutations(self.datas, i):
                all_arrangements.append(list(permutation))
        return all_arrangements


    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        """
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result