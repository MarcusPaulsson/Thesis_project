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
        self.transformed_string = self._transform_string(input_string)
        self.palindrome_lengths = [0] * len(self.transformed_string)
        self.center = 0
        self.right_boundary = 0
        self._manacher_algorithm()

    def _transform_string(self, s):
        """
        Transforms the input string to insert a unique character between all characters.
        :param s: The original string, str.
        :return: The transformed string, str.
        """
        return '|' + '|'.join(s) + '|'

    def _manacher_algorithm(self):
        """
        Implements the Manacher algorithm to fill the palindrome_lengths array.
        """
        for i in range(len(self.transformed_string)):
            mirror = 2 * self.center - i
            
            if i < self.right_boundary:
                self.palindrome_lengths[i] = min(self.right_boundary - i, self.palindrome_lengths[mirror])
            
            a, b = i + (1 + self.palindrome_lengths[i]), i - (1 + self.palindrome_lengths[i])
            while a < len(self.transformed_string) and b >= 0 and self.transformed_string[a] == self.transformed_string[b]:
                self.palindrome_lengths[i] += 1
                a += 1
                b -= 1
            
            if i + self.palindrome_lengths[i] > self.right_boundary:
                self.center = i
                self.right_boundary = i + self.palindrome_lengths[i]

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
        while left >= 0 and right < len(string) and string[left] == string[right]:
            diff += 1
            left -= 1
            right += 1
        return diff - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)
        start = (center_index - max_length) // 2  # Adjust for transformed string
        return self.input_string[start:start + max_length]