def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count frequencies of each character
    freq = Counter(s)
    unique_count = len(freq)
    
    # If k is greater than the total possible subsequences, return -1
    if k > (1 << unique_count):
        return -1
    
    # List of all possible subsequences and their costs
    costs = []
    
    # Generate all subsequences
    for i in range(1 << n):
        subsequence = ''.join(s[j] for j in range(n) if (i & (1 << j)))
        costs.append(len(subsequence))
    
    costs.sort()
    
    # Calculate the minimum cost for the first k unique subsequences
    total_cost = 0
    for i in range(k):
        total_cost += n - costs[i]
    
    return total_cost

# Reading input
n, k = map(int, input().split())
s = input().strip()

# Getting the result
result = min_cost_to_obtain_set(n, k, s)
print(result)