def max_beauty_after_swap(n, trophies):
    # Find the current maximum length of golden trophies
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

    # If there are no golden trophies, return 0
    if max_length == 0:
        return 0

    # If there's only one segment of golden trophies, we can only swap with a silver
    if len(segments) == 1:
        return max_length

    # Calculate the maximum possible length after one swap
    max_possible_length = max_length
    for i in range(len(segments) - 1):
        # Check if we can merge two segments by swapping one silver trophy
        max_possible_length = max(max_possible_length, segments[i] + segments[i + 1])

    # If we can swap with a silver trophy, we can increase the length by 1
    return max_possible_length + 1

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))