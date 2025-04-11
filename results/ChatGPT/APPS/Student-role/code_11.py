def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)

    # Calculate chocolates if we prioritize Red tiles
    chocolates_red_first = (count_a - count_ab) * p + (count_b - count_ab) * q

    # Calculate chocolates if we prioritize Blue tiles
    chocolates_blue_first = (count_b - count_ab) * q + (count_a - count_ab) * p

    # Return the maximum of both strategies
    return max(chocolates_red_first, chocolates_blue_first)

# Example usage:
# n, a, b, p, q = map(int, input().split())
# print(max_chocolates(n, a, b, p, q))