from itertools import combinations

def min_cost_to_obtain_set(n, k, s):
    # Create a set to hold unique subsequences
    unique_subsequences = set()
    
    # Generate all possible subsequences
    for length in range(n + 1):
        for comb in combinations(s, length):
            unique_subsequences.add(''.join(comb))
    
    # Check if we can obtain at least k unique subsequences
    if len(unique_subsequences) < k:
        return -1

    # Calculate the minimum cost for the first k unique subsequences
    costs = sorted(n - len(subseq) for subseq in unique_subsequences)
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))