def solve():
  d, k, a, b, t = map(int, input().split())

  if d <= k:
    print(d * a)
  else:
    cost_driving_all = k * a + t + (d - k) * a
    cost_driving_and_walking = k * a + (d - k) * b
    
    num_breaks = (d // k) - 1
    remaining_distance = d % k
    
    if remaining_distance == 0:
      num_breaks += 1
      remaining_distance = k
    
    cost_multiple_drives = 0
    if num_breaks > 0:
      cost_multiple_drives = k * a * num_breaks + t * num_breaks
    
    cost_last_drive = remaining_distance * a
    
    if cost_last_drive + t > remaining_distance * b:
      cost_last_drive = remaining_distance * b
      t = 0
      
    if t > 0:
        cost_last_drive += t
    else:
        cost_last_drive = remaining_distance * b

    cost_all_drives = 0
    num_full_drives = d // k
    remaining_dist = d % k
    if remaining_dist == 0 and d > 0:
      num_full_drives -= 1
      remaining_dist = k

    cost_all_drives = k * a * num_full_drives + t * num_full_drives + remaining_dist * b
        
    cost_multiple_drives = k * a * num_breaks + t * num_breaks

    remaining_after_multiple = d - k * num_breaks

    if remaining_after_multiple > 0:
      
      if remaining_after_multiple * a + t < remaining_after_multiple * b:
        cost_multiple_drives += remaining_after_multiple * a
        cost_multiple_drives += t
      else:
        cost_multiple_drives += remaining_after_multiple * b
    
    print(min(cost_driving_all, cost_driving_and_walking, cost_all_drives))

solve()