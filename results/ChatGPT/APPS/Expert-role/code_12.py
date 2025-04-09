def max_beauty_with_swap(n, trophies):
    # Find the current longest segment of 'G'
    max_length = 0
    current_length = 0
    segments = []
    
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            segments.append(current_length)
            max_length = max(max_length, current_length)
            current_length = 0
    segments.append(current_length)  # Add the last segment
    max_length = max(max_length, current_length)

    # If there are no 'S' trophies to swap with
    if 'S' not in trophies:
        return max_length

    # Now calculate the maximum length if we swap one 'S' with one 'G'
    max_possible_length = max_length
    
    for i in range(len(segments) - 1):
        # If we can swap the 'S' between two segments of 'G'
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1] + 1)

    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()

# Calculate and output the result
print(max_beauty_with_swap(n, trophies))