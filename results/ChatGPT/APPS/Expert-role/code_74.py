def min_cost_to_obtain_set(n, k, s):
    unique_subsequences = set()
    total_cost = 0
    
    # To collect all possible distinct subsequences
    for i in range(1 << n):
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(s[j])
        unique_subseq = ''.join(subseq)
        if unique_subseq not in unique_subsequences:
            unique_subsequences.add(unique_subseq)
            total_cost += n - len(unique_subseq)
        
        if len(unique_subsequences) >= k:
            break
    
    if len(unique_subsequences) < k:
        return -1
    return total_cost

n, k = map(int, input().split())
s = input().strip()
print(min_cost_to_obtain_set(n, k, s))