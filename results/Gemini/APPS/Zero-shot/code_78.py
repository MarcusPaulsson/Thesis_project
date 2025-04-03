def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    ans = float('inf')

    for r in range(n):
        for c in range(m):
            cost = 0
            for i in range(m):
                if grid[r][i] == '.':
                    cost += 1
            for i in range(n):
                if grid[i][c] == '.':
                    cost += 1
            if grid[r][c] == '.':
                cost -= 1
            ans = min(ans, cost)

    print(ans)

q = int(input())
for _ in range(q):
    solve()