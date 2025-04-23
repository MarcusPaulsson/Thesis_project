def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time taken if Vasiliy drives full segments and walks the remaining distance
    time_with_driving = full_segments * (k * a + t) + remaining_distance * b - t
    min_time = min(min_time, time_with_driving)
    
    # Check if he can drive fewer segments and walk the rest
    for segments in range(full_segments + 1):
        distance_driven = segments * k
        time_taken = segments * (k * a + t) + (d - distance_driven) * b
        
        # If he drives the last segment, he doesn't need to repair after it
        if segments > 0:
            time_taken -= t
        
        min_time = min(min_time, time_taken)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))