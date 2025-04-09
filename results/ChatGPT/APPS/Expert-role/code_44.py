def minimal_time(d, k, a, b, t):
    # Total time if Vasiliy walks the entire distance
    walk_time = d * b
    
    # Initialize the minimal time with the walk time
    min_time = walk_time
    
    # Calculate the maximum number of complete segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent if he drives full segments and walks the remaining distance
    drive_time = full_segments * k * a + (full_segments - 1) * t + remaining_distance * b
    min_time = min(min_time, drive_time)
    
    # If there are full segments, consider the case where he repairs the car
    if full_segments > 0:
        drive_time = full_segments * k * a + (full_segments * t) + remaining_distance * b
        min_time = min(min_time, drive_time)
    
    # Consider driving less than full segments
    for i in range(full_segments + 1):
        # Time if he drives i segments, repairs, then walks the remaining distance
        drive_time = i * k * a + i * t + remaining_distance * b
        min_time = min(min_time, drive_time)
    
    return min_time

# Read input values
d, k, a, b, t = map(int, input().split())
# Calculate and print the minimal time
print(minimal_time(d, k, a, b, t))