class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets,str.
        """
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'

        """
        self.expr = "".join(char for char in self.expr if char in self.left_brackets or char in self.right_brackets)

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.
        >>> b = BalancedBrackets("a(b)c")
        >>> b.check_balanced_brackets()
        True

        """
        self.clear_expr()
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in self.expr:
            if char in self.left_brackets:
                stack.append(char)
            elif char in self.right_brackets:
                if not stack:
                    return False
                top = stack.pop()
                if bracket_map[char] != top:
                    return False
        return not stack