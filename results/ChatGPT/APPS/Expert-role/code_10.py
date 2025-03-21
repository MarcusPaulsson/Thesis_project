def find_subsequence(t, test_cases):
    results = []
    for n, p in test_cases:
        # Initialize the subsequence with the first and last element
        subsequence = [p[0]]
        
        # Traverse the array to find elements that contribute to the max sum
        for i in range(1, n):
            if (p[i] - p[i-1]) * (p[i] - p[i-1]) > 0:  # Check if the absolute difference is significant
                subsequence.append(p[i])

        # Always include the last element to ensure at least two elements
        if subsequence[-1] != p[-1]:
            subsequence.append(p[-1])

        # If we only have one element, we need to take the last element as well
        if len(subsequence) == 1:
            subsequence.append(p[-1])

        results.append((len(subsequence), subsequence))

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Get results
results = find_subsequence(t, test_cases)

# Output results
for k, subsequence in results:
    print(k)
    print(" ".join(map(str, subsequence)))