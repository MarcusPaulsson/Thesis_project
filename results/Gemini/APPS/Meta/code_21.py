def solve():
  n = int(input())
  a = list(map(int, input().split()))

  min_idx = a.index(1)
  max_idx = a.index(n)

  ans = 0
  for i in range(n):
    temp_a = a[:]
    temp_a[min_idx], temp_a[i] = temp_a[i], temp_a[min_idx]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))

  for i in range(n):
    temp_a = a[:]
    temp_a[max_idx], temp_a[i] = temp_a[i], temp_a[max_idx]
    ans = max(ans, abs(temp_a.index(1) - temp_a.index(n)))
    
  print(ans)

solve()