def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)

    # Calculate chocolates
    chocolates_a = count_a * p
    chocolates_b = count_b * q

    # If p > q, prioritize painting Red
    if p > q:
        chocolates = chocolates_a + (count_b - count_ab) * q
    else:
        chocolates = (count_a - count_ab) * p + chocolates_b

    return chocolates

# Read input
n, a, b, p, q = map(int, input().split())
# Print the result
print(max_chocolates(n, a, b, p, q))