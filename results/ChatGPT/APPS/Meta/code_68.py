def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences
    total_subsequences = 0
    costs = []
    
    # For each unique character, calculate the number of subsequences we can create
    for char, count in freq.items():
        # The number of subsequences that can be formed with this character
        # is 2^count - 1 (excluding the empty subsequence)
        subsequences_count = (1 << count) - 1  # 2^count - 1
        total_subsequences += subsequences_count
        
        # The cost of adding subsequences of length 1 to count
        for length in range(1, count + 1):
            costs.append(n - length)
    
    # If we cannot create enough unique subsequences
    if total_subsequences < k:
        return -1
    
    # Sort costs to minimize the total cost
    costs.sort()
    
    # Calculate the minimum cost to obtain exactly k unique subsequences
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)