def solve():
    n = int(input())
    result = []
    start = 2 * 1
    for i in range(n):
        result.append(start)
        start += 2
    print(*result)

t = int(input())
for _ in range(t):
    solve()