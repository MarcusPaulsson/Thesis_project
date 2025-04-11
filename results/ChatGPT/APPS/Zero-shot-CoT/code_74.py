def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character in the string
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the number of unique subsequences we can generate
    unique_subsequences = 0
    costs = []
    
    # Generate subsequences and their costs
    for char, count in freq.items():
        for length in range(1, count + 1):
            unique_subsequences += 1
            costs.append(n - length)
    
    # If we can't generate enough unique subsequences
    if unique_subsequences < k:
        return -1
    
    # Sort costs to minimize the total cost
    costs.sort()
    
    # Calculate the minimum cost for the first k unique subsequences
    return sum(costs[:k])

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))