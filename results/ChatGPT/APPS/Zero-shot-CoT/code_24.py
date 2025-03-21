import sys
import math

def find_a_b(d):
    if d == 0:
        return (0.0, 0.0)
    if d == 1:
        return None
    phi = (1 + math.sqrt(5)) / 2
    a = (d * phi - d) / (phi ** 2 - 1)
    b = d - a
    return (a, b)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    d = int(sys.stdin.readline().strip())
    result = find_a_b(d)
    if result is None:
        print("N")
    else:
        a, b = result
        print(f"Y {a:.9f} {b:.9f}")