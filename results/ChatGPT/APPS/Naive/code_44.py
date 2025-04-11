def minimal_time_to_post_office(d, k, a, b, t):
    # Calculate the number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k
    
    # Time spent driving full segments
    time_driving_segments = full_segments * (k * a)
    
    # Time spent repairing the car after each full segment (except the last one)
    time_repairing_segments = full_segments * t if full_segments > 0 else 0
    
    # Time spent driving the remaining distance
    time_driving_remaining = remaining_distance * a
    
    # Total time if he drives the full distance
    total_time_driving = time_driving_segments + time_repairing_segments + time_driving_remaining
    
    # Total time if he walks the entire distance
    total_time_walking = d * b
    
    # The minimal time will be the minimum of both strategies
    return min(total_time_driving, total_time_walking)

# Example usage
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))