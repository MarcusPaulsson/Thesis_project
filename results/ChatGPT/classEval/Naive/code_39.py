from collections import deque

class ExpressionCalculator:
    """
    This class performs calculations with basic arithmetic operations: addition, subtraction,
    multiplication, division, and modulo in postfix notation.
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
        tokens = expression.split()
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(float(token))
            else:
                second = stack.pop()
                first = stack.pop()
                result = self._calculate(first, second, token)
                stack.append(result)

        return stack[0]

    def prepare(self, expression):
        """
        Prepare the infix expression for conversion to postfix notation.
        
        :param expression: string, the infix expression to be prepared
        
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2 + 3 * 4")
        >>> expression_calculator.postfix_stack
        deque(['2', '3', '4', '*', '+'])
        """
        output = []
        operators = deque()
        tokens = expression.replace(" ", "")

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token in self.operator_priority:
                while (operators and 
                       self.operator_priority[token] <= self.operator_priority[operators[-1]]):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        self.postfix_stack = deque(output)

    @staticmethod
    def is_operator(c):
        """
        Check if a character is an operator.
        
        :param c: string, the character to be checked
        :return: bool, True if the character is an operator, False otherwise
        
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.is_operator("+")
        True
        """
        return c in {'+', '-', '*', '/', '%'}

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
        return self.operator_priority[cur] >= self.operator_priority[peek]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
        Perform the mathematical calculation based on the given operands and operator.
        
        :param first_value: float, the first operand
        :param second_value: float, the second operand
        :param current_op: string, the operator
        :return: float, the calculated result
        
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate(2, 3, "+")
        5.0
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
        Transform the infix expression to a format suitable for conversion.
        
        :param expression: string, the infix expression to be transformed
        :return: string, the transformed expression
        
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
        return expression.replace(" ", "")