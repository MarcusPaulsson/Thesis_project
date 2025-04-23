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
        """
        num1 = num1.lstrip('0') or '0'
        num2 = num2.lstrip('0') or '0'

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
        """
        num1 = num1.lstrip('0') or '0'
        num2 = num2.lstrip('0') or '0'

        if BigNumCalculator.compare(num1, num2) < 0:
            num1, num2 = num2, num1
            sign = "-"
        else:
            sign = ""

        n1 = len(num1)
        n2 = len(num2)

        result = []
        borrow = 0

        i = n1 - 1
        j = n2 - 1

        while j >= 0:
            digit1 = int(num1[i])
            digit2 = int(num2[j]) + borrow

            if digit1 < digit2:
                digit1 += 10
                borrow = 1
            else:
                borrow = 0

            result.append(str(digit1 - digit2))
            i -= 1
            j -= 1

        while i >= 0:
            digit1 = int(num1[i]) - borrow

            if digit1 < 0:
                digit1 += 10
                borrow = 1
            else:
                borrow = 0

            result.append(str(digit1))
            i -= 1

        res = ''.join(result[::-1]).lstrip('0')

        return sign + (res or "0")

    @staticmethod
    def multiply(num1, num2):
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')
        if not num1 or not num2:
            return "0"

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

        result = "".join(map(str, product))

        return result.lstrip('0') or "0"

    @staticmethod
    def compare(num1, num2):
        """
        Compares two big numbers.
        :param num1: The first number to compare,str.
        :param num2: The second number to compare,str.
        :return: 1 if num1 > num2, -1 if num1 < num2, 0 if num1 == num2.
        """
        n1 = len(num1)
        n2 = len(num2)

        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
        else:
            for i in range(n1):
                if int(num1[i]) > int(num2[i]):
                    return 1
                elif int(num1[i]) < int(num2[i]):
                    return -1
            return 0