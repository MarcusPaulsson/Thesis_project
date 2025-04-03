def count_ambiguous_pairs(m, d, w):
    total_pairs = 0
    # Calculate the maximum offset for the days
    max_offset = min(d, w)
    
    # Calculate the number of ambiguous pairs
    for x in range(1, m):
        y_start = x + 1
        y_end = min(m, x + max_offset - 1)
        total_pairs += max(0, y_end - y_start + 1)

    return total_pairs

t = int(input())
results = []
for _ in range(t):
    m, d, w = map(int, input().split())
    results.append(count_ambiguous_pairs(m, d, w))

print('\n'.join(map(str, results)))