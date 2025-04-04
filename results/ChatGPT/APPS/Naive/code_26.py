import sys

def calculate_expressions(x, y, z):
    expressions = [
        (x ** (y ** z), f"{x}^{y}^{z}"),
        (x ** (z ** y), f"{x}^{z}^{y}"),
        ((x ** y) ** z, f"( {x}^{y} )^{z}"),
        ((x ** z) ** y, f"( {x}^{z} )^{y}"),
        (y ** (x ** z), f"{y}^{x}^{z}"),
        (y ** (z ** x), f"{y}^{z}^{x}"),
        ((y ** x) ** z, f"( {y}^{x} )^{z}"),
        ((y ** z) ** x, f"( {y}^{z} )^{x}"),
        (z ** (x ** y), f"{z}^{x}^{y}"),
        (z ** (y ** x), f"{z}^{y}^{x}"),
        ((z ** x) ** y, f"( {z}^{x} )^{y}"),
        ((z ** y) ** x, f"( {z}^{y} )^{x}"),
    ]
    return expressions

def find_max_expression(expressions):
    max_value = float('-inf')
    index = -1
    for i, (value, expr) in enumerate(expressions):
        if value > max_value:
            max_value = value
            index = i
    return index, expressions[index][1]

def main():
    # Read input
    x, y, z = map(float, sys.stdin.readline().strip().split())
    
    # Calculate expressions
    expressions = calculate_expressions(x, y, z)
    
    # Find max expression and its index
    index, max_expr = find_max_expression(expressions)
    
    # Print the result
    print(max_expr)

if __name__ == "__main__":
    main()