def max_chocolates(n, a, b, p, q):
    count_a = n // a
    count_b = n // b
    count_ab = n // (a * b)  # Count of indices that are divisible by both a and b

    # Calculate the maximum chocolates based on the strategy
    # Paint the common divisible by both a and b with the more rewarding color
    if p > q:
        chocolates = (count_a * p) + (count_b * q) - (count_ab * q)
    else:
        chocolates = (count_a * p) + (count_b * q) - (count_ab * p)

    return chocolates

# Read inputs
n, a, b, p, q = map(int, input().split())
print(max_chocolates(n, a, b, p, q))