def min_cost_to_obtain_set(n, k, s):
    # Create a set to store unique subsequences
    unique_subsequences = set()
    
    # Generate all possible subsequences
    for i in range(1 << n):  # 2^n combinations
        subsequence = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subsequence.append(s[j])
        unique_subsequences.add(''.join(subsequence))
    
    # Calculate the size of unique subsequences
    m = len(unique_subsequences)

    # If we can't generate enough unique subsequences
    if m < k:
        return -1
    
    # Calculate the minimum cost
    total_cost = 0
    # We can generate the subsequences of lengths from 0 to n
    # Collecting costs for all possible lengths
    costs = [0] * (n + 1)
    
    for length in range(n + 1):
        costs[length] = n - length  # Cost of length 'length' subsequence
    
    # We need to take k unique subsequences
    # We can take sequences of length 0 to n
    for length in range(n + 1):
        if k <= 0:
            break
        count = min(k, m * (1 << (n - length)))  # Number of subsequences of this length
        total_cost += count * costs[length]
        k -= count
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output result
print(min_cost_to_obtain_set(n, k, s))