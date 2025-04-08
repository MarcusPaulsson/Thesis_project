def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        ans = k * a
        remaining_distance = d - k
        
        if k * b <= t + k * a:
            ans += remaining_distance * b
        else:
            num_breaks = remaining_distance // k
            ans += num_breaks * (t + k * a)
            remaining_distance %= k
            
            ans += min(remaining_distance * b, t + remaining_distance * a)
        
        print(ans)

solve()