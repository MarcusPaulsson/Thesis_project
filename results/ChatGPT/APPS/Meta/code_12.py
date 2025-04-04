def max_beauty_with_one_swap(n, trophies):
    # Step 1: Find the lengths of contiguous segments of 'G'
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

    # Step 2: Calculate the maximum beauty without any swaps
    max_beauty = max(segments) if segments else 0

    # Step 3: Check for possible swaps to increase the beauty
    if len(segments) < 2:
        return max_beauty  # No possible swaps if less than two segments

    # Step 4: Check adjacent segments to see if a swap could merge them
    for i in range(len(segments) - 1):
        max_beauty = max(max_beauty, segments[i] + segments[i + 1])
    
    # We can also consider the case where we swap a 'S' with a 'G' on the edge
    if trophies[0] == 'S' and segments:
        max_beauty = max(max_beauty, segments[0] + 1)
    if trophies[-1] == 'S' and segments:
        max_beauty = max(max_beauty, segments[-1] + 1)

    return max_beauty

# Input reading
n = int(input().strip())
trophies = input().strip()

# Output the result
print(max_beauty_with_one_swap(n, trophies))