def max_beauty_after_swap(n, trophies):
    max_length = 0
    current_length = 0
    segments = []

    # Count segments of golden trophies
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

    # If there are no golden trophies
    if max_length == 0:
        return 0

    # Calculate the maximum length after one swap
    if len(segments) == 1:
        return max_length  # Only one segment of G's

    max_possible_length = max_length
    for i in range(len(segments) - 1):
        # Check if we can connect two segments by swapping one S
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1])

    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))