def min_cost_to_get_k_subsequences(n, k, s):
    unique_subsequences = set()
    subsequence_costs = []
    
    # Generate all unique subsequences
    for i in range(n):
        for j in range(i + 1, n + 1):
            subsequence = s[i:j]
            if subsequence not in unique_subsequences:
                unique_subsequences.add(subsequence)
                # Cost is n - length of subsequence
                subsequence_costs.append(n - len(subsequence))

    # Check if we have enough unique subsequences
    if len(unique_subsequences) < k:
        return -1  

    # Sort costs to find the minimum total cost for k subsequences
    subsequence_costs.sort()
    total_cost = sum(subsequence_costs[:k])
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_get_k_subsequences(n, k, s))