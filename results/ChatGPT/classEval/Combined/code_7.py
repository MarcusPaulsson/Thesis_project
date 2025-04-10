class BalancedBrackets:
    """
    A class to check for balanced brackets in an expression.
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets, str.
        """
        self.expr = expr
        self.stack = []
        self.bracket_pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        self.valid_brackets = set(self.bracket_pairs.keys()).union(self.bracket_pairs.values())

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        """
        self.expr = ''.join(char for char in self.expr if char in self.valid_brackets)

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for char in self.expr:
            if char in self.bracket_pairs:
                self.stack.append(char)
            elif char in self.bracket_pairs.values():
                if not self.stack or self.bracket_pairs[self.stack.pop()] != char:
                    return False
        return not self.stack