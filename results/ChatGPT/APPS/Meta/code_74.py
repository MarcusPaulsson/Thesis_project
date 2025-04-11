def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all possible subsequences
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # If we cannot obtain k unique subsequences
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate the minimum cost
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    # Sort costs and take the k smallest
    costs.sort()
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)