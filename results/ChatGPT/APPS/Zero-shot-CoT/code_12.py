def max_beauty_with_swap(n, trophies):
    max_length = 0
    current_length = 0
    segments = []

    # Calculate current segments of G's
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
                max_length = max(max_length, current_length)
            current_length = 0
    if current_length > 0:
        segments.append(current_length)
        max_length = max(max_length, current_length)

    # If there are no G's
    if max_length == 0:
        return 0

    # If we can swap one S with a G
    if len(segments) > 1:
        # We can connect two segments of G's with one S in between
        for i in range(len(segments) - 1):
            max_length = max(max_length, segments[i] + segments[i + 1])
    
    # If there is at least one S, we can potentially increase the max length by 1
    if 'S' in trophies:
        max_length += 1

    return max_length

# Read input
n = int(input().strip())
trophies = input().strip()

# Get the result
result = max_beauty_with_swap(n, trophies)

# Print the result
print(result)