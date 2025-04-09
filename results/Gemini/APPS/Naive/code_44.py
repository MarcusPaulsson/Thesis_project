def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
    else:
        cost_driving_all = k * a + t + (d - k) * a
        cost_drive_k_walk_rest = k * a + (d - k) * b
        
        num_breaks = (d - 1) // k
        
        cost_with_breaks = 0
        
        if num_breaks == 0:
          cost_with_breaks = d * a
        else:
          
          full_breaks = (d // k) - 1 
          
          
          if full_breaks < 0:
            full_breaks = 0
            
          cost_with_breaks = (k * a + t) * (full_breaks + 1) + (d % k) * a
          
          if d % k == 0:
              cost_with_breaks -= (d % k) * a
          
        
        cost_walk_rest_after_first_k = k * a + (d - k) * b
        
        cost_alt_break = 0
        
        if d > k:
            breaks = (d - 1) // k
            
            if breaks > 0:
                
                
                cost_alt_break = (k * a + t) * breaks
                
                remaining_dist = d - k * breaks
                
                cost_alt_break += min(remaining_dist * a, remaining_dist * b + t)
            else:
                cost_alt_break = d * a
        else:
            cost_alt_break = d * a
            
        if d <= k:
            print(d * a)
        else:
           
            
            
            
            cost_efficient_breaks = 0
            
            
            if d > k:
                num_full_ks = (d // k)
                remaining_dist = d % k
                
                if remaining_dist == 0:
                    num_full_ks -= 1
                    remaining_dist = k
                    
                if num_full_ks > 0:
                    cost_efficient_breaks = (k * a) * num_full_ks + t * num_full_ks
                    cost_efficient_breaks += min(remaining_dist * a, remaining_dist * b)
                else:
                    cost_efficient_breaks = d * a
            else:
                cost_efficient_breaks = d * a
           
           
            if t > k * b - k * a :
                print(k * a + (d-k) * b)
            else:
                num_breaks = (d - 1) // k

                if num_breaks == 0:
                    print(d * a)
                else:
                    print(min(
                        d * a + num_breaks * t,
                        k * a + (d - k) * b + num_breaks * t,
                        k * a + (d - k) * b
                    ))
solve()