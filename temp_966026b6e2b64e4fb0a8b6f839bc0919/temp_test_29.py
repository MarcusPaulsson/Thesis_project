def solve():
  n = int(input())
  a = list(map(int, input().split()))

  ans = [-1] * n
  
  for k in range(1, n + 1):
    amazing_num = -1
    
    candidates = set()
    for i in range(n - k + 1):
      subsegment = a[i:i+k]
      
      if i == 0:
        candidates = set(subsegment)
      else:
        candidates = candidates.intersection(set(subsegment))

    if candidates:
      amazing_num = min(candidates)
    
    ans[k-1] = amazing_num

  print(*ans)

t = int(input())
for _ in range(t):
  solve()