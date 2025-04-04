import math

def catch_x_mouse(m, x):
    return m // math.gcd(x, m)

m, x = map(int, input().split())
print(catch_x_mouse(m, x))