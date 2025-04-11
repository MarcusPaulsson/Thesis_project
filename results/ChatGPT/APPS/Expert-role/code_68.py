def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences
    total_unique_subsequences = 0
    total_cost = 0
    
    # Generate all possible subsequences and their costs
    for length in range(n + 1):
        for char, count in freq.items():
            if count > 0:
                # Calculate the number of subsequences of this length
                subsequences_count = (1 << count) - 1  # 2^count - 1 (excluding empty subsequence)
                total_unique_subsequences += subsequences_count
                
                # Calculate the cost for subsequences of this length
                total_cost += subsequences_count * (n - length)
                
                if total_unique_subsequences >= k:
                    return total_cost
    
    # If we cannot reach k unique subsequences
    if total_unique_subsequences < k:
        return -1
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)