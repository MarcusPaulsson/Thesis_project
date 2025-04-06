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
    
    a = [best_gcd * i for i in range(1, k)]
    remaining = n - sum(a)
    
    if remaining <= a[-1]:
        print(-1)
        return
    
    a.append(remaining)
    print(*a)

solve()