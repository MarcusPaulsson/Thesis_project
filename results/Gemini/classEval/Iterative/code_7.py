class BalancedBrackets:
    """
    This is a class that checks for bracket matching
    """

    def __init__(self, expr):
        """
        Initializes the class with an expression.
        :param expr: The expression to check for balanced brackets, str.
        """
        self.expr = expr
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.bracket_map = {")": "(", "}": "{", "]": "["}

    def is_balanced(self):
        """
        Checks if the expression has balanced brackets.
        :return: True if the expression has balanced brackets, False otherwise.

        """
        stack = []
        for char in self.expr:
            if char in self.left_brackets:
                stack.append(char)
            elif char in self.right_brackets:
                if not stack:
                    return False
                top = stack.pop()
                if self.bracket_map[char] != top:
                    return False
        return not stack