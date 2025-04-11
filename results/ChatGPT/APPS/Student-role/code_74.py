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
    
    # Calculate the cost for the k unique subsequences
    costs = []
    for subseq in unique_subsequences:
        costs.append(n - len(subseq))
    
    costs.sort()
    
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))