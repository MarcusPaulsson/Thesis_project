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
        self.operat_priority = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "(": 0}

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        """
        postfix_expr = self.prepare(expression)
        stack = []

        for token in postfix_expr:
            if not self.is_operator(token):
                stack.append(Decimal(token))
            else:
                second = stack.pop()
                first = stack.pop()
                result = self._calculate(first, second, token)
                stack.append(result)

        return float(stack[0])

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        output = []
        operator_stack = []

        expression = self.transform(expression)
        tokens = self.tokenize(expression)

        for token in tokens:
            if not self.is_operator(token):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while (operator_stack and operator_stack[-1] in self.operat_priority and
                       self.compare(token, operator_stack[-1])):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        self.postfix_stack = deque(output)
        return self.postfix_stack

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '%', '(', ')'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        return self.operat_priority[cur] <= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        if current_op == "+":
            return first_value + second_value
        elif current_op == "-":
            return first_value - second_value
        elif current_op == "*":
            return first_value * second_value
        elif current_op == "/":
            return first_value / second_value
        elif current_op == "%":
            return first_value % second_value
        else:
            raise ValueError("Invalid operator")

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        """
        return expression.replace(" ", "")

    @staticmethod
    def tokenize(expression):
        """
        Tokenizes the input expression into individual elements
        :param expression: string, the expression to be tokenized
        :return: list, the list of tokens
        """
        tokens = []
        current_token = ''

        for char in expression:
            if char.isdigit() or char == '.':
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                    current_token = ''
                if char in {'+', '-', '*', '/', '%', '(', ')'}:
                    tokens.append(char)

        if current_token:
            tokens.append(current_token)

        return tokens