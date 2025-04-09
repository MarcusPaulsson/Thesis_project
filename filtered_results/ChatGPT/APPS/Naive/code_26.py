import math

def evaluate_expression(x, y, z):
    expressions = [
        (x ** (y ** z), "x^y^z"),
        (x ** (z ** y), "x^z^y"),
        ((x ** y) ** z, "(x^y)^z"),
        ((x ** z) ** y, "(x^z)^y"),
        (y ** (x ** z), "y^x^z"),
        (y ** (z ** x), "y^z^x"),
        ((y ** x) ** z, "(y^x)^z"),
        ((y ** z) ** x, "(y^z)^x"),
        (z ** (x ** y), "z^x^y"),
        (z ** (y ** x), "z^y^x"),
        ((z ** x) ** y, "(z^x)^y"),
        ((z ** y) ** x, "(z^y)^x")
    ]
    
    max_value = float('-inf')
    max_expr = None
    
    for value, expr in expressions:
        if value > max_value:
            max_value = value
            max_expr = expr
            
    return max_expr

# Input
x, y, z = map(float, input().split())

# Output the expression with the maximum value
print(evaluate_expression(x, y, z))