def minimal_time(d, k, a, b, t):
    # Calculate the time if Vasiliy walks the entire distance
    time_if_walk = d * b
    
    # Calculate the number of full segments the car can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate the time if Vasiliy uses the car for full segments and walks the remaining distance
    time_using_car = full_segments * (k * a + t) + remaining_distance * a
    
    # If there are full segments, we need to subtract the last repair time
    if full_segments > 0:
        time_using_car -= t
    
    # Compare the two strategies and return the minimum time
    return min(time_if_walk, time_using_car)

# Read input
d, k, a, b, t = map(int, input().split())
# Print the result
print(minimal_time(d, k, a, b, t))