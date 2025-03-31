class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                num = ''
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                operand_stack.append(float(num))
            elif expression[i] in self.operators:
                operator_stack.append(expression[i])
                i += 1
            else:
                return None # error
        while len(operator_stack) > 0:
            self.apply_operator(operand_stack, operator_stack)
        if len(operand_stack) != 1:
            return None # error
        else:
            return operand_stack[0]

    def precedence(self, operator):
        if operator == '^':
            return 3
        elif operator in ['/', '*']:
            return 2
        elif operator in ['+', '-']:
            return 1
        else:
            return 0 # error

    def apply_operator(self, operand_stack, operator_stack):
        op = self.operators[operator_stack[-1]](operand_stack.pop(), operand_stack.pop())
        operand_stack.append(op)
        operator_stack.pop()
