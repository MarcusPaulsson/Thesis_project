def main():
    # Read input values and convert them to floats
    x, y, z = map(float, input().split())
    
    # Define the expressions and their corresponding labels
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
    
    # Find the maximum value and the corresponding expression
    max_value, max_expression = max(expressions, key=lambda pair: pair[0])
    
    # Print the result
    print(max_expression)

if __name__ == "__main__":
    main()