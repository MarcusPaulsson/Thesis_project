def solve():
  n = int(input())
  x = list(map(int, input().split()))

  min_cost = float('inf')

  for target in range(1, 101):
    cost = 0
    for i in range(n):
      diff = abs(x[i] - target)
      cost += diff % 2
    min_cost = min(min_cost, cost)
  
  even_count = 0
  odd_count = 0
  for val in x:
    if val % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  
  min_cost = min(min_cost, min(even_count, odd_count))
  
  
  print(min_cost)

solve()