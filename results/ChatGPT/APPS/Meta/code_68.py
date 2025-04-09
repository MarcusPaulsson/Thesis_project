def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences possible
    unique_subsequences_count = 0
    total_cost = 0
    
    # Start with the full string as a subsequence
    unique_subsequences_count += 1  # The full string itself
    total_cost += 0  # Cost for full string is 0
    
    # Use a list to keep track of costs for each unique subsequence
    subsequence_costs = []
    
    # Generate all possible subsequences by reducing one character at a time
    for char, count in freq.items():
        for length in range(1, count + 1):
            subsequence_costs.append(n - length)  # Cost is n - length of subsequence
    
    # Sort the costs to minimize the total cost
    subsequence_costs.sort()
    
    # If the total unique subsequences we can generate is less than k, return -1
    total_unique = len(subsequence_costs)
    if total_unique < k:
        return -1
    
    # Calculate the minimum cost for the first k subsequences
    min_total_cost = sum(subsequence_costs[:k])
    
    return min_total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))