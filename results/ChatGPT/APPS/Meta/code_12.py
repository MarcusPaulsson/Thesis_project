def max_beauty_after_swap(n, trophies):
    # Step 1: Find the longest segment of golden trophies and their indices
    max_length = 0
    current_length = 0
    segments = []
    
    for i in range(n):
        if trophies[i] == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
                max_length = max(max_length, current_length)
            current_length = 0
    if current_length > 0:
        segments.append(current_length)
        max_length = max(max_length, current_length)
    
    # If there are no golden trophies
    if not segments:
        return 0
    
    # Step 2: Consider the case of swapping
    max_possible = max_length
    
    # If there's at least one silver trophy to swap with
    if 'S' in trophies:
        # Check between segments
        for i in range(len(segments) - 1):
            combined_length = segments[i] + segments[i + 1]
            max_possible = max(max_possible, combined_length + 1)  # +1 for the swap
    
    # Return the maximum possible length
    return max_possible

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))