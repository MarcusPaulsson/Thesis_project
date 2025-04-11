def solve():
    n, k = map(int, input().split())

    if k * (k + 1) // 2 > n:
        print(-1)
        return

    best_gcd = 1
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, i)
            if i >= k * (k + 1) // 2:
                best_gcd = max(best_gcd, n // i)

    if best_gcd == 1 and k * (k + 1) // 2 > n:
        print(-1)
        return

    first = best_gcd
    result = []
    for i in range(1, k):
        result.append(first * i)
    
    last = n - sum(result)
    if last <= result[-1]:
        print(-1)
        return

    result.append(last)
    
    print(*result)

solve()