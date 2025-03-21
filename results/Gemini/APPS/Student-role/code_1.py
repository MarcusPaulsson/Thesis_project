def solve():
  q = int(input())
  for _ in range(q):
    n, m, k = map(int, input().split())

    if n > k or m > k:
      print(-1)
      continue

    if (n % 2) != (m % 2):
      if k % 2 == 0:
        print(-1)
      else:
        print(k - 1)
    else:
      print(k)

solve()