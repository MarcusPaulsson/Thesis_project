def max_beauty_with_one_swap(n, trophies):
    max_length = 0
    current_length = 0
    segments = []
    
    # Create a list of lengths of segments of 'G'
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
    
    # If all trophies are golden
    if len(segments) == 0:
        return n
    
    # If there's only one segment of golden trophies
    if len(segments) == 1:
        return segments[0]
    
    # Check for the possibility of merging two segments by swapping one 'S'
    for i in range(len(segments) - 1):
        max_length = max(max_length, segments[i] + segments[i + 1])
    
    # If we can swap one 'S' to extend a segment by 1
    if len(segments) > 0:
        max_length += 1
    
    return max_length

# Input reading
n = int(input().strip())
trophies = input().strip()

# Output the result
print(max_beauty_with_one_swap(n, trophies))