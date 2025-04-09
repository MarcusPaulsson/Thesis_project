def solve():
  n = int(input())
  total_sum = n * (n + 1) // 2
  if total_sum % 2 == 0:
    print(0)
  else:
    print(1)

solve()