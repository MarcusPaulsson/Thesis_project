def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        cost1 = k * a + t + (d - k) * b
        
        num_breaks = (d - 1) // k
        
        cost2 = num_breaks * (k * a + t) + (d - num_breaks * k) * a
        
        if t < (k * (b - a)):
            print(min(cost1, cost2))
        else:
            print(d * a + (d // k) * t)

solve()