class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations 
    including addition, subtraction, multiplication, division, and exponentiation.
    """

    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf'),  # handle division by zero
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Evaluates the given arithmetic expression.
        :param expression: str, a valid arithmetic expression
        :return: float, the result of the expression; None if invalid or empty.
        """
        if not expression:
            return None

        operand_stack = []
        operator_stack = []
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                operand_stack.append(num)
                continue

            if char in self.operators:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(char)):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)

            elif char == '(':
                operator_stack.append(char)

            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # remove '('

            i += 1

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the precedence level of the given operator.
        :param operator: str, the operator to evaluate
        :return: int, the precedence level
        """
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Applies the top operator to the top two operands.
        :param operand_stack: list, stack of operands
        :param operator_stack: list, stack of operators
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        result = self.operators[operator](left, right)
        operand_stack.append(result)