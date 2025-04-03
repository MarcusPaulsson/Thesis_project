def max_happiness(t, test_cases):
    results = []
    
    for case in test_cases:
        n, k, a, w = case
        a.sort()
        w.sort()
        
        # Calculate total happiness
        total_happiness = 0
        
        # The maximum values will be assigned to friends with the largest w_i
        for i in range(k):
            total_happiness += a[n - 1 - i]  # max value for each friend
            total_happiness += a[i]          # min value for each friend
        
        results.append(total_happiness)

    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    test_cases.append((n, k, a, w))

results = max_happiness(t, test_cases)

# Printing results
for result in results:
    print(result)