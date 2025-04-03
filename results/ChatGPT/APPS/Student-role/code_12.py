def max_beauty_after_swap(n, trophies):
    # Find the lengths of all segments of golden trophies
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
    
    # If there are no segments of golden trophies
    if not segments:
        return 0
    
    # Calculate the maximum length of golden trophies segment
    max_length = max(segments)

    # If there's only one segment, we cannot increase its length by any swap
    if len(segments) == 1:
        return max_length
    
    # Check potential enhancements by swaps
    max_possible = max_length
    
    for i in range(len(segments) - 1):
        # Check if there's a silver trophy between two segments of golden trophies
        if trophies.count('S') > 0:
            combined_length = segments[i] + segments[i + 1] + 1
            max_possible = max(max_possible, combined_length)
    
    return max_possible

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))