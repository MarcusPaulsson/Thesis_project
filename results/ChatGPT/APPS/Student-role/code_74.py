def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences using a bitmask approach
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # If the number of unique subsequences is less than k, return -1
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate the minimum cost
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    # Sort costs and take the sum of the smallest k costs
    costs.sort()
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Calculate and print the result
result = min_cost_to_obtain_set(n, k, s)
print(result)