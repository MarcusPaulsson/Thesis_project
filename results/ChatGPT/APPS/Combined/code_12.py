def max_beauty_after_swap(n, trophies):
    segments = []
    current_length = 0

    # Step 1: Find segments of 'G's
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                segments.append(current_length)
            current_length = 0

    if current_length > 0:
        segments.append(current_length)

    # If there are no 'G's, return 0
    if not segments:
        return 0

    # Step 2: Calculate the maximum beauty possible with one swap
    max_length = max(segments)
    max_possible_length = max_length

    # Combine segments of 'G's with a swap of one 'S' in between
    for i in range(len(segments) - 1):
        combined_length = segments[i] + segments[i + 1]
        max_possible_length = max(max_possible_length, combined_length)

    # Check if we can extend the longest segment by one if there's at least one 'S'
    if 'S' in trophies:
        max_possible_length = max(max_possible_length, max_length + 1)

    return max_possible_length

# Input reading
n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))