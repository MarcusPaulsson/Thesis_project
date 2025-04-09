def solve():
    d, k, a, b, t = map(int, input().split())
    
    if d <= k:
        print(d * a)
    else:
        cost1 = k * a + (d - k) * b
        
        num_breaks = (d - 1) // k
        
        cost2 = num_breaks * (k * a + t) + (d - num_breaks * k) * a
        
        cost3 = (d // k) * (k * a + t) + (d % k) * b

        cost4 = k*a + t + (d-k)*b
        
        if t + k*a > k*b:
            print(k*a + (d-k)*b)

        else:
             print(min(cost1, cost2))
    

solve()