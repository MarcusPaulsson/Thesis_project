def minimal_time_to_post_office(d, k, a, b, t):
    # Total time if walking the entire distance
    min_time = d * b
    
    # Calculate how many full segments of k kilometers can be driven
    full_segments = d // k
    remaining_distance = d % k
    
    # Time for full segments driving
    time_with_full_segments = full_segments * (k * a + t)  # driving + repair time
    
    # If there are full segments, we subtract the repair time for the last segment
    if full_segments > 0:
        time_with_full_segments -= t
    
    # Add the time for the remaining distance (either by car or on foot)
    time_with_full_segments += remaining_distance * a  # driving the remaining distance
    
    # Compare with walking the remaining distance
    time_with_full_segments_alternative = full_segments * (k * a + t) + remaining_distance * b
    
    # Update min_time with the best option
    min_time = min(min_time, time_with_full_segments, time_with_full_segments_alternative)

    return min_time

# Read input
d, k, a, b, t = map(int, input().split())
# Get the result
result = minimal_time_to_post_office(d, k, a, b, t)
# Print the result
print(result)