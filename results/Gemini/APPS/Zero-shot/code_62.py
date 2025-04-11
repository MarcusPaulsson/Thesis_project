def solve():
  a, b, c = map(int, input().split())
  
  best_cost = float('inf')
  best_triple = None
  
  for A in range(1, 2 * a + 1):
    for B_mult in range(1, 2 * b // A + 2):
      B = A * B_mult
      if B == 0:
          continue
      for C_mult in range(1, 2 * c // B + 2):
        C = B * C_mult
        
        cost = abs(a - A) + abs(b - B) + abs(c - C)
        
        if cost < best_cost:
          best_cost = cost
          best_triple = (A, B, C)
          
  print(best_cost)
  print(*best_triple)

t = int(input())
for _ in range(t):
  solve()