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
        self.find_longest_palindrome()

    def preprocess_string(self, string):
        """
        Preprocesses the string to add separators between characters for easier palindrome detection.
        :param string: The original string, str.
        :return: The preprocessed string with separators, str.
        """
        return '|' + '|'.join(string) + '|'

    def find_longest_palindrome(self):
        """
        Implements Manacher's algorithm to find the lengths of palindromes centered at each character.
        """
        center = 0
        right = 0
        for i in range(len(self.processed_string)):
            mirror = 2 * center - i
            if i < right:
                self.palindrome_lengths[i] = min(right - i, self.palindrome_lengths[mirror])
            
            # Attempt to expand palindrome centered at i
            a, b = i + (1 + self.palindrome_lengths[i]), i - (1 + self.palindrome_lengths[i])
            while a < len(self.processed_string) and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                self.palindrome_lengths[i] += 1
                a += 1
                b -= 1
            
            # Adjust center and right boundary if expanded past right
            if i + self.palindrome_lengths[i] > right:
                center = i
                right = i + self.palindrome_lengths[i]

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
        start = (center_index - max_length) // 2  # Convert back to the original string index
        return self.input_string[start:start + max_length]

# Unit tests should be run separately; the code above is the implementation of the Manacher algorithm.