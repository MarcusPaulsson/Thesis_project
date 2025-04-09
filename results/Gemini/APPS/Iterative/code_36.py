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

    k = max(0, k - 1)
    n -= 3 * k * (k + 1)
    k += 1

    x, y = 2 * k, 0

    if n <= k:
        x -= 2 * n
    elif n <= 2 * k:
        x -= 2 * k
        n -= k
        y += 2 * n
    elif n <= 3 * k:
        n -= 2 * k
        x -= (k - n)
        y += 2 * k
    elif n <= 4 * k:
        n -= 3 * k
        x += 2 * n
        y += (2 * k - 2*n)
    elif n <= 5 * k:
        n -= 4 * k
        x += 2*k - 2*n
        y -= 2*n
    else:
        n -= 5 * k
        x -= 2*k + (-2*n)
        y -= (2 * k - 2*n)
    
    print(x, y)

solve()