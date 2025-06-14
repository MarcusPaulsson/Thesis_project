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
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1:
            num1 = '0'
        if not num2:
            num2 = '0'

        n1 = len(num1)
        n2 = len(num2)
        max_len = max(n1, n2)

        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])
            sum_digits = digit1 + digit2 + carry
            result = str(sum_digits % 10) + result
            carry = sum_digits // 10

        if carry:
            result = str(carry) + result

        return result.lstrip('0') or '0'

    @staticmethod
    def subtract(num1, num2):
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract,str.
        :param num2: The second number to subtract,str.
        :return: The difference of the two numbers,str.
        """
        num1 = num1.lstrip('0')
        num2 = num2.lstrip('0')

        if not num1:
            num1 = '0'
        if not num2:
            num2 = '0'

        n1 = len(num1)
        n2 = len(num2)

        if n1 < n2 or (n1 == n2 and num1 < num2):
            return '-' + BigNumCalculator.subtract(num2, num1)

        max_len = max(n1, n2)
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        result = ''
        borrow = 0

        for i in range(max_len - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])
            diff = digit1 - digit2 - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result

        return result.lstrip('0') or '0'

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

        if not num1:
            num1 = '0'
        if not num2:
            num2 = '0'

        n1 = len(num1)
        n2 = len(num2)
        result = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2
                p1 = i + j
                p2 = i + j + 1
                sum_val = product + result[p2]
                result[p2] = sum_val % 10
                result[p1] += sum_val // 10

        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') or '0'