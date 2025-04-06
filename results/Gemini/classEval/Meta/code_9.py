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
        num1 = num1.strip()
        num2 = num2.strip()

        result = ""
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            sum_digits = digit1 + digit2 + carry
            carry = sum_digits // 10
            result = str(sum_digits % 10) + result

            i -= 1
            j -= 1

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
        num1 = num1.strip()
        num2 = num2.strip()

        # Determine which number is larger
        if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
            num1, num2 = num2, num1
            sign = "-"
        else:
            sign = ""

        result = ""
        borrow = 0
        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0:
            digit1 = int(num1[i])
            digit2 = int(num2[j]) if j >= 0 else 0

            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result

            i -= 1
            j -= 1

        # Remove leading zeros
        while len(result) > 1 and result[0] == '0':
            result = result[1:]

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
        num1 = num1.strip()
        num2 = num2.strip()

        if num1 == "0" or num2 == "0":
            return "0"

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

        # Convert result to string
        result_str = "".join(map(str, result))

        # Remove leading zeros
        while len(result_str) > 1 and result_str[0] == '0':
            result_str = result_str[1:]

        return result_str