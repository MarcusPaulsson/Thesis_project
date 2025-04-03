def max_beauty_after_swap(n, trophies):
    # Count the current longest segment of golden trophies
    current_max = 0
    current_count = 0
    segments = []

    for trophy in trophies:
        if trophy == 'G':
            current_count += 1
        else:
            if current_count > 0:
                segments.append(current_count)
                current_max = max(current_max, current_count)
            current_count = 0
    
    if current_count > 0:
        segments.append(current_count)
        current_max = max(current_max, current_count)

    # If there are no golden trophies, max beauty is 0
    if not segments:
        return 0

    # Calculate the maximum possible beauty after one swap
    max_beauty = current_max

    for i in range(len(segments) - 1):
        # Consider merging two segments by swapping one silver to golden
        combined = segments[i] + segments[i + 1]
        max_beauty = max(max_beauty, combined)

    # Check if we can increase the max length by 1 if there's at least one silver trophy
    if 'S' in trophies:
        max_beauty = max(max_beauty, current_max + 1)

    return max_beauty

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))