from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    """
    A class to perform calculations with basic arithmetic operations, including addition, subtraction,
    multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator.
        """
        self.postfix_stack = deque()
        self.operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    def calculate(self, expression):
        """
        Calculate the result of the given infix expression.
        :param expression: string, the infix expression to be calculated
        :return: float, the calculated result
        """
        self.prepare(expression)
        stack = []
        for token in self.postfix_stack:
            if self.is_operator(token):
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
            else:
                stack.append(Decimal(token))
        return float(stack.pop())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation.
        :param expression: string, the infix expression to be prepared
        """
        self.postfix_stack.clear()
        output = []
        operators = []
        tokens = self.transform(expression).split()

        for token in tokens:
            if self.is_number(token):
                output.append(token)
            elif self.is_operator(token):
                while (operators and operators[-1] in self.operator_priority and
                       self.compare(token, operators[-1])):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the '('

        while operators:
            output.append(operators.pop())

        self.postfix_stack = deque(output)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator.
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators.
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        return self.operator_priority[cur] <= self.operator_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator.
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        first_value = Decimal(first_value)
        second_value = Decimal(second_value)
        operations = {
            '+': first_value + second_value,
            '-': first_value - second_value,
            '*': first_value * second_value,
            '/': first_value / second_value,
            '%': first_value % second_value
        }
        return operations.get(current_op, ValueError(f"Invalid operator: {current_op}"))

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion.
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        return expression.replace(" ", "")

    @staticmethod
    def is_number(token):
        """
        Check if the token is a valid number (integer or decimal).
        :param token: string, the token to check
        :return: bool, True if the token is a number, False otherwise
        """
        try:
            Decimal(token)
            return True
        except (ValueError, InvalidOperation):
            return False