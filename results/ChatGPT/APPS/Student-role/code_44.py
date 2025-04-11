def minimal_time(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    walk_time = d * b
    
    # Initialize the minimum time with the walking time
    min_time = walk_time
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate the time for driving full segments and walking the remaining distance
    drive_time = full_segments * k * a
    repair_time = full_segments * t
    total_time = drive_time + repair_time + remaining_distance * b
    
    # Update the minimum time if this option is better
    min_time = min(min_time, total_time)
    
    # Check if he can drive less than full segments and walk the rest
    for i in range(full_segments + 1):
        drive_time = i * k * a
        repair_time = i * t
        remaining_distance = d - i * k
        
        if remaining_distance >= 0:
            total_time = drive_time + repair_time + remaining_distance * b
            min_time = min(min_time, total_time)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time(d, k, a, b, t))