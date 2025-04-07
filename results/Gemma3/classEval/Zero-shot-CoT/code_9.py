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
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))
        carry = 0
        result = ''
        for i in range(len(num1) - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])
            sum_digits = digit1 + digit2 + carry
            result = str(sum_digits % 10) + result
            carry = sum_digits // 10
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
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))
        borrow = 0
        result = ''
        for i in range(len(num1) - 1, -1, -1):
            digit1 = int(num1[i])
            digit2 = int(num2[i])
            diff = digit1 - digit2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result = str(diff) + result
        if borrow:
            return "-" + result
        else:
            return result

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
        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1.zfill(len(num1))
        num2 = num2.zfill(len(num2))

        products = []
        for i in range(len(num2) - 1, -1, -1):
            product = []
            carry = 0
            for j in range(len(num1) - 1, -1, -1):
                digit1 = int(num1[j])
                digit2 = int(num2[i])
                product_digit = (digit1 * digit2 + carry) % 10
                carry = (digit1 * digit2 + carry) // 10
                product.insert(0, str(product_digit))
            if carry:
                product.insert(0, str(carry))
            products.append("".join(product) + "0" * (len(num2) - 1 - i))

        result = "0"
        for product in products:
            result = BigNumCalculator.add(result, product)

        return result