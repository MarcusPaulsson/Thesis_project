def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all possible subsequences
    from itertools import combinations
    for length in range(n + 1):
        for indices in combinations(range(n), length):
            subseq = ''.join(s[i] for i in indices)
            unique_subsequences.add(subseq)
    
    # If we cannot obtain k unique subsequences
    if len(unique_subsequences) < k:
        return -1

    # Calculate costs of subsequences
    costs = [n - len(subseq) for subseq in unique_subsequences]
    
    # Sort costs and take the minimum k costs
    costs.sort()
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))