class BalancedBrackets:
    """
    This class checks for balanced brackets in a given expression.
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets, str.
        """
        self.expr = expr
        self.stack = []
        self.bracket_map = {")": "(", "}": "{", "]": "["}

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        """
        self.expr = ''.join(filter(lambda char: char in self.bracket_map.values() or char in self.bracket_map.keys(), self.expr))

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        """
        for char in self.expr:
            if char in self.bracket_map.values():  # If it's a left bracket
                self.stack.append(char)
            elif char in self.bracket_map.keys():  # If it's a right bracket
                if not self.stack or self.stack.pop() != self.bracket_map[char]:
                    return False
        return not self.stack
