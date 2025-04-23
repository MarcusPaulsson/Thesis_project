class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations
    on numerical expressions using the operators +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initializes the operations for the five operators: '+', '-', '*', '/', '^'.
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
        Calculates the value of a given arithmetic expression.
        
        :param expression: str, the arithmetic expression to evaluate
        :return: float, the result of the expression or None if invalid
        """
        if not expression:
            return None
        
        operand_stack = []
        operator_stack = []
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isdigit():
                num = self._parse_number(expression, i)
                operand_stack.append(num)
                i += len(str(num))  # Move index forward by the length of the number
                continue
            
            if char in self.operators:
                while (operator_stack and 
                       self.precedence(operator_stack[-1]) >= self.precedence(char)):
                    self._apply_operator(operand_stack, operator_stack)
                operator_stack.append(char)

            elif char == '(':
                operator_stack.append(char)

            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self._apply_operator(operand_stack, operator_stack)
                operator_stack.pop()  # Remove the '('

            i += 1

        while operator_stack:
            self._apply_operator(operand_stack, operator_stack)

        return operand_stack[0] if operand_stack else None

    def _parse_number(self, expression, index):
        """
        Parses a number from the expression starting at the given index.
        
        :param expression: str, the expression to parse
        :param index: int, the starting index for parsing
        :return: int, the parsed number
        """
        num = 0
        while index < len(expression) and expression[index].isdigit():
            num = num * 10 + int(expression[index])
            index += 1
        return num

    def precedence(self, operator):
        """
        Returns the precedence of the specified operator.
        
        :param operator: str, the operator to evaluate
        :return: int, the precedence of the operator
        """
        precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_map.get(operator, 0)

    def _apply_operator(self, operand_stack, operator_stack):
        """
        Applies the operator at the top of the operator stack to the top two operands
        on the operand stack and pushes the result back onto the operand stack.
        
        :param operand_stack: list, the stack of operands
        :param operator_stack: list, the stack of operators
        """
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        result = self.operators[operator](left_operand, right_operand)
        operand_stack.append(result)