def solve():
  a, b, c = map(int, input().split())

  if c == 0:
    if a == b:
      print("YES")
    else:
      print("NO")
    return

  diff = b - a

  if diff % c == 0 and diff // c >= 0:
    print("YES")
  else:
    print("NO")

solve()