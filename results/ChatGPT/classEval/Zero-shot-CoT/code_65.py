class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, 
    including handling the conversion of both the integer and decimal parts, and incorporating appropriate 
    connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", 
                            "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        if x is None:
            return ""
        if x == 0:
            return "ZERO ONLY"
        
        integer_part = int(x)
        decimal_part = round((x - integer_part) * 100)

        words = self.convert_integer(integer_part)
        if decimal_part > 0:
            words += " AND CENTS " + self.convert_integer(decimal_part)

        return words + " ONLY"

    def format_string(self, x):
        return self.format(float(x))

    def trans_two(self, s):
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            ten_part = self.NUMBER_TEN[num // 10 - 1]
            one_part = self.NUMBER[num % 10]
            return ten_part + (" " + one_part if one_part else "")

    def trans_three(self, s):
        num = int(s)
        if num < 100:
            return self.trans_two(s)
        else:
            hundred_part = self.NUMBER[num // 100] + " HUNDRED"
            remainder = num % 100
            if remainder == 0:
                return hundred_part
            else:
                return hundred_part + " AND " + self.trans_two(str(remainder))

    def parse_more(self, i):
        return self.NUMBER_MORE[i]

    def convert_integer(self, num):
        if num == 0:
            return "ZERO"
        
        words = ""
        if num >= 1000:
            thousands = num // 1000
            words += self.trans_three(str(thousands)) + " " + self.parse_more(1)
            num %= 1000
        
        if num >= 100:
            words += " " + self.trans_three(str(num)) if words else self.trans_three(str(num))
        elif num > 0:
            words += " " + self.trans_two(str(num)) if words else self.trans_two(str(num))
        
        return words.strip()