import math

def solve():
    x, y, z = map(float, input().split())

    expressions = [
        "x^y^z", "x^z^y", "(x^y)^z", "(x^z)^y",
        "y^x^z", "y^z^x", "(y^x)^z", "(y^z)^x",
        "z^x^y", "z^y^x", "(z^x)^y", "(z^y)^x"
    ]

    values = [
        x ** (y ** z),
        x ** (z ** y),
        (x ** y) ** z,
        (x ** z) ** y,
        y ** (x ** z),
        y ** (z ** x),
        (y ** x) ** z,
        (y ** z) ** x,
        z ** (x ** y),
        z ** (y ** x),
        (z ** x) ** y,
        (z ** y) ** x
    ]

    max_val = float('-inf')
    max_index = -1

    for i, val in enumerate(values):
        if val > max_val:
            max_val = val
            max_index = i

    print(expressions[max_index])

solve()