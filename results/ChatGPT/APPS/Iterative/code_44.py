def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate time if Vasiliy walks the entire distance
    time_if_walks = d * b
    
    # Initialize minimum time as walking time
    min_time = time_if_walks
    
    # Calculate the number of full segments the car can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time taken to use the car for full segments
    time_with_car = full_segments * (k * a + t) - (t if full_segments > 0 else 0)
    
    # Add time for remaining distance (by car or foot)
    if remaining_distance > 0:
        time_with_car_drive_remaining = time_with_car + (remaining_distance * a)
        time_with_car_walk_remaining = time_with_car + t + (remaining_distance * b)
        
        min_time = min(min_time, time_with_car_drive_remaining, time_with_car_walk_remaining)
    else:
        min_time = min(min_time, time_with_car)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
# Output result
print(minimal_time_to_post_office(d, k, a, b, t))