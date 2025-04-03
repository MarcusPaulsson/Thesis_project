import math

def solve():
    n = int(input())
    print(1 / math.tan(math.pi / (2 * n)))

t = int(input())
for _ in range(t):
    solve()