def max_beauty_after_swap(n, trophies):
    # Find the lengths of segments of golden trophies
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
    
    # If there are no golden trophies
    if not segments:
        return 0
    
    # Calculate the maximum length of golden trophies without any swap
    max_length = max(segments)
    
    # If there is only one segment, we cannot increase the length by swapping
    if len(segments) == 1:
        return max_length
    
    # Calculate the maximum possible length with one swap
    max_possible_length = max_length
    
    for i in range(len(segments) - 1):
        # Check if we can swap a silver trophy between two segments of golden trophies
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1])
    
    # If we can swap a silver trophy with a golden trophy at the ends
    if 'S' in trophies:
        max_possible_length += 1
    
    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))