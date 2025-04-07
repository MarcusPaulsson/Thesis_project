class Manacher:
    """
    This class implements the Manacher's algorithm to find the longest palindromic substring in a given string.
    """

    def __init__(self, input_string):
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, string):
        """
        Calculates the length of the palindromic substring centered at the given center.
        :param center: The center of the palindromic substring, int.
        :param string: The processed string with '|' inserted, str.
        :return: The length of the palindromic substring radius, int.
        """
        length = 0
        left = center - 1
        right = center + 1

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
        processed_string = '#' + '#'.join(self.input_string) + '#'
        max_length = 0
        center_index = 0

        for i in range(len(processed_string)):
            current_length = self.palindromic_length(i, processed_string)
            if current_length > max_length:
                max_length = current_length
                center_index = i

        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]