from collections import deque
import decimal
import re


class ExpressionCalculator:
    """
    A class to calculate the result of arithmetic expressions.
    Supports +, -, *, /, %, and parentheses.
    Handles negative numbers and operator precedence correctly.
    """

    def __init__(self):
        """
        Initializes the ExpressionCalculator with operator precedence and stacks.
        """
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '~': 3,  # Unary minus (negative sign)
            '(': 0,  # Lowest precedence to ensure it stays on the stack
        }

    def calculate(self, expression):
        """
        Calculates the result of the given expression.

        Args:
            expression (str): The arithmetic expression to calculate.

        Returns:
            float: The result of the expression, or None if an error occurs.
        """
        try:
            postfix = self._infix_to_postfix(expression)
            result = self._evaluate_postfix(postfix)
            return float(result)
        except Exception as e:
            print(f"Error during calculation: {e}")
            return None

    def _infix_to_postfix(self, expression):
        """
        Converts an infix expression to postfix notation.

        Args:
            expression (str): The infix expression.

        Returns:
            list: The postfix expression as a list of tokens.
        """
        expression = self._preprocess_expression(expression)
        output = []
        operators = deque()

        for token in re.findall(r"(\d+(\.\d*)?|\.\d+|\+|-|\*|/|%|\(|\))", expression):
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove the '('
            elif token in self.precedence:
                while operators and self.precedence[token] <= self.precedence.get(operators[-1], -1):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def _evaluate_postfix(self, postfix):
        """
        Evaluates a postfix expression.

        Args:
            postfix (list): The postfix expression as a list of tokens.

        Returns:
            decimal.Decimal: The result of the evaluation.
        """
        stack = []
        for token in postfix:
            if self._is_number(token):
                stack.append(decimal.Decimal(token))
            else:
                if token == '~':  # Unary minus
                    operand = stack.pop()
                    stack.append(-operand)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = self._apply_operator(operand1, operand2, token)
                    stack.append(result)

        return stack[0]

    def _apply_operator(self, operand1, operand2, operator):
        """
        Applies the given operator to the two operands.

        Args:
            operand1 (decimal.Decimal): The first operand.
            operand2 (decimal.Decimal): The second operand.
            operator (str): The operator.

        Returns:
            decimal.Decimal: The result of the operation.
        """
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '%':
            return operand1 % operand2
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    def _preprocess_expression(self, expression):
        """
        Preprocesses the expression to handle whitespace and unary minus.

        Args:
            expression (str): The original expression.

        Returns:
            str: The preprocessed expression.
        """
        expression = expression.replace(" ", "")
        expression = expression.replace("(-", "(0-")
        if expression.startswith("-"):
            expression = "0" + expression
        return expression

    @staticmethod
    def _is_number(s):
        """
        Checks if a string is a number (integer or decimal).

        Args:
            s (str): The string to check.

        Returns:
            bool: True if the string is a number, False otherwise.
        """
        try:
            decimal.Decimal(s)
            return True
        except decimal.InvalidOperation:
            return False