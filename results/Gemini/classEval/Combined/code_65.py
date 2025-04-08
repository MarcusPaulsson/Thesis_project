class NumberWordFormatter:
    """
    This class converts numbers to their English word representation.
    It handles integer and decimal parts, and incorporates units.
    """

    def __init__(self):
        """Initialize the NumberWordFormatter with word lists."""
        self.ONES = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.TEENS = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                      "EIGHTEEN", "NINETEEN"]
        self.TENS = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.THOUSANDS = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, number):
        """
        Convert a number (int or float) to its word representation.

        Args:
            number (int or float): The number to convert.

        Returns:
            str: The word representation of the number, or an empty string if None is passed.
        """
        if number is None:
            return ""

        number = str(number)
        if "." in number:
            integer_part, decimal_part = number.split(".")
            integer_word = self._format_integer(integer_part)
            decimal_word = self._format_integer(decimal_part)

            if integer_word == "ZERO":
                return "CENTS " + decimal_word + " ONLY"
            else:
                return integer_word + " AND CENTS " + decimal_word + " ONLY"
        else:
            return self._format_integer(number)

    def _format_integer(self, number_str):
        """
        Convert an integer string to its word representation.

        Args:
            number_str (str): The integer as a string.

        Returns:
            str: The word representation of the integer.
        """
        if not number_str:
            return ""

        num = int(number_str)
        if num == 0:
            return "ZERO ONLY"

        result = []
        group_index = 0
        while num > 0:
            group = num % 1000
            if group != 0:
                words = self._convert_group(group)
                if group_index > 0:
                    words += " " + self.THOUSANDS[group_index]
                result.append(words)
            num //= 1000
            group_index += 1

        result.reverse()
        return " ".join(result) + " ONLY"

    def _convert_group(self, number):
        """
        Convert a number (0-999) to its word representation.

        Args:
            number (int): The number to convert (0-999).

        Returns:
            str: The word representation of the number.
        """
        hundreds = number // 100
        tens_and_ones = number % 100

        words = []
        if hundreds > 0:
            words.append(self.ONES[hundreds])
            words.append("HUNDRED")

        if tens_and_ones > 0:
            if hundreds > 0:
                words.append("AND")

            if tens_and_ones < 10:
                words.append(self.ONES[tens_and_ones])
            elif 10 <= tens_and_ones < 20:
                words.append(self.TEENS[tens_and_ones - 10])
            else:
                tens = tens_and_ones // 10
                ones = tens_and_ones % 10
                words.append(self.TENS[tens])
                if ones > 0:
                    words.append(self.ONES[ones])

        return " ".join(words)