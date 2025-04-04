class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators '+', '-', '*', '/', '^'.
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
        Calculate the value of a given expression.
        
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None.
        
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
        operand_stack = []
        operator_stack = []
        num = ''
        
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    operand_stack.append(float(num))
                    num = ''
                while (operator_stack and 
                       self.precedence(char) <= self.precedence(operator_stack[-1])):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)

        if num:
            operand_stack.append(float(num))

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator.
        
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        precedence_order = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_order.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers 
        at the top of the operand stack, and store the result at the top of the operand stack.
        
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack
        
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        operator = operator_stack.pop()
        result = self.operators[operator](left_operand, right_operand)
        operand_stack.append(result)
        return operand_stack, operator_stack