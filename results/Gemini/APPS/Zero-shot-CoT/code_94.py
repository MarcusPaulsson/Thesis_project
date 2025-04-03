def solve():
  n, T = map(int, input().split())
  a = list(map(int, input().split()))

  colors = [0] * n
  
  
  for i in range(n):
    if a[i] * 2 < T:
      colors[i] = 0
    elif a[i] * 2 > T:
      colors[i] = 1
    else:
      
      colors[i] = i % 2
  
  print(*colors)


t = int(input())
for _ in range(t):
  solve()