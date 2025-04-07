class Calculator:
    """
    A calculator class that evaluates arithmetic expressions.
    Supports +, -, *, /, and ^ (exponentiation).
    """

    def __init__(self):
        """
        Initializes the calculator with supported operators and their functions.
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        self.precedence_levels = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def calculate(self, expression):
        """
        Calculates the value of an arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the expression, or None if the expression is invalid.
        """
        try:
            operand_stack = []
            operator_stack = []
            tokens = self._tokenize(expression)

            for token in tokens:
                if isinstance(token, float):
                    operand_stack.append(token)
                elif token in self.operators:
                    while operator_stack and self._precedence(operator_stack[-1]) >= self._precedence(token):
                        self._apply_operator(operand_stack, operator_stack)
                    operator_stack.append(token)
                elif token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        self._apply_operator(operand_stack, operator_stack)
                    if operator_stack and operator_stack[-1] == '(':
                        operator_stack.pop()  # Remove the opening parenthesis
                    else:
                        return None  # Mismatched parentheses
                else:
                    return None  # Invalid token

            while operator_stack:
                if operator_stack[-1] == '(':
                    return None  # Unmatched parenthesis
                self._apply_operator(operand_stack, operator_stack)

            if len(operand_stack) == 1:
                return operand_stack[0]
            else:
                return None  # Invalid expression

        except (ValueError, ZeroDivisionError, IndexError):
            return None  # Handle errors during calculation

    def _tokenize(self, expression):
        """
        Tokenizes the input expression into numbers, operators, and parentheses.

        Args:
            expression (str): The input arithmetic expression.

        Returns:
            list: A list of tokens (numbers as floats, operators, and parentheses).
        """
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            if expression[i].isdigit() or expression[i] == '.':
                num_str = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                try:
                    tokens.append(float(num_str))
                except ValueError:
                    return None  # Invalid number format
                i -= 1
            elif expression[i] in self.operators or expression[i] in ('(', ')'):
                tokens.append(expression[i])
            else:
                return None  # Invalid character
            i += 1
        return tokens

    def _precedence(self, operator):
        """
        Returns the precedence of the given operator.

        Args:
            operator (str): The operator.

        Returns:
            int: The precedence of the operator.
        """
        return self.precedence_levels.get(operator, 0)

    def _apply_operator(self, operand_stack, operator_stack):
        """
        Applies the top operator from the operator stack to the top two operands from the operand stack.

        Args:
            operand_stack (list): The stack of operands.
            operator_stack (list): The stack of operators.
        """
        operator = operator_stack.pop()
        if len(operand_stack) < 2:
            raise IndexError("Not enough operands for operator")

        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()

        try:
            result = self.operators[operator](operand1, operand2)
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero")

        operand_stack.append(result)