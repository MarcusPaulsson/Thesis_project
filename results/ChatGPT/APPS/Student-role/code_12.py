def max_beauty_after_swap(n, trophies):
    max_length = 0
    current_length = 0
    segments = []

    # Count lengths of golden trophy segments
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
            current_length = 0

    if current_length > 0:
        segments.append(current_length)

    # If there are no golden trophies
    if not segments:
        return 0

    # The maximum length without any swap
    max_length = max(segments)

    # If there's only one segment of golden trophies, return its length
    if len(segments) == 1:
        return max_length

    # Try to combine segments by swapping
    for i in range(len(segments) - 1):
        combined_length = segments[i] + segments[i + 1]
        max_length = max(max_length, combined_length)

    # Also check if we can increase the length by 1 if we have at least one silver trophy to swap
    if 'S' in trophies:
        max_length += 1

    return max_length

# Input reading
n = int(input().strip())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))