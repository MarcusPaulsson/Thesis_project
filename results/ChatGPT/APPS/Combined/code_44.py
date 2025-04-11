def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate time for driving full segments and walking the remaining distance
    time_with_driving = (full_segments * (k * a + t)) + (remaining_distance * a)
    
    # If there are full segments, subtract the last repair time
    if full_segments > 0:
        time_with_driving -= t
    
    # Update minimum time if driving is better
    min_time = min(min_time, time_with_driving)
    
    # Check if he can drive the last segment without needing to repair
    if remaining_distance > 0:
        time_with_driving += t + (remaining_distance * a)
        min_time = min(min_time, time_with_driving)
    
    return min_time

# Read input values
d, k, a, b, t = map(int, input().split())
# Output the minimal time
print(minimal_time_to_post_office(d, k, a, b, t))