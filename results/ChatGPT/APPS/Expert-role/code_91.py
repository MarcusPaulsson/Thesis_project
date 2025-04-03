def possible_permutation(t, test_cases):
    results = []
    
    for n, q in test_cases:
        p = []
        used = set()
        max_seen = 0
        impossible = False
        
        for i in range(n):
            if q[i] > max_seen:
                p.append(q[i])
                used.add(q[i])
                max_seen = q[i]
            else:
                # We need to fill this position with a number we haven't used yet
                for num in range(1, n + 1):
                    if num not in used:
                        p.append(num)
                        used.add(num)
                        break
        
        if len(set(p)) != n:
            results.append("-1")
        else:
            results.append(" ".join(map(str, p)))
    
    return results

# Read input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    q = list(map(int, input().strip().split()))
    test_cases.append((n, q))

# Get results
results = possible_permutation(t, test_cases)

# Print output
for result in results:
    print(result)