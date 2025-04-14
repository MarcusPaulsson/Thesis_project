class NumberWordFormatter:
    """
    Converts numbers into their corresponding English word representation.
    Handles integer and decimal parts.
    """

    def __init__(self):
        """Initialize the formatter with word lists."""
        self.ONES = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.TEENS = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                      "EIGHTEEN", "NINETEEN"]
        self.TENS = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.MAGNITUDES = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, number):
        """
        Converts a number (int or float) to its English word representation.

        Args:
            number (int or float): The number to convert.

        Returns:
            str: The number in words, or an empty string if input is None.
        """
        if number is None:
            return ""

        if isinstance(number, float):
            integer_part = int(number)
            decimal_part = round((number - integer_part) * 100)
            integer_words = self.format(integer_part)
            decimal_words = self.format(decimal_part)

            if integer_part == 0:
                return "CENTS " + decimal_words + " ONLY"
            return integer_words + " AND CENTS " + decimal_words + " ONLY"

        if number == 0:
            return "ZERO ONLY"

        return self._format_integer(int(number))

    def format_string(self, number_string):
        """
        Converts a string representation of a number to words.

        Args:
            number_string (str): The string to convert.

        Returns:
            str: The number in words, or an empty string on error.
        """
        try:
            number = float(number_string)
            return self.format(number)
        except ValueError:
            return ""

    def _format_integer(self, number):
        """
        Helper function to format an integer into words.

        Args:
            number (int): The integer to format.

        Returns:
            str: The integer in words.
        """
        if number == 0:
            return "ZERO ONLY"

        parts = []
        magnitude_index = 0
        while number > 0:
            # Process the last three digits
            three_digits = number % 1000
            if three_digits != 0:
                parts.insert(0, self._format_less_than_1000(three_digits) + " " + self.MAGNITUDES[magnitude_index])

            number //= 1000
            magnitude_index += 1

        return " ".join(part for part in parts if part).strip() + " ONLY"

    def _format_less_than_1000(self, number):
        """
        Formats a number less than 1000 into words.

        Args:
            number (int): The number to format (0-999).

        Returns:
            str: The number in words.
        """
        hundreds = number // 100
        remainder = number % 100

        words = []
        if hundreds > 0:
            words.append(self.ONES[hundreds])
            words.append("HUNDRED")

            if remainder > 0:
                words.append("AND")

        if remainder > 0:
            words.append(self._format_less_than_100(remainder))

        return " ".join(words).strip()

    def _format_less_than_100(self, number):
        """
        Formats a number less than 100 into words.

        Args:
            number (int): The number to format (0-99).

        Returns:
            str: The number in words.
        """
        if number < 10:
            return self.ONES[number]
        elif 10 <= number < 20:
            return self.TEENS[number - 10]
        else:
            tens = number // 10
            ones = number % 10
            if ones == 0:
                return self.TENS[tens - 1]
            else:
                return self.TENS[tens - 1] + " " + self.ONES[ones]

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        """
        if len(s) != 2:
            return ""

        if s[0] == '0':
            if s[1] == '0':
                return ""
            else:
                return self.ONES[int(s[1])]
        elif s[0] == '1':
            return self.TEENS[int(s[1])]
        else:
            if s[1] == '0':
                return self.TENS[int(s[0]) - 1]
            else:
                return self.TENS[int(s[0]) - 1] + " " + self.ONES[int(s[1])]

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        """
        if len(s) != 3:
            return ""

        result = []
        if s[0] != '0':
            result.append(self.ONES[int(s[0])])
            result.append("HUNDRED")

        two_digit = s[1:]
        two_digit_words = self.trans_two(two_digit)

        if result and two_digit_words:
            result.append("AND")

        if two_digit_words:
            result.append(two_digit_words)

        return " ".join(result).strip()

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        """
        return self.MAGNITUDES[i]