class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, 
    including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, x):
        """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        if x is None:
            return ""
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = round((x - integer_part) * 100)
            return f"{self.format_integer(integer_part)} AND CENTS {self.trans_two(str(decimal_part).zfill(2))} ONLY"
        return f"{self.format_integer(int(x))} ONLY"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format
        :param x: str, the string representation of a number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
        try:
            return self.format(float(x))
        except ValueError:
            return ""

    def trans_two(self, s):
        """
        Converts a two-digit number into words format
        :param s: str, the two-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_two("23")
        "TWENTY THREE"
        """
        num = int(s)
        if 10 <= num < 20:
            return self.NUMBER_TEEN[num - 10]
        elif num >= 20:
            return self.NUMBER_TEN[num // 10 - 1] + (f" {self.NUMBER[num % 10]}" if num % 10 != 0 else "")
        return self.NUMBER[num]

    def trans_three(self, s):
        """
        Converts a three-digit number into words format
        :param s: str, the three-digit number
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.trans_three("123")
        "ONE HUNDRED AND TWENTY THREE"
        """
        num = int(s)
        if num == 0:
            return ""
        elif num < 100:
            return self.trans_two(s)
        else:
            return self.NUMBER[num // 100] + " HUNDRED" + (f" AND {self.trans_two(str(num % 100).zfill(2))}" if num % 100 != 0 else "")

    def parse_more(self, i):
        """
        Parses the thousand/million/billion suffix based on the index
        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude
        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
        return self.NUMBER_MORE[i]
    
    def format_integer(self, num):
        """
        Converts an integer number into words format by breaking it down into chunks
        :param num: int, the integer number
        :return: str, the number in words format
        """
        if num == 0:
            return "ZERO"
        
        parts = []
        chunk_index = 0
        
        while num > 0:
            chunk = num % 1000
            if chunk > 0:
                prefix = self.trans_three(str(chunk).zfill(3))
                if chunk_index > 0:
                    prefix += f" {self.parse_more(chunk_index)}"
                parts.append(prefix)
            num //= 1000
            chunk_index += 1
            
        return ' AND '.join(reversed(parts))