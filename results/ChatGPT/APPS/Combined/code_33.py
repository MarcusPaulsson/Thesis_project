def count_common_ap_integers(a1, b1, a2, b2, L, R):
    def find_first_valid_x(start, step, b, limit):
        if step == 0:
            return b if start <= limit else None
        if (start - b) % step == 0 and start <= limit:
            return start
        if step > 0:
            return b + ((start - b + step - 1) // step) * step
        return None

    def find_last_valid_x(end, step, b):
        if step == 0:
            return b if end >= b else None
        if (end - b) % step == 0:
            return end
        if step > 0:
            return b + (end - b) // step * step
        return None

    # Calculate the first and last valid x for both progressions
    first_x1 = find_first_valid_x(L, a1, b1, R)
    last_x1 = find_last_valid_x(R, a1, b1)
    
    first_x2 = find_first_valid_x(L, a2, b2, R)
    last_x2 = find_last_valid_x(R, a2, b2)

    # If any of the ranges are invalid, return 0
    if None in (first_x1, last_x1, first_x2, last_x2):
        return 0

    # Calculate the common range
    start = max(first_x1, first_x2)
    end = min(last_x1, last_x2)

    if start > end:
        return 0

    # Count the number of valid integers in the common range
    count = (end - start) // a1 + 1
    return count

# Input reading
a1, b1, a2, b2, L, R = map(int, input().split())
result = count_common_ap_integers(a1, b1, a2, b2, L, R)
print(result)