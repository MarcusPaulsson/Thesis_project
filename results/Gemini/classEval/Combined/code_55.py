class Manacher:
    """
    This class implements the Manacher's algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string):
        """
        Initializes the Manacher class with the given input_string.

        :param input_string: The input string to be processed.
        :type input_string: str
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Calculates the length of the palindromic substring centered at 'center' with a given 'diff'.

        This function iteratively expands outwards from the center, checking for palindrome properties.

        :param center: The center index of the potential palindrome in the processed string.
        :type center: int
        :param diff: The offset from the center to compare characters. Starts at 1.
        :type diff: int
        :param string: The processed string (with '|' inserted).
        :type string: str
        :return: The length of the palindromic substring centered at 'center'.
        :rtype: int
        """
        length = 0
        while (center - diff >= 0 and center + diff < len(string) and
               string[center - diff] == string[center + diff]):
            length += 1
            diff += 1
        return length

    def palindromic_string(self):
        """
        Finds the longest palindromic substring within the input string using Manacher's algorithm.

        :return: The longest palindromic substring found in the input string.
        :rtype: str
        """
        # Preprocess the string by inserting '|' between characters and at the beginning/end.
        processed_string = '|' + '|'.join(list(self.input_string)) + '|'

        longest_palindrome = ''

        for i in range(len(processed_string)):
            length = self.palindromic_length(i, 1, processed_string)
            current_palindrome = processed_string[i - length: i + length + 1]
            current_palindrome = current_palindrome.replace('|', '')

            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome

        return longest_palindrome