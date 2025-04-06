d, k, a, b, t = map(int, input().split())

if d <= k:
    print(d * a)
else:
    cost_driving = k * a + t
    cost_walking = k * b

    if cost_driving > cost_walking:
        print(k * a + (d - k) * b)
    else:
        num_breaks = d // k
        remaining_distance = d % k

        time = num_breaks * (k * a + t)
        time -= t
        
        
        time += min(t + remaining_distance * a, remaining_distance * b) 
        

        print(time)