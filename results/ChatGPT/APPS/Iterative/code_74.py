def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    total_cost = 0
    
    # Generate all possible subsequences
    for i in range(1 << n):
        subsequence = []
        for j in range(n):
            if i & (1 << j):
                subsequence.append(s[j])
        subsequence_str = ''.join(subsequence)
        if subsequence_str not in unique_subsequences:
            unique_subsequences.add(subsequence_str)
            total_cost += n - len(subsequence_str)
            if len(unique_subsequences) == k:
                return total_cost
    
    return -1 if len(unique_subsequences) < k else total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))