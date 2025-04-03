def solve():
  n, m = map(int, input().split())
  
  grains = n
  day = 0
  
  while True:
    day += 1
    
    grains += m
    grains = min(n, grains)
    
    grains -= day
    
    if grains <= 0:
      print(day)
      return

solve()