def min_cost_to_obtain_set(n, k, s):
    from collections import defaultdict
    
    # Count the frequency of each character
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    
    # Calculate the number of unique subsequences
    unique_subsequences = 0
    total_cost = 0
    
    # Generate all possible subsequences
    for length in range(n + 1):
        for char in freq:
            if freq[char] >= length:
                unique_subsequences += 1
                total_cost += (n - length)
                if unique_subsequences >= k:
                    return total_cost
    
    # If we can't reach k unique subsequences
    if unique_subsequences < k:
        return -1
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)