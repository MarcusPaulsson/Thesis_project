def max_beauty(n, trophies):
    # Count the lengths of segments of golden trophies
    segments = []
    current_length = 0
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
            current_length = 0
    if current_length > 0:
        segments.append(current_length)

    # If there are no golden trophies, return 0
    if not segments:
        return 0

    # Calculate the initial maximum length of golden segments
    max_length = max(segments)
    
    # If there is only one segment of golden trophies, no need to swap
    if len(segments) == 1:
        return max_length

    # Consider swapping a silver trophy with a golden one
    max_possible_length = max_length
    for i in range(len(segments) - 1):
        # Check if we can connect two segments by swapping one silver trophy
        if segments[i + 1] > 0:  # There must be a silver trophy between segments
            combined_length = segments[i] + segments[i + 1]  # Combine segments
            max_possible_length = max(max_possible_length, combined_length)

    return max_possible_length

# Input reading
n = int(input().strip())
trophies = input().strip()

# Output the result
print(max_beauty(n, trophies))