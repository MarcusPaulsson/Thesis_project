import random

class TwentyFourPointGame:
    """
    This is a game of twenty-four points, which generates four numbers and checks whether the player's expression is equal to 24.
    """

    def __init__(self) -> None:
        self.nums = []

    def _generate_cards(self) -> None:
        """
        Generate random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self) -> list[int]:
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        self._generate_cards()
        return self.nums

    def answer(self, expression: str) -> bool:
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        if self._is_valid_expression(expression):
            return self.evaluate_expression(expression)
        return False

    def evaluate_expression(self, expression: str) -> bool:
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            return eval(expression) == 24
        except (SyntaxError, NameError, ZeroDivisionError):
            return False

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Check if the expression is valid and uses only the numbers from the player's cards.
        :param expression: string, mathematical expression
        :return: bool, True if valid, False otherwise
        """
        allowed_numbers = set(map(str, self.nums))
        tokens = expression.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
        return all(token in allowed_numbers for token in tokens)