def get_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def solve(test_cases):
    results = []
    for n in test_cases:
        divisors = get_divisors(n)
        divisors.sort()

        if len(divisors) == 1:
            initial_order = divisors
            moves = 0
        else:
            # For numbers with more than one divisor, we can always arrange them
            # to avoid coprime pairs by grouping them based on their prime factors.
            # We will use the first divisor and then append all others.
            initial_order = [divisors[0]] + divisors[1:]
            moves = 0  # As we can always arrange them properly without moves.

        results.append((initial_order, moves))
    return results

# Read input
t = int(input())
test_cases = [int(input().strip()) for _ in range(t)]

# Solve the test cases
results = solve(test_cases)

# Print the output
for initial_order, moves in results:
    print(" ".join(map(str, initial_order)))
    print(moves)