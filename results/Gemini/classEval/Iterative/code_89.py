import random
import operator
import itertools

class TwentyFourPointGame:
    """
    A game of twenty-four points, which generates four numbers and checks whether a player's expression evaluates to 24.
    """

    def __init__(self):
        self.nums = []

    def _generate_cards(self):
        """
        Generate four random numbers between 1 and 9 for the cards.
        """
        self.nums = [random.randint(1, 9) for _ in range(4)]

    def get_my_cards(self):
        """
        Get a list of four random numbers between 1 and 9 representing the player's cards.
        :return: list of integers, representing the player's cards
        """
        self._generate_cards()
        return self.nums

    def is_solvable(self):
      """
      Check if the current set of cards is solvable.
      :return: bool, True if solvable, False otherwise
      """
      if not self.nums:
        return False

      ops = [operator.add, operator.sub, operator.mul, operator.truediv]
      for a, b, c, d in itertools.permutations(self.nums):
          for op1, op2, op3 in itertools.product(ops, ops, ops):
              try:
                  if abs(op3(op2(op1(a, b), c), d) - 24) < 1e-6:
                      return True
                  if abs(op2(op1(a, b), op3(c, d)) - 24) < 1e-6:
                      return True
                  if abs(op1(a, op3(op2(b, c), d)) - 24) < 1e-6:
                      return True
                  if abs(op1(a, op2(b, op3(c, d))) - 24) < 1e-6:
                      return True
                  if abs(op3(op1(a, op2(b, c)), d) - 24) < 1e-6:
                      return True
              except ZeroDivisionError:
                  continue
      return False

    def answer(self, expression):
        """
        Check if a given mathematical expression using the cards can evaluate to 24.
        :param expression: string, mathematical expression using the cards
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            # Validate that the expression only uses allowed characters and the numbers
            allowed_chars = set("0123456789+-*/.() ")
            allowed_numbers = set(str(num) for num in self.nums)
            expression_chars = set(expression)
            is_valid = all(char in allowed_chars for char in expression_chars) and \
                       all(number in expression for number in allowed_numbers)

            if not is_valid:
                return False

            result = eval(expression)
            return abs(result - 24) < 1e-6  # Use a tolerance for floating-point comparisons
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        """
        try:
            result = eval(expression)
            return abs(result - 24) < 1e-6  # Use a tolerance for floating-point comparisons
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            return False