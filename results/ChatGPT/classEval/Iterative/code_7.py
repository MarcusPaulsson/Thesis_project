class BalancedBrackets:
    """
    This is a class that checks for bracket matching.
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets, str.
        """
        self.stack = []
        self.bracket_map = {")": "(", "}": "{", "]": "["}
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
        self.expr = ''.join(char for char in self.expr if char in self.bracket_map or char in self.bracket_map.values())

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True
        >>> b = BalancedBrackets("a(b{c)d}e")
        >>> b.check_balanced_brackets()
        True
        >>> b = BalancedBrackets("a(b[c}d)e")
        >>> b.check_balanced_brackets()
        False
        """
        self.clear_expr()
        for char in self.expr:
            if char in self.bracket_map.values():
                self.stack.append(char)
            elif char in self.bracket_map.keys():
                if not self.stack or self.stack.pop() != self.bracket_map[char]:
                    return False
        return len(self.stack) == 0