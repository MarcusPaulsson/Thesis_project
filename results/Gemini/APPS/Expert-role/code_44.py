def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        ans = k * a
        d -= k
        
        if t + k * a < k * b:
            num_breaks = d // k
            ans += num_breaks * (t + k * a)
            d -= num_breaks * k
            
            if d > 0:
                ans += min(t + d * a, d * b)
        else:
            ans += d * b
        print(ans)

solve()