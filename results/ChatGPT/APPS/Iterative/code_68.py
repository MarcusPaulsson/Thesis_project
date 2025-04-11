def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict

    # Count the frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    # Calculate the number of unique subsequences and their costs
    unique_subsequences = 0
    costs = []

    # Generate all possible subsequences and their costs
    for length in range(n + 1):
        for char, count in freq.items():
            if count > 0:
                # The cost to create a subsequence of this length
                cost = n - length
                # Count how many unique subsequences of this length can be formed
                count_of_subsequences = min(count, 2 ** length - 1)
                unique_subsequences += count_of_subsequences
                costs.extend([cost] * count_of_subsequences)

    # If we cannot form at least k unique subsequences
    if unique_subsequences < k:
        return -1

    # Sort costs and sum the minimum k costs
    costs.sort()
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))