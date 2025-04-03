def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    def check_cross(x, y):
        for i in range(n):
            if grid[i][y] == '.':
                return False
        for j in range(m):
            if grid[x][j] == '.':
                return False
        return True

    def calculate_cost(x, y):
        cost = 0
        for i in range(n):
            if grid[i][y] == '.':
                cost += 1
        for j in range(m):
            if grid[x][j] == '.':
                cost += 1
        return cost

    min_cost = float('inf')
    for x in range(n):
        for y in range(m):
            cost = calculate_cost(x, y)
            min_cost = min(min_cost, cost)

    print(min_cost)

q = int(input())
for _ in range(q):
    solve()