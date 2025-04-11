def max_beauty_after_swap(n, trophies):
    max_golden_subsegment = trophies.count('G')
    if max_golden_subsegment == n:
        return n
    
    golden_indices = [i for i, t in enumerate(trophies) if t == 'G']
    silver_indices = [i for i, t in enumerate(trophies) if t == 'S']
    
    if len(golden_indices) == 0:
        return 0
    
    max_length = 0
    for i in golden_indices:
        for j in silver_indices:
            if i == j:
                continue
            new_trophies = list(trophies)
            new_trophies[i], new_trophies[j] = new_trophies[j], new_trophies[i]
            new_golden_indices = [k for k, t in enumerate(new_trophies) if t == 'G']
            new_max_length = max(max_length, max_golden_subsegment)
            for k in range(len(new_golden_indices) - 1):
                new_max_length = max(new_max_length, new_golden_indices[k+1] - new_golden_indices[k])
            if new_max_length == n:
                return n
            max_length = max(max_length, new_max_length)
    
    return max_length

n = int(input())
trophies = input().strip()
print(max_beauty_after_swap(n, trophies))