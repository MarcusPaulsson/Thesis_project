def clean_string(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        s = test_cases[i][1]
        
        # Count the number of 0s and 1s
        count_0 = s.count('0')
        count_1 = s.count('1')
        
        # Construct the clean string
        if count_0 > 0 and count_1 > 0:
            results.append('0' * count_0 + '1' * count_1)
        else:
            results.append('0' * count_0 + '1' * count_1)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Get results
results = clean_string(t, test_cases)

# Print results
for result in results:
    print(result)