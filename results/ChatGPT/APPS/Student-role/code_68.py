def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the maximum number of unique subsequences we can generate
    unique_subsequences = 0
    total_cost = 0
    cost_per_length = [0] * (n + 1)
    
    # Calculate the cost for each possible length of subsequence
    for length in range(n + 1):
        cost_per_length[length] = n - length
    
    # Generate subsequences and calculate their costs
    for char, count in freq.items():
        # For each character, we can generate subsequences of lengths 1 to count
        for length in range(1, count + 1):
            unique_subsequences += 1
            total_cost += cost_per_length[length]
            if unique_subsequences >= k:
                return total_cost
    
    # If we reach here, we couldn't generate enough unique subsequences
    if unique_subsequences < k:
        return -1
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))