def max_beauty_after_swap(n, trophies):
    # Find the lengths of contiguous segments of 'G'
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
    
    # Calculate the maximum length of 'G' segments
    max_length = max(segments)
    
    # If there is only one segment, no swap can increase its length
    if len(segments) == 1:
        return max_length
    
    # Check for possible swaps between segments
    max_possible_length = max_length
    
    for i in range(len(segments) - 1):
        # If we swap a 'S' between two segments of 'G', we can combine them
        combined_length = segments[i] + segments[i + 1]
        max_possible_length = max(max_possible_length, combined_length)
    
    # If we can swap a 'S' with a 'G' to increase the length of the longest segment
    max_possible_length = min(max_possible_length + 1, n)
    
    return max_possible_length

# Input reading
n = int(input().strip())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))