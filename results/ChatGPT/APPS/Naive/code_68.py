def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences
    unique_subsequences = 0
    total_cost = 0
    
    # For each unique character, calculate the number of subsequences
    for char, count in freq.items():
        # Number of subsequences that can be formed with this character
        # is 2^count - 1 (excluding the empty subsequence)
        unique_subsequences += (1 << count) - 1  # 2^count - 1
        total_cost += count * (1 << count) - 1  # Cost of all subsequences
    
    # If we cannot form at least k unique subsequences, return -1
    if unique_subsequences < k:
        return -1
    
    # Calculate the minimum cost to obtain exactly k unique subsequences
    cost = 0
    remaining = k
    
    # We will use a list to keep track of costs for each unique subsequence length
    costs = []
    
    for char, count in freq.items():
        for length in range(1, count + 1):
            # Cost to form subsequences of this length
            costs.append((n - length, (1 << length) - 1))  # (cost, number of subsequences)
    
    # Sort costs by cost ascending
    costs.sort()
    
    for cost, num_subseq in costs:
        if remaining <= 0:
            break
        if num_subseq <= remaining:
            cost += num_subseq * cost
            remaining -= num_subseq
        else:
            cost += remaining * cost
            remaining = 0
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))