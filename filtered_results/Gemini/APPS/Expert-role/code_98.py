def solve():
  n = int(input())
  
  ans = float('inf')
  
  for i in range(1, int(n**0.5) + 2):
    if n % i == 0:
      j = n // i
      ans = min(ans, i + j - 2)
      
  print(ans)

solve()