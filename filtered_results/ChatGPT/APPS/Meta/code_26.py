import sys

# Read input
x, y, z = map(float, input().strip().split())

# Expressions and their corresponding representations
expressions = [
    (x**(y**z), "x^y^z"),
    (x**(z**y), "x^z^y"),
    ((x**y)**z, "(x^y)^z"),
    ((x**z)**y, "(x^z)^y"),
    (y**(x**z), "y^x^z"),
    (y**(z**x), "y^z^x"),
    ((y**x)**z, "(y^x)^z"),
    ((y**z)**x, "(y^z)^x"),
    (z**(x**y), "z^x^y"),
    (z**(y**x), "z^y^x"),
    ((z**x)**y, "(z^x)^y"),
    ((z**y)**x, "(z^y)^x")
]

# Find the maximum value and its index
max_value = max(expressions, key=lambda item: item[0])
max_index = expressions.index(max_value)

# Output the corresponding expression
print(max_value[1])