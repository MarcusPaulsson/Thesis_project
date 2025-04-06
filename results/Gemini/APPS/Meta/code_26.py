import math

def solve():
    x, y, z = map(float, input().split())

    results = []
    results.append(("x^y^z", x ** (y ** z)))
    results.append(("x^z^y", x ** (z ** y)))
    results.append(("(x^y)^z", (x ** y) ** z))
    results.append(("(x^z)^y", (x ** z) ** y))
    results.append(("y^x^z", y ** (x ** z)))
    results.append(("y^z^x", y ** (z ** x)))
    results.append(("(y^x)^z", (y ** x) ** z))
    results.append(("(y^z)^x", (y ** z) ** x))
    results.append(("z^x^y", z ** (x ** y)))
    results.append(("z^y^x", z ** (y ** x)))
    results.append(("(z^x)^y", (z ** x) ** y))
    results.append(("(z^y)^x", (z ** y) ** x))

    max_val = float('-inf')
    max_expr = ""

    for expr, val in results:
        if val > max_val:
            max_val = val
            max_expr = expr

    print(max_expr)

solve()