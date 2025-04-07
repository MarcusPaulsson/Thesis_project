from collections import deque
from decimal import Decimal


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
        expression = expression.replace(" ", "")
        tokens = expression.split('+')
        if len(tokens) == 1:
            tokens = expression.split('-')
        if len(tokens) == 1:
            tokens = expression.split('*')
        if len(tokens) == 1:
            tokens = expression.split('/')
        if len(tokens) == 1:
            tokens = expression.split('%')

        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(Decimal(token))
            else:
                if len(stack) < 2:
                    return "Invalid expression"
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        return "Division by zero"
                    stack.append(operand1 / operand2)
                elif token == '%':
                    if operand2 == 0:
                        return "Modulo by zero"
                    stack.append(operand1 % operand2)
                else:
                    return "Invalid operator"

        if len(stack) == 1:
            return float(stack[0])
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
        expression = expression.replace(" ", "")
        self.postfix_stack = deque()
        op_stack = []

        for char in expression:
            if char.isdigit():
                self.postfix_stack.append(char)
            elif char in "+-*/%":
                while op_stack and self.compare(char, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(char)
        while op_stack:
            self.postfix_stack.append(op_stack.pop())

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
        return c in "+-*/%"

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
        priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2
        }
        return priority.get(cur, 0) >= priority.get(peek, 0)

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
        first = Decimal(first_value)
        second = Decimal(second_value)
        if current_op == '+':
            return first + second
        elif current_op == '-':
            return first - second
        elif current_op == '*':
            return first * second
        elif current_op == '/':
            if second == 0:
                return "Division by zero"
            return first / second
        elif current_op == '%':
            if second == 0:
                return "Modulo by zero"
            return first % second
        else:
            return "Invalid operator"

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