def max_beauty(n, trophies):
    segments = []
    current_length = 0
    
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
    
    # Calculate the maximum length of golden trophies without any swaps
    max_length = max(segments)

    # If there's only one segment, we cannot increase its length by swapping
    if len(segments) == 1:
        return max_length

    # Try to merge segments by swapping one silver trophy
    for i in range(len(segments) - 1):
        # Check if we can swap a silver between two segments
        max_length = max(max_length, segments[i] + segments[i + 1])

    # Check if a swap can be made if there is at least one silver trophy
    if 'S' in trophies:
        max_length += 1

    return max_length

# Input reading
n = int(input().strip())
trophies = input().strip()
print(max_beauty(n, trophies))