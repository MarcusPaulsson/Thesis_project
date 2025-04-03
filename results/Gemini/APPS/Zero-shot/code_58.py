def solve():
  n, m, k = map(int, input().split())
  
  dp = {}
  
  def calculate_cost(h, w, target):
    if (h, w, target) in dp:
      return dp[(h, w, target)]
    
    if target == 0:
      return 0
    if h * w == target:
      return 0
    if h * w < target or target < 0:
      return float('inf')
    
    min_cost = float('inf')
    
    # Horizontal cuts
    for i in range(1, h):
      cost = w * w
      min_cost = min(min_cost, cost + calculate_cost(i, w, target) + calculate_cost(h - i, w, 0))
      min_cost = min(min_cost, cost + calculate_cost(i, w, 0) + calculate_cost(h - i, w, target))

      for target1 in range(0, target + 1):
         cost = w * w
         min_cost = min(min_cost, cost + calculate_cost(i, w, target1) + calculate_cost(h - i, w, target - target1))
    
    # Vertical cuts
    for i in range(1, w):
      cost = h * h
      min_cost = min(min_cost, cost + calculate_cost(h, i, target) + calculate_cost(h, w - i, 0))
      min_cost = min(min_cost, cost + calculate_cost(h, i, 0) + calculate_cost(h, w - i, target))
      
      for target1 in range(0, target + 1):
          cost = h * h
          min_cost = min(min_cost, cost + calculate_cost(h, i, target1) + calculate_cost(h, w - i, target - target1))
    
    dp[(h, w, target)] = min_cost
    return min_cost
  
  print(calculate_cost(n, m, k))

t = int(input())
for _ in range(t):
  solve()