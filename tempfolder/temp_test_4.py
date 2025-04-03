def is_beautiful_permutation(t, test_cases):
    results = []
    
    for n, p in test_cases:
        beautiful = ['0'] * n
        max_seen = 0
        
        for i in range(n):
            max_seen = max(max_seen, p[i])
            if max_seen == i + 1:
                beautiful[i] = '1'
        
        results.append(''.join(beautiful))
    
    return results


# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    test_cases.append((n, p))

# Getting results
results = is_beautiful_permutation(t, test_cases)

# Printing output
for result in results:
    print(result)