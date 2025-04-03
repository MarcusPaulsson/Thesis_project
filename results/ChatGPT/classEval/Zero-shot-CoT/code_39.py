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
        self.operator_stack = deque()
        self.operat_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 3 4 * +")
        14.0
        """
        tokens = expression.split()
        for token in tokens:
            if not self.is_operator(token):
                self.postfix_stack.append(Decimal(token))
            else:
                second_value = self.postfix_stack.pop()
                first_value = self.postfix_stack.pop()
                result = self._calculate(first_value, second_value, token)
                self.postfix_stack.append(result)
        return float(self.postfix_stack.pop())

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        """
        output = []
        tokens = []
        num = ""
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    tokens.append(num)
                    num = ""
                if char in self.operat_priority:
                    tokens.append(char)
        if num:
            tokens.append(num)
        
        for token in tokens:
            if not self.is_operator(token):
                output.append(token)
            else:
                while (self.operator_stack and 
                       self.compare(token, self.operator_stack[-1])):
                    output.append(self.operator_stack.pop())
                self.operator_stack.append(token)

        while self.operator_stack:
            output.append(self.operator_stack.pop())
        
        self.postfix_stack = output

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
        return c in {'+', '-', '*', '/', '%'}

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
        return self.operat_priority[cur] <= self.operat_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator
        :param first_value: Decimal, the first operand
        :param second_value: Decimal, the second operand
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
            return first_value / second_value
        elif current_op == '%':
            return first_value % second_value

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
        return ''.join(expression.split())