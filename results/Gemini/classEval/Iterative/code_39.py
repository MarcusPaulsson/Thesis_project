from collections import deque
import decimal


class ExpressionCalculator:
    """
    A class to evaluate arithmetic expressions. Supports +, -, *, /, %, and parentheses.
    """

    OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    def calculate(self, expression):
        """
        Calculates the result of an arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate (e.g., "2 + 3 * 4").

        Returns:
            decimal.Decimal: The result of the expression.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        division by zero, invalid operator).
        """
        try:
            postfix = self._infix_to_postfix(expression)
            return self._evaluate_postfix(postfix)
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}. Reason: {e}") from e

    def _infix_to_postfix(self, expression):
        """
        Converts an infix expression to postfix notation.

        Args:
            expression (str): The infix expression (e.g., "2 + 3 * 4").

        Returns:
            list: The postfix expression as a list of tokens (e.g., ['2', '3', '4', '*', '+']).
        """
        expression = expression.replace(" ", "")  # Remove spaces
        output_queue = []
        operator_stack = deque()

        for token in self._tokenize(expression):
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):  # Handle negative numbers
                output_queue.append(token)
            elif token in self.OPERATORS:
                while operator_stack and operator_stack[-1] in self.OPERATORS and \
                        self.OPERATORS[token] <= self.OPERATORS[operator_stack[-1]]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unbalanced parentheses")
                operator_stack.pop()  # Remove the '('
            else:
                raise ValueError(f"Invalid token: {token}")

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            output_queue.append(operator_stack.pop())

        return output_queue

    def _evaluate_postfix(self, postfix):
        """
        Evaluates a postfix expression.

        Args:
            postfix (list): The postfix expression as a list of tokens (e.g., ['2', '3', '4', '*', '+']).

        Returns:
            decimal.Decimal: The result of the expression.
        """
        stack = deque()
        for token in postfix:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(decimal.Decimal(token))
            elif token in self.OPERATORS:
                if len(stack) < 2:
                    raise ValueError("Not enough operands for operator")
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self._apply_operator(operand1, operand2, token)
                stack.append(result)
            else:
                raise ValueError(f"Invalid token in postfix expression: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")

        return stack.pop()

    def _apply_operator(self, operand1, operand2, operator):
        """
        Applies an arithmetic operator to two operands.

        Args:
            operand1 (decimal.Decimal): The first operand.
            operand2 (decimal.Decimal): The second operand.
            operator (str): The operator (+, -, *, /, %).

        Returns:
            decimal.Decimal: The result of the operation.
        """
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError("Division by zero")
            return operand1 / operand2
        elif operator == '%':
            if operand2 == 0:
                raise ZeroDivisionError("Modulo by zero")
            return operand1 % operand2
        else:
            raise ValueError(f"Invalid operator: {operator}")

    def _tokenize(self, expression):
        """
        Tokenizes the input expression, handling multi-digit numbers and negative numbers.

        Args:
            expression (str): The arithmetic expression.

        Returns:
            list: A list of tokens (numbers and operators).
        """
        tokens = []
        current_number = ""
        for char in expression:
            if char.isdigit():
                current_number += char
            elif char in self.OPERATORS or char in "()":
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                tokens.append(char)
            elif char == '-' and (not tokens or tokens[-1] in self.OPERATORS or tokens[-1] == '('):
                current_number = "-"  # Handle negative numbers
            else:
                raise ValueError(f"Invalid character in expression: {char}")

        if current_number:
            tokens.append(current_number)
        return tokens