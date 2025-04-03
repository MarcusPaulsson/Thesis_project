class Manacher:
    """
    This is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string
        self.processed_string = self._preprocess(input_string)
        self.palindrome_lengths = [0] * len(self.processed_string)

    def _preprocess(self, s):
        """
        Preprocesses the input string to insert separators between characters.
        :param s: The original input string, str.
        :return: The processed string with separators, str.
        """
        return '|' + '|'.join(s) + '|'

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
        while (center - diff >= 0 and center + diff < len(string)):
            if string[center - diff] != string[center + diff]:
                break
            diff += 1
        return diff - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        max_length = 0
        center_index = 0
        for i in range(len(self.processed_string)):
            length = self.palindromic_length(i, 0, self.processed_string)
            self.palindrome_lengths[i] = length
            if length > max_length:
                max_length = length
                center_index = i
        
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]