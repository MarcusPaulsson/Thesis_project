def find_permutation(t, test_cases):
    results = []
    for n, q in test_cases:
        p = []
        used = set()
        last_max = 0
        possible = True
        
        for i in range(n):
            if q[i] > last_max:
                # We need to add a new maximum
                p.append(q[i])
                used.add(q[i])
                last_max = q[i]
            else:
                # We can use the smallest unused number
                for j in range(1, n + 1):
                    if j not in used:
                        p.append(j)
                        used.add(j)
                        break
                        
            if len(p) != i + 1:
                possible = False
                break
        
        if possible and len(set(p)) == n:
            results.append(" ".join(map(str, p)))
        else:
            results.append("-1")
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    test_cases.append((n, q))

# Getting results
results = find_permutation(t, test_cases)

# Printing results
for result in results:
    print(result)