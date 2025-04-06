import decimal
from collections import deque


class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        tokens = expression.split()
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(float(token))
            elif token in {'+', '-', '*', '/', '%'}:
                if len(stack) < 2:
                    return "Invalid expression"
                second_value = stack.pop()
                first_value = stack.pop()
                try:
                    result = self._calculate(first_value, second_value, token)
                    stack.append(result)
                except ZeroDivisionError:
                    return "Division by zero error"
            else:
                return "Invalid expression"

        if len(stack) == 1:
            return stack[0]
        else:
            return "Invalid expression"

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        expression = self.transform(expression)
        op_stack = []
        output = []
        for char in expression:
            if char.isdigit():
                output.append(char)
            elif self.is_operator(char):
                while op_stack and self.is_operator(op_stack[-1]) and self.compare(char, op_stack[-1]):
                    output.append(op_stack.pop())
                op_stack.append(char)
            elif char == '(':
                op_stack.append(char)
            elif char == ')':
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                op_stack.pop()  # Remove the '('
        while op_stack:
            output.append(op_stack.pop())
        self.postfix_stack = deque(output)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True

        """
        return c in {'+', '-', '*', '/', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        return priority.get(cur, 0) <= priority.get(peek, 0)

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0

        """
        first_value = float(first_value)
        second_value = float(second_value)
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                raise ZeroDivisionError("Division by zero")
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value
        else:
            return 0.0

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
        return expression.replace(" ", "")