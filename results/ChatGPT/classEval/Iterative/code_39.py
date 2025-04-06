from collections import deque
from decimal import Decimal

class ExpressionCalculator:
    """
    This class performs calculations with basic arithmetic operations,
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
        Calculate the result of the given postfix expression.
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 3 4 * +")
        14.0
        """
        stack = []
        tokens = expression.split()
        for token in tokens:
            if self.is_number(token):
                stack.append(Decimal(token))
            elif self.is_operator(token):
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
            else:
                raise ValueError(f"Invalid token: {token}")
        return float(stack.pop())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation.
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2 + 3 * 4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        output = []
        operator_stack = []
        tokens = self.transform(expression).split()

        for token in tokens:
            if self.is_number(token):
                output.append(token)
            elif self.is_operator(token):
                while (operator_stack and operator_stack[-1] in self.operator_priority and
                       self.compare(token, operator_stack[-1])):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                raise ValueError(f"Invalid token: {token}")

        while operator_stack:
            output.append(operator_stack.pop())

        self.postfix_stack = output

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '%'}.
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True
        """
        return c in {'+', '-', '*', '/', '%'}

    @staticmethod
    def is_number(c):
        """
        Check if the token is a number.
        :param c: string, the token to be checked
        :return: bool, True if the token is a number, False otherwise
        """
        try:
            Decimal(c)
            return True
        except (ValueError, InvalidOperation):
            return False

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators.
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True
        """
        return self.operator_priority[cur] <= self.operator_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator.
        :param first_value: decimal.Decimal, the first operand
        :param second_value: decimal.Decimal, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate(Decimal("2"), Decimal("3"), "+")
        Decimal('5')
        """
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value
        else:
            raise ValueError(f"Invalid operator: {current_op}")

    @staticmethod
    def transform(expression):
        """
        Transform the infix expression to a format suitable for conversion.
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
        return ''.join(expression.split())