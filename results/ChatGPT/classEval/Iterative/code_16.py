class Calculator:
    """
    A class for a calculator capable of performing basic arithmetic calculations on numerical expressions
    using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the operators '+', '-', '*', '/', '^'.
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf'),  # Handle division by zero
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression.
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        >>> calculator.calculate('2/0')
        inf
        """
        tokens = self.tokenize(expression)
        operand_stack = []
        operator_stack = []

        for token in tokens:
            if self.is_number(token):
                operand_stack.append(float(token))
            else:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(token)

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def tokenize(self, expression):
        """
        Tokenizes the input expression into numbers and operators.
        :param expression: string, the expression to tokenize
        :return: list of tokens
        """
        tokens = []
        num = ''
        for char in expression:
            if char in self.operators or char in '()':
                if num:
                    tokens.append(num)
                    num = ''
                tokens.append(char)
            else:
                num += char
        if num:
            tokens.append(num)
        return tokens

    def precedence(self, operator):
        """
        Returns the priority of the specified operator.
        :param operator: string, given operator
        :return: int, the priority of the given operator; returns 0 if the operator is unknown
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        return {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top
        of the operand stack and store the result at the top of the operand stack.
        :param operand_stack: list
        :param operator_stack: list
        """
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        result = self.operators[operator](left_operand, right_operand)
        operand_stack.append(result)

    def is_number(self, token):
        """
        Check if the token is a number.
        :param token: string, token to check
        :return: bool, True if token is a number, otherwise False
        """
        try:
            float(token)
            return True
        except ValueError:
            return False