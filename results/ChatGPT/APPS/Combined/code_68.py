from collections import Counter
from math import comb

def min_cost_to_obtain_set(n, k, s):
    freq = Counter(s)
    
    # Calculate the number of unique subsequences we can generate
    unique_subsequences = 0
    costs = []
    
    # Generate all possible subsequences and their costs
    for length in range(1, n + 1):
        subseq_count = sum(comb(freq[char], length) for char in freq)
        if subseq_count > 0:
            unique_subsequences += subseq_count
            costs.append((length, subseq_count * (n - length)))
    
    # If we cannot generate enough unique subsequences
    if unique_subsequences < k:
        return -1
    
    # Sort costs by length
    costs.sort()
    
    # Calculate the minimum cost to obtain k unique subsequences
    total_cost = 0
    remaining_k = k
    
    for length, cost in costs:
        if remaining_k <= 0:
            break
        # Calculate how many we can take from this length
        take = min(remaining_k, cost // (n - length))
        total_cost += take * (n - length)
        remaining_k -= take
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))