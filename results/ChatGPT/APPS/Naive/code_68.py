def min_cost_to_obtain_set(n, k, s):
    # Calculate the maximum number of unique subsequences possible
    unique_chars = set(s)
    max_unique_subsequences = 0
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Generate all possible unique subsequences
    for count in char_count.values():
        max_unique_subsequences += (1 << count) - 1  # 2^count - 1 unique subsequences
    
    # If the maximum unique subsequences is less than k, it's impossible
    if max_unique_subsequences < k:
        return -1
    
    # Minimum cost to obtain k unique subsequences
    total_cost = 0
    subsequence_count = 0
    
    # Start with the largest subsequence (which costs 0)
    # and decrease the length to create new unique subsequences
    for length in range(n, 0, -1):
        if subsequence_count >= k:
            break
        # Count how many unique subsequences we can obtain of this length
        current_subseq_count = (1 << length) - 1  # 2^length - 1
        available = min(current_subseq_count, k - subsequence_count)
        
        # Each subsequence of this length costs (n - length)
        total_cost += (n - length) * available
        subsequence_count += available
    
    return total_cost

# Input Handling
n, k = map(int, input().split())
s = input().strip()
result = min_cost_to_obtain_set(n, k, s)
print(result)