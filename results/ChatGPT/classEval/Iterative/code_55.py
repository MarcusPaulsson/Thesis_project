class Manacher:
    """
    This class implements the Manacher algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string: str) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string
        self.processed_string = self.preprocess_string(input_string)
        self.palindrome_lengths = [0] * len(self.processed_string)
        self.center = 0
        self.right_boundary = 0
        self.longest_palindrome = ''

    def preprocess_string(self, string: str) -> str:
        """
        Preprocesses the input string to insert delimiters for easier palindrome detection.
        :param string: The original string, str.
        :return: The processed string with delimiters, str.
        """
        return '|' + '|'.join(string) + '|'

    def palindromic_string(self) -> str:
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        for i in range(len(self.processed_string)):
            mirror = 2 * self.center - i
            
            if i < self.right_boundary:
                self.palindrome_lengths[i] = min(self.right_boundary - i, self.palindrome_lengths[mirror])
            
            # Attempt to expand palindrome centered at i
            a, b = i + (1 + self.palindrome_lengths[i]), i - (1 + self.palindrome_lengths[i])
            while a < len(self.processed_string) and b >= 0 and self.processed_string[a] == self.processed_string[b]:
                self.palindrome_lengths[i] += 1
                a += 1
                b -= 1
            
            # Update center and right boundary
            if i + self.palindrome_lengths[i] > self.right_boundary:
                self.center = i
                self.right_boundary = i + self.palindrome_lengths[i]
                
            # Track the longest palindrome
            if self.palindrome_lengths[i] > len(self.longest_palindrome):
                start = (i - self.palindrome_lengths[i]) // 2
                self.longest_palindrome = self.input_string[start:start + self.palindrome_lengths[i]]

        return self.longest_palindrome