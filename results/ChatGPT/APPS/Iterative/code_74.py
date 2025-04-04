def min_cost_to_get_subsequences(n, k, s):
    if k <= 0:
        return 0  # No subsequences needed
    
    unique_chars = set(s)
    max_subsequences = 0
    costs = []
    
    # Count distinct characters and calculate costs for subsequences
    for char in unique_chars:
        count = s.count(char)
        costs.append(count)  # Each character can contribute subsequences
        max_subsequences += (1 << count) - 1  # 2^count - 1
    
    # If we can't form enough unique subsequences
    if max_subsequences < k:
        return -1
    
    # Sort costs in descending order to minimize total cost
    costs.sort(reverse=True)
    
    total_cost = 0
    needed = k
    
    # Calculate minimum cost to get k unique subsequences
    for i in range(min(len(costs), needed)):
        total_cost += costs[i]
    
    # If more unique subsequences are needed than we have distinct characters
    if needed > len(costs):
        total_cost += (needed - len(costs)) * n  # Remaining needed subsequences come from full length
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get result
result = min_cost_to_get_subsequences(n, k, s)

# Print result
print(result)