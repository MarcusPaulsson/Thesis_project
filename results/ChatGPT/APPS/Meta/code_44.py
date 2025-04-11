def minimal_time_to_post_office(d, k, a, b, t):
    # Initialize the minimum time to a large number
    min_time = float('inf')
    
    # Calculate how many full segments of k kilometers can be driven
    full_segments = d // k
    remaining_distance = d % k
    
    # Time if Vasiliy drives all full segments and walks the remaining distance
    time_if_driving_all = full_segments * (k * a + t) + remaining_distance * a - t
    min_time = min(min_time, time_if_driving_all)
    
    # Check if it's better to walk some distance instead of driving
    for segments in range(full_segments + 1):
        distance_driven = segments * k
        time_spent = segments * (k * a + t)
        
        # Remaining distance to walk
        remaining_distance = d - distance_driven
        
        # If remaining distance is negative, break
        if remaining_distance < 0:
            break
        
        # Calculate total time
        total_time = time_spent + remaining_distance * b
        
        # Update minimum time
        min_time = min(min_time, total_time)
    
    return min_time

# Example usage:
# d, k, a, b, t = map(int, input().split())
# print(minimal_time_to_post_office(d, k, a, b, t))