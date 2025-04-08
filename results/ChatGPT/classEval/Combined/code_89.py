import random
import re
import unittest

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

# Unit tests
class TwentyFourPointGameTest(unittest.TestCase):
    def setUp(self):
        self.game = TwentyFourPointGame()

    def test_get_my_cards(self):
        cards = self.game.get_my_cards()
        self.assertEqual(len(cards), 4)
        for card in cards:
            self.assertIn(card, range(1, 10))

    def test_answer_valid_expression(self):
        self.game.nums = [4, 3, 6, 6]
        result = self.game.answer('4*3+6+6')
        self.assertTrue(result)

    def test_answer_invalid_expression(self):
        result = self.game.answer('1+1+1+1')
        self.assertFalse(result)

    def test_answer_invalid_syntax(self):
        result = self.game.answer('1+')
        self.assertFalse(result)

    def test_answer_invalid_characters(self):
        result = self.game.answer('abc')
        self.assertFalse(result)

    def test_answer_exceeding_numbers(self):
        self.game.nums = [1, 1, 1, 1]
        result = self.game.answer('1+1+1+2')
        self.assertFalse(result)

    def test_evaluate_expression(self):
        result = self.game.evaluate_expression('4*3+6+6')
        self.assertTrue(result)

    def test_evaluate_expression_invalid(self):
        result = self.game.evaluate_expression('1+1+1+1')
        self.assertFalse(result)

    def test_evaluate_expression_invalid_syntax(self):
        result = self.game.evaluate_expression('1+')
        self.assertFalse(result)

    def test_evaluate_expression_invalid_characters(self):
        result = self.game.evaluate_expression('abc')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()