def max_beauty_after_swap(n, trophies):
    # Calculate the lengths of golden segments
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
    
    # Find the maximum length without any swap
    max_length = max(segments)
    
    # If there's only one segment, we cannot swap to increase the length
    if len(segments) == 1:
        return max_length
    
    # Calculate the maximum possible length with one swap
    max_with_swap = max_length
    
    for i in range(len(segments) - 1):
        # Consider swapping a silver trophy between two golden segments
        max_with_swap = max(max_with_swap, segments[i] + segments[i + 1])
    
    return min(max_with_swap + 1, n)  # We cannot exceed n

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))