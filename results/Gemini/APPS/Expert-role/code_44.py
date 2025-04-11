def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        cost1 = k * a + t + (d - k) * b
        
        num_breaks = (d // k) - 1
        remaining_dist = d % k
        
        if remaining_dist == 0:
            num_breaks += 1
            remaining_dist = k
        
        cost2 = k * a
        
        if num_breaks > 0:
            cost2 += num_breaks * (k * a + t)
        
        cost2 += remaining_dist * min(a, b)
        
        if remaining_dist == k and a > b:
            cost2 -= remaining_dist * (a - b)
            
        
        cost3 = 0
        num_full_breaks = d // k
        rem_dist = d % k
        
        if rem_dist == 0 and d > 0:
            num_full_breaks -= 1
            rem_dist = k
            
        if num_full_breaks > 0:
            cost3 += num_full_breaks * (k * a + t)
        
        cost3 += rem_dist * b if rem_dist > 0 else 0
        cost3 += k * a if d > 0 else 0
        
        
        cost4 = 0
        num_full_breaks = d // k
        rem_dist = d % k
        
        if rem_dist == 0 and d > 0:
            num_full_breaks -= 1
            rem_dist = k
            
        if num_full_breaks > 0:
            cost4 += num_full_breaks * (k * a + t)
        
        cost4 += rem_dist * b if rem_dist > 0 else 0
        cost4 += k * a if d > 0 else 0
        
        if k * a + t > k * b:
            num_breaks = (d // k)
            rem_dist = d % k
            
            if rem_dist == 0 and d > 0:
                num_breaks -= 1
                rem_dist = k
            
            cost5 = num_breaks * (k * a + t) + rem_dist * b
            
            if d <= k:
                cost5 = d * a
            else:
                cost5 = k * a + (d - k) * b
            
            print(min(cost5, d * a + max(0, (d // k) - 1) * t))
        else:
            print(min(d * a + max(0, (d // k) - 1) * t, d * a + (d // k - 1) * t + (d % k) * b))

solve()