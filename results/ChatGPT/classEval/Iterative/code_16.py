class Calculator:
    """
    This is a class for a calculator, capable of performing basic arithmetic calculations 
    on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
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

        def apply_operator(operand_stack, operator_stack):
            operator = operator_stack.pop()
            right = operand_stack.pop()
            left = operand_stack.pop()
            result = self.operators[operator](left, right)
            operand_stack.append(result)

        def precedence(operator):
            if operator in ('+', '-'):
                return 1
            elif operator in ('*', '/'):
                return 2
            elif operator == '^':
                return 3
            return 0

        operand_stack = []
        operator_stack = []
        index = 0
        n = len(expression)

        while index < n:
            if expression[index].isspace():
                index += 1
                continue
            
            if expression[index].isdigit():
                num = 0
                while index < n and expression[index].isdigit():
                    num = num * 10 + int(expression[index])
                    index += 1
                operand_stack.append(num)
                continue

            if expression[index] in self.operators:
                while (operator_stack and 
                       precedence(operator_stack[-1]) >= precedence(expression[index])):
                    apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[index])

            elif expression[index] == '(':
                operator_stack.append(expression[index])

            elif expression[index] == ')':
                while operator_stack and operator_stack[-1] != '(':
                    apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # pop the '('

            index += 1

        while operator_stack:
            apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator.
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        elif operator == '^':
            return 3
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on 
        the two numbers at the top of the operand stack, and store the results at the 
        top of the operand stack.
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand_stack and operator_stack
        """
        operator = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        result = self.operators[operator](left, right)
        operand_stack.append(result)
        return operand_stack, operator_stack