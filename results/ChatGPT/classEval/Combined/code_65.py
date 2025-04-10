class NumberWordFormatter:
    """
    This class converts numbers into their corresponding English word representation, including handling
    both integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize the NumberWordFormatter object with mappings for number words.
        """
        self.units = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", 
                      "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
        self.tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.magnitude = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, number):
        """
        Converts a number into words format.
        :param number: int or float, the number to be converted
        :return: str, the number in words format
        """
        if number is None:
            return ""

        if isinstance(number, float):
            integer_part = int(number)
            decimal_part = int(round((number - integer_part) * 100))
            words = self.convert_integer_to_words(integer_part)
            if decimal_part > 0:
                words += f" AND CENTS {self.convert_two_digits_to_words(decimal_part)} ONLY"
            else:
                words += " ONLY"
            return words
        
        return self.convert_integer_to_words(int(number)) + " ONLY"

    def format_string(self, number_str):
        """
        Converts a string representation of a number into words format.
        :param number_str: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(number_str))

    def convert_integer_to_words(self, number):
        """
        Converts an integer into words format.
        :param number: int, the integer to convert
        :return: str, the number in words format
        """
        if number == 0:
            return "ZERO"

        words = ""
        if number >= 1000:
            thousands = number // 1000
            words += self.convert_three_digits_to_words(thousands) + " " + self.magnitude[1] + " "
            number %= 1000
        
        if number > 0:
            words += self.convert_three_digits_to_words(number)
        
        return words.strip()

    def convert_two_digits_to_words(self, number):
        """
        Converts a two-digit number into words format.
        :param number: int, the two-digit number
        :return: str, the number in words format
        """
        if number < 10:
            return self.units[number]
        elif number < 20:
            return self.teens[number - 10]
        else:
            ten = number // 10
            one = number % 10
            return self.tens[ten] + (" " + self.units[one] if one > 0 else "").strip()

    def convert_three_digits_to_words(self, number):
        """
        Converts a three-digit number into words format.
        :param number: int, the three-digit number
        :return: str, the number in words format
        """
        if number < 100:
            return self.convert_two_digits_to_words(number)
        
        hundred = number // 100
        remainder = number % 100
        if remainder > 0:
            return f"{self.units[hundred]} HUNDRED AND {self.convert_two_digits_to_words(remainder)}"
        return f"{self.units[hundred]} HUNDRED"