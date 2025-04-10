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
            '/': lambda x, y: x / y,
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
        
        operand_stack = []
        operator_stack = []
        i = 0
        n = len(expression)

        while i < n:
            # Skip whitespace
            if expression[i] == ' ':
                i += 1
                continue
            
            # Handle numbers
            if expression[i].isdigit():
                num = 0
                while i < n and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                operand_stack.append(num)
                continue
            
            # Handle operators
            if expression[i] in self.operators:
                while (operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i])):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
            
            # Handle parentheses
            elif expression[i] == '(':
                operator_stack.append(expression[i])
            elif expression[i] == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Remove the '('
            else:
                return None  # Invalid character
            
            i += 1

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator
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
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: None
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        result = self.operators[operator](left, right)
        operand_stack.append(result)