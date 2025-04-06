def solve():
  a = int(input())
  
  if a == 1:
    print(0)
    return
    
  ans = 0
  curr = 2
  while curr <= a:
    curr *= 2
    ans += 1
  
  print(ans)

solve()