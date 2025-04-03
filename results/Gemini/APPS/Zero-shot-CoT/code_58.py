def solve():
    n, m, k = map(int, input().split())

    dp = {}

    def calculate_cost(rows, cols, target):
        if (rows, cols, target) in dp:
            return dp[(rows, cols, target)]

        if target == 0:
            return 0
        if target == rows * cols:
            return 0
        if target < 0 or target > rows * cols:
            return float('inf')

        min_cost = float('inf')

        # Horizontal breaks
        for i in range(1, rows):
            cost = cols * cols
            for j in range(target + 1):
                min_cost = min(min_cost, cost + calculate_cost(i, cols, j) + calculate_cost(rows - i, cols, target - j))

        # Vertical breaks
        for i in range(1, cols):
            cost = rows * rows
            for j in range(target + 1):
                min_cost = min(min_cost, cost + calculate_cost(rows, i, j) + calculate_cost(rows, cols - i, target - j))

        dp[(rows, cols, target)] = min_cost
        return min_cost

    print(calculate_cost(n, m, k))

t = int(input())
for _ in range(t):
    solve()