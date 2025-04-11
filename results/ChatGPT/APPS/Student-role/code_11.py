def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)  # Count of tiles that are divisible by both a and b

    # Calculate chocolates if we paint common tiles Red or Blue
    chocolates_if_red = count_a * p + (count_b - count_ab) * q
    chocolates_if_blue = count_b * q + (count_a - count_ab) * p

    return max(chocolates_if_red, chocolates_if_blue)

# Input
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))