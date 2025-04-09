import sys

# Read input
x, y, z = map(float, sys.stdin.readline().strip().split())

# Define the expressions and their corresponding values
expressions = [
    (f"x^y^z", x ** (y ** z)),
    (f"x^z^y", x ** (z ** y)),
    (f"(x^y)^z", (x ** y) ** z),
    (f"(x^z)^y", (x ** z) ** y),
    (f"y^x^z", y ** (x ** z)),
    (f"y^z^x", y ** (z ** x)),
    (f"(y^x)^z", (y ** x) ** z),
    (f"(y^z)^x", (y ** z) ** x),
    (f"z^x^y", z ** (x ** y)),
    (f"z^y^x", z ** (y ** x)),
    (f"(z^x)^y", (z ** x) ** y),
    (f"(z^y)^x", (z ** y) ** x)
]

# Find the maximum value and the corresponding expression
max_value = -1
max_expression = ""
for expr, value in expressions:
    if value > max_value:
        max_value = value
        max_expression = expr

# Output the result
print(max_expression)