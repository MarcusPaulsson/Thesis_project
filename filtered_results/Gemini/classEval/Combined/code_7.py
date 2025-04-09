class BalancedBrackets:
    """
    This class checks for bracket matching in an expression.
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.

        :param expr: The expression to check for balanced brackets (string).
        """
        self.expr = expr

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.

        >>> b = BalancedBrackets("a(b)c")
        >>> b.clear_expr()
        >>> b.expr
        '()'
        """
        brackets = "(){}[]"
        self.expr = "".join(char for char in self.expr if char in brackets)

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
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack:
                    return False
                top = stack.pop()
                if bracket_map[char] != top:
                    return False

        return not stack