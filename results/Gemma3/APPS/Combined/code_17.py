def solve():
    n, k, t = map(int, input().split())
    
    if t <= k:
        print(t)
    else:
        time_since_peak = t - k
        standing = k
        if time_since_peak < k:
            standing -= time_since_peak % k
        else:
            standing -= k
        
        if standing < 0:
            standing += k
        
        print(standing)

solve()