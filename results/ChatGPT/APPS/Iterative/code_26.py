import math

def main():
    # Read and parse the input
    try:
        x, y, z = map(float, input("Enter three numbers separated by spaces: ").strip().split())
    except ValueError:
        print("Invalid input. Please enter three numerical values.")
        return

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

    # Find the maximum value and its corresponding index
    max_value, max_index = max((val, idx) for idx, (val, _) in enumerate(expressions))

    # Output the corresponding expression
    print(expressions[max_index][1])

if __name__ == "__main__":
    main()