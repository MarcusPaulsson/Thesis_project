def solve():
  n = int(input())
  
  best_moves = float('inf')
  
  for i in range(1, int(n**0.5) + 2):
    if n % i == 0:
      j = n // i
      moves = (i - 1) + (j - 1)
      best_moves = min(best_moves, moves)
      
  print(best_moves)

solve()