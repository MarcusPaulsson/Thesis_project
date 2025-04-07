# Read input
x, y, z = map(float, input().split())

# Calculate all expressions with their labels
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

# Find the maximum value and corresponding expression
max_value, max_index = max((value, idx) for idx, (value, _) in enumerate(expressions))
# Output the corresponding expression with the smallest index
print(expressions[max_index][1])