def minimal_time(d, k, a, b, t):
    # If the car can drive the entire distance without breaking down
    if d <= k:
        return d * a
    
    # Calculate number of complete segments the car can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time taken if using the car for full segments and walking the rest
    time_using_car = (full_segments * (k * a + t)) + (remaining_distance * a)
    
    # Time taken if walking the entire distance
    time_walking = d * b
    
    # Minimum time considering both strategies
    return min(time_using_car, time_walking)

# Read input
d, k, a, b, t = map(int, input().split())
# Output the result
print(minimal_time(d, k, a, b, t))