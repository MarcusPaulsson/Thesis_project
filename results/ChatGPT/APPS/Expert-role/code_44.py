def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the maximum number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate the time for driving full segments and walking the remaining distance
    if full_segments > 0:
        time_with_driving = full_segments * (k * a + t) + remaining_distance * b - t
        min_time = min(min_time, time_with_driving)
    
    # Calculate the time for driving full segments and repairing the car
    if full_segments > 0 and remaining_distance > 0:
        time_with_driving_and_repair = full_segments * (k * a + t) + remaining_distance * a
        min_time = min(min_time, time_with_driving_and_repair)
    
    # Calculate the time for driving the last segment if it fits
    if remaining_distance > 0:
        time_with_partial_drive = full_segments * (k * a + t) + remaining_distance * a
        min_time = min(min_time, time_with_partial_drive)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))