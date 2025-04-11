def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences
    total_unique_subsequences = 0
    costs = []
    
    # For each unique character, calculate the number of subsequences it can generate
    for char, count in freq.items():
        # Number of subsequences that can be formed with this character
        # is 2^count - 1 (excluding the empty subsequence)
        num_subsequences = (1 << count) - 1  # 2^count - 1
        total_unique_subsequences += num_subsequences
        
        # Each subsequence of length `l` has a cost of `n - l`
        for length in range(1, count + 1):
            costs.append(n - length)
    
    # If we cannot form at least k unique subsequences, return -1
    if total_unique_subsequences < k:
        return -1
    
    # Sort costs to minimize the total cost
    costs.sort()
    
    # Calculate the minimum cost to obtain exactly k unique subsequences
    min_cost = sum(costs[:k])
    
    return min_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)