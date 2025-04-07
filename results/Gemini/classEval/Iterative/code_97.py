import re

class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """

    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion.
        """
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 if idx else 2), 0) # Handles hundred correctly

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]

    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer.

        Handles hyphenated numbers and correctly parses complex numbers.
        :param textnum: string, the word string to be converted
        :return: int, the converted integer, or None if conversion fails
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        32
        >>> w2n.text2int("one hundred and forty-two")
        142
        >>> w2n.text2int("two million three hundred forty-five thousand six hundred and seventy-eight")
        2345678
        >>> w2n.text2int("invalid input") is None
        True
        """
        textnum = textnum.lower()
        textnum = re.sub(r'[\s-]+', ' ', textnum).strip()  # Normalize whitespace and hyphens
        tokens = textnum.split()

        current = 0
        result = 0

        for word in tokens:
            if word not in self.numwords:
                return None  # Invalid input

            scale, increment = self.numwords[word]
            current = current * scale + increment

            if scale > 100:
                result += current
                current = 0

        result += current
        return result

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.

        Handles hyphenated words in the input.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        True
        >>> w2n.is_valid_input("thirty-invalid")
        False
        """
        textnum = textnum.lower()
        textnum = re.sub(r'[\s-]+', ' ', textnum).strip()  # Normalize whitespace and hyphens
        tokens = textnum.split()

        for word in tokens:
            if word not in self.numwords:
                return False
        return True