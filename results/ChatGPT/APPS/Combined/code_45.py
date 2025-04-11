def find_sequence(n, k):
    # Calculate the minimum sum of the first k natural numbers
    min_sum = k * (k + 1) // 2
    if n < min_sum:
        return -1

    # Calculate the maximum possible GCD
    max_gcd = n // k
    while max_gcd > 0:
        # Calculate the required sum with this GCD
        required_sum = min_sum * max_gcd
        if required_sum <= n:
            # If we can form the sequence
            sequence = [(i * max_gcd) for i in range(1, k + 1)]
            return sequence
        max_gcd -= 1

    return -1

# Input reading
n, k = map(int, input().split())
result = find_sequence(n, k)

# Output the result
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))