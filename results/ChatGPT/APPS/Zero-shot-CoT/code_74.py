def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    unique_subsequences = list(unique_subsequences)
    m = len(unique_subsequences)
    
    if m < k:
        return -1
    
    # Calculate costs
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    costs.sort()
    
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)