def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate total time if walking the entire distance
    walking_time = d * b
    
    # If driving is quicker than walking, calculate the mixed strategy
    if a * k + t < b:
        # Full segments of k that can be driven
        full_segments = d // k
        remaining_distance = d % k
        
        # Calculate driving time for full segments
        driving_time = full_segments * (k * a + t)
        
        # If there are full segments, subtract the last repair time
        if full_segments > 0:
            driving_time -= t
            
        # Add time for the remaining distance driven
        driving_time += remaining_distance * a
        
        # Return the minimum of walking time and driving time
        return min(driving_time, walking_time)

    # If driving is not quicker, just walk
    return walking_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))