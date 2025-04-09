def count_common_integers(a1, b1, a2, b2, L, R):
    def adjust(start, step):
        if start < L:
            # Find the first valid integer >= L
            start += ((L - start + step - 1) // step) * step
        elif start > R:
            return None
        return start

    # Calculate the first valid x values for both sequences
    start1 = adjust(b1, a1)
    start2 = adjust(b2, a2)

    if start1 is None or start2 is None:
        return 0

    # Ensure we start from the maximum of both starts
    start = max(start1, start2)

    # Count the number of valid integers in the range [L, R]
    count = 0
    while start <= R:
        if (start - b1) % a1 == 0 and (start - b2) % a2 == 0:
            count += 1
        start += max(a1, a2)

    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_integers(a1, b1, a2, b2, L, R)
print(result)