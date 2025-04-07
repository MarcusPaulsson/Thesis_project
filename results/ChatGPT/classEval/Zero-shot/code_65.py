class NumberWordFormatter:
    """
    This is a class that provides to convert numbers into their corresponding English word representation, including handling the conversion of both the integer and decimal parts, and incorporating appropriate connectors and units.
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
        self.NUMBER_SUFFIX = ["k", "w", "", "m", "", "", "b", "", "", "t", "", "", "p", "", "", "e"]

    def format(self, x):
        if x is None:
            return ""
        if isinstance(x, float):
            integer_part = int(x)
            decimal_part = round((x - integer_part) * 100)
            return f"{self.format_integer(integer_part)} AND CENTS {self.trans_two(str(decimal_part))} ONLY"
        return f"{self.format_integer(int(x))} ONLY"

    def format_string(self, x):
        return self.format(float(x))

    def trans_two(self, s):
        num = int(s)
        if num < 10:
            return self.NUMBER[num]
        elif 10 <= num < 20:
            return self.NUMBER_TEEN[num - 10]
        else:
            ten = num // 10
            one = num % 10
            return f"{self.NUMBER_TEN[ten - 1]} {self.NUMBER[one]}".strip()

    def trans_three(self, s):
        num = int(s)
        if num < 100:
            return self.trans_two(s)
        else:
            hundred = num // 100
            rest = num % 100
            return f"{self.NUMBER[hundred]} HUNDRED AND {self.trans_two(str(rest))}".strip()

    def parse_more(self, i):
        return self.NUMBER_MORE[i]

    def format_integer(self, num):
        if num == 0:
            return "ZERO"
        parts = []
        thousands = 0
        while num > 0:
            if num % 1000 != 0:
                parts.append(f"{self.trans_three(str(num % 1000))} {self.parse_more(thousands)}".strip())
            num //= 1000
            thousands += 1
        return " AND ".join(reversed(parts)).strip()