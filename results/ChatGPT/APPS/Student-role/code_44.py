def minimal_time(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    walk_time = d * b
    
    # Calculate the number of full segments the car can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate the time if Vasiliy drives the car for full segments and walks the remaining distance
    drive_time = full_segments * (k * a + t) + remaining_distance * a
    
    # If there are full segments, we need to subtract the last repair time
    if full_segments > 0:
        drive_time -= t
    
    # Compare the two times and return the minimum
    return min(walk_time, drive_time)

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time(d, k, a, b, t))