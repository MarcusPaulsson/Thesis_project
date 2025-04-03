def solve():
    c, m, x = map(int, input().split())
    print(min(c, m, (c + m + x) // 3))

q = int(input())
for _ in range(q):
    solve()