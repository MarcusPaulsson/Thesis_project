def max_beauty_after_swap(n, trophies):
    # Find the longest segment of golden trophies
    max_length = 0
    current_length = 0
    segments = []

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

    # If there are no golden trophies, return 0
    if max_length == 0:
        return 0

    # If we have at least one silver trophy, consider swaps
    if 'S' in trophies:
        if len(segments) > 1:
            # We can connect two segments of 'G' by swapping an 'S'
            max_length = max(max_length, segments[0] + segments[1])
            for i in range(1, len(segments)):
                max_length = max(max_length, segments[i-1] + segments[i] + 1)

    return max_length

# Input reading
n = int(input().strip())
trophies = input().strip()

# Calculate and print the result
print(max_beauty_after_swap(n, trophies))