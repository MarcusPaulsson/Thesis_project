from collections import Counter
from math import comb

def min_cost_to_obtain_set(n, k, s):
    freq = Counter(s)
    unique_chars = len(freq)
    
    if unique_chars < k:
        return -1
    
    total_subsequences = 0
    costs = []
    
    for length in range(1, n + 1):
        subseq_count = sum(comb(freq[char], length) for char in freq if freq[char] >= length)
        total_subsequences += subseq_count
        costs.append((n - length) * subseq_count)
        
        if total_subsequences >= k:
            break
    
    if total_subsequences < k:
        return -1
    
    min_cost = 0
    remaining = k
    
    for length, cost in enumerate(costs):
        if remaining <= 0:
            break
        if total_subsequences >= remaining:
            min_cost += cost * remaining
            break
        else:
            min_cost += cost * total_subsequences
            remaining -= total_subsequences
    
    return min_cost