def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    from itertools import combinations

    # Count the frequency of each character in the string
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    # Generate unique subsequences and their costs
    unique_subsequences = set()
    total_cost = 0

    # We can generate subsequences by picking combinations of indices
    for length in range(1, n + 1):
        for indices in combinations(range(n), length):
            subsequence = ''.join(s[i] for i in indices)
            if subsequence not in unique_subsequences:
                unique_subsequences.add(subsequence)
                cost = n - length  # cost is the number of deleted characters
                total_cost += cost

                # If we already have k unique subsequences, we can stop
                if len(unique_subsequences) >= k:
                    return total_cost
    
    # If we have fewer than k unique subsequences, it's impossible
    return -1 if len(unique_subsequences) < k else total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print
result = min_cost_to_obtain_set(n, k, s)
print(result)