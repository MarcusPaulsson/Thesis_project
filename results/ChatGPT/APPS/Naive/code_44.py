def min_time_to_post_office(d, k, a, b, t):
    # If d is less than or equal to k, we can drive the entire distance without repairs
    if d <= k:
        return d * a
    
    # Calculate the time using only the car and the time using both car and walking
    full_drive_time = (d // k) * (k * a + t) + (d % k) * a
    walking_time = d * b
    
    # Calculate the minimum time by evaluating combinations of driving and walking
    min_time = min(full_drive_time, walking_time)
    
    # Evaluate the cases where we can drive part of the distance and walk the rest
    for i in range(d // k + 1):
        distance_driven = i * k
        remaining_distance = d - distance_driven
        
        # Time spent driving i segments of k km and walking the remaining distance
        if remaining_distance >= 0:
            current_time = (i * (k * a + t) - t) + remaining_distance * b
            min_time = min(min_time, current_time)
    
    return min_time

# Input reading
d, k, a, b, t = map(int, input().strip().split())
print(min_time_to_post_office(d, k, a, b, t))