def calculate_expressions(x, y, z):
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
        ((z ** y) ** x, "(z^y)^x"),
    ]
    return expressions

def find_max_expression(x, y, z):
    expressions = calculate_expressions(x, y, z)
    max_value = max(value for value, _ in expressions)
    for value, expr in expressions:
        if value == max_value:
            return expr

# Read input
x, y, z = map(float, input().split())

# Find and print the maximum expression
result = find_max_expression(x, y, z)
print(result)