class Manacher:
    """
    This is a class that implements a Manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        """
        Calculates the length of the palindromic substring based on a given center and difference.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference from the center, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        """
        if center - diff < 0 or center + diff >= len(string):
            return diff
        if string[center - diff] != string[center + diff]:
            return diff
        return self.palindromic_length(center, diff + 1, string)

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        """
        processed_string = '|'.join(list(self.input_string)) + '|'
        max_length = 0
        center_index = 0
        for i in range(len(processed_string)):
            length = self.palindromic_length(i, 0, processed_string)
            if length > max_length:
                max_length = length
                center_index = i
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]