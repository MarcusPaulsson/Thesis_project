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
        operand_stack = []
        operator_stack = []
        i = 0
        n = len(expression)

        while i < n:
            if expression[i].isdigit() or (expression[i] == '-' and (i == 0 or expression[i-1] in "+-*/^")):
                num = 0
                while i < n and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        fraction = 0
                        decimal_place = 1
                        i += 1
                        while i < n and expression[i].isdigit():
                            fraction = fraction * 10 + int(expression[i])
                            decimal_place *= 10
                            i += 1
                        num += fraction / decimal_place
                    else:
                        num = num * 10 + int(expression[i])
                        i += 1
                operand_stack.append(num)
            else:
                while (operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i])):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(expression[i])
                i += 1

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[-1] if operand_stack else None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator == '^':
            return 3
        elif operator in ('*', '/'):
            return 2
        elif operator in ('+', '-'):
            return 1
        return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operand stack and store the results at the top of the operand stack
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