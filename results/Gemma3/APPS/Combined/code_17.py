def solve():
    n, k, t = map(int, input().split())
    
    if t <= k:
        print(t)
    else:
        time_since_peak = t - k
        standing = k - (time_since_peak % k)
        print(standing)

solve()