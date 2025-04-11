def max_beauty_after_swap(n, trophies):
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
    
    if not segments:
        return 0
    
    max_length = max(segments)
    
    if len(segments) > 1:
        max_length = max(max_length, segments[0] + segments[1] + 1)
    
    return max_length

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))