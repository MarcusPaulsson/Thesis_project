import math

# Read input
x, y, z = map(float, input().split())

# Define the expressions
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

# Find the maximum value and the corresponding expression
max_value = -math.inf
max_index = -1

for i, (value, expr) in enumerate(expressions):
    if value > max_value:
        max_value = value
        max_index = i

# Output the corresponding expression
print(expressions[max_index][1])