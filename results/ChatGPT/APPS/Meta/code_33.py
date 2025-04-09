def count_common_ap(a1, b1, a2, b2, L, R):
    def first_valid_x(a, b, start):
        if start <= b:
            return b
        if (start - b) % a == 0:
            return start
        return start + (a - (start - b) % a)

    def last_valid_x(a, b, end):
        if end < b:
            return None
        if (end - b) % a == 0:
            return end
        return end - (end - b) % a

    # Find the first and last valid x in both arithmetic progressions
    first_a1 = first_valid_x(a1, b1, L)
    last_a1 = last_valid_x(a1, b1, R)
    first_a2 = first_valid_x(a2, b2, L)
    last_a2 = last_valid_x(a2, b2, R)

    if first_a1 is None or last_a1 is None or first_a2 is None or last_a2 is None:
        return 0

    # Use a set to find the common terms
    common_count = 0
    for x in range(first_a1, last_a1 + 1, a1):
        if first_a2 <= x <= last_a2 and (x - b2) % a2 == 0:
            common_count += 1

    return common_count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
print(count_common_ap(a1, b1, a2, b2, L, R))