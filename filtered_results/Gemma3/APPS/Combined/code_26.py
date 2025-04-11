def solve():
    x, y, z = map(float, input().split())
    
    expressions = [
        x**(y**z),
        x**(z**y),
        (x**y)**z,
        (x**z)**y,
        y**(x**z),
        y**(z**x),
        (y**x)**z,
        (y**z)**x,
        z**(x**y),
        z**(y**x),
        (z**x)**y,
        (z**y)**x
    ]
    
    expression_strings = [
        "x^y^z",
        "x^z^y",
        "(x^y)^z",
        "(x^z)^y",
        "y^x^z",
        "y^z^x",
        "(y^x)^z",
        "(y^z)^x",
        "z^x^y",
        "z^y^x",
        "(z^x)^y",
        "(z^y)^x"
    ]
    
    max_val = float('-inf')
    max_index = -1
    
    for i in range(len(expressions)):
        if expressions[i] > max_val:
            max_val = expressions[i]
            max_index = i
            
    print(expression_strings[max_index])

solve()