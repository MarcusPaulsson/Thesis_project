import math

def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)
                
    if best_gcd == 1 and k * (k+1) // 2 > n:
      print("-1")
      return

    result = []
    sum_so_far = 0
    for i in range(1, k):
        result.append(best_gcd * i)
        sum_so_far += best_gcd * i

    result.append(n - sum_so_far)
    print(*result)

solve()