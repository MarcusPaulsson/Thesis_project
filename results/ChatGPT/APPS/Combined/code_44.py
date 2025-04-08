def minimal_time_to_post_office(distance, segment_length, drive_time, walk_time, repair_time):
    # Calculate the number of full segments and the remaining distance
    full_segments = distance // segment_length
    remaining_distance = distance % segment_length

    # Calculate the time spent driving full segments with repairs
    total_drive_time = full_segments * (segment_length * drive_time + repair_time)
    
    if full_segments > 0:
        total_drive_time -= repair_time  # Remove the last repair time as it's not needed after the last segment

    # Add time for the remaining distance
    total_drive_time += remaining_distance * drive_time

    # Calculate the time if Vasiliy walks the entire distance
    total_walk_time = distance * walk_time

    # Return the minimum time between driving and walking
    return min(total_drive_time, total_walk_time)

# Input reading
d, k, a, b, t = map(int, input().split())
print(minimal_time_to_post_office(d, k, a, b, t))