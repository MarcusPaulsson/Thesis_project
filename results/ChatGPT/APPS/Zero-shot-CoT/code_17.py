def count_tuples(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        count = 0
        # Dictionary to store the occurrence of each number
        positions = {}
        
        for i in range(n):
            if a[i] not in positions:
                positions[a[i]] = []
            positions[a[i]].append(i)

        # Now we will find valid tuples
        for j in range(n):
            for l in range(j + 1, n):
                if a[j] == a[l]:
                    # We need to find pairs (i, k) such that i < j < k
                    for i in range(j):
                        if a[i] == a[j]:  # a[i] == a[k]
                            count += len(positions[a[i]]) - (i + 1)  # k must be after i
            
        results.append(count)

    return results

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = count_tuples(test_cases)

# Print results
for result in results:
    print(result)