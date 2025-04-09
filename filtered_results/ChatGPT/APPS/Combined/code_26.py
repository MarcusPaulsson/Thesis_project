def calculate_expressions(x, y, z):
    # Define the expressions and their corresponding string representations
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
    
    # Find the maximum value and the corresponding expression with the smallest index
    max_value_index = max(range(len(expressions)), key=lambda i: expressions[i][0])
    return expressions[max_value_index][1]

# Read input
input_values = input().strip().split()
x = float(input_values[0])
y = float(input_values[1])
z = float(input_values[2])

# Calculate and print the result
result_expression = calculate_expressions(x, y, z)
print(result_expression)