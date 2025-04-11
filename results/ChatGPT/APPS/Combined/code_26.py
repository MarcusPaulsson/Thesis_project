def main():
    import sys
    from math import pow

    # Step 1: Read input and parse the numbers
    x, y, z = map(float, input().strip().split())

    # Step 2: Define expressions and their corresponding labels
    expressions = [
        (pow(x, pow(y, z)), "x^y^z"),
        (pow(x, pow(z, y)), "x^z^y"),
        (pow(pow(x, y), z), "(x^y)^z"),
        (pow(pow(x, z), y), "(x^z)^y"),
        (pow(y, pow(x, z)), "y^x^z"),
        (pow(y, pow(z, x)), "y^z^x"),
        (pow(pow(y, x), z), "(y^x)^z"),
        (pow(pow(y, z), x), "(y^z)^x"),
        (pow(z, pow(x, y)), "z^x^y"),
        (pow(z, pow(y, x)), "z^y^x"),
        (pow(pow(z, x), y), "(z^x)^y"),
        (pow(pow(z, y), x), "(z^y)^x"),
    ]

    # Step 3: Find the maximum value and corresponding expression
    max_value = float('-inf')
    max_expression = ""
    
    for value, expr in expressions:
        if value > max_value:
            max_value = value
            max_expression = expr

    # Output the result
    print(max_expression)

if __name__ == "__main__":
    main()