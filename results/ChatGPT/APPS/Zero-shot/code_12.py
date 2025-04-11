def max_beauty_after_swap(n, trophies):
    max_length = 0
    current_length = 0
    segments = []

    # Calculate lengths of segments of 'G's
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

    # If there are no 'G's, return 0
    if not segments:
        return 0

    # Check for the possibility of swapping
    if len(segments) == 1:
        return max_length  # Only one segment of 'G's

    # Calculate the maximum possible length after one swap
    max_possible_length = max_length
    for i in range(len(segments) - 1):
        # If we swap a 'S' between two segments of 'G's
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1])

    # If we can add one more 'G' to the longest segment
    max_possible_length = min(max_possible_length + 1, n)

    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))