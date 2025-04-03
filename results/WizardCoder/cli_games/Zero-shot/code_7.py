class BalancedBrackets:

    def __init__(self, expr):
        self.stack = []
        self.left_brackets = ["(", "{", "["]
        self.right_brackets = [")", "}", "]"]
        self.expr = expr

    def clear_expr(self):
        for char in self.expr:
            if char not in self.left_brackets + self.right_brackets:
                self.expr = self.expr.replace(char, "")

    def check_balanced_brackets(self):
        for char in self.expr:
            if char in self.left_brackets:
                self.stack.append(char)
            elif char in self.right_brackets:
                if not self.stack or char != {'(': ')', '{': '}', '[': ']'}[self.stack[-1]]:
                    return False
                self.stack.pop()
        return len(self.stack) == 0