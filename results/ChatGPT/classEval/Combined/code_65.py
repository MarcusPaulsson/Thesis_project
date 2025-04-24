class NumberWordFormatter:
    """
    A class to convert numbers into their corresponding English word representation,
    handling both integer and decimal parts with appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize the NumberWordFormatter object with number representations.
        """
        self.units = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.teens = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                      "EIGHTEEN", "NINETEEN"]
        self.tens = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.scales = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, number):
        """
        Converts a number (int or float) into words format.
        :param number: int or float, the number to be converted into words format
        :return: str, the number in words format
        """
        if number is None:
            return ""
        
        if isinstance(number, float):
            integer_part = int(number)
            decimal_part = int(round((number - integer_part) * 100))
            return f"{self._convert_integer(integer_part)} AND CENTS {self._convert_two_digits(decimal_part)} ONLY"
        
        return f"{self._convert_integer(int(number))} ONLY"

    def format_string(self, number_str):
        """
        Converts a string representation of a number into words format.
        :param number_str: str, the string representation of a number
        :return: str, the number in words format
        """
        return self.format(float(number_str))

    def _convert_two_digits(self, num):
        """
        Converts a two-digit number into words format.
        :param num: int, the two-digit number
        :return: str, the number in words format
        """
        if num < 10:
            return self.units[num]
        elif num < 20:
            return self.teens[num - 10]
        else:
            ten = num // 10
            one = num % 10
            return f"{self.tens[ten]} {self.units[one]}".strip()

    def _convert_three_digits(self, num):
        """
        Converts a three-digit number into words format.
        :param num: int, the three-digit number
        :return: str, the number in words format
        """
        hundred = num // 100
        remainder = num % 100
        if hundred == 0:
            return self._convert_two_digits(remainder)
        return f"{self.units[hundred]} HUNDRED AND {self._convert_two_digits(remainder)}".strip()

    def _convert_integer(self, num):
        """
        Converts an integer number into words format.
        :param num: int, the integer number to be converted
        :return: str, the number in words format
        """
        if num == 0:
            return "ZERO"
        
        parts = []
        scale_index = 0
        
        while num > 0:
            if num % 1000 != 0:
                parts.append(f"{self._convert_three_digits(num % 1000)} {self.scales[scale_index]}".strip())
            num //= 1000
            scale_index += 1
        
        return ' AND '.join(reversed(parts)).strip()