class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        operand_stack = []
        operator_stack = []
        tokens = self.tokenize(expression)

        for token in tokens:
            if self.is_number(token):
                operand_stack.append(float(token))
            elif token in self.operators:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Remove the '('

        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)

        if operand_stack:
            return operand_stack[0]
        else:
            return None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        return operand_stack, operator_stack

    def tokenize(self, expression):
        """
        Splits the expression into tokens (numbers and operators).
        """
        tokens = []
        current_number = ""
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            elif char in self.operators or char in "()":
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                tokens.append(char)
            elif char.isspace():
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
            else:
                pass #Ignore invalid character
        if current_number:
            tokens.append(current_number)
        return tokens

    def is_number(self, token):
        """
        Checks if a token is a number.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False