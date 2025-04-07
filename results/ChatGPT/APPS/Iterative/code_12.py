def max_beauty_with_swap(n, trophies):
    lengths = []
    max_length = 0
    current_length = 0

    # Calculate lengths of consecutive 'G's
    for trophy in trophies:
        if trophy == 'G':
            current_length += 1
        else:
            if current_length > 0:
                lengths.append(current_length)
                max_length = max(max_length, current_length)
            current_length = 0

    # Append any remaining length of 'G's
    if current_length > 0:
        lengths.append(current_length)
        max_length = max(max_length, current_length)

    # If there are no 'G's, return 0
    if not lengths:
        return 0

    # If there's only one segment of 'G's, the best we can do is that segment
    if len(lengths) == 1:
        return max_length

    # Calculate potential new max length by swapping
    potential_max = max_length
    for i in range(len(lengths) - 1):
        # If we can swap a 'S' between two segments of 'G's
        potential_max = max(potential_max, lengths[i] + lengths[i + 1])

    return min(potential_max + 1, n)  # Ensure we do not exceed n

# Input reading
n = int(input())
trophies = input().strip()

# Output the result
print(max_beauty_with_swap(n, trophies))