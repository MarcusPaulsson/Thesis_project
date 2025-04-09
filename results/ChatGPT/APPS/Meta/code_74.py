def min_cost_to_get_k_subsequences(n, k, s):
    # Calculate the unique characters and their frequencies
    from collections import Counter
    freq = Counter(s)
    
    # Calculate the maximum number of unique subsequences we can get
    unique_subsequences_count = 0
    total_cost = 0
    total_possible_subsequences = 0

    # To hold the cost of adding subsequences
    subsequence_costs = []
    
    # Calculate the number of unique subsequences we can generate
    for length in range(1, n + 1):
        current_cost = n - length
        # The number of different subsequences of this length
        num_subsequences_of_length = 1
        for char in freq:
            num_subsequences_of_length *= (1 + min(freq[char], length))
        num_subsequences_of_length -= 1  # Remove the empty subsequence
        
        if num_subsequences_of_length > 0:
            unique_subsequences_count += num_subsequences_of_length
            total_cost += num_subsequences_of_length * current_cost
            subsequence_costs.append((num_subsequences_of_length, current_cost))

    # Now we have the total unique subsequences count
    if unique_subsequences_count < k:
        return -1
    
    # If we have enough unique subsequences, we need to minimize the cost
    subsequence_costs.sort(key=lambda x: x[1])  # Sort by cost
    remaining_k = k
    total_min_cost = 0
    
    for count, cost in subsequence_costs:
        if remaining_k <= 0:
            break
        if count >= remaining_k:
            total_min_cost += remaining_k * cost
            remaining_k = 0
        else:
            total_min_cost += count * cost
            remaining_k -= count
    
    return total_min_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()
print(min_cost_to_get_k_subsequences(n, k, s))