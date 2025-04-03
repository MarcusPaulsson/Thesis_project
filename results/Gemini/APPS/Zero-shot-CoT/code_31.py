def solve():
  s = input()
  n = len(s)
  x, y = 0, 0
  visited = set()
  total_time = 0
  
  for move in s:
    nx, ny = x, y
    if move == 'N':
      ny += 1
    elif move == 'S':
      ny -= 1
    elif move == 'W':
      nx -= 1
    else:
      nx += 1
    
    segment = tuple(sorted([(x, y), (nx, ny)]))
    
    if segment in visited:
      total_time += 1
    else:
      total_time += 5
      visited.add(segment)
      
    x, y = nx, ny
    
  print(total_time)
  

t = int(input())
for _ in range(t):
  solve()