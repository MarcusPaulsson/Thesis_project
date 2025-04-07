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

        len1 = len(num1)
        len2 = len(num2)

        if len1 < len2:
            num1, num2 = num2, num1
            len1, len2 = len2, len1

        result = []
        carry = 0

        for i in range(len2):
            digit1 = int(num1[len1 - 1 - i])
            digit2 = int(num2[len2 - 1 - i])
            sum_digits = digit1 + digit2 + carry
            result.append(str(sum_digits % 10))
            carry = sum_digits // 10

        for i in range(len2, len1):
            digit1 = int(num1[len1 - 1 - i])
            sum_digits = digit1 + carry
            result.append(str(sum_digits % 10))
            carry = sum_digits // 10

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

        if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
            num1, num2 = num2, num1
            sign = '-'
        else:
            sign = ''

        len1 = len(num1)
        len2 = len(num2)

        result = []
        borrow = 0

        for i in range(len2):
            digit1 = int(num1[len1 - 1 - i])
            digit2 = int(num2[len2 - 1 - i])
            diff = digit1 - digit2 - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result.append(str(diff))

        for i in range(len2, len1):
            digit1 = int(num1[len1 - 1 - i])
            diff = digit1 - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result.append(str(diff))

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
        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1 or not num2:
            return '0'

        len1 = len(num1)
        len2 = len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                sum_val = product + result[p2]

                result[p2] = sum_val % 10
                result[p1] += sum_val // 10

        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str if result_str else '0'