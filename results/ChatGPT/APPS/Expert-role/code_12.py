def max_beauty_with_swap(n, trophies):
    if 'G' not in trophies:
        return 0
    
    # Find lengths of segments of golden trophies
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
        
    if len(segments) == 0:
        return 0
    
    # Calculate maximum length without any swap
    max_length = max(segments)
    
    # If there's only one segment, no swap can increase the beauty
    if len(segments) == 1:
        return max_length
    
    # Now consider swapping the first S in between two segments
    max_possible = max_length
    
    for i in range(len(segments) - 1):
        # The longest segment can be increased by 1 if we swap an 'S' between two 'G' segments
        max_possible = max(max_possible, segments[i] + segments[i + 1])
    
    return min(max_possible + 1, n)

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_with_swap(n, trophies))