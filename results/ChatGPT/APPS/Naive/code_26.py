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
    
    max_value = float('-inf')
    max_index = -1
    
    for index, (value, expr) in enumerate(expressions):
        if value > max_value:
            max_value = value
            max_index = index
            
    return expressions[max_index][1]

# Read input
x, y, z = map(float, input().split())
result = calculate_expressions(x, y, z)
print(result)