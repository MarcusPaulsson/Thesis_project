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

    def _transform_string(self, s):
        """
        Transforms the input string to insert separators to handle even-length palindromes.
        :param s: The input string, str.
        :return: Transformed string with separators, str.
        """
        return '#' + '#'.join(s) + '#'

    def palindromic_length(self, center, diff, string):
        """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        return min(self.palindrome_lengths[center + diff], self.right_boundary - (center + diff)) if center + diff < self.right_boundary else 0

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        for i in range(len(self.transformed_string)):
            mirror = 2 * self.center - i
            if i < self.right_boundary:
                self.palindrome_lengths[i] = self.palindromic_length(self.center, i - self.center, self.transformed_string)

            # Attempt to expand the palindrome around the current center
            a, b = i + (1 + self.palindrome_lengths[i]), i - (1 + self.palindrome_lengths[i])
            while a < len(self.transformed_string) and b >= 0 and self.transformed_string[a] == self.transformed_string[b]:
                self.palindrome_lengths[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary if we've expanded past the current right boundary
            if i + self.palindrome_lengths[i] > self.right_boundary:
                self.center = i
                self.right_boundary = i + self.palindrome_lengths[i]

        # Find the maximum length of the palindrome
        max_length = max(self.palindrome_lengths)
        center_index = self.palindrome_lengths.index(max_length)

        # Extract the longest palindromic substring from the original string
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]

# Example usage
manacher = Manacher('ababa')
print(manacher.palindromic_string())  # Output: 'ababa'