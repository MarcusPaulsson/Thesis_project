def max_beauty_with_swap(n, trophies):
    # Step 1: Calculate the maximum length of golden trophies without any swaps
    max_length = 0
    current_length = 0
    segments = []
    
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            segments.append(current_length)
            max_length = max(max_length, current_length)
            current_length = 0
    segments.append(current_length)
    max_length = max(max_length, current_length)
    
    # If there are no silver trophies, return max_length immediately
    if 'S' not in trophies:
        return max_length
    
    # Step 2: Check for the possibility of increasing the length by one swap
    max_possible_length = max_length
    
    # We need to check adjacent segments of 'G's separated by 'S'
    for i in range(len(segments) - 1):
        if segments[i] > 0 and segments[i + 1] > 0:
            # If there is an S between two segments of Gs
            combined_length = segments[i] + segments[i + 1]
            max_possible_length = max(max_possible_length, combined_length + 1)
    
    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()

# Calculate and print the result
print(max_beauty_with_swap(n, trophies))