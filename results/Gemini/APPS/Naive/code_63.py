def solve():
  n = int(input())
  a = list(map(int, input().split()))

  min_instability = float('inf')

  for i in range(n):
    temp_a = a[:i] + a[i+1:]
    
    max_val = max(temp_a)
    min_val = min(temp_a)
    
    instability = max_val - min_val
    min_instability = min(min_instability, instability)

  print(min_instability)

solve()