def minimal_time(d, k, a, b, t):
    # Time when Vasiliy only walks
    time_by_foot = d * b
    
    # Time when Vasiliy uses the car
    full_segments = d // k
    remaining_distance = d % k
    
    # Total time using car: time for full segments + time for remaining distance
    time_by_car = full_segments * (k * a + t) + remaining_distance * a
    
    # If there is any distance left, subtract the last repair time if it was added
    if remaining_distance == 0 and full_segments > 0:
        time_by_car -= t
    
    # Compare time by foot and time by car
    return min(time_by_foot, time_by_car)

# Input reading
d, k, a, b, t = map(int, input().split())
# Output the result
print(minimal_time(d, k, a, b, t))