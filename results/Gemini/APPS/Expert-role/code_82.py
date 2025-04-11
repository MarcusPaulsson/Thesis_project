def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    l = 0
    r = n - 1
    count = 0
    
    while l <= r:
        if a[l] <= k:
            count += 1
            l += 1
        elif a[r] <= k:
            count += 1
            r -= 1
        else:
            break
            
        if l > r:
            break
        
        can_solve_left = a[l] <= k if l <= r else False
        can_solve_right = a[r] <=k if l <= r else False
        
        if not can_solve_left and not can_solve_right:
            break
        

    print(count)

solve()