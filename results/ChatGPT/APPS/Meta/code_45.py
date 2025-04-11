def find_sequence(n, k):
    # Check if it's possible to create a strictly increasing sequence of k positive numbers that sums to n
    if n < (k * (k + 1)) // 2:
        return -1  # Not enough to form the sequence

    # The minimum sum of the first k natural numbers is k * (k + 1) / 2
    # We can find the maximum GCD by starting from 1 and going upwards
    # The maximum GCD we can use is n // k
    max_gcd = n // k

    # We will create the sequence with the maximum GCD
    sequence = [(i + 1) * max_gcd for i in range(k)]
    total_sum = sum(sequence)

    # Adjust the last element to ensure the sum equals n
    sequence[-1] += (n - total_sum)

    return sequence

# Read input
n, k = map(int, input().split())
result = find_sequence(n, k)

# Print the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))