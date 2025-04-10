class BigNumCalculator:
    """
    A class to perform arithmetic operations on big numbers represented as strings.
    """

    @staticmethod
    def add(num1: str, num2: str) -> str:
        """
        Adds two big numbers.
        :param num1: The first number to add, str.
        :param num2: The second number to add, str.
        :return: The sum of the two numbers, str.
        """
        num1 = list(map(int, num1[::-1]))
        num2 = list(map(int, num2[::-1]))

        max_length = max(len(num1), len(num2))
        carry = 0
        result = []

        for i in range(max_length):
            digit1 = num1[i] if i < len(num1) else 0
            digit2 = num2[i] if i < len(num2) else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(total % 10)

        if carry:
            result.append(carry)

        return ''.join(map(str, result[::-1]))

    @staticmethod
    def subtract(num1: str, num2: str) -> str:
        """
        Subtracts two big numbers.
        :param num1: The first number to subtract, str.
        :param num2: The second number to subtract, str.
        :return: The difference of the two numbers, str.
        """
        num1 = list(map(int, num1[::-1]))
        num2 = list(map(int, num2[::-1]))

        max_length = max(len(num1), len(num2))
        borrow = 0
        result = []

        for i in range(max_length):
            digit1 = num1[i] if i < len(num1) else 0
            digit2 = num2[i] if i < len(num2) else 0
            if digit1 < digit2 + borrow:
                digit1 += 10
                result.append(digit1 - digit2 - borrow)
                borrow = 1
            else:
                result.append(digit1 - digit2 - borrow)
                borrow = 0

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))

    @staticmethod
    def multiply(num1: str, num2: str) -> str:
        """
        Multiplies two big numbers.
        :param num1: The first number to multiply, str.
        :param num2: The second number to multiply, str.
        :return: The product of the two numbers, str.
        """
        num1 = list(map(int, num1[::-1]))
        num2 = list(map(int, num2[::-1]))
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = num1[i] * num2[j] + result[i + j]
                result[i + j] = product % 10
                result[i + j + 1] += product // 10

        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))