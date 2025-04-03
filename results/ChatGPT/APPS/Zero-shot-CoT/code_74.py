def min_cost_to_obtain_set(n, k, s):
    unique_characters = set(s)
    count_unique = len(unique_characters)
    
    # If number of unique characters is less than k, it's impossible
    if count_unique < k:
        return -1
    
    # Calculate the total number of unique subsequences we can generate
    total_subsequences = 0
    cost = 0
    power_of_two = 1  # 2^0
    
    for length in range(1, n + 1):
        power_of_two *= 2
        total_subsequences += power_of_two - 1  # We exclude the empty subsequence
        cost += n - length  # Cost to add subsequences of this length
        
        if total_subsequences >= k:
            return cost - (total_subsequences - k)  # Adjust cost if we have extras
    
    # If we still don't have enough subsequences after considering all lengths
    return -1

# Read input
n, k = map(int, input().split())
s = input().strip()

# Calculate and output the result
result = min_cost_to_obtain_set(n, k, s)
print(result)