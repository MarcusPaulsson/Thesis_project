def minimal_time(d, k, a, b, t):
    # Initialize the minimum time to infinity
    min_time = float('inf')
    
    # Calculate how many full segments of k fit into d
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate time using the car for full segments and walking the remaining distance
    time_with_car = full_segments * (k * a) + remaining_distance * a + full_segments * t
    min_time = min(min_time, time_with_car)
    
    # Check the case where we walk the full distance
    time_walking = d * b
    min_time = min(min_time, time_walking)
    
    # Consider driving segments and walking the rest
    for segments in range(full_segments + 1):
        distance_by_car = segments * k
        if distance_by_car > d:
            break
            
        time_by_car = distance_by_car * a + segments * t
        remaining_distance = d - distance_by_car
        time_by_foot = remaining_distance * b

        total_time = time_by_car + time_by_foot
        min_time = min(min_time, total_time)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
# Output the minimal time
print(minimal_time(d, k, a, b, t))