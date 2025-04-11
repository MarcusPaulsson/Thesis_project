def minimal_time_to_post_office(d, k, a, b, t):
    # Total time if Vasiliy walks the entire distance
    walk_time = d * b
    
    # Initialize the minimum time with the walking time
    min_time = walk_time
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate time for driving full segments and walking the remaining distance
    if full_segments > 0:
        driving_time = full_segments * k * a
        repair_time = (full_segments - 1) * t if full_segments > 1 else 0
        total_time = driving_time + repair_time + remaining_distance * b
        min_time = min(min_time, total_time)
    
    # Check if Vasiliy can drive one less segment and walk the rest
    if full_segments > 0:
        driving_time = (full_segments - 1) * k * a
        repair_time = (full_segments - 1) * t
        total_time = driving_time + repair_time + k * a + remaining_distance * b
        min_time = min(min_time, total_time)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))