def min_cost_to_obtain_set(n, k, s):
    from collections import Counter

    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences and their costs
    total_cost = 0
    unique_subsequences = 0
    
    for count in sorted(freq.values(), reverse=True):
        # Calculate unique subsequences contributed by this character
        current_subsequences = 0
        
        for length in range(1, count + 1):
            num_subsequences = 1 << (count - length)  # 2^(count-length)
            current_subsequences += num_subsequences
            total_cost += (n - length) * num_subsequences  # cost for this length
            
            if current_subsequences >= k:
                break
        
        unique_subsequences += current_subsequences
        
        if unique_subsequences >= k:
            break

    if unique_subsequences < k:
        return -1  # Impossible to obtain k unique subsequences

    # Now we need to find the minimum cost to obtain exactly k unique subsequences
    remaining_k = k
    current_cost = 0
    
    for count in sorted(freq.values(), reverse=True):
        for length in range(1, count + 1):
            num_subsequences = 1 << (count - length)  # Number of subsequences of this length
            
            if remaining_k <= num_subsequences:
                current_cost += (n - length) * remaining_k
                return current_cost
            
            current_cost += (n - length) * num_subsequences
            remaining_k -= num_subsequences
            
            if remaining_k <= 0:
                break

    return current_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Get the result
result = min_cost_to_obtain_set(n, k, s)
print(result)