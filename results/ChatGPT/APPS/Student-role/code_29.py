def amazing_numbers(t, test_cases):
    results = []
    for n, a in test_cases:
        last_position = {}
        freq = {}
        for i in range(n):
            if a[i] not in last_position:
                last_position[a[i]] = []
            last_position[a[i]].append(i)
            freq[a[i]] = freq.get(a[i], 0) + 1
        
        k_amazing = [-1] * n
        for number, positions in last_position.items():
            positions.append(n)  # Add a virtual end position
            min_length = float('inf')
            for j in range(len(positions) - 1):
                min_length = min(min_length, positions[j + 1] - positions[j])
            if min_length > 1:
                k = min_length - 1
                if k >= 1:
                    k_amazing[k - 1] = min(k_amazing[k - 1], number) if k_amazing[k - 1] != -1 else number
        
        for k in range(n - 1):
            k_amazing[k + 1] = min(k_amazing[k + 1], k_amazing[k]) if k_amazing[k + 1] != -1 else k_amazing[k]
        
        results.append(" ".join(map(str, k_amazing)))

    return results

# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print
results = amazing_numbers(t, test_cases)
for result in results:
    print(result)