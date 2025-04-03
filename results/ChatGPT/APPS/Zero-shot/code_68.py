def min_cost_to_obtain_set(n, k, s):
    subsequence_count = {}
    
    # Generate all unique subsequences and their respective costs
    from itertools import combinations
    
    for length in range(1, n + 1):
        for indices in combinations(range(n), length):
            subsequence = ''.join(s[i] for i in indices)
            cost = n - length
            if subsequence not in subsequence_count:
                subsequence_count[subsequence] = cost
    
    # If we cannot reach k unique subsequences
    if len(subsequence_count) < k:
        return -1
    
    # Collect costs and sort them to minimize total cost
    costs = sorted(subsequence_count.values())
    
    # Calculate the minimum total cost for the first k unique subsequences
    total_cost = sum(costs[:k])
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))