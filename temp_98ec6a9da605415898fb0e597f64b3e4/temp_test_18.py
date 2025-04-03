def minimum_cost(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences using bit manipulation
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # If we cannot form k unique subsequences
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate the costs
    costs = []
    for subseq in unique_subsequences:
        costs.append(n - len(subseq))
    
    # Sort the costs and take the sum of the smallest k costs
    costs.sort()
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(minimum_cost(n, k, s))