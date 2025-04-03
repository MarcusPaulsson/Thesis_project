def min_cost_to_form_set(n, k, s):
    # Function to calculate the number of distinct subsequences and their costs
    from collections import Counter

    # Count frequency of each character
    freq = Counter(s)

    # Initialize variables for total cost and total subsequences
    total_cost = 0
    total_subsequences = 0
    
    # Calculate distinct subsequences
    for length in range(1, n + 1):
        # Number of distinct subsequences of a given length
        distinct_count = 0
        for char, count in freq.items():
            if count >= length:
                distinct_count += 1

        if distinct_count == 0:
            break

        # Each subsequence of length `length` has a cost of `n - length`
        cost_for_this_length = (n - length) * distinct_count

        if total_subsequences + distinct_count < k:
            total_subsequences += distinct_count
            total_cost += cost_for_this_length
        else:
            # If we can fulfill k with this length
            needed = k - total_subsequences
            total_cost += (n - length) * needed
            break

    # If we could not reach k distinct subsequences
    if total_subsequences < k:
        return -1
    return total_cost

# Reading input
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_form_set(n, k, s))