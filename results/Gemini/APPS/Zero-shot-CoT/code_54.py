def solve():
  q = int(input())
  for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    
    total_sum = 0
    for x in s:
      total_sum += x
    
    if total_sum >= 2048:
      print("YES")
    else:
      print("NO")

solve()