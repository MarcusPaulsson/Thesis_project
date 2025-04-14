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

        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2:
            num1, num2 = num2, num1
            len1, len2 = len2, len1

        result = ""
        carry = 0
        i = len1 - 1
        j = len2 - 1

        while j >= 0:
            digit_sum = int(num1[i]) + int(num2[j]) + carry
            result = str(digit_sum % 10) + result
            carry = digit_sum // 10
            i -= 1
            j -= 1

        while i >= 0:
            digit_sum = int(num1[i]) + carry
            result = str(digit_sum % 10) + result
            carry = digit_sum // 10
            i -= 1

        if carry:
            result = str(carry) + result

        return result

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

        if BigNumCalculator.is_smaller(num1, num2):
            num1, num2 = num2, num1
            sign = "-"
        else:
            sign = ""

        len1 = len(num1)
        len2 = len(num2)

        result = ""
        borrow = 0
        i = len1 - 1
        j = len2 - 1

        while j >= 0:
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            diff = digit1 - digit2 - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result
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

            result = str(diff) + result
            i -= 1

        result = result.lstrip('0')
        if not result:
            result = '0'

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
            return "0"

        len1 = len(num1)
        len2 = len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2

                p1 = i + j + 1
                p2 = i + j

                sum_val = product + result[p1]

                result[p1] = sum_val % 10
                result[p2] += sum_val // 10

        result_str = "".join(map(str, result)).lstrip('0')
        return result_str if result_str else "0"

    @staticmethod
    def is_smaller(num1, num2):
        """
        Helper function to compare two big numbers.
        :param num1: The first number to compare,str.
        :param num2: The second number to compare,str.
        :return: True if num1 < num2, False otherwise.
        """
        len1 = len(num1)
        len2 = len(num2)

        if len1 < len2:
            return True
        elif len1 > len2:
            return False
        else:
            for i in range(len1):
                if int(num1[i]) < int(num2[i]):
                    return True
                elif int(num1[i]) > int(num2[i]):
                    return False
            return False