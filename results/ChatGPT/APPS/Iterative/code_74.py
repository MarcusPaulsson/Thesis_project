from itertools import combinations

def min_cost_to_get_k_subsequences(n, k, s):
    unique_chars = set(s)
    unique_count = len(unique_chars)

    if k > (1 << unique_count) - 1:  # 2^unique_count - 1
        return -1

    costs = []
    for length in range(1, n + 1):
        for subseq in combinations(s, length):
            subseq_str = ''.join(subseq)
            if subseq_str not in costs:
                costs.append(subseq_str)
                if len(costs) == k:
                    return sum(n - len(t) for t in costs)
    
    return -1

n, k = map(int, input().split())
s = input().strip()
result = min_cost_to_get_k_subsequences(n, k, s)
print(result)