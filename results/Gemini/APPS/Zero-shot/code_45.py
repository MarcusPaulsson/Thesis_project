def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print("-1")
        return

    best_gcd = 1
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)

    if best_gcd == 0:
        print("-1")
        return

    result = []
    for i in range(1, k):
        result.append(best_gcd * i)
    
    result.append(n - sum(result))

    if all(result[i] < result[i+1] for i in range(len(result)-1)) and all(x > 0 for x in result):
       print(*result)

    else:
      print("-1")



solve()