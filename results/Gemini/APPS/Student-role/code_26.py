def solve():
  n, m = map(int, input().split())
  if (n == 1 and m >= 1) or (n >= 1 and m == 1) or (n == 2 and m == 2):
    print("YES")
  else:
    print("NO")

t = int(input())
for _ in range(t):
  solve()