def minimal_time_to_post_office(d, k, a, b, t):
    # If the car can drive the entire distance without breaking
    if d <= k:
        return d * a
    
    # Calculate the number of full segments the car can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time taken if using the car for full segments and walking the remaining distance
    time_using_car = (full_segments * (k * a + t)) + (remaining_distance * a) - t
    
    # Time taken if walking the entire distance
    time_walking = d * b
    
    # Return the minimum time
    return min(time_using_car, time_walking)

# Read input
d, k, a, b, t = map(int, input().split())
# Calculate and print the result
print(minimal_time_to_post_office(d, k, a, b, t))