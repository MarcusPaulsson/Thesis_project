from itertools import combinations

def min_cost_to_obtain_set(n, k, s):
    subsequences = set()
    
    # Generate all unique subsequences
    for i in range(n + 1):
        for combo in combinations(s, i):
            subsequences.add(''.join(combo))
    
    # If the number of unique subsequences is less than k, return -1
    if len(subsequences) < k:
        return -1
    
    # Calculate the cost for the k smallest subsequences
    costs = []
    for t in subsequences:
        costs.append(n - len(t))  # Cost is n - |t|
    
    costs.sort()
    
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result
result = min_cost_to_obtain_set(n, k, s)

# Print the result
print(result)