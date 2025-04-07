class Manacher:
    """
    his is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """
        left = center - diff
        right = center + diff
        if left >= 0 and right < len(string) and string[left] == string[right]:
            return self.palindromic_length(center, diff + 2, string) + 1
        else:
            return 0

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        string = '|'.join(list(self.input_string))
        string = '|' + string + '|'
        max_length = 0
        center_index = 0
        for i in range(1, len(string) - 1):
            length = self.palindromic_length(i, 1, string)
            if length > max_length:
                max_length = length
                center_index = i

        start = (center_index - max_length) // 2
        end = (center_index + max_length) // 2

        return self.input_string[start:end]