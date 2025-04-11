def minimal_time_to_post_office(d, k, a, b, t):
    # Initialize the minimum time to a large number
    min_time = float('inf')
    
    # Calculate how many full segments of k kilometers can be driven
    full_segments = d // k
    remaining_distance = d % k
    
    # Calculate time if using the car for full segments and walking the rest
    time_using_car = full_segments * (k * a + t) + remaining_distance * a - t  # subtract t for the last segment
    min_time = min(min_time, time_using_car)
    
    # Calculate time if walking the entire distance
    time_walking = d * b
    min_time = min(min_time, time_walking)
    
    # Check combinations of driving and walking
    for i in range(full_segments + 1):
        distance_driven = i * k
        time_spent = i * (k * a + t)  # time for driving and repairing
        
        if distance_driven < d:
            remaining_distance = d - distance_driven
            time_spent += remaining_distance * b  # time for walking the remaining distance
        
        min_time = min(min_time, time_spent)
    
    return min_time

# Read input
d, k, a, b, t = map(int, input().split())
# Calculate and print the result
print(minimal_time_to_post_office(d, k, a, b, t))