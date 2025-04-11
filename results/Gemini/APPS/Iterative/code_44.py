d, k, a, b, t = map(int, input().split())

if d <= k:
    print(d * a)
else:
    cost = k * a
    d -= k
    
    if a * k + t < b * k:
        num_breaks = d // k
        
        if num_breaks > 0:
            cost += num_breaks * min(a * k + t, b * k)
        
        d %= k
        
        if d > 0:
            cost += min(a * d + t, b * d)
    else:
        cost += b * d
        
    print(cost)