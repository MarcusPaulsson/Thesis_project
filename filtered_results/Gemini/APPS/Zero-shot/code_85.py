def solve():
  a, b = map(int, input().split())
  
  ans = -1
  for price in range(1, 10001):
    tax8 = int(price * 0.08)
    tax10 = int(price * 0.10)
    
    if tax8 == a and tax10 == b:
      ans = price
      break
      
  print(ans)

solve()