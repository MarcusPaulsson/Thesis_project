class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """

    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
        """
        self.numwords = self._initialize_numwords()
        self.ordinal_words = {
            'first': 1, 'second': 2, 'third': 3, 'fifth': 5,
            'eighth': 8, 'ninth': 9, 'twelfth': 12
        }

    def _initialize_numwords(self):
        """
        Initialize the number words mapping.
        :return: A dictionary mapping words to their numeric values.
        """
        numwords = {}
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):
            numwords[word] = (10 ** (idx * 3 or 2), 0)

        return numwords

    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string.
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        """
        if not self.is_valid_input(textnum):
            raise ValueError("Invalid input for conversion.")

        textnum = textnum.replace("-", " ")
        parts = textnum.split()
        current = result = 0

        for part in parts:
            if part in self.numwords:
                scale, increment = self.numwords[part]
                current += increment
                if scale > 1:
                    current *= scale
                    result += current
                    current = 0
            elif part in self.ordinal_words:
                current += self.ordinal_words[part]

        return str(result + current)

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        """
        words = textnum.replace("-", " ").split()
        return all(word in self.numwords or word in self.ordinal_words for word in words)