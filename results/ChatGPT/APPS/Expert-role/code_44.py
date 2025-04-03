def minimal_time(d, k, a, b, t):
    # Initialize the minimum time
    min_time = float('inf')

    # Calculate the maximum number of full segments Vasiliy can drive
    full_segments = d // k
    remaining_distance = d % k

    # Check all possible ways to drive and walk
    for segments in range(full_segments + 1):
        # Distance covered by car
        distance_by_car = segments * k
        # Time spent driving
        time_driving = distance_by_car * a
        # Time spent repairing the car
        time_repairing = segments * t

        # Remaining distance that needs to be walked
        distance_by_foot = d - distance_by_car
        # Time spent walking
        time_walking = distance_by_foot * b

        # Total time for this strategy
        total_time = time_driving + time_repairing + time_walking
        # Update minimum time found
        min_time = min(min_time, total_time)

    # Check if he can drive the remaining distance without repair
    if remaining_distance > 0:
        time_driving = full_segments * k * a + remaining_distance * a
        time_repairing = full_segments * t
        total_time = time_driving + time_repairing
        min_time = min(min_time, total_time)

    return min_time

# Input
d, k, a, b, t = map(int, input().split())
# Output
print(minimal_time(d, k, a, b, t))