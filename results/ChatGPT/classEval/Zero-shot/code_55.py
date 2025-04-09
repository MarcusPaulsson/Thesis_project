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
        self.palindrome_lengths = self._manacher_algorithm()

    def _transform_string(self, s):
        """Transforms the input string by inserting a special character between each character."""
        return '|' + '|'.join(s) + '|'

    def _manacher_algorithm(self):
        """Implements Manacher's algorithm to find the lengths of palindromes centered at each character."""
        n = len(self.transformed_string)
        lengths = [0] * n
        center = right = 0
        
        for i in range(n):
            mirror = 2 * center - i
            if i < right:
                lengths[i] = min(right - i, lengths[mirror])
            a, b = i + (1 + lengths[i]), i - (1 + lengths[i])
            while a < n and b >= 0 and self.transformed_string[a] == self.transformed_string[b]:
                lengths[i] += 1
                a += 1
                b -= 1
            if i + lengths[i] > right:
                center, right = i, i + lengths[i]

        return lengths

    def palindromic_length(self, center, diff, string):
        """
        Calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        left = center - diff
        right = center + diff
        count = 0
        while left >= 0 and right < len(string) and string[left] == string[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        max_length = 0
        center_index = 0
        for i, length in enumerate(self.palindrome_lengths):
            if length > max_length:
                max_length = length
                center_index = i
        
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

