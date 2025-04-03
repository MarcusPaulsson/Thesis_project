x, y, z = map(float, input().split())

a1 = y**z * (x > 1) + z**y * (x <= 1)
a2 = z**y * (x > 1) + y**z * (x <= 1)
a3 = y * z
a4 = z * y
a5 = x**z * (y > 1) + z**x * (y <= 1)
a6 = z**x * (y > 1) + x**z * (y <= 1)
a7 = x * z
a8 = z * x
a9 = x**y * (z > 1) + y**x * (z <= 1)
a10 = y**x * (z > 1) + x**y * (z <= 1)
a11 = x * y
a12 = y * x

max_val = float('-inf')
result = ""

if a1 > max_val:
    max_val = a1
    result = "x^y^z"

if a2 > max_val:
    max_val = a2
    result = "x^z^y"

if a3 > max_val:
    max_val = a3
    result = "(x^y)^z"

if a4 > max_val:
    max_val = a4
    result = "(x^z)^y"

if a5 > max_val:
    max_val = a5
    result = "y^x^z"

if a6 > max_val:
    max_val = a6
    result = "y^z^x"

if a7 > max_val:
    max_val = a7
    result = "(y^x)^z"

if a8 > max_val:
    max_val = a8
    result = "(y^z)^x"

if a9 > max_val:
    max_val = a9
    result = "z^x^y"

if a10 > max_val:
    max_val = a10
    result = "z^y^x"

if a11 > max_val:
    max_val = a11
    result = "(z^x)^y"

if a12 > max_val:
    max_val = a12
    result = "(z^y)^x"

print(result)