class NumberWordFormatter:
    """
    Converts numbers into their corresponding English word representation.
    Handles integer and decimal parts.
    """

    def __init__(self):
        """Initialize the formatter with word lists."""
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, x):
        """
        Converts a number (int or float) into words.

        Args:
            x: The number to convert.

        Returns:
            The number in words as a string.
        """
        if x is None:
            return ""

        if isinstance(x, float):
            return self._format_float(x)

        if isinstance(x, str):
            try:
                x = int(x)
            except ValueError:
                return ""

        if not isinstance(x, int):
            return ""

        if x == 0:
            return "ZERO ONLY"

        return self._format_integer(x)

    def format_string(self, x):
        """
        Converts a string representation of a number into words.

        Args:
            x: The string representation of a number.

        Returns:
            The number in words as a string.
        """
        try:
            number = float(x)
            return self.format(number)
        except ValueError:
            return ""

    def _format_float(self, x):
        """Handles the formatting of float numbers."""
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)
        integer_words = self.format(integer_part)
        decimal_words = self.format(decimal_part)

        if integer_words == "ZERO ONLY":
            return f"CENTS {decimal_words.replace(' ONLY', '')} ONLY"

        return f"{integer_words.replace(' ONLY', '')} AND CENTS {decimal_words.replace(' ONLY', '')} ONLY"

    def _format_integer(self, x):
        """Handles the formatting of integer numbers."""
        num_str = str(x)
        num_len = len(num_str)
        words = []
        i = num_len - 1
        group_index = 0

        while i >= 0:
            group = ""
            if i >= 2:
                group = num_str[i - 2:i + 1]
                i -= 3
            else:
                group = num_str[0:i + 1]
                i = -1

            if int(group) != 0:
                group_words = self._trans_three(group)
                more_word = self._parse_more(group_index)
                if more_word:
                    words.insert(0, more_word)
                words.insert(0, group_words)

            group_index += 1

        return " ".join(words).strip() + " ONLY"

    def _trans_two(self, s):
        """
        Converts a two-digit number into words.

        Args:
            s: The two-digit number as a string.

        Returns:
            The number in words as a string.
        """
        if len(s) != 2:
            return ""

        if s[0] == '0':
            return self.NUMBER[int(s[1])]

        if s[0] == '1':
            return self.NUMBER_TEEN[int(s[1])]

        if s[1] == '0':
            return self.NUMBER_TEN[int(s[0]) - 1]

        return self.NUMBER_TEN[int(s[0]) - 1] + " " + self.NUMBER[int(s[1])]

    def _trans_three(self, s):
        """
        Converts a three-digit number into words.

        Args:
            s: The three-digit number as a string.

        Returns:
            The number in words as a string.
        """
        if len(s) != 3:
            return ""

        words = []
        if s[0] != '0':
            words.append(self.NUMBER[int(s[0])])
            words.append("HUNDRED")

        two_digits = self._trans_two(s[1:])
        if two_digits:
            if words:
                words.append("AND")
            words.append(two_digits)

        return " ".join(words).strip()

    def _parse_more(self, i):
        """
        Gets the suffix (thousand, million, billion) based on the index.

        Args:
            i: The index representing the magnitude.

        Returns:
            The corresponding suffix as a string.
        """
        if i < len(self.NUMBER_MORE):
            return self.NUMBER_MORE[i]
        else:
            return ""