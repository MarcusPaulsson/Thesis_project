from collections import deque
import decimal


class ExpressionCalculator:
    """
    This is a class in Python that can perform calculations with basic arithmetic operations, including addition, subtraction, multiplication, division, and modulo.
    """

    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operator_stack = deque()

    def calculate(self, expression):
        """
        Calculate the result of the given infix expression
        :param expression: string, the infix expression to be calculated
        :return: float, the calculated result
        """
        self.prepare(expression)
        postfix_list = list(self.postfix_stack)
        expression_stack = deque()
        for item in postfix_list:
            if item not in "+-*/%":
                expression_stack.append(item)
            else:
                second_value = expression_stack.pop()
                first_value = expression_stack.pop()
                result = self._calculate(first_value, second_value, item)
                expression_stack.append(str(result))
        return float(expression_stack[0])

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        self.postfix_stack = deque()
        self.operator_stack = deque()
        expression = self.transform(expression)
        num = ""
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    self.postfix_stack.append(num)
                    num = ""
                if char == '(':
                    self.operator_stack.append(char)
                elif char == ')':
                    while self.operator_stack and self.operator_stack[-1] != '(':
                        self.postfix_stack.append(self.operator_stack.pop())
                    self.operator_stack.pop()
                elif self.is_operator(char):
                    while self.operator_stack and self.operator_stack[-1] != '(' and self.compare(char, self.operator_stack[-1]):
                        self.postfix_stack.append(self.operator_stack.pop())
                    self.operator_stack.append(char)

        if num:
            self.postfix_stack.append(num)
        while self.operator_stack:
            self.postfix_stack.append(self.operator_stack.pop())

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        return priority.get(peek, 0) >= priority.get(cur, 0)

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
        first_value = decimal.Decimal(first_value)
        second_value = decimal.Decimal(second_value)
        if current_op == '+':
            return first_value + second_value
        elif current_op == '-':
            return first_value - second_value
        elif current_op == '*':
            return first_value * second_value
        elif current_op == '/':
            return first_value / second_value
        elif current_op == '%':
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
        expression = expression.replace(" ", "")
        expression = expression.replace("~", "0-")

        if expression.startswith('-'):
            expression = '0' + expression
        expression = expression.replace('(-', '(0-')

        return expression