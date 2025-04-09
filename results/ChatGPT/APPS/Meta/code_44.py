d, k, a, b, t = map(int, input().split())

def min_time(d, k, a, b, t):
    # Initialize the minimum time with the case where Vasiliy walks the entire distance
    min_time = d * b

    # Calculate the maximum number of full trips Vasiliy can take with the car
    full_trips = d // k
    remaining_distance = d % k

    # Iterate through the number of full trips from 0 to full_trips
    for trips in range(full_trips + 1):
        # Distance covered by car in this many trips
        distance_by_car = trips * k
        
        # Time spent driving this distance
        time_driving = distance_by_car * a
        
        # Time spent repairing the car (trips - 1 repairs)
        time_repairing = (trips - 1) * t if trips > 0 else 0
        
        # Remaining distance to walk
        distance_to_walk = d - distance_by_car
        
        # Time spent walking the remaining distance
        time_walking = distance_to_walk * b
        
        # Total time for this scenario
        total_time = time_driving + time_repairing + time_walking
        
        # Update minimum time if we found a better option
        min_time = min(min_time, total_time)

    return min_time

print(min_time(d, k, a, b, t))