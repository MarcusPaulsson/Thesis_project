def max_beauty_after_swap(n, trophies):
    segments = []
    current_length = 0

    # Calculate the lengths of segments of golden trophies
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

    # If there's only one segment, we can only swap with a silver trophy
    if len(segments) == 1:
        return segments[0]

    # Calculate the maximum beauty by considering swaps
    max_beauty = max(segments)
    for i in range(len(segments) - 1):
        # Check if we can connect two segments by swapping a silver trophy
        max_beauty = max(max_beauty, segments[i] + segments[i + 1])

    # If we can swap a silver trophy to extend the longest segment
    max_beauty = max(max_beauty, max(segments) + 1)

    return max_beauty

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_after_swap(n, trophies))