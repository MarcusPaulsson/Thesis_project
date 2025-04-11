def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the maximum number of unique subsequences we can form
    unique_subsequences = 0
    total_cost = 0
    
    # To store the costs of subsequences of different lengths
    costs = []
    
    # Generate all possible subsequences and their costs
    for length in range(1, n + 1):
        # Calculate the number of unique subsequences of this length
        count = sum(1 for c in freq if freq[c] >= length)
        if count > 0:
            unique_subsequences += count
            costs.append((n - length) * count)
    
    # If we cannot form at least k unique subsequences
    if unique_subsequences < k:
        return -1
    
    # Sort costs to minimize total cost
    costs.sort()
    
    # Calculate the minimum cost to obtain exactly k unique subsequences
    total_cost = sum(costs[:k])
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))