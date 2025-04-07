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
        length = 0
        while center - diff >= 0 and center + diff < len(string) and string[center - diff] == string[center + diff]:
            length += 1
            diff += 1
        return length

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        processed_string = '|'.join(list(self.input_string)) + '|'
        max_length = 0
        center_index = 0
        for i in range(len(processed_string)):
            length = self.palindromic_length(i, 0, processed_string)
            if length > max_length:
                max_length = length
                center_index = i
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]