def minimal_time(d, k, a, b, t):
    # Calculate full trips with the car
    full_trips = d // k
    remaining_distance = d % k
    
    # Time if using the car for all full trips
    time_using_car = full_trips * (k * a + t) + remaining_distance * a
    
    # If there are full trips, we need to subtract the last repair time
    if full_trips > 0:
        time_using_car -= t
    
    # Time if walking the whole distance
    time_walking = d * b
    
    # Minimum time between using the car and walking
    return min(time_using_car, time_walking)

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time(d, k, a, b, t))