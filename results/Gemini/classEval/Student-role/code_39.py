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
        self.operat_stack = deque()
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
        self.prepare(expression)
        stack = []
        while self.postfix_stack:
            token = self.postfix_stack.popleft()
            if not self.is_operator(token):
                stack.append(token)
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)
        return float(stack[0])


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        self.postfix_stack = deque()
        self.operat_stack = deque()
        expression = self.transform(expression)
        i = 0
        while i < len(expression):
            c = expression[i]
            if c.isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                self.postfix_stack.append(expression[i:j])
                i = j
            elif c == '(':
                self.operat_stack.append(c)
                i += 1
            elif c == ')':
                while self.operat_stack and self.operat_stack[-1] != '(':
                    self.postfix_stack.append(self.operat_stack.pop())
                self.operat_stack.pop()
                i += 1
            elif self.is_operator(c):
                while self.operat_stack and self.operat_stack[-1] != '(' and self.compare(c, self.operat_stack[-1]):
                    self.postfix_stack.append(self.operat_stack.pop())
                self.operat_stack.append(c)
                i += 1
            else:
                i += 1

        while self.operat_stack:
            self.postfix_stack.append(self.operat_stack.pop())


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
        return c in {'+', '-', '*', '/', '(', ')', '%', '~'}


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
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '~': 3}
        return priority[cur] <= priority[peek]


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
        elif current_op == '~':
            return 0 - second_value
        else:
            raise ValueError("Invalid operator")


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
        expression = expression.replace(" ", "")
        new_expression = ""
        for i in range(len(expression)):
            if expression[i] == '-' and (i == 0 or expression[i - 1] in {'(', '+', '-', '*', '/'}):
                new_expression += '~'
            else:
                new_expression += expression[i]
        return new_expression