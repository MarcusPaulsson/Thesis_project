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
            '/': lambda x, y: x / y if y != 0 else None,  # Handle division by zero
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        """
        if not expression:
            return None

        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                operand_stack.append(float(num))
                i -= 1  # Correct the index after extracting the number
            elif char in self.operators:
                while operator_stack and operator_stack[-1] in self.operators and self.precedence(char) <= self.precedence(operator_stack[-1]):
                    result = self.apply_operator(operand_stack, operator_stack)
                    if result is None:
                        return None # Propagate errors from apply_operator
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    result = self.apply_operator(operand_stack, operator_stack)
                    if result is None:
                        return None  # Propagate errors from apply_operator
                if not operator_stack:
                    return None  # unbalanced parentheses
                operator_stack.pop()  # Remove the '('
            i += 1

        while operator_stack:
            result = self.apply_operator(operand_stack, operator_stack)
            if result is None:
                return None  # Propagate errors from apply_operator

        if operand_stack:
            if len(operand_stack) > 1:
                return None # Invalid Expression
            return operand_stack[0]
        else:
            return None

    def precedence(self, operator):
        """
        Returns the priority of the specified operator, where the higher the priority, the greater the assignment. The priority of '^' is greater than '/' and '*', and the priority of '/' and '*' is greater than '+' and '-'
        :param operator: string, given operator
        :return: int, the priority of the given operator, otherwise return 0
        """
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        """
        if len(operand_stack) < 2 or not operator_stack:
            return None

        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        try:
            result = self.operators[operator](operand1, operand2)
        except ZeroDivisionError:
            return None

        if result is None:
            return None

        operand_stack.append(result)
        return result