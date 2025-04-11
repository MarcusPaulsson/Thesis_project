def solve():
  n, k = map(int, input().split())
  t = input()
  
  if k == 1:
    print(t)
    return
  
  max_overlap = 0
  for i in range(1, n):
    if t[:n-i] == t[i:]:
      max_overlap = n - i
      break
  
  s = t
  for _ in range(k - 1):
    s += t[max_overlap:]
  
  print(s)

solve()