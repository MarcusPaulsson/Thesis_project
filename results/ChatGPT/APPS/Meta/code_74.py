def min_cost_to_obtain_set(n, k, s):
    # Create a set to store unique subsequences
    unique_subsequences = set()

    # Generate all possible subsequences using bit masking
    for mask in range(1 << n):
        subsequence = []
        for i in range(n):
            if mask & (1 << i):
                subsequence.append(s[i])
        unique_subsequences.add(''.join(subsequence))

    # Calculate the number of unique subsequences
    unique_count = len(unique_subsequences)
    
    # If the number of unique subsequences is less than k, return -1
    if unique_count < k:
        return -1

    # Calculate the minimum cost to obtain k unique subsequences
    sorted_lengths = sorted(n - len(subseq) for subseq in unique_subsequences)
    return sum(sorted_lengths[:k])

# Read input
n, k = map(int, input().split())
s = input().strip()

# Get the result and print it
result = min_cost_to_obtain_set(n, k, s)
print(result)