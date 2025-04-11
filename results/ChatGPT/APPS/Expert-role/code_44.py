def minimal_time(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent driving full segments and repairing
    time_driving_full_segments = full_segments * (k * a + t)
    
    # Time spent driving the remaining distance
    time_driving_remaining = remaining_distance * a
    
    # Total time if using the car for full segments and walking the remaining distance
    total_time_using_car = time_driving_full_segments + time_driving_remaining
    
    # Compare with walking the full distance
    min_time = min(min_time, total_time_using_car)
    
    # Check if it's better to drive one less segment and walk the remaining distance
    if full_segments > 0:
        time_driving_one_less_segment = (full_segments - 1) * (k * a + t) + k * a
        total_time_one_less_segment = time_driving_one_less_segment + (d - (full_segments - 1) * k) * b
        min_time = min(min_time, total_time_one_less_segment)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time(d, k, a, b, t))