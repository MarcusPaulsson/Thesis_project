import math

# Read input
x, y, z = map(float, input().strip().split())

# Define all expressions
expressions = [
    (x**(y**z), 'x^y^z'),
    (x**(z**y), 'x^z^y'),
    ((x**y)**z, '(x^y)^z'),
    ((x**z)**y, '(x^z)^y'),
    (y**(x**z), 'y^x^z'),
    (y**(z**x), 'y^z^x'),
    ((y**x)**z, '(y^x)^z'),
    ((y**z)**x, '(y^z)^x'),
    (z**(x**y), 'z^x^y'),
    (z**(y**x), 'z^y^x'),
    ((z**x)**y, '(z^x)^y'),
    ((z**y)**x, '(z^y)^x')
]

# Find the maximum value and the corresponding index
max_value, max_expression = max(expressions, key=lambda item: item[0])

# Print the corresponding expression with the maximum value
print(max_expression)