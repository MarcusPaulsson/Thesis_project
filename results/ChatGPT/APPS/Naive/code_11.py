def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)  # Tiles that are painted both Red and Blue

    # Calculate the maximum chocolates
    chocolates_red = count_a * p
    chocolates_blue = count_b * q

    # Since tiles divisible by both a and b can be painted either color,
    # we need to choose the better option for those tiles.
    if p > q:
        # Paint the overlapping tiles Red
        chocolates = chocolates_red + (count_b - count_ab) * q
    else:
        # Paint the overlapping tiles Blue
        chocolates = chocolates_blue + (count_a - count_ab) * p

    return chocolates

# Example usage:
# n, a, b, p, q = map(int, input().split())
# print(max_chocolates(n, a, b, p, q))