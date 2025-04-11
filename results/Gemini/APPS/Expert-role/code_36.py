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

    x, y = 2 * k, 0

    if n <= k:
        x -= 2 * n
        print(x, y)
        return
    
    n -= k
    x -= 2 * k
    y += 2 * n
    
    if n <= k:
        print(x, y)
        return
    
    n -= k
    x += n * 2
    y += n * 2
    
    if n <= k:
        print(x, y)
        return
    
    n -= k
    x += 2 * k - 2 * n
    
    if n <= k:
        print(x, y)
        return
    
    n -= k
    x -= 2 * n
    y -= 2 * n
    
    if n <= k:
        print(x, y)
        return
    
    n -= k
    x -= 2 * k - 2 * n
    y -= 2 * k
    
    print(x, y)

solve()