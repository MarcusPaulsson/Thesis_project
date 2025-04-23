def max_beauty_after_swap(n, trophies):
    segments = []
    current_length = 0
    
    # Calculate lengths of segments of 'G's
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
            current_length = 0
            
    if current_length > 0:
        segments.append(current_length)
    
    # If there are no 'G's, return 0
    if not segments:
        return 0
    
    # If there's only one segment, return its length
    if len(segments) == 1:
        return segments[0]
    
    # Calculate the maximum possible length after one swap
    max_possible_length = max(segments)
    
    for i in range(len(segments) - 1):
        # Check if we can merge two segments by swapping one 'S'
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1])
    
    # If we can swap an 'S' with a 'G' at the ends, we can add 1 to the max length
    if 'S' in trophies:
        max_possible_length += 1
    
    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))