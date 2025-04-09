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
    
    max_beauty = max(segments)

    if len(segments) == 1:
        return max_beauty

    for i in range(len(segments) - 1):
        potential_beauty = segments[i] + segments[i + 1]
        max_beauty = max(max_beauty, potential_beauty)

    return max_beauty

# Input reading
n = int(input())
trophies = input().strip()

# Get the result and print it
print(max_beauty_after_swap(n, trophies))