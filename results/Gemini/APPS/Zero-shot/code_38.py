def solve():
  n, k1, k2 = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  max_a = max(a)
  max_b = max(b)
  
  if max_a > max_b:
    print("YES")
  else:
    print("NO")

t = int(input())
for _ in range(t):
  solve()