class NumberWordFormatter:
    """
    Converts numbers into their corresponding English word representation.
    Handles integer parts, and incorporates appropriate connectors and units.
    """

    def __init__(self):
        """Initialize NumberWordFormatter object."""
        self.NUMBER = ["", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
        self.NUMBER_TEEN = ["TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN",
                            "EIGHTEEN", "NINETEEN"]
        self.NUMBER_TEN = ["TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]
        self.NUMBER_MORE = ["", "THOUSAND", "MILLION", "BILLION"]  # Up to billions
        self.AND = "AND"
        self.ONLY = "ONLY"
        self.HUNDRED = "HUNDRED"
        self.ZERO = "ZERO"

    def format(self, x):
        """
        Converts a number into words format.

        Args:
            x: int or float, the number to be converted into words format.  Only integer part is considered.

        Returns:
            str, the number in words format. Returns "Invalid input" if input is not an integer or float.

        Examples:
            >>> formatter = NumberWordFormatter()
            >>> formatter.format(123456)
            'ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY'
            >>> formatter.format(0)
            'ZERO ONLY'
            >>> formatter.format(1234567890)
            'ONE BILLION TWO HUNDRED AND THIRTY FOUR MILLION FIVE HUNDRED AND SIXTY SEVEN THOUSAND EIGHT HUNDRED AND NINETY ONLY'
        """
        if not isinstance(x, (int, float)):
            return "Invalid input"

        x = int(x)  # Consider only the integer part

        if x == 0:
            return f"{self.ZERO} {self.ONLY}"

        if x < 0:
            return "Invalid input: Cannot convert negative numbers"

        result = []
        i = 0
        while x > 0:
            n = x % 1000
            if n != 0:
                words = self._trans_three(n)
                if i > 0:  # Add magnitude only if the chunk is not zero
                    words += f" {self.NUMBER_MORE[i]}"
                result.append(words)
            x //= 1000
            i += 1

        result.reverse()
        return " ".join(result).strip() + f" {self.ONLY}"

    def format_string(self, x):
        """
        Converts a string representation of a number into words format.

        Args:
            x: str, the string representation of a number

        Returns:
            str, the number in words format. Returns "Invalid input" if the string does not represent a valid integer.

        Examples:
            >>> formatter = NumberWordFormatter()
            >>> formatter.format_string("123456")
            'ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY'
            >>> formatter.format_string("abc")
            'Invalid input: Not a valid number string'
        """
        try:
            num = int(x)
            return self.format(num)
        except ValueError:
            return "Invalid input: Not a valid number string"

    def _trans_two(self, n):
        """
        Converts a two-digit number (0-99) into words.  Private helper function.

        Args:
            n: int, the two-digit number

        Returns:
            str, the number in words format

        Examples:
            >>> formatter = NumberWordFormatter()
            >>> formatter._trans_two(23)
            'TWENTY THREE'
            >>> formatter._trans_two(9)
            'NINE'
            >>> formatter._trans_two(10)
            'TEN'
            >>> formatter._trans_two(19)
            'NINETEEN'
        """
        if n < 10:
            return self.NUMBER[n]
        elif 10 <= n <= 19:
            return self.NUMBER_TEEN[n - 10]
        else:
            tens = n // 10
            ones = n % 10
            if ones == 0:
                return self.NUMBER_TEN[tens - 1]
            else:
                return f"{self.NUMBER_TEN[tens - 1]} {self.NUMBER[ones]}"

    def _trans_three(self, n):
        """
        Converts a three-digit number (0-999) into words. Private helper function.

        Args:
            n: int, the three-digit number

        Returns:
            str, the number in words format

        Examples:
            >>> formatter = NumberWordFormatter()
            >>> formatter._trans_three(123)
            'ONE HUNDRED AND TWENTY THREE'
            >>> formatter._trans_three(100)
            'ONE HUNDRED'
            >>> formatter._trans_three(5)
            'FIVE'
        """
        hundreds = n // 100
        remainder = n % 100

        words = []
        if hundreds > 0:
            words.append(f"{self.NUMBER[hundreds]} {self.HUNDRED}")

        if remainder > 0:
            if hundreds > 0:
                words.append(self.AND)
            words.append(self._trans_two(remainder))

        return " ".join(words)