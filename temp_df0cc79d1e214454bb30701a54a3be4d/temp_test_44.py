def solve():
    n = int(input())
    ans = []
    for i in range(2, 2 * n + 2, 2):
        ans.append(i)
    print(*ans)

t = int(input())
for _ in range(t):
    solve()