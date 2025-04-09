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
            
        
        if a[l-1] > k and a[r+1] > k and l <= r:
            break
            
        
    print(count)

solve()