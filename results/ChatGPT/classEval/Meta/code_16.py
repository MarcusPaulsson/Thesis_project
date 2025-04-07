class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initialize the operations performed by the five operators '+', '-', '*', '/', '^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else float('inf'),  # Handle division by zero
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return: If successful, returns the value of the expression; otherwise, returns None
        """
        if not expression:
            return None

        def shunting_yard(expression):
            output = []
            operators = []
            num = ''
            for char in expression:
                if char.isdigit() or char == '.':
                    num += char
                else:
                    if num:
                        output.append(float(num))
                        num = ''
                    if char in self.operators:
                        while (operators and self.precedence(operators[-1]) >= self.precedence(char)):
                            output.append(operators.pop())
                        operators.append(char)
                    elif char == '(':
                        operators.append(char)
                    elif char == ')':
                        while operators and operators[-1] != '(':
                            output.append(operators.pop())
                        operators.pop()  # Pop the '('
            if num:
                output.append(float(num))
            while operators:
                output.append(operators.pop())
            return output

        def evaluate_rpn(rpn):
            stack = []
            for token in rpn:
                if isinstance(token, float):
                    stack.append(token)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self.operators[token](a, b))
            return stack[0]

        rpn = shunting_yard(expression)
        return evaluate_rpn(rpn)

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. 
        The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
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
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack, 
        and store the results at the top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        b = operand_stack.pop()
        a = operand_stack.pop()
        result = self.operators[operator](a, b)
        operand_stack.append(result)
        return operand_stack, operator_stack