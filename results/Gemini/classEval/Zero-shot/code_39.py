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
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]
        self.operator_stack = deque()

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
        postfix_list = list(self.postfix_stack)
        stack = deque()
        for item in postfix_list:
            if item.isdigit() or (item.startswith('~') and item[1:].isdigit()):
                stack.append(item)
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, item)
                stack.append(str(result))
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
        self.operator_stack = deque()
        expression = expression.replace(" ", "")
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit() or (char == '~'):
                num = char
                i += 1
                while i < len(expression) and (expression[i].isdigit()):
                    num += expression[i]
                    i += 1
                self.postfix_stack.append(num)
                i -= 1
            elif self.is_operator(char):
                while self.operator_stack and self.compare(char, self.operator_stack[-1]):
                    self.postfix_stack.append(self.operator_stack.pop())
                self.operator_stack.append(char)
            elif char == '(':
                self.operator_stack.append(char)
            elif char == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.postfix_stack.append(self.operator_stack.pop())
                self.operator_stack.pop()
            i += 1
        while self.operator_stack:
            self.postfix_stack.append(self.operator_stack.pop())


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
        op_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '(': 0, ')': 0}
        return op_priority[peek] >= op_priority[cur]


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
        first_value = float(first_value.replace('~', '-'))
        second_value = float(second_value.replace('~', '-'))
        if current_op == '+':
            return decimal.Decimal(first_value + second_value)
        elif current_op == '-':
            return decimal.Decimal(first_value - second_value)
        elif current_op == '*':
            return decimal.Decimal(first_value * second_value)
        elif current_op == '/':
            return decimal.Decimal(first_value / second_value)
        elif current_op == '%':
            return decimal.Decimal(first_value % second_value)
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
        i = 0
        while i < len(expression):
            if expression[i] == '-' and (i == 0 or expression[i - 1] in {'(', '+', '-', '*', '/'}):
                new_expression += '~'
            else:
                new_expression += expression[i]
            i += 1
        return new_expression