def min_cost_to_obtain_set(n, k, s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Calculate the total number of unique subsequences we can generate
    unique_subsequences = 0
    cost = 0
    
    # We can create a subsequence of length i by deleting (n - i) characters
    # We iterate over all possible lengths of subsequences
    for length in range(1, n + 1):
        # Number of unique subsequences of this specific length
        unique_count = 1
        for char, count in freq.items():
            if count >= length:
                unique_count *= (count - length + 1)
        
        if unique_count > 0:
            unique_subsequences += unique_count
            cost += unique_count * (n - length)
        
        # If we have reached the required size, we can stop
        if unique_subsequences >= k:
            return cost
    
    # If we exit the loop and haven't reached k, it's impossible
    return -1

# Read input values
n, k = map(int, input().split())
s = input().strip()

# Get the result and print
result = min_cost_to_obtain_set(n, k, s)
print(result)