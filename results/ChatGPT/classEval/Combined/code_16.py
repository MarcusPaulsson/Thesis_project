class Calculator:
    """
    A simple calculator for performing basic arithmetic operations 
    using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
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
        
        :param expression: str, the expression to evaluate
        :return: float or None, the result of the evaluation or None for invalid input
        """
        if not expression:
            return None

        operand_stack = []
        operator_stack = []
        index = 0
        length = len(expression)

        while index < length:
            char = expression[index]

            if char.isdigit():
                num = self.extract_number(expression, index)
                operand_stack.append(num)
                index += len(str(num))  # Move index forward to the end of the number

            elif char in self.operators:
                while (operator_stack and
                       self.precedence(operator_stack[-1]) >= self.precedence(char)):
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)

            elif char == '(':
                operator_stack.append(char)

            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Remove '('

            index += 1

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def extract_number(self, expression, index):
        """
        Extracts a full number from the expression starting at the given index.
        
        :param expression: str, the expression containing the number
        :param index: int, the starting index to extract the number
        :return: int, the extracted number
        """
        num = 0
        while index < len(expression) and expression[index].isdigit():
            num = num * 10 + int(expression[index])
            index += 1
        return num

    def precedence(self, operator):
        """
        Returns the precedence of the specified operator.
        
        :param operator: str, the operator to check
        :return: int, the precedence level of the operator
        """
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        """
        Applies the operator at the top of the operator stack 
        to the two topmost numbers on the operand stack.
        
        :param operand_stack: list, the stack of operands
        :param operator_stack: list, the stack of operators
        """
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        result = self.operators[operator](left_operand, right_operand)
        operand_stack.append(result)