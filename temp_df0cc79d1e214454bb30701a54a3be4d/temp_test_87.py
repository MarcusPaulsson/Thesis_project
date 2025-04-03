import math

def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

def solve():
  m, d, w = map(int, input().split())
  
  w = w // gcd(d - 1, w)
  
  mn = min(m, d)
  
  k = mn // w
  
  ans = mn * k - w * (k * (k + 1) // 2)
  
  print(ans)

t = int(input())
for _ in range(t):
  solve()