def solve():
  n, k = map(int, input().split())
  s = input()
  
  wins = 0
  for char in s:
    if char == 'W':
      wins += 1
  
  if wins + k >= n:
    print(2 * n - 1)
    return
  
  if wins == 0:
    if k == 0:
      print(0)
    else:
      print(2 * k - 1)
    return
  
  
  
  gaps = []
  start = -1
  end = -1
  
  for i in range(n):
    if s[i] == 'W':
      if start == -1:
        start = i
      end = i
  
  
  curr_gap = 0
  for i in range(start + 1, end + 1):
    if s[i] == 'L':
      curr_gap += 1
    else:
      if curr_gap > 0:
        gaps.append(curr_gap)
        curr_gap = 0
  
  if curr_gap > 0:
      gaps.append(curr_gap)

  
  gaps.sort()
  
  score = 0
  
  for i in range(n):
    if s[i] == 'W':
      if i > 0 and s[i-1] == 'W':
        score += 2
      else:
        score += 1
  
  
  for gap in gaps:
    if k >= gap:
      score += 2 * gap + 1
      k -= gap
    else:
      score += 2 * k
      k = 0
      break

  score += 2 * k
  
  print(score)

t = int(input())
for _ in range(t):
  solve()