def max_beauty_after_swap(n, trophies):
    segments = []
    current_length = 0
    
    # Count segments of golden trophies
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
    
    # Calculate the maximum length without any swap
    max_length = max(segments)
    
    # Check for possible improvement by swapping
    for i in range(len(segments) - 1):
        # If we swap a silver trophy between two segments of golden trophies
        max_length = max(max_length, segments[i] + segments[i + 1])
    
    # If there is at least one silver trophy, we can swap it with a golden trophy
    if 'S' in trophies:
        max_length = max(max_length, max(segments) + 1)
    
    return max_length

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))