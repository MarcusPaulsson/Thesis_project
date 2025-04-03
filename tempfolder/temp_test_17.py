def count_tuples(t, test_cases):
    results = []
    for n, a in test_cases:
        count = 0
        
        # Dictionary to count occurrences of pairs
        pair_count = {}
        
        # Iterate through all possible j, l pairs
        for j in range(1, n - 1):
            for l in range(j + 1, n):
                if a[j] == a[l]:  # Only consider pairs where a[j] == a[l]
                    # Count how many i's can form a valid tuple with this j, l
                    # Count how many k's can form a valid tuple with this j, l
                    # We are looking for i < j and k > j
                    for i in range(j):
                        if a[i] == a[j]:  # a[i] must equal a[k]
                            if (a[i], a[j]) in pair_count:
                                count += pair_count[(a[i], a[j])]
                    
                    # Now we add this pair to the pair_count dictionary
                    if (a[j], a[l]) not in pair_count:
                        pair_count[(a[j], a[l])] = 0
                    pair_count[(a[j], a[l])] += 1
        
        results.append(count)
    
    return results


# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results and print them
results = count_tuples(t, test_cases)
for result in results:
    print(result)