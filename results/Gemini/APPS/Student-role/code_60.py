def solve():
  a, b = map(int, input().split())
  print(a ^ 0 + b ^ 0)

t = int(input())
for _ in range(t):
  solve()