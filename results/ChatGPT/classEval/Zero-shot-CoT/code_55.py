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
        self.palindrome_lengths = self._manacher_algorithm()

    def _preprocess(self, s):
        """
        Preprocess the string to insert separators.
        :param s: The original input string.
        :return: The processed string with separators.
        """
        return '|' + '|'.join(s) + '|'

    def _manacher_algorithm(self):
        """
        Implements the Manacher's algorithm to find the lengths of palindromes.
        :return: A list of lengths of palindromes centered at each character.
        """
        n = len(self.processed_string)
        lengths = [0] * n
        center = 0
        right = 0

        for i in range(n):
            mirror = 2 * center - i
            
            if i < right:
                lengths[i] = min(right - i, lengths[mirror])

            a, b = i + (1 + lengths[i]), i - (1 + lengths[i])
            while a < n and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                lengths[i] += 1
                a += 1
                b -= 1

            if i + lengths[i] > right:
                center = i
                right = i + lengths[i]

        return lengths

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
        
        if left < 0 or right >= len(string):
            return 0
        
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return (right - left - 1) // 2

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

