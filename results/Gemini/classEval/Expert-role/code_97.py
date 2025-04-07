class Words2Numbers:
    """
    The class provides a text-to-number conversion utility, allowing conversion of written numbers (in words) to their numerical representation.
    """


    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
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
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]


    def text2int(self, textnum):
        """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        textnum = textnum.replace('-', ' ')
        current_number = 0
        result = 0
        for word in textnum.split():
            if word in self.numwords:
                scale, increment = self.numwords[word]
                current_number = current_number * scale + increment
                if scale > 100:
                    result += current_number
                    current_number = 0
            elif word in self.ordinal_words:
                result += self.ordinal_words[word]
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:-len(ending)] + replacement
                        if word in self.numwords:
                            scale, increment = self.numwords[word]
                            current_number = current_number * scale + increment
                            if scale > 100:
                                result += current_number
                                current_number = 0
                            break
                else:
                    continue
                break
        result += current_number
        return str(result)

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        textnum = textnum.replace('-', ' ')
        valid_words = set(self.numwords.keys()) | set(self.ordinal_words.keys())
        for ending, _ in self.ordinal_endings:
            valid_words.update([word + ending for word in self.units + self.tens])
        for word in textnum.split():
            if word not in valid_words:
                valid = False
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = word[:-len(ending)] + replacement
                        if word in self.numwords:
                            valid = True
                            break
                if not valid:
                    return False
        return True