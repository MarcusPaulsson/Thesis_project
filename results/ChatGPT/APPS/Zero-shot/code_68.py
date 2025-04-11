def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character in the string
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the number of unique subsequences we can generate
    unique_subsequences = 0
    total_cost = 0
    costs = []
    
    # Generate subsequences and their costs
    for length in range(1, n + 1):
        # For each unique character, we can create subsequences of this length
        for char, count in freq.items():
            if count >= length:
                # The number of ways to choose 'length' characters from 'count' is C(count, length)
                # This is equivalent to the number of unique subsequences of this length
                unique_subsequences += 1
                costs.append(n - length)  # Cost of adding this subsequence
    
    # If we can't generate enough unique subsequences
    if unique_subsequences < k:
        return -1
    
    # Sort costs to minimize total cost
    costs.sort()
    
    # Calculate the minimum total cost to obtain k unique subsequences
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)