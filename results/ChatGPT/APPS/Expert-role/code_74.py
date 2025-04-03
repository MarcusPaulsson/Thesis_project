def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    
    # Generate all unique subsequences
    for i in range(1 << n):  # There are 2^n possible subsequences
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(s[j])
        unique_subsequences.add(''.join(subseq))
    
    if len(unique_subsequences) < k:
        return -1
    
    # Sort the unique subsequences based on their length (ascending)
    sorted_subsequences = sorted(unique_subsequences, key=len)
    
    total_cost = 0
    for i in range(k):
        total_cost += n - len(sorted_subsequences[i])
    
    return total_cost

# Input reading
n, k = map(int, input().split())
s = input().strip()

# Output the result
print(min_cost_to_obtain_set(n, k, s))