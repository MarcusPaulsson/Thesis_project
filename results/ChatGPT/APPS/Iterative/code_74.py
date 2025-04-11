def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    total_cost = 0

    # Generate all unique subsequences
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequence = ''.join(subsequence)
        if unique_subsequence not in unique_subsequences:
            unique_subsequences.add(unique_subsequence)
            total_cost += n - len(unique_subsequence)

    if len(unique_subsequences) < k:
        return -1
    else:
        return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)