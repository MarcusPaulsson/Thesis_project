def min_skip_points(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        
        skip_points = 0
        i = 0
        
        while i < n:
            if a[i] == 1:  # If the boss is hard
                if i + 1 < n and a[i + 1] == 1:  # If the next boss is also hard
                    skip_points += 1  # Use a skip point for the first hard boss
                    i += 2  # Move past both
                else:
                    skip_points += 1  # Use a skip point for the hard boss
                    i += 1  # Move past the hard boss
            else:
                i += 1  # Move past the easy boss
                
        results.append(skip_points)
    
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Getting results
results = min_skip_points(t, test_cases)

# Printing results
for result in results:
    print(result)