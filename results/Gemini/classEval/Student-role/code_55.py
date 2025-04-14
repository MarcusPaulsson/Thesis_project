class Manacher:
    """
    his is a class that implements a manacher algorithm to find the Longest palindromic substring in a given string.
    """

    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

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
        if center - diff < 0 or center + diff >= len(string):
            return diff - 1

        if string[center - diff] == string[center + diff]:
            return self.palindromic_length(center, diff + 1, string)
        else:
            return diff - 1

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        processed_string = '|'.join(list(self.input_string))
        processed_string = '|' + processed_string + '|'
        max_length = 0
        center_index = 0

        for i in range(len(processed_string)):
            current_length = self.palindromic_length(i, 1, processed_string)

            if current_length > max_length:
                max_length = current_length
                center_index = i

        start = (center_index - max_length) // 2
        end = start + max_length

        return self.input_string[start:end]