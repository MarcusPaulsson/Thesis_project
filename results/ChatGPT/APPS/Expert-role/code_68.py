def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the maximum number of unique subsequences we can generate
    unique_subsequences_count = 0
    total_cost = 0
    
    # We can generate subsequences of lengths from 0 to n
    for length in range(n + 1):
        # The number of subsequences of length `length` is C(n, length)
        # We can use the formula for combinations to calculate this
        if length == 0:
            count = 1  # only the empty subsequence
        else:
            count = 0
            for char in freq:
                count += freq[char] * (1 << (n - freq[char]))  # 2^(n - freq[char])
        
        if unique_subsequences_count + count >= k:
            # We can reach or exceed k with this length
            total_cost += (n - length) * (k - unique_subsequences_count)
            return total_cost
        
        unique_subsequences_count += count
        total_cost += (n - length) * count
    
    return -1

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result
result = min_cost_to_obtain_set(n, k, s)

# Print the result
print(result)