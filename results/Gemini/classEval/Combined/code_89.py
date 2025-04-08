import random

class TwentyFourPointGame:
    """
    A game of twenty-four points, which generates four numbers and checks whether a player's expression equals 24.
    """

    def __init__(self):
        """
        Initializes the game with an empty list of numbers.
        """
        self.nums = []

    def get_my_cards(self):
        """
        Generates and returns a list of four random numbers between 1 and 9 (inclusive).
        :return: list of integers, representing the player's cards
        """
        self.nums = self._generate_cards()
        return self.nums

    def _generate_cards(self):
        """
        Generates a list of four random numbers between 1 and 9.
        :return: A list of four integers.
        """
        return [random.randint(1, 9) for _ in range(4)]

    def answer(self, expression):
        """
        Checks if a given mathematical expression using the current cards evaluates to 24.
        It now validates whether the expression contains only permitted characters.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        if not self.nums:
            return [0, 0, 0, 0]

        if not self._is_valid_expression(expression):
            return False

        return self.evaluate_expression(expression)

    def evaluate_expression(self, expression):
        """
        Evaluates a mathematical expression and checks if the result is close to 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            result = eval(expression)
            return abs(result - 24) < 1e-6  # Using a small tolerance for floating-point comparisons
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False

    def _is_valid_expression(self, expression):
        """
        Validates if the expression contains only allowed characters.
        Allowed characters are digits, basic arithmetic operators, parentheses, and spaces.
        :param expression: string, the expression to validate
        :return: bool, True if the expression is valid, False otherwise
        """
        allowed_chars = set("0123456789+-*/(). ")
        return all(char in allowed_chars for char in expression)