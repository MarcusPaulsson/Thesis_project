def solve():
  n, m = map(int, input().split())
  
  if n == m:
    print(0)
    return
  
  if m % n != 0:
    print(-1)
    return
  
  diff = m // n
  
  count2 = 0
  count3 = 0
  
  while diff % 2 == 0:
    diff //= 2
    count2 += 1
  
  while diff % 3 == 0:
    diff //= 3
    count3 += 1
    
  if diff != 1:
    print(-1)
    return
  
  print(count2 + count3)

solve()