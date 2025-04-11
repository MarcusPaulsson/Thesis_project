def solve():
    d, k, a, b, t = map(int, input().split())

    if d <= k:
        print(d * a)
        return

    cost_only_driving = k * a + t + (d - k) * a
    cost_drive_and_walk = k * a + (d - k) * b

    if cost_drive_and_walk < cost_only_driving:
        print(cost_drive_and_walk)
        return

    num_breaks = (d - 1) // k
    total_driving_cost = num_breaks * (k * a + t)
    remaining_distance_last = d - num_breaks * k
    total_driving_cost += remaining_distance_last * a
    
    cost_with_breaks = total_driving_cost
    
    print(cost_with_breaks)
    

solve()