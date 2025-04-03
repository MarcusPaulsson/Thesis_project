# Read input values
x, y, z = map(float, input().split())

# Define the expressions and their corresponding representations
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

# Find the maximum value and its index
max_value, max_index = max((value, index) for index, (value, _) in enumerate(expressions))

# Print the corresponding expression
print(expressions[max_index][1])