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

    # Calculate the maximum possible length after one swap
    if len(segments) == 1:
        return max_length  # Only one segment of golden trophies

    # Check possible merges by swapping a silver trophy
    max_possible = max_length
    for i in range(1, len(segments)):
        # Check if we can merge two segments by swapping a silver trophy
        max_possible = max(max_possible, segments[i - 1] + segments[i])

    return max_possible

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))