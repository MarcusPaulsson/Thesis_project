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
        expression = self.transform(expression)
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                self.postfix_stack.append(Decimal(token))
            elif self.is_operator(token):
                if len(self.postfix_stack) < 2:
                    return "Invalid expression"
                operand2 = self.postfix_stack.pop()
                operand1 = self.postfix_stack.pop()
                result = self._calculate(operand1, operand2, token)
                self.postfix_stack.append(result)
            else:
                return "Invalid expression"
        if len(self.postfix_stack) == 1:
            return float(self.postfix_stack.pop())
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
        tokens = expression.split()
        op_stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                self.postfix_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()  # Pop the '('
            elif self.is_operator(token):
                while op_stack and op_stack[-1] != '(' and self.operat_priority[self.get_operator_index(token)] <= self.operat_priority[self.get_operator_index(op_stack[-1])]:
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(token)
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
        return c in {'+', '-', '*', '/', '(', ')', '%'}

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
        return self.operat_priority[self.get_operator_index(cur)] >= self.operat_priority[self.get_operator_index(peek)]

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
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            if second_value == 0:
                return "Division by zero"
            return first_value / second_value
        elif current_op == '%':
            if second_value == 0:
                return "Modulo by zero"
            return first_value % second_value
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
        expression = expression.replace('(', '~(')
        expression = expression.replace(')', ')~')
        expression = expression.replace('-', '~')
        return expression.replace(' ', '')

    def get_operator_index(self, operator):
        if operator == '+':
            return 0
        elif operator == '-':
            return 1
        elif operator == '*':
            return 2
        elif operator == '/':
            return 3
        elif operator == '%':
            return 4
        elif operator == '(':
            return 5
        elif operator == ')':
            return 6
        else:
            return 7