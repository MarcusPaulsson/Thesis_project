def find_sequence(n, k):
    # Check if it is possible to have a strictly increasing sequence of k elements that sum to n
    min_sum = k * (k + 1) // 2  # 1 + 2 + ... + k
    if n < min_sum:
        return -1

    # The maximum GCD we can use is n // k, because we need each number to be at least that much
    max_gcd = n // k

    # We can start from max_gcd and build the sequence
    sequence = [(i + 1) * max_gcd for i in range(k)]

    # Check if the sum exceeds n
    current_sum = sum(sequence)
    if current_sum > n:
        return -1

    # Adjust the last element to make the sum equal to n
    sequence[-1] += n - current_sum

    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))