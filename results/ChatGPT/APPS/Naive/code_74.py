def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences
    for i in range(1 << n):
        subsequence = ''.join(s[j] for j in range(n) if (i & (1 << j)))
        unique_subsequences.add(subsequence)
    
    # Remove the empty subsequence
    if '' in unique_subsequences:
        unique_subsequences.remove('')
    
    # If the number of unique subsequences is less than k, return -1
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate costs for each unique subsequence
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    # Sort costs and return the sum of the smallest k costs
    costs.sort()
    return sum(costs[:k])

# Input reading
n, k = map(int, input().strip().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))