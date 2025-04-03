def minimal_time(d, k, a, b, t):
    # Time if Vasiliy walks the entire distance
    walk_time = d * b

    # Initialize the minimum time to the walking time
    min_time = walk_time

    # Calculate the maximum number of full k kilometers Vasiliy can drive
    full_drives = d // k
    remaining_distance = d % k

    # Calculate time taken for each possible scenario of driving and walking
    for drives in range(full_drives + 1):
        # Distance driven by car
        distance_driven = drives * k

        # Time taken for driving
        driving_time = distance_driven * a
        
        # Time taken for repairs
        repairs_time = drives * t

        # Remaining distance to walk
        distance_to_walk = d - distance_driven
        
        # Time taken for walking
        walking_time = distance_to_walk * b

        # Total time for this combination
        total_time = driving_time + repairs_time + walking_time

        # Update the minimum time
        min_time = min(min_time, total_time)

    return min_time

# Read input
d, k, a, b, t = map(int, input().split())
# Print the result
print(minimal_time(d, k, a, b, t))