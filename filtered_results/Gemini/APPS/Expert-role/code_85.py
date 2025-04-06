def solve():
  a, b = map(int, input().split())

  for price in range(1, 2501):
    tax8 = int(price * 0.08)
    tax10 = int(price * 0.1)
    if tax8 == a and tax10 == b:
      print(price)
      return

  print(-1)

solve()