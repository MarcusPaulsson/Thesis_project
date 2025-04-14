class BigNumCalculator:
    """
    This is a class that implements big number calculations, including adding, subtracting and multiplying.
    """

    @staticmethod
    def add(num1, num2):
        """
        Adds two big numbers.
        :param num1: The first number to add,str.
        :param num2: The second number to add,str.
        :return: The sum of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1:
            num1 = '0'
        if not num2:
            num2 = '0'

        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            num1, num2 = num2, num1
            n1, n2 = n2, n1

        result = []
        carry = 0
        i = n1 - 1
        j = n2 - 1

        while j >= 0:
            digit_sum = int(num1[i]) + int(num2[j]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10
            i -= 1
            j -= 1

        while i >= 0:
            digit_sum = int(num1[i]) + carry
            result.append(str(digit_sum % 10))
            carry = digit_sum // 10
            i -= 1

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'

        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1:
            num1 = '0'
        if not num2:
            num2 = '0'

        if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
            num1, num2 = num2, num1
            sign = '-'
        else:
            sign = ''

        n1 = len(num1)
        n2 = len(num2)
        result = []
        borrow = 0
        i = n1 - 1
        j = n2 - 1

        while j >= 0:
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(diff))
            i -= 1
            j -= 1

        while i >= 0:
            digit1 = int(num1[i])
            diff = digit1 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(diff))
            i -= 1

        res = ''.join(result[::-1]).lstrip('0')
        if not res:
            return '0'
        return sign + res

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'

        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1 or not num2:
            return '0'

        n1 = len(num1)
        n2 = len(num2)
        product = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            carry = 0
            for j in range(n2 - 1, -1, -1):
                product[i + j + 1] += int(num1[i]) * int(num2[j]) + carry
                carry = product[i + j + 1] // 10
                product[i + j + 1] %= 10
            product[i] += carry

        result = ''.join(map(str, product)).lstrip('0')
        return result if result else '0'