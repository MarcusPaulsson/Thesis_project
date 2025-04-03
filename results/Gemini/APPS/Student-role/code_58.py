def solve():
  n, m, k = map(int, input().split())

  dp = {}

  def calculate_cost(rows, cols, target):
    if (rows, cols, target) in dp:
      return dp[(rows, cols, target)]

    if target == 0:
      return 0
    
    if rows * cols == target:
      return 0
    
    if rows * cols < target:
      return float('inf')

    min_cost = float('inf')

    # Horizontal breaks
    for i in range(1, rows):
      cost = cols * cols
      cost += calculate_cost(i, cols, min(target, i * cols))
      cost += calculate_cost(rows - i, cols, max(0, target - i * cols))
      min_cost = min(min_cost, cost)

    # Vertical breaks
    for i in range(1, cols):
      cost = rows * rows
      cost += calculate_cost(rows, i, min(target, rows * i))
      cost += calculate_cost(rows, cols - i, max(0, target - rows * i))
      min_cost = min(min_cost, cost)

    dp[(rows, cols, target)] = min_cost
    return min_cost

  print(calculate_cost(n, m, k))

t = int(input())
for _ in range(t):
  solve()