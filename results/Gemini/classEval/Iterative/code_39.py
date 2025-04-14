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
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]


    def calculate(self, expression):
        """
        Calculate the result of the given infix expression
        :param expression: string, the infix expression to be calculated
        :return: float, the calculated result
        """
        try:
            expression = self.transform(expression)
            self.prepare(expression)
            postfix_list = list(self.postfix_stack)
            stack = deque()
            for item in postfix_list:
                if not self.is_operator(item):
                    stack.append(item)
                else:
                    second_value = stack.pop()
                    first_value = stack.pop()
                    result = self._calculate(first_value, second_value, item)
                    stack.append(str(result))
            return float(stack[0])
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")


    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        """
        self.postfix_stack = deque()
        self.operator_stack = deque()
        expression = self.transform(expression)
        i = 0
        while i < len(expression):
            c = expression[i]
            if c.isdigit():
                j = i
                num_str = ""
                while j < len(expression) and expression[j].isdigit():
                    num_str += expression[j]
                    j += 1
                self.postfix_stack.append(num_str)
                i = j
                continue
            elif self.is_operator(c):
                if c == '(':
                    self.operator_stack.append(c)
                elif c == ')':
                    while self.operator_stack and self.operator_stack[-1] != '(':
                        self.postfix_stack.append(self.operator_stack.pop())
                    if self.operator_stack:
                        self.operator_stack.pop()  # Remove the '('
                    else:
                        raise ValueError("Unmatched parentheses")
                else:
                    while self.operator_stack and self.operator_stack[-1] != '(' and self.compare(c, self.operator_stack[-1]):
                        self.postfix_stack.append(self.operator_stack.pop())
                    self.operator_stack.append(c)
                i += 1
            else:
                i += 1

        while self.operator_stack:
            if self.operator_stack[-1] == '(':
                raise ValueError("Unmatched parentheses")
            self.postfix_stack.append(self.operator_stack.pop())


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
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
        return priority.get(cur, 0) <= priority.get(peek, 0)


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
            if second_value == 0:
                raise ZeroDivisionError("Division by zero")
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
        expression = expression.replace("(-", "(~")
        expression = expression.replace("~(", "0-(")
        if expression.startswith("-"):
            expression = "~" + expression[1:]
        return expression.replace("~", "0-")