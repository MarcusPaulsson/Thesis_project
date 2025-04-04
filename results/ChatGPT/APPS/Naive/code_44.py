def minimal_time_to_post_office(d, k, a, b, t):
    # If d is less than or equal to k, Vasiliy can drive the whole distance without any breaks
    if d <= k:
        return d * a

    # Calculate the number of full segments he can drive before needing to walk
    full_segments = d // k
    remaining_distance = d % k

    # Calculate time for driving full segments with repairs
    time_driving = full_segments * (k * a + t)  # time driving + repair time for full segments
    time_driving -= t  # subtract the last repair time since he doesn't need to repair after reaching the destination

    # Calculate time for the remaining distance
    time_remaining = remaining_distance * a

    # Calculate time if he decides to walk the entire distance
    time_walking = d * b

    # Return the minimum time between driving with repairs and walking the entire distance
    return min(time_driving + time_remaining, time_walking)

# Input reading
d, k, a, b, t = map(int, input().split())
# Output the result
print(minimal_time_to_post_office(d, k, a, b, t))