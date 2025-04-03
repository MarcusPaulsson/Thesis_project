def minimal_time_to_post_office(d, k, a, b, t):
    # If the car can drive the entire distance without breaking down
    if d <= k:
        return d * a
    
    # Time if only walking
    time_if_walking = d * b
    
    # Time if using the car
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent driving the full segments
    time_using_car = full_segments * (k * a + t)
    
    # Time spent driving the remaining distance (if any)
    if remaining_distance > 0:
        time_using_car += remaining_distance * a
    
    # Adjust for the last segment, no repair after the last one
    if full_segments > 0:
        time_using_car -= t
    
    # Compare both strategies
    return min(time_if_walking, time_using_car)

# Read input
d, k, a, b, t = map(int, input().split())
# Calculate and print the minimal time
print(minimal_time_to_post_office(d, k, a, b, t))