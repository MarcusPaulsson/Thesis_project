import math

# Read input
x, y, z = map(float, input().split())

# Define expressions and their corresponding outputs
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
    ((z**y)**x, "(z^y)^x"),
]

# Find the maximum value and the smallest index with that value
max_value = -float('inf')
best_index = -1

for index, (value, expression) in enumerate(expressions):
    if value > max_value:
        max_value = value
        best_index = index

# Output the corresponding expression
print(expressions[best_index][1])