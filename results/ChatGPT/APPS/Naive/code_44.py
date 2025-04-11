def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k

    # Time if he drives all full segments and walks the remaining distance
    time_using_car = full_segments * (k * a + t) + remaining_distance * a
    time_using_car -= t  # Remove the last repair time since he doesn't need to repair after the last segment

    # Time if he walks the entire distance
    time_walking = d * b

    # Calculate the minimum time considering both strategies
    min_time = min(time_using_car, time_walking)

    # Check if he can drive some distance, repair, and then walk the rest
    if full_segments > 0:
        for i in range(full_segments + 1):
            time = (i * (k * a + t)) + (d - i * k) * b
            min_time = min(min_time, time)

    return min_time

# Input reading
d, k, a, b, t = map(int, input().split())
result = minimal_time_to_post_office(d, k, a, b, t)
print(result)