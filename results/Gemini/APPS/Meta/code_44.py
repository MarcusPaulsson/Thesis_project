def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        cost_driving_all = k * a + t + (d - k) * a
        cost_drive_k_walk_rest = k * a + (d - k) * b

        num_breaks = (d - 1) // k
        
        cost_with_breaks = 0
        
        if d <= k:
            cost_with_breaks = d * a
        else:
            num_full_breaks = d // k
            
            if num_full_breaks > 0:
                cost_with_breaks = (k * a + t) * (num_full_breaks - 1) + k * a
                remaining_distance = d - k * num_full_breaks
                if remaining_distance > 0:
                    cost_with_breaks += min(remaining_distance * a + t, remaining_distance * b)
                else:
                    cost_with_breaks += t
            else:
                cost_with_breaks = k * a + min(t + (d - k) * a, (d - k) * b)

        
        if d > k:
            first_k = k * a
            remaining = d - k
            
            if t + k * a < k * b:
                num_breaks = (d - k - 1) // k + 1
                
                if num_breaks > 0:
                    cost_with_breaks = k * a + min(t * num_breaks + (d - k) * a, (d - k) * b)
                else:
                    cost_with_breaks = k * a + (d - k) * b
            else:
                cost_with_breaks = k * a + (d - k) * b
        
        
        if d > k:
            if t + k * a < k * b:
                num_breaks = (d - k - 1) // k + 1
                
                if num_breaks > 0:
                    cost_with_breaks = k * a + min(t * num_breaks + (d - k) * a, (d - k) * b)
                else:
                    cost_with_breaks = k * a + (d - k) * b
            else:
                cost_with_breaks = k * a + (d - k) * b
        
        
        if d > k:
            num_full_breaks = d // k
            
            if num_full_breaks > 0:
                cost_with_breaks = (k * a + t) * (num_full_breaks - 1) + k * a
                remaining_distance = d - k * num_full_breaks
                if remaining_distance > 0:
                    cost_with_breaks += min(remaining_distance * a + t, remaining_distance * b)
                else:
                    cost_with_breaks += t
            else:
                cost_with_breaks = k * a + min(t + (d - k) * a, (d - k) * b)
        
        if d <= k:
            print(d * a)
        else:
            print(min(k * a + (d - k) * b, (d // k) * (k * a + t) + (d % k) * a if d % k != 0 else (d // k - 1) * (k * a + t) + k * a))

solve()