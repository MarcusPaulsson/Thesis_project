def solve():
    n, m = map(int, input().split())

    left = 0
    right = 2 * 10**9 

    ans = -1

    while left <= right:
        mid = (left + right) // 2
        
        total_sparrows = mid * (mid + 1) // 2
        
        
        
        full_barns = (total_sparrows - n + (n + m - 1)) // (n + m) if total_sparrows > n else 0
       

        
        remaining_grains = n + full_barns * m - total_sparrows
        
        if remaining_grains <= 0:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(ans)

solve()