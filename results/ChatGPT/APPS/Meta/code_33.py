def count_common_ap(a1, b1, a2, b2, L, R):
    # Calculate the first possible value of x in the range [L, R]
    def first_value(a, b, start):
        if (start - b) % a == 0:
            return start
        return start + (a - (start - b) % a) % a

    # Calculate the last possible value of x in the range [L, R]
    def last_value(a, b, end):
        if (end - b) % a == 0:
            return end
        return end - (end - b) % a

    # Find the first and last values for both progressions
    first_x1 = first_value(a1, b1, L)
    last_x1 = last_value(a1, b1, R)
    
    first_x2 = first_value(a2, b2, L)
    last_x2 = last_value(a2, b2, R)

    # If the first value of one progression is greater than the last of the other, return 0
    if first_x1 > last_x2 or first_x2 > last_x1:
        return 0

    # Calculate the number of common values in the range
    count = 0
    for x in range(max(first_x1, first_x2), min(last_x1, last_x2) + 1):
        if (x - b1) % a1 == 0 and (x - b2) % a2 == 0:
            count += 1

    return count

# Read input
a1, b1, a2, b2, L, R = map(int, input().split())
# Print the result
print(count_common_ap(a1, b1, a2, b2, L, R))