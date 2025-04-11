def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    min_time = d * b
    
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time taken if Vasiliy drives full segments and then walks the remaining distance
    if full_segments > 0:
        time_with_driving = (full_segments * k * a) + (full_segments - 1) * t + remaining_distance * b
        min_time = min(min_time, time_with_driving)
    
    # Consider the case where Vasiliy drives less than full segments
    for i in range(full_segments + 1):
        time_with_driving = (i * k * a) + (i * t) + (d - i * k) * b
        min_time = min(min_time, time_with_driving)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
# Output the result
print(minimal_time_to_post_office(d, k, a, b, t))