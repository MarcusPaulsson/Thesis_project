def count_common_ap(a1, b1, a2, b2, L, R):
    def first_valid(start, step, lower_bound):
        if start > lower_bound:
            return start
        if (lower_bound - start) % step == 0:
            return lower_bound
        return start + ((lower_bound - start) // step + 1) * step

    def last_valid(start, step, upper_bound):
        if start > upper_bound:
            return -1
        return start + ((upper_bound - start) // step) * step

    # Calculate the first and last valid x for both sequences
    x1_start = b1
    x2_start = b2
    
    # Find the first valid x in the range [L, R]
    x1_first = first_valid(x1_start, a1, L)
    x2_first = first_valid(x2_start, a2, L)

    # Find the last valid x in the range [L, R]
    x1_last = last_valid(x1_start, a1, R)
    x2_last = last_valid(x2_start, a2, R)

    # Initialize the count of common integers
    count = 0

    # Iterate through the arithmetic sequence of one of the progressions
    for x in range(x1_first, x1_last + 1, a1):
        if (x - b2) % a2 == 0 and L <= x <= R:
            count += 1

    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().strip().split())
result = count_common_ap(a1, b1, a2, b2, L, R)
print(result)