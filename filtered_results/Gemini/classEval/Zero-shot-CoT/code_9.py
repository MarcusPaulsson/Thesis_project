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

        num1 = num1[::-1]
        num2 = num2[::-1]

        len1 = len(num1)
        len2 = len(num2)
        carry = 0
        result = ''

        for i in range(max(len1, len2)):
            digit1 = int(num1[i]) if i < len1 else 0
            digit2 = int(num2[i]) if i < len2 else 0

            sum_digits = digit1 + digit2 + carry
            carry = sum_digits // 10
            result += str(sum_digits % 10)

        if carry:
            result += str(carry)

        return result[::-1]

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

        num1 = num1[::-1]
        num2 = num2[::-1]

        len1 = len(num1)
        len2 = len(num2)
        borrow = 0
        result = ''

        for i in range(len1):
            digit1 = int(num1[i])
            digit2 = int(num2[i]) if i < len2 else 0

            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result += str(diff)

        result = result[::-1].lstrip('0')
        if not result:
            return '0'

        return sign + result

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

        num1 = num1[::-1]
        num2 = num2[::-1]

        len1 = len(num1)
        len2 = len(num2)

        result = [0] * (len1 + len2)

        for i in range(len1):
            for j in range(len2):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                result[i + j] += product
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        result_str = ''.join(map(str, result[::-1])).lstrip('0')
        if not result_str:
            return '0'

        return result_str