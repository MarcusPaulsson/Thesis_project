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
        self.processed_string = self.preprocess_string(input_string)
        self.palindrome_lengths = [0] * len(self.processed_string)
        self.longest_palindrome = ""
        self.center = 0
        self.right_boundary = 0

    def preprocess_string(self, s):
        """
        Preprocesses the input string to insert separators between characters.
        :param s: The original string, str.
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
        length = 0
        while (center - length >= 0) and (center + length < len(string)) and (string[center - length] == string[center + length]):
            length += 1
        return length - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        for i in range(len(self.processed_string)):
            mirror = 2 * self.center - i
            if i < self.right_boundary:
                self.palindrome_lengths[i] = min(self.right_boundary - i, self.palindrome_lengths[mirror])

            a, b = i + (1 + self.palindrome_lengths[i]), i - (1 + self.palindrome_lengths[i])
            while a < len(self.processed_string) and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                self.palindrome_lengths[i] += 1
                a += 1
                b -= 1

            if i + self.palindrome_lengths[i] > self.right_boundary:
                self.center = i
                self.right_boundary = i + self.palindrome_lengths[i]

            if self.palindrome_lengths[i] > len(self.longest_palindrome) // 2:
                start = (i - self.palindrome_lengths[i]) // 2
                self.longest_palindrome = self.input_string[start:start + self.palindrome_lengths[i]]

        return self.longest_palindrome