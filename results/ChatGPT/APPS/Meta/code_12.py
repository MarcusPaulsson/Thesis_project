def max_beauty_after_swap(n, trophies):
    # Step 1: Find the current longest segment of 'G's
    max_length = 0
    current_length = 0
    segments = []
    
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
    
    # Step 2: If there are no 'S' trophies, return the current max_length
    if 'S' not in trophies:
        return max_length
    
    # Step 3: Calculate the maximum possible length after one swap
    max_possible_length = max_length
    
    for i in range(len(segments) - 1):
        # Check if we can swap an 'S' trophy between two segments of 'G's
        combined_length = segments[i] + segments[i + 1]
        max_possible_length = max(max_possible_length, combined_length + 1)
    
    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))