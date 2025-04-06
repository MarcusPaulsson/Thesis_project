import random

class TwentyFourPointGame:
    """
    This is a game of twenty-four points, which generates four numbers and checks whether the player's expression evaluates to 24.
    """

    def __init__(self) -> None:
        self.nums = self._generate_cards()

    def _generate_cards(self) -> list:
        """
        Generate four random numbers between 1 and 9 for the cards.
        :return: list of integers, representing the player's cards
        """
        return [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self) -> list:
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        >>> game = TwentyFourPointGame()
        >>> len(game.get_my_cards()) == 4
        True
        """
        return self.nums

    def answer(self, expression: str) -> bool:
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> game.answer(ans)
        True
        """
        return self.evaluate_expression(expression)

    def evaluate_expression(self, expression: str) -> bool:
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> game.evaluate_expression(ans)
        True
        """
        try:
            result = eval(expression)
            return result == 24
        except (SyntaxError, NameError, ZeroDivisionError):
            return False