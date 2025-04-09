import random
import re


class TwentyFourPointGame:
    """
    This is a game of twenty-four points, which generates four numbers
    and checks whether a player's expression evaluates to 24.
    """

    def __init__(self) -> None:
        self.nums = []

    def _generate_cards(self):
        """
        Generate four unique random numbers between 1 and 9 for the cards.
        """
        self.nums = random.sample(range(1, 10), 4)

    def get_my_cards(self):
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
            result = eval(expression)
            return result == 24
        except (SyntaxError, NameError, ZeroDivisionError):
            return False

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Check if the expression is valid and only contains allowed numbers and operators.
        :param expression: string, mathematical expression
        :return: bool, True if the expression is valid, False otherwise
        """
        allowed_chars = set("0123456789+-*/() ")
        return (all(char in allowed_chars for char in expression) and
                all(num in map(str, self.nums) for num in re.findall(r'\d+', expression)))
