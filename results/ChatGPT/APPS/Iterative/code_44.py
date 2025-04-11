def minimal_time(d, k, a, b, t):
    total_time = float('inf')
    
    # Calculate time if using the car for all full segments
    full_segments = d // k
    remaining_distance = d % k

    # Time if using the car for all full segments
    time_using_car = full_segments * (k * a + t) + remaining_distance * a
    if full_segments > 0:
        time_using_car -= t  # Remove the last repair time if we don't need it

    # Time if walking the entire distance
    time_walking = d * b

    # Compare the time using car and walking
    total_time = min(time_using_car, time_walking)

    # Consider mixed strategies
    for i in range(full_segments + 1):
        time = i * (k * a + t) + (d - i * k) * b
        if i > 0:
            time -= t  # Remove the last repair time if we don't need it
        total_time = min(total_time, time)

    return total_time

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time(d, k, a, b, t))