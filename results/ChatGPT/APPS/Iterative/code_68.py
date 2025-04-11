def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    from math import comb

    # Count the frequency of each character
    freq = Counter(s)
    
    # Calculate the number of unique subsequences we can generate
    unique_subsequences_count = 0
    subsequence_costs = []

    # Generate subsequences and their costs
    for length in range(1, n + 1):
        for char in freq:
            if freq[char] >= length:
                # The number of ways to choose 'length' characters from 'freq[char]'
                count = comb(freq[char], length)
                unique_subsequences_count += count
                subsequence_costs.extend([n - length] * count)
    
    # If we cannot generate enough unique subsequences
    if unique_subsequences_count < k:
        return -1
    
    # Sort costs to minimize the total cost
    subsequence_costs.sort()
    
    # Calculate the minimum cost to obtain k unique subsequences
    total_cost = sum(subsequence_costs[:k])
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))