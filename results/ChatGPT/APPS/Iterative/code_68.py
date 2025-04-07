def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict

    # Count distinct subsequences and their deletion costs
    distinct_subsequences = set()
    costs = []

    # Generate all subsequences using bit masking
    for i in range(1 << n):
        subseq = []
        deleted_count = 0
        for j in range(n):
            if i & (1 << j):
                subseq.append(s[j])
            else:
                deleted_count += 1
        subseq_str = ''.join(subseq)
        if subseq_str not in distinct_subsequences:
            distinct_subsequences.add(subseq_str)
            costs.append(deleted_count)

    # Number of distinct subsequences
    total_distinct = len(distinct_subsequences)

    # If we can't have k distinct subsequences
    if total_distinct < k:
        return -1

    # Sort the costs to minimize total cost
    costs.sort()

    # The minimum cost to obtain k distinct subsequences
    return sum(costs[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))