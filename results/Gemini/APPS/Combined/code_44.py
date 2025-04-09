def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
        return

    cost_driving_only = k * a + (d - k) * b
    cost_with_repairs = 0
    
    num_full_drives = d // k
    
    cost_with_repairs = num_full_drives * (k * a + t)
    remaining_distance = d % k
    
    
    if remaining_distance > 0:
        cost_with_repairs -= t
        cost_with_repairs += remaining_distance * a
        
    
    
    if t + k * a < k * b:
        
        num_breaks = (d - 1) // k
        cost_alt = 0
        if num_breaks > 0:
            cost_alt = num_breaks * (k * a + t)
            remaining_distance_last = d - num_breaks * k
            cost_alt += remaining_distance_last * a
        else:
            cost_alt = d * a
    else:
        cost_alt = k * a + (d - k) * b
        
    cost_with_repairs = k * a + (num_full_drives -1) * (k * a + t)
    if num_full_drives > 1:
        cost_with_repairs+= (d % k) * a
    else:
        cost_with_repairs = d * a

    if t + k * a < k * b:
        cost_with_repairs = 0
      
        num_breaks = (d - 1) // k
        
        if num_breaks > 0:
            cost_with_repairs = num_breaks * (k * a + t)
            remaining_distance_last = d - num_breaks * k
            cost_with_repairs += remaining_distance_last * a
        else:
            cost_with_repairs = d * a

    else:
        cost_with_repairs = k * a + (d - k) * b
        

    print(min(cost_with_repairs, cost_driving_only))

solve()