class Manacher:
    """
    This is a class that implements a Manacher's algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string
        self.processed_string = self.preprocess_string(input_string)
        self.palindrome_lengths = self.manacher_algorithm()

    def preprocess_string(self, s):
        """
        Preprocesses the string to insert separators for easier palindrome detection.
        :param s: The original input string, str.
        :return: The processed string with separators, str.
        """
        return '|' + '|'.join(s) + '|'

    def manacher_algorithm(self):
        """
        Implements Manacher's algorithm to find all palindromic lengths.
        :return: A list of lengths of palindromes centered at each position, list of int.
        """
        n = len(self.processed_string)
        palindrome_lengths = [0] * n
        center = right_boundary = 0

        for i in range(n):
            mirror = 2 * center - i
            if i < right_boundary:
                palindrome_lengths[i] = min(right_boundary - i, palindrome_lengths[mirror])

            # Expanding around the center
            a, b = i + (1 + palindrome_lengths[i]), i - (1 + palindrome_lengths[i])
            while a < n and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                palindrome_lengths[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary
            if i + palindrome_lengths[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_lengths[i]

        return palindrome_lengths

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        left = center - diff
        right = center + diff
        length = 0

        while left >= 0 and right < len(string) and string[left] == string[right]:
            length += 1
            left -= 1
            right += 1

        return length

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        max_length = 0
        center_index = 0

        for i in range(len(self.palindrome_lengths)):
            if self.palindrome_lengths[i] > max_length:
                max_length = self.palindrome_lengths[i]
                center_index = i

        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

# Test cases provided in the prompt can be run using unittest as described.