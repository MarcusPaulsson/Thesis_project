def min_cost_to_obtain_set(n, k, s):
    from itertools import combinations
    
    unique_subsequences = set()
    
    # Generate all possible subsequences
    for length in range(n + 1):
        for comb in combinations(range(n), length):
            subseq = ''.join(s[i] for i in comb)
            unique_subsequences.add(subseq)
    
    # If we can't obtain k unique subsequences
    if len(unique_subsequences) < k:
        return -1
    
    # Calculate the costs for the unique subsequences
    costs = []
    for subseq in unique_subsequences:
        cost = n - len(subseq)
        costs.append(cost)
    
    # Sort costs and take the minimum k costs
    costs.sort()
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))