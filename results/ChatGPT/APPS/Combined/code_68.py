def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    from math import comb

    # Count frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    # Calculate the total number of unique subsequences
    unique_subsequences = 0
    subsequence_costs = []

    # Generate all possible subsequences and their costs
    for length in range(1, n + 1):
        for count in freq.values():
            if count >= length:
                # Calculate the number of subsequences of this length
                num_subsequences = comb(count, length)
                unique_subsequences += num_subsequences
                subsequence_costs.append((length, num_subsequences))

    # If we cannot form at least k unique subsequences
    if unique_subsequences < k:
        return -1

    # Sort costs by length (cost increases with length)
    subsequence_costs.sort()

    # Calculate the minimum cost to obtain k unique subsequences
    total_cost = 0
    remaining_k = k

    for length, num in subsequence_costs:
        if remaining_k <= 0:
            break
        if num <= remaining_k:
            total_cost += num * (n - length)
            remaining_k -= num
        else:
            total_cost += remaining_k * (n - length)
            remaining_k = 0

    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))