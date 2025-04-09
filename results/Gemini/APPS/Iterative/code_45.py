def solve():
  n, k = map(int, input().split())

  if k * (k + 1) // 2 > n:
    print("-1")
    return

  best_gcd = 1
  i = 1
  while i * i <= n:
    if n % i == 0:
      if n // i >= k * (k + 1) // 2:
        best_gcd = max(best_gcd, i)
      if i >= k * (k + 1) // 2:
        best_gcd = max(best_gcd, n // i)
    i += 1

  first = best_gcd
  remaining_sum = n // best_gcd

  if remaining_sum < k * (k + 1) // 2:
    print("-1")
    return

  result = []
  for i in range(1, k):
    result.append(i * first)
    remaining_sum -= i
  result.append(remaining_sum * first)

  if all(result[i] < result[i + 1] for i in range(len(result) - 1)):
    print(*result)
  else:
    print("-1")


solve()