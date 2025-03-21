def count_tuples(t, test_cases):
    results = []
    for n, a in test_cases:
        count = 0
        freq = {}
        
        # Count occurrences of pairs (a[j], a[l]) for j < l
        for j in range(n):
            for l in range(j + 1, n):
                if a[j] == a[l]:
                    if (a[j], j) not in freq:
                        freq[(a[j], j)] = 0
                    freq[(a[j], j)] += 1
        
        # Calculate valid tuples using (a[i], a[k]) pairs
        for k in range(n):
            for i in range(k):
                if a[i] == a[k]:
                    # For each (i, k) pair, add the number of (j, l) pairs found
                    count += freq.get((a[i], k), 0)
        
        results.append(count)
    
    return results


# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = count_tuples(t, test_cases)

# Output results
for result in results:
    print(result)