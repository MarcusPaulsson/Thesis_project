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
        """
        expression = self.transform(expression)
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                self.postfix_stack.append(token)
            elif token == '(':
                self.postfix_stack.append(token)
            elif token == ')':
                while self.postfix_stack and self.postfix_stack[-1] != '(':
                    self.postfix_stack.append(self.postfix_stack.pop())
                self.postfix_stack.pop()  # Remove the '('
            elif self.is_operator(token):
                while self.postfix_stack and self.postfix_stack[-1] != '(' and self.compare(token, self.postfix_stack[-1]):
                    self.postfix_stack.append(self.postfix_stack.pop())
                self.postfix_stack.append(token)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator in {'+', '-', '*', '/', '(', ')', '%'}
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        """
        return c in {'+', '-', '*', '/', '(', ')', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        """
        cur_index = self.operat_priority[self.get_operator_index(cur)]
        peek_index = self.operat_priority[self.get_operator_index(peek)]
        return cur_index >= peek_index

    def get_operator_index(self, operator):
        operators = ['+', '-', '*', '/', '%']
        return operators.index(operator) if operator in operators else -1

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: string, the first operand
        :param second_value: string, the second operand
        :param current_op: string, the operator
        :return: decimal.Decimal, the calculated result
        """
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
        expression = expression.replace('(', '~(')
        expression = expression.replace(')', ')~')
        expression = expression.replace(' ', '')
        return expression