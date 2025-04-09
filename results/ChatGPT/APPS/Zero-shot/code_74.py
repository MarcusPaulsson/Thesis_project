def min_cost_to_obtain_set(n, k, s):
    # Unique subsequences set
    unique_subsequences = set()
    
    # Generate all possible subsequences
    for i in range(1 << n):
        subsequence = ""
        for j in range(n):
            if i & (1 << j):
                subsequence += s[j]
        unique_subsequences.add(subsequence)
    
    # If the number of unique subsequences is less than k, return -1
    if len(unique_subsequences) < k:
        return -1

    # List of lengths of all unique subsequences
    lengths = sorted([len(subseq) for subseq in unique_subsequences])
    
    # Calculate minimum cost
    total_cost = 0
    for i in range(k):
        total_cost += n - lengths[i]
    
    return total_cost

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)