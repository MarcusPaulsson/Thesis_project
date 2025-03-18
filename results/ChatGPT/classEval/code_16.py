class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators '+', '-', '*', '/', '^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        def evaluate(tokens):
            operand_stack = []
            operator_stack = []

            def apply_operator():
                operator = operator_stack.pop()
                right = operand_stack.pop()
                left = operand_stack.pop()
                result = self.operators[operator](left, right)
                operand_stack.append(result)

            i = 0
            while i < len(tokens):
                if tokens[i].isdigit():
                    operand_stack.append(float(tokens[i]))
                elif tokens[i] in self.operators:
                    while (operator_stack and
                           self.precedence(operator_stack[-1]) >= self.precedence(tokens[i])):
                        apply_operator()
                    operator_stack.append(tokens[i])
                i += 1

            while operator_stack:
                apply_operator()

            return operand_stack[0] if operand_stack else None

        tokens = []
        current_number = []
        for char in expression:
            if char.isdigit() or char == '.':
                current_number.append(char)
            else:
                if current_number:
                    tokens.append(''.join(current_number))
                    current_number = []
                if char in self.operators:
                    tokens.append(char)
        if current_number:
            tokens.append(''.join(current_number))

        return evaluate(tokens)

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        if operator == '^':
            return 3
        elif operator in ('*', '/'):
            return 2
        elif operator in ('+', '-'):
            return 1
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        result = self.operators[operator](left, right)
        operand_stack.append(result)
        return operand_stack, operator_stack