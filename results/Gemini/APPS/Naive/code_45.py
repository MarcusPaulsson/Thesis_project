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

    first = best_gcd
    result = []
    for i in range(1, k):
        result.append(first * i)
    result.append(n // best_gcd * best_gcd - sum(result))
    
    if any(x <= 0 for x in result):
        print(-1)
        return
    
    if len(set(result)) != len(result):
        print(-1)
        return

    if sum(result) != n:
        print(-1)
        return

    if not all(x % best_gcd == 0 for x in result):
        print(-1)
        return

    if not all(result[i] < result[i+1] for i in range(len(result)-1)):
        print(-1)
        return
    
    print(*result)

solve()