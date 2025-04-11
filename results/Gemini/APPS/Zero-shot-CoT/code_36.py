def solve():
    n = int(input())

    if n == 0:
        print(0, 0)
        return

    l, r = 0, 10**9
    k = 0
    while l <= r:
        mid = (l + r) // 2
        if 3 * mid * (mid + 1) >= n:
            k = mid
            r = mid - 1
        else:
            l = mid + 1

    n -= 3 * k * (k - 1)
    k -= 1
    k += 1
    
    if n <= k:
        print(2 * k - n, 2 * n)
    elif n <= 2 * k:
        n -= k
        print(k - 2 * n, 2 * k)
    elif n <= 3 * k:
        n -= 2 * k
        print(-k - n, 2 * k - 2 * n)
    elif n <= 4 * k:
        n -= 3 * k
        print(-2 * k + n, -2 * n)
    elif n <= 5 * k:
        n -= 4 * k
        print(-k + 2 * n, -2 * k)
    else:
        n -= 5 * k
        print(k + n, -2 * k + 2 * n)

solve()