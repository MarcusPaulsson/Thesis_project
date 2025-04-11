def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all subsequences
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # Calculate the cost for each unique subsequence
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    # Sort costs to minimize total cost
    costs.sort()
    
    if len(costs) < k:
        return -1
    
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))