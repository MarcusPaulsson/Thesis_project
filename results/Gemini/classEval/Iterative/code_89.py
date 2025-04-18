import random

class TwentyFourPointGame:
    """
    This ia a game of twenty-four points, which provides to generate four numbers and check whether player's expression is equal to 24.
    """

    def __init__(self) -> None:
        self.nums = []


    def _generate_cards(self):
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]


    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()

        """
        self._generate_cards()
        return self.nums


    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
        if not self.nums:
            return [0, 0, 0, 0]
        try:
            # Check if the expression contains only allowed characters and numbers
            allowed_chars = set("0123456789+-*/. ")
            if not all(c in allowed_chars for c in expression):
                return False

            result = eval(expression)
            return abs(result - 24) < 1e-6
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False


    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
        try:
            # Check if the expression contains only allowed characters and numbers
            allowed_chars = set("0123456789+-*/. ")
            if not all(c in allowed_chars for c in expression):
                return False

            result = eval(expression)
            return abs(result - 24) < 1e-6
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False