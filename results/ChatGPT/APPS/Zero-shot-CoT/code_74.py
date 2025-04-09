def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    total_cost = 0
    
    # Generate all unique subsequences and their costs
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        subsequence_str = ''.join(subsequence)
        if subsequence_str not in unique_subsequences:
            unique_subsequences.add(subsequence_str)
            total_cost += n - len(subsequence_str)
        
        if len(unique_subsequences) >= k:
            break
    
    if len(unique_subsequences) < k:
        return -1
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))