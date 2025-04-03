def min_skip_points(t, test_cases):
    results = []

    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        
        skip_points = 0
        i = 0
        
        while i < n:
            if a[i] == 1:
                skip_points += 1
                if i + 1 < n and a[i + 1] == 1:
                    i += 2  # Skip the next hard boss too
                else:
                    i += 1  # Only skip this one hard boss
            else:
                i += 1  # Easy boss, just kill it
        
        results.append(skip_points)
    
    return results

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = min_skip_points(t, test_cases)

# Output results
for result in results:
    print(result)