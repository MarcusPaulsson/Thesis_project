def solve():
  n = int(input())
  pairs = []
  for _ in range(n):
    pairs.append(list(map(int, input().split())))

  valid = True
  for i in range(n):
    p, c = pairs[i]
    if c > p:
      valid = False
      break
    if i > 0:
      prev_p, prev_c = pairs[i-1]
      if p < prev_p or c < prev_c:
        valid = False
        break
      if p - prev_p < c - prev_c:
        valid = False
        break
  
  if valid:
    print("YES")
  else:
    print("NO")

t = int(input())
for _ in range(t):
  solve()