def solve():
  s = input()
  n = len(s)
  
  counts = {'R': 0, 'S': 0, 'P': 0}
  for char in s:
    counts[char] += 1
  
  best_choice = ''
  if counts['R'] >= counts['S'] and counts['R'] >= counts['P']:
    best_choice = 'P'
  elif counts['S'] >= counts['R'] and counts['S'] >= counts['P']:
    best_choice = 'R'
  else:
    best_choice = 'S'
  
  print(best_choice * n)

t = int(input())
for _ in range(t):
  solve()