import math

# Read input
x, y, z = map(float, input().split())

# Define the 12 expressions
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

# Find the maximum value and its index, ensuring to return the first one in case of ties
max_value, max_index = max((value, index) for index, (value, _) in enumerate(expressions))

# Print the corresponding expression, adjusting index for 1-based output
print(expressions[max_index][1])