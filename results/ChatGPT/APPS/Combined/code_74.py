def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences using bit manipulation
    for i in range(1 << n):
        subsequence = ''.join(s[j] for j in range(n) if (i & (1 << j)))
        unique_subsequences.add(subsequence)
    
    # If the number of unique subsequences is less than k, return -1
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate the costs of each unique subsequence
    costs = sorted(n - len(subseq) for subseq in unique_subsequences)
    
    # Return the sum of the smallest k costs
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))