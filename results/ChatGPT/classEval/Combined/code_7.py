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
        self.left_brackets = {"(": ")", "{": "}", "[": "]"}
        self.right_brackets = {")", "}", "]"}
        self.stack = []

    def clear_expr(self):
        """
        Clears the expression of all characters that are not brackets.
        """
        self.expr = ''.join(char for char in self.expr if char in self.left_brackets or char in self.right_brackets)

    def check_balanced_brackets(self):
        """
        Checks if the expression has balanced brackets.
        
        :return: True if the expression has balanced brackets, False otherwise.
        """
        self.clear_expr()  # Ensure we are checking only brackets
        self.stack.clear()  # Clear the stack for a fresh check

        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack or self.left_brackets[self.stack.pop()] != char:
                    return False
        return not self.stack