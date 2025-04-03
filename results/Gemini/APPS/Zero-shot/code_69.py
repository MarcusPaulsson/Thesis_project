def solve():
  a, b = map(int, input().split())
  s = input()
  n = len(s)
  
  gaps = []
  
  first_one = -1
  last_one = -1
  
  for i in range(n):
    if s[i] == '1':
      if first_one == -1:
        first_one = i
      last_one = i
      
  if first_one == -1:
    print(0)
    return
  
  
  
  current_gap = 0
  for i in range(first_one + 1, last_one + 1):
    if s[i] == '0':
      current_gap += 1
    else:
      if current_gap > 0:
        gaps.append(current_gap)
      current_gap = 0
      
  
  cost = a
  
  for gap in gaps:
    cost += min(a, gap * b)
  
  print(cost)
  

t = int(input())
for _ in range(t):
  solve()