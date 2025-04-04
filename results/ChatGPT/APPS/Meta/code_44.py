def minimal_time_to_post_office(d, k, a, b, t):
    if k >= d:
        # If the car can drive the entire distance without breaking
        return d * a
    
    # Calculate the number of full segments the car can drive before needing repair
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent if driving the full segments
    time_by_car = full_segments * (k * a + t)  # time driving full segments + repair time

    # If there is remaining distance after the last full segment
    if remaining_distance > 0:
        time_by_car += remaining_distance * a  # time for the remaining distance
    
    # Calculate time if walking the entire distance
    time_by_foot = d * b
    
    # The minimal time
    return min(time_by_car, time_by_foot)

# Example usage:
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))