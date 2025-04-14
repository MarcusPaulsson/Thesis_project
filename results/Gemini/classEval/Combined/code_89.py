import random

class TwentyFourPointGame:
    """
    This is a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

    def __init__(self) -> None:
        """
        Initializes the game with an empty list of numbers.
        """
        self.nums = []


    def _generate_cards(self):
        """
        Generates four random numbers between 1 and 9 (inclusive) for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]


    def get_my_cards(self):
        """
        Generates and returns a list of four random numbers between 1 and 9, representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        self._generate_cards()
        return self.nums


    def answer(self, expression):
        """
        Checks if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        if not self.nums:
            return [0, 0, 0, 0]  # Or raise an exception, depending on desired behavior

        return self.evaluate_expression(expression)


    def evaluate_expression(self, expression):
        """
        Evaluates a mathematical expression and checks if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            result = eval(expression)
            return abs(result - 24) < 1e-6  # Using a small tolerance for floating-point comparisons
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False