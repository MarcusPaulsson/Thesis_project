def find_sequence(n, k):
    # Calculate the minimum sum required for the first k natural numbers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        return -1

    # Calculate the maximum possible gcd
    max_gcd = n // k

    # Iterate to find the largest gcd that allows forming a valid sequence
    for g in range(max_gcd, 0, -1):
        total = g * min_sum  # Total sum if we use g as the gcd
        if total <= n:
            # We can form the sequence
            sequence = [g * i for i in range(1, k + 1)]
            # Adjust the last element to match the sum n
            sequence[-1] += (n - total)
            return sequence

    return -1

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print output
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))