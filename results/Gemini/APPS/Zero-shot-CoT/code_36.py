def solve():
    n = int(input())
    
    if n == 0:
        print(0, 0)
        return
    
    l, r = 0, 10**9
    k = 0
    while l <= r:
        mid = (l + r) // 2
        if 3 * mid * (mid + 1) <= n:
            k = mid
            l = mid + 1
        else:
            r = mid - 1
    
    rem = n - 3 * k * (k + 1)
    
    x, y = 2 * k, 0
    
    if rem == 0:
        print(x, y)
        return
    
    if rem <= k:
        x -= rem * 2
        print(x, y)
        return
    
    rem -= k
    x -= k * 2
    x -= rem
    y += rem * 2
    
    if rem == 0:
        print(x, y)
        return
    
    if rem <= k:
        print(x, y)
        return
    
    rem -= k
    x -= k
    y += k * 2

    x += rem * 2
    
    if rem == 0:
        print(x, y)
        return

    if rem <= k:
        print(x, y)
        return
    
    rem -= k
    
    x += k * 2
    x += rem
    y -= rem * 2

    if rem == 0:
        print(x, y)
        return
    
    if rem <= k:
        print(x, y)
        return
    
    rem -= k
    x += k
    y -= k * 2
    x -= rem * 2

    if rem == 0:
        print(x, y)
        return
    
    if rem <= k:
        print(x, y)
        return
    
    rem -= k
    x -= k * 2
    x -= rem
    y += rem * 2

    print(x,y)
solve()