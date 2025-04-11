def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the number of unique subsequences we can form
    unique_subsequences = 0
    costs = []
    
    # For each unique character, calculate the number of subsequences
    for count in freq.values():
        # The number of subsequences formed by this character is 2^count - 1 (excluding the empty subsequence)
        unique_subsequences += (1 << count) - 1
        costs.append(count)  # The cost of using this character is its count
    
    # If we cannot form at least k unique subsequences
    if unique_subsequences < k:
        return -1
    
    # Sort costs in descending order
    costs.sort(reverse=True)
    
    total_cost = 0
    remaining_k = k
    
    # We will try to take the largest costs first to minimize the total cost
    for cost in costs:
        if remaining_k <= 0:
            break
        # The maximum number of subsequences we can take from this character
        max_subsequences = (1 << cost) - 1
        
        if remaining_k > max_subsequences:
            total_cost += cost * max_subsequences
            remaining_k -= max_subsequences
        else:
            total_cost += cost * remaining_k
            remaining_k = 0
    
    # If we still have remaining k, we need to add more subsequences
    if remaining_k > 0:
        total_cost += remaining_k  # Each additional subsequence will cost at least 1
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)