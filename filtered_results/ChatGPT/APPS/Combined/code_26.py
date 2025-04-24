def calculate_expressions(x, y, z):
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
    
    return expressions

def find_max_expression(x, y, z):
    expressions = calculate_expressions(x, y, z)
    max_value, max_index = max(expressions, key=lambda item: item[0])
    
    return max_index

if __name__ == "__main__":
    x, y, z = map(float, input().split())
    result = find_max_expression(x, y, z)
    print(result)