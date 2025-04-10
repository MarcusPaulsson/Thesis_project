from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    """
    A class to perform calculations with basic arithmetic operations: 
    addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initializes the expression calculator with an empty postfix stack 
        and operator precedence.
        """
        self.postfix_stack = deque()
        self.operator_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    def calculate(self, expression):
        """
        Calculate the result of the given infix expression.
        
        :param expression: str, the infix expression to be calculated
        :return: float, the calculated result
        """
        self.prepare(expression)
        stack = []
        
        for token in self.postfix_stack:
            if not self.is_operator(token):
                stack.append(Decimal(token))
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        
        return float(stack[0])

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation.

        :param expression: str, the infix expression to be prepared
        """
        expression = self.transform(expression)
        output = []
        operators = []

        for char in expression:
            if char.isdigit() or (char == '-' and (not output or output[-1] in self.operator_priority)):
                output.append(char)
            elif self.is_operator(char):
                while (operators and operators[-1] in self.operator_priority and 
                       self.compare(char, operators[-1])):
                    output.append(operators.pop())
                operators.append(char)
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '(' from operators

        while operators:
            output.append(operators.pop())

        self.postfix_stack = deque(output)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator.

        :param c: str, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '%'}

    def compare(self, current, top):
        """
        Compare the precedence of two operators.

        :param current: str, the current operator
        :param top: str, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        return self.operator_priority[current] <= self.operator_priority[top]

    @staticmethod
    def _calculate(first_value, second_value, operator):
        """
        Perform the mathematical calculation based on the given operands and operator.

        :param first_value: Decimal, the first operand
        :param second_value: Decimal, the second operand
        :param operator: str, the operator
        :return: Decimal, the calculated result
        """
        operations = {
            '+': first_value + second_value,
            '-': first_value - second_value,
            '*': first_value * second_value,
            '/': first_value / second_value,
            '%': first_value % second_value
        }
        return operations.get(operator, ValueError(f"Invalid operator: {operator}"))

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion.

        :param expression: str, the infix expression to be transformed
        :return: str, the transformed expression
        """
        return ''.join(expression.split())