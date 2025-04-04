class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
    """

    def __init__(self):
        """
        Initialize NumberWordFormatter object.
        """
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]

    def format(self, x):
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = int((x - integer_part) * 100)
        else:
            integer_part = x
            decimal_part = 0
            
        integer_words = self.convert_integer(integer_part)
        decimal_words = self.convert_integer(decimal_part) if decimal_part > 0 else ""
        
        return (f"{integer_words} ONLY" + (f" AND {decimal_words}" if decimal_part > 0 else "")).strip()

    def format_string(self, x):
        return self.format(float(x))

    def trans_two(self, s):
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            ten = self.NUMBER_TEN[num // 10]
            one = self.NUMBER[num % 10]
            return f"{ten} {one}".strip()

    def trans_three(self, s):
        num = int(s)
        if num < 100:
            return self.trans_two(s)
        else:
            hundred = self.NUMBER[num // 100] + " HUNDRED"
            rest = self.trans_two(s[1:])
            return f"{hundred} AND {rest}".strip()

    def parse_more(self, i):
        return self.NUMBER_MORE[i]

    def convert_integer(self, num):
        if num == 0:
            return "ZERO"
        
        words = []
        index = 0
        
        while num > 0:
            if num % 1000 != 0:
                words_part = self.trans_three(str(num % 1000))
                if index > 0:
                    words_part += f" {self.parse_more(index)}"
                words.append(words_part)
            num //= 1000
            index += 1
        
        return ' '.join(reversed(words)).strip()