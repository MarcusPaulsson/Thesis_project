def solve():
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  
  if all(x == 0 for x in a):
    print(0)
    return
  
  a.sort()
  
  total = sum(a[n-k-1:])
  
  print(total)
  

t = int(input())
for _ in range(t):
  solve()