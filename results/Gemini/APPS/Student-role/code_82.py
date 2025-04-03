def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 2:
        print(p[1], p[0])
        return

    if p == list(range(1, n + 1)):
        print(*list(range(n, 0, -1)))
    else:
        print(*list(range(n, 0, -1)))

t = int(input())
for _ in range(t):
    solve()