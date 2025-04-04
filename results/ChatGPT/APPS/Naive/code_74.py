def min_cost_to_obtain_set(n, k, s):
    from itertools import combinations

    # Generate all unique subsequences
    unique_subsequences = set()
    for i in range(n + 1):
        for combo in combinations(s, i):
            unique_subsequences.add(''.join(combo))
    
    # Sort subsequences by length, then by lexicographical order
    sorted_subsequences = sorted(unique_subsequences, key=lambda x: (len(x), x))

    # If the number of unique subsequences is less than k, return -1
    if len(sorted_subsequences) < k:
        return -1

    # Calculate the total cost for the first k unique subsequences
    total_cost = 0
    for i in range(k):
        total_cost += n - len(sorted_subsequences[i])

    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output result
result = min_cost_to_obtain_set(n, k, s)
print(result)