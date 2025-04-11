def calculate_expressions(x, y, z):
    return [
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

def find_max_expression(x, y, z):
    expressions = calculate_expressions(x, y, z)
    max_value, max_expr = max(expressions, key=lambda item: item[0])
    return max_expr

# Input reading
x, y, z = map(float, input().strip().split())

# Finding the maximum expression
result = find_max_expression(x, y, z)

# Output the result
print(result)