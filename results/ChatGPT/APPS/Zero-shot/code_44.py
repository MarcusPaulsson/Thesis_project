def minimal_time_to_post_office(d, k, a, b, t):
    # Time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent driving full segments and repairing
    time_driving_full_segments = full_segments * (k * a + t)
    
    # If there are remaining kilometers to drive
    if remaining_distance > 0:
        time_driving_full_segments += remaining_distance * a
    
    # If there are full segments, we need to subtract the last repair time
    if full_segments > 0:
        time_driving_full_segments -= t
    
    # Compare with the time spent walking the remaining distance
    min_time = min(min_time, time_driving_full_segments + (remaining_distance * b))
    
    return min_time

# Read input
d, k, a, b, t = map(int, input().split())
# Calculate and print the result
print(minimal_time_to_post_office(d, k, a, b, t))