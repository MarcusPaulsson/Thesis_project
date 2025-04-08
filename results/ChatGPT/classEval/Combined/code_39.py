from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    """
    A class to perform calculations with basic arithmetic operations
    including addition, subtraction, multiplication, division, and modulo.
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
        return float(self.evaluate_postfix())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation.
        :param expression: string, the infix expression to be prepared
        """
        output = []
        operator_stack = []
        tokens = self.tokenize(expression)

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif self.is_operator(token):
                while (operator_stack and operator_stack[-1] in self.operator_priority and
                       self.compare(token, operator_stack[-1])):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Pop the '('

        while operator_stack:
            output.append(operator_stack.pop())

        self.postfix_stack = deque(output)

    def evaluate_postfix(self):
        """
        Evaluate the postfix expression from the postfix stack.
        :return: Decimal, the evaluated result
        """
        stack = []
        for token in self.postfix_stack:
            if self.is_operator(token):
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
            else:
                stack.append(Decimal(token))
        return stack[0]

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '%'}.
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
        :param first_value: Decimal, the first operand
        :param second_value: Decimal, the second operand
        :param current_op: string, the operator
        :return: Decimal, the calculated result
        """
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value
        else:
            raise ValueError("Invalid Operator")

    @staticmethod
    def tokenize(expression):
        """
        Tokenize the infix expression by removing spaces.
        :param expression: string, the infix expression to be tokenized
        :return: list of tokens
        """
        return ''.join(expression.split())