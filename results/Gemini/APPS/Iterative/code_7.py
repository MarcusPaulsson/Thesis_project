def solve():
    n, m = map(int, input().split())

    l, r = 0, 2 * 10**9
    ans = r

    while l <= r:
        mid = (l + r) // 2
        
        total_sparrows = mid * (mid + 1) // 2
        
        
        full_barns = 0
        if total_sparrows > n:
            full_barns = (total_sparrows - n + m - 1) // m
        
        
        grain_left = n + full_barns * m - total_sparrows
        
        if grain_left <= 0:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)

solve()