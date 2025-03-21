import math

def solve():
    n = int(input())
    ans = 1 / math.tan(math.pi / (2 * n))
    print(ans)

t = int(input())
for _ in range(t):
    solve()